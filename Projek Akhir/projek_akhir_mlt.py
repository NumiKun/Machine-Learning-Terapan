# -*- coding: utf-8 -*-
"""projek_akhir_MLT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1USfUXT63vg3IpY0lW2TkQhQYG1cVjj9m

## Import Libraries

### Impor library untuk manipulasi data, visualisasi, ekstraksi fitur teks, dan modeling rekomendasi.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import kagglehub
import os
import shutil
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import LabelEncoder
!pip install scikit-surprise

"""### Menghapus versi numpy yang ada dan menginstal ulang versi 1.26.4 untuk memastikan kompatibilitas dengan library lain."""

!pip uninstall numpy -y
!pip install numpy==1.26.4

"""### Mengimpor modul dari library Surprise untuk membangun model collaborative filtering, termasuk SVD dan fungsi evaluasi."""

from surprise import Dataset, Reader, SVD, accuracy
from surprise.model_selection import train_test_split

"""## Data Loading

### Mengunduh dataset buku dari Kaggle menggunakan `kagglehub`.
"""

source_path = kagglehub.dataset_download("arashnic/book-recommendation-dataset")

"""### Memindahkan dataset yang sudah diunduh ke folder `/content` agar mudah diakses."""

destination_path = '/content/book-recommendation-dataset'

if not os.path.exists(destination_path):
    os.makedirs(destination_path)

for item in os.listdir(source_path):
    s = os.path.join(source_path, item)
    d = os.path.join(destination_path, item)
    if os.path.isdir(s):
        shutil.copytree(s, d)
    else:
        shutil.copy2(s, d)

print(f"Dataset copied to: {destination_path}")

"""## Data Understanding

#### Memuat file CSV buku ke DataFrame dan menampilkan 5 baris pertama untuk melihat struktur data.
"""

books = pd.read_csv('/content/book-recommendation-dataset/Books.csv', low_memory=False)
display(books.head())

"""Insight: Dataset berisi informasi dasar buku seperti ISBN, Judul Buku (Book-Title), Penulis (Book-Author), Tahun Terbit (Year-Of-Publication), dan Penerbit (Publisher). Ada juga beberapa kolom yang berisi URL gambar buku dengan ukuran kecil, sedang, dan besar (Image-URL-S, Image-URL-M, Image-URL-L) yang dapat digunakan untuk tampilan visual.

#### Memuat file CSV berisi data rating pengguna terhadap buku dan menampilkan 5 baris pertama untuk melihat struktur data.
"""

ratings = pd.read_csv('/content/book-recommendation-dataset/Ratings.csv')
display(ratings.head())

"""Insight: Output tersebut menunjukkan data rating buku oleh pengguna, di mana setiap baris merepresentasikan sebuah interaksi antara pengguna (User-ID) dan buku (ISBN) dengan skor rating (Book-Rating) yang diberikan. Terlihat ada nilai rating nol, yang kemungkinan menunjukkan ketidaktertarikan atau interaksi minimal.

#### Memuat file CSV berisi data pengguna dan menampilkan 5 baris pertama untuk melihat struktur data pengguna.
"""

users = pd.read_csv('/content/book-recommendation-dataset/Users.csv')
display(users.head())

"""Insight: Output ini menunjukkan data dasar pengguna dengan kolom User-ID, Location, dan Age. Terlihat bahwa sebagian besar data Age masih kosong (NaN), yang menandakan perlunya penanganan missing value pada kolom umur untuk analisis lebih lanjut.

### Univariate Eksploratory Data Analysis

#### Books Variable

##### Menampilkan ringkasan struktur dataset buku.
"""

print("Info dataset Books:")
print(books.info())

"""Insight: Dataset buku memiliki sekitar 271 ribu entri dengan delapan kolom yang mencakup informasi penting seperti ISBN, judul, penulis, tahun terbit, penerbit, dan beberapa URL gambar buku dengan ukuran berbeda. Sebagian besar kolom memiliki data lengkap tanpa nilai kosong, kecuali beberapa baris pada kolom penulis, penerbit, dan URL gambar berukuran besar yang menunjukkan adanya data hilang yang perlu diperhatikan saat preprocessing. Semua kolom bertipe objek, sehingga beberapa kolom seperti tahun terbit memerlukan konversi tipe data agar dapat diolah secara numerik.

##### Meampilkan Statistik Data Books
"""

print(f"Total data buku: {len(books)}")

for col in ['Book-Title', 'Book-Author', 'Year-Of-Publication', 'Publisher']:
    print(f"\nKolom: {col}")
    print(f"Jumlah nilai unik: {books[col].nunique()}")
    print("5 nilai teratas berdasarkan frekuensi:")
    print(books[col].value_counts().head())

"""Insight: Data buku sangat kaya dan beragam, dengan total sekitar 271 ribu entri dan lebih dari 242 ribu judul unik, menunjukkan bahwa sebagian besar buku hanya muncul satu kali atau sangat sedikit kemunculannya. Beberapa judul klasik seperti Selected Poems dan Little Women termasuk yang paling sering muncul, namun frekuensi tertinggi pun relatif rendah, yaitu puluhan kali saja.

Penulis terkenal seperti Agatha Christie, William Shakespeare, dan Stephen King mendominasi daftar dengan ratusan karya yang terdaftar, memberikan gambaran bahwa karya-karya dari penulis populer memiliki bobot signifikan dalam dataset. Tahun terbit bervariasi antara akhir abad ke-20 dan awal abad ke-21, dengan tahun 2002 sebagai tahun terbit terbanyak, mengindikasikan bahwa dataset ini lebih banyak memuat buku-buku modern.

##### Visualisasi Distribusi Tahun Terbit Buku
"""

books['Year-Of-Publication'] = pd.to_numeric(books['Year-Of-Publication'], errors='coerce')

plt.figure(figsize=(14,6))
sns.histplot(books['Year-Of-Publication'].dropna(), bins=100, kde=False, color='skyblue')
plt.title('Distribusi Tahun Terbit Buku (Semua Tahun)')
plt.xlabel('Year-Of-Publication')
plt.ylabel('Jumlah Buku')
plt.show()

"""Insight: Distribusi tahun terbit buku menunjukkan sebagian besar buku berada pada rentang tahun modern, terutama setelah tahun 1900, dengan lonjakan besar pada tahun-tahun terbaru menjelang tahun 2000-an hingga sekitar 2010-an. Ada juga sejumlah kecil data dengan tahun terbit 0 atau nilai ekstrem, yang mungkin merupakan data tidak valid atau placeholder yang perlu dibersihkan. Pola ini mengindikasikan bahwa koleksi buku dalam dataset lebih banyak memuat karya-karya relatif baru dibandingkan dengan buku-buku klasik atau sangat tua.

##### Visualisasi Publisher dan Penulis Terbanyak
"""

plt.figure(figsize=(14,6))
top_publishers = books['Publisher'].value_counts().head(10)
sns.barplot(x=top_publishers.values, y=top_publishers.index, palette='viridis')
plt.title('10 Publisher Buku Terbanyak')
plt.xlabel('Jumlah Buku')
plt.ylabel('Publisher')
plt.show()

plt.figure(figsize=(14,6))
top_authors = books['Book-Author'].value_counts().head(10)
sns.barplot(x=top_authors.values, y=top_authors.index, palette='magma')
plt.title('10 Penulis Buku Terbanyak')
plt.xlabel('Jumlah Buku')
plt.ylabel('Penulis')
plt.show()

"""Insight:

Dari visualisasi publisher dan penulis terbanyak, dapat disimpulkan beberapa hal penting:

Publisher Teratas: Penerbit seperti Harlequin, Silhouette, dan Pocket mendominasi jumlah buku dalam dataset, dengan Harlequin memiliki jumlah buku terbanyak yang mencapai sekitar 7.500 judul. Ini menunjukkan peran besar penerbit besar dalam menyediakan koleksi buku yang luas dan beragam.

Penulis Teratas: Penulis seperti Agatha Christie, William Shakespeare, dan Stephen King merupakan pengarang dengan jumlah karya terbanyak dalam dataset. Agatha Christie menjadi yang paling produktif dengan lebih dari 600 judul buku. Ini menunjukkan bahwa karya-karya dari penulis populer sangat berpengaruh dan sering muncul dalam dataset.

##### Cek Missing Values pada Dataset Books
"""

print("\nJumlah missing values tiap kolom:")
print(books.isna().sum())

"""Insight: Beberapa kolom dalam dataset buku memiliki nilai yang hilang, meskipun jumlahnya relatif sedikit. Kolom Book-Author dan Publisher masing-masing kehilangan 2 entri, sedangkan Year-Of-Publication dan Image-URL-L kehilangan 3 entri.

#### Ratings Variable

##### Menampilkan ringkasan struktur dataset ratings.
"""

print("Info dataset Ratings:")
print(ratings.info())

"""Insight: Dataset ratings terdiri dari sekitar 1,15 juta entri dengan tiga kolom utama: User-ID, ISBN, dan Book-Rating. Semua kolom tidak memiliki nilai kosong, menunjukkan data lengkap untuk setiap interaksi pengguna dengan buku. Kolom User-ID dan Book-Rating bertipe numerik (int64), sedangkan ISBN bertipe objek, mencerminkan kode unik buku.

##### Meampilkan Statistik Data Ratings
"""

print(f"Jumlah data ratings: {len(ratings)}")
print(f"Jumlah nilai unik rating: {ratings['Book-Rating'].nunique()}")
print("Frekuensi nilai rating (top 10):")
print(ratings['Book-Rating'].value_counts().head(10))

"""Insight: Distribusi rating menunjukkan bahwa nilai 0 mendominasi jumlah rating yang diberikan, yaitu sebanyak lebih dari 700 ribu, yang bisa mengindikasikan pengguna yang tidak memberikan penilaian atau interaksi minimal dengan buku. Rating dengan nilai 8 dan 10 juga cukup sering muncul, menunjukkan preferensi positif yang kuat terhadap beberapa buku. Sedangkan rating di bawah 5 memiliki frekuensi yang lebih rendah, menunjukkan bahwa pengguna cenderung memberikan rating tinggi atau tidak memberikan rating (0).

##### Visualisasi Distribusi Rating Buku
"""

plt.figure(figsize=(10,5))
sns.countplot(x='Book-Rating', data=ratings, palette='coolwarm', order=sorted(ratings['Book-Rating'].unique()))
plt.title('Distribusi Rating Buku')
plt.xlabel('Book-Rating')
plt.ylabel('Jumlah Rating')
plt.show()

"""Insight: Distribusi rating buku menunjukkan bahwa sebagian besar interaksi pengguna berupa rating bernilai 0, yang mungkin mengindikasikan ketidaktertarikan atau rating default. Rating dengan nilai 8, 9, dan 10 juga cukup sering diberikan, menandakan bahwa pengguna cenderung memberikan penilaian positif pada buku yang mereka sukai. Rating rendah (1 hingga 4) jarang muncul, menunjukkan bahwa pengguna lebih sering memberikan rating tinggi atau tidak memberikan rating sama sekali.

##### Cek Missing Values pada Dataset Ratings
"""

print("\nJumlah missing values tiap kolom:")
print(ratings.isna().sum())

"""Insight: Dataset ratings tidak memiliki missing value yang perlu ditangani.

#### Users Variable

##### Menampilkan ringkasan struktur dataset users.
"""

print("Info dataset Users:")
print(users.info())

"""Insight: Dataset pengguna berisi sekitar 278 ribu entri dengan tiga kolom utama: User-ID, Location, dan Age. Kolom User-ID dan Location lengkap tanpa nilai kosong, sementara kolom Age memiliki sekitar 110 ribu nilai yang hilang, menunjukkan kebutuhan penanganan missing value pada usia pengguna.

##### Meampilkan Statistik Data Users
"""

print(f"Total data users: {len(users)}")

for col in ['User-ID', 'Location']:
    if col in users.columns:
        print(f"\nKolom: {col}")
        print(f"Jumlah nilai unik: {users[col].nunique()}")
        print("5 nilai teratas berdasarkan frekuensi:")
        print(users[col].value_counts().head())

"""Insight: Dataset pengguna terdiri dari sekitar 278 ribu entri dengan setiap User-ID unik, menunjukkan bahwa setiap baris mewakili pengguna berbeda tanpa duplikasi. Kolom Location memiliki lebih dari 57 ribu nilai unik, mencerminkan keberagaman geografis yang sangat luas. Lokasi yang paling sering muncul adalah kota-kota besar dan populer seperti London, Toronto, Sydney, Melbourne, dan Portland, yang menunjukkan konsentrasi pengguna utama berada di wilayah perkotaan besar di berbagai negara.

##### Visualisasi Distribusi Users
"""

if 'Location' in users.columns:
    plt.figure(figsize=(14,6))
    top_locations = users['Location'].value_counts().head(10)
    sns.barplot(x=top_locations.values, y=top_locations.index, palette='crest')
    plt.title('10 Lokasi User Terbanyak')
    plt.xlabel('Jumlah User')
    plt.ylabel('Lokasi')
    plt.show()

"""Insight: Visualisasi menunjukkan bahwa pengguna dalam dataset paling banyak berasal dari kota-kota besar di berbagai negara, dengan London, Inggris sebagai lokasi terbanyak, diikuti oleh Toronto (Kanada), Sydney dan Melbourne (Australia), serta beberapa kota besar di Amerika Serikat seperti Portland, Chicago, Seattle, dan New York. Keberadaan kota-kota besar ini sebagai pusat pengguna menunjukkan konsentrasi tinggi pada wilayah urban dan dapat memberikan gambaran demografis yang penting untuk personalisasi dan segmentasi dalam sistem rekomendasi.

##### Cek Missing Values pada Dataset Users
"""

print("\nJumlah missing values tiap kolom:")
print(users.isna().sum())

"""Insight: Sebagian besar data kolom Age pada dataset pengguna hilang, dengan sekitar 110 ribu nilai kosong, sedangkan kolom User-ID dan Location lengkap tanpa missing value.

## Data Preparation

### Menangani Missing Values

#### Menangani Missing Values pada Books Variable

##### Mengisi nilai kosong pada kolom `Book-Author` dan `Publisher` dengan label default 'Unknown Author' dan 'Unknown Publisher'
"""

books['Book-Author'] = books['Book-Author'].fillna('Unknown Author')
books['Publisher'] = books['Publisher'].fillna('Unknown Publisher')

"""##### Mengisi nilai kosong pada kolom `Year-Of-Publication` dengan nilai median tahun terbit"""

median_year = books['Year-Of-Publication'].median()
books['Year-Of-Publication'] = books['Year-Of-Publication'].fillna(median_year).astype(int)

"""##### Mengisi nilai kosong pada kolom `Image-URL-L` dengan teks 'No Image'"""

books['Image-URL-L'] = books['Image-URL-L'].fillna('No Image')

"""##### Mengecek kembali Missing Value"""

print(books.isna().sum())

"""Insight: Missing Value pada books variable berhasil diatasi.

#### Menangani Missing Values pada Ratings Variable
"""

print("Missing values di Ratings:")
print(ratings.isna().sum())

"""Insight: Variable Ratings tidak memiliki missing value.

#### Menangani Missing Values pada Users Variable

##### Mengisi nilai kosong pada kolom `Age` dengan nilai median usia pengguna
"""

median_age = users['Age'].median()
users['Age'] = users['Age'].fillna(median_age).astype(int)

"""##### Mengecek kembali missing value"""

print(users.isna().sum())

"""Insight: Missing value pada users variable berhasil diatasi

### Memfilter dataset rating untuk hanya mengambil baris dengan nilai `Book-Rating` lebih dari 0
"""

df = ratings[ratings['Book-Rating'] > 0][['User-ID', 'ISBN', 'Book-Rating']]

"""### Mendefinisikan skala rating dari 1 sampai 10 dan memuat dataset rating ke format yang sesuai"""

reader = Reader(rating_scale=(1, 10))
data = Dataset.load_from_df(df, reader)

"""### Membagi Data Training dan Testing"""

trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

"""## Model Development Collaborative Filtering dengan Algoritma SVD

### Membuat dan Melatih Model SVD
"""

model = SVD(n_factors=50, n_epochs=30, random_state=42)
model.fit(trainset)

"""### Membuat Fungsi Rekomendasi Buku untuk User"""

def recommend_books_for_user(user_id, model, df, n=10):
    all_books = df['ISBN'].unique()
    books_rated_by_user = df[df['User-ID'] == user_id]['ISBN'].values
    books_to_predict = [book for book in all_books if book not in books_rated_by_user]
    predictions = [model.predict(user_id, book) for book in books_to_predict]
    predictions.sort(key=lambda x: x.est, reverse=True)
    top_preds = predictions[:n]
    recommended_books = []
    for pred in top_preds:
        book_info_df = books[books['ISBN'] == pred.iid]
        if not book_info_df.empty:
            book_info = book_info_df.iloc[0]
            recommended_books.append({
                'ISBN': pred.iid,
                'Book-Title': book_info['Book-Title'],
                'Book-Author': book_info['Book-Author'],
                'Estimated Rating': pred.est
            })
        else:
            pass
    return pd.DataFrame(recommended_books)

"""### Menguji Sistem Rekomendasi untuk User"""

user_id = 276772  # ganti ID dan run untuk mendapat rekomendasi

books_read_by_user = df[df['User-ID'] == user_id].merge(books[['ISBN', 'Book-Title', 'Book-Author']], on='ISBN')

print(f"Books read by User-ID {user_id}:")
if not books_read_by_user.empty:
    display(books_read_by_user[['Book-Title', 'Book-Author', 'Book-Rating']])
else:
    print("This user has not rated any books.")

recommendations = recommend_books_for_user(user_id, model, df, n=10)

print(f"\nRecommended books for User-ID {user_id}:")
if not recommendations.empty:
    display(recommendations)
else:
    print("No recommendations found for this user.")

"""Insight: Pengguna dengan User-ID 276772 telah memberikan rating pada tiga buku dengan skor tinggi, menunjukkan preferensi yang kuat terhadap genre atau penulis tertentu. Rekomendasi yang dihasilkan oleh model SVD menyajikan daftar buku dengan prediksi rating tinggi, yang meliputi karya populer dan penulis terkenal seperti J.K. Rowling, Dan Brown, J.R.R. Tolkien, dan Stephen King. Hal ini menunjukkan bahwa model berhasil menangkap preferensi pengguna dan menyarankan buku yang relevan dan berkualitas tinggi sesuai minat mereka.

## Evaluasi Model dengan RMSE
"""

predictions = model.test(testset)
rmse = accuracy.rmse(predictions)

"""Insight: Hasil evaluasi model dengan RMSE sebesar 1.6401 menunjukkan bahwa model memiliki tingkat kesalahan yang tergolong moderat dan dapat diterima mengingat kompleksitas dan karakteristik dataset yang sangat beragam. Preferensi pengguna yang beragam dan distribusi rating yang tidak merata, termasuk banyaknya rating nol, menyulitkan model dalam memprediksi dengan presisi tinggi. Selain itu, model hanya mengandalkan data rating tanpa fitur pendukung seperti genre atau demografi pengguna, sehingga keterbatasan informasi ini juga memengaruhi akurasi prediksi. Kebisingan dan inkonsistensi dalam dataset yang besar turut menjadi faktor yang menyumbang tingginya nilai error"""