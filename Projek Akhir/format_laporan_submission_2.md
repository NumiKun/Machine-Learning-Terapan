# Laporan Proyek Machine Learning - Rizki Surya Nugroho
---
## Project Overview

Sistem rekomendasi telah menjadi bagian integral dari pengalaman digital modern, mengubah cara produk, layanan, dan informasi ditemukan di berbagai platform [1]. Mulai dari platform *e-commerce* seperti Amazon dan Netflix, hingga media sosial seperti YouTube dan Spotify, sistem rekomendasi bertujuan untuk memprediksi preferensi pengguna dan menyajikan item yang relevan dan menarik. Di sektor literatur, di mana jutaan buku diterbitkan setiap tahunnya, tantangan bagi pembaca untuk menemukan judul yang sesuai dengan minat mereka semakin besar. Dalam konteks ini, sistem rekomendasi buku memiliki peran krusial untuk mengatasi *information overload* dan memfasilitasi penemuan literatur baru.

Tanpa sistem rekomendasi yang efektif, pembaca sering kali kesulitan menavigasi lautan buku yang tersedia. Pembaca mungkin terpaku pada penulis atau genre yang sudah dikenal, atau bahkan melewatkan karya-karya yang berpotensi menjadi favorit karena kurangnya visibilitas. Masalah *information overload* ini tidak hanya menghambat pengalaman pembaca tetapi juga membatasi eksposur bagi penulis baru dan judul-judul yang kurang populer. Sebuah sistem rekomendasi buku yang efisien dapat memecahkan masalah ini dengan menganalisis preferensi membaca pengguna di masa lalu dan pola interaksi mereka dengan buku-buku lain, kemudian menyarankan judul-judul yang kemungkinan besar akan disukai.

Riset menunjukkan bahwa sistem rekomendasi yang dipersonalisasi secara signifikan meningkatkan kepuasan pengguna dan keterlibatan dengan platform. Sebuah studi yang diterbitkan dalam *GSC Advanced Research and Reviews* menyoroti bahwa rekomendasi produk yang disesuaikan dapat meningkatkan niat beli dan loyalitas pelanggan [2]. Khususnya dalam konteks buku, rekomendasi yang akurat dapat mendorong pembaca untuk menjelajahi genre baru, menemukan penulis yang belum dikenal, dan memperluas cakrawala literatur mereka. Hal ini tidak hanya menguntungkan pembaca tetapi juga para penerbit dan penulis dengan meningkatkan penjualan dan visibilitas.

Dalam proyek ini, sistem rekomendasi buku dikembangkan menggunakan pendekatan *collaborative filtering* dengan algoritma Singular Value Decomposition (SVD). Pendekatan ini dipilih karena efektivitasnya dalam mengidentifikasi pola tersembunyi dalam data interaksi pengguna-item (dalam kasus ini, pengguna-buku). SVD bekerja dengan mendekomposisi matriks rating besar menjadi komponen-komponen yang lebih kecil, yang memungkinkan sistem untuk menangkap preferensi implisit pengguna dan karakteristik buku secara lebih efisien [3]. Dengan memodelkan hubungan antara pengguna dan buku berdasarkan rating yang telah diberikan, sistem dapat memprediksi rating yang mungkin diberikan pengguna untuk buku-buku yang belum pernah mereka baca, sehingga menghasilkan rekomendasi yang dipersonalisasi.

Tujuan utama dari sistem ini adalah untuk menyediakan rekomendasi buku yang relevan dan meningkatkan pengalaman penemuan literatur bagi pengguna. Sistem ini diharapkan dapat membantu pembaca menemukan buku-buku yang tidak hanya sesuai dengan selera mereka tetapi juga memperkenalkan mereka pada berbagai judul dan penulis yang mungkin tidak akan ditemukan melalui metode pencarian tradisional.

### Referensi:
[1] Syahputra, F., Siregar, A. T. A., Nainggolan, Y. S. A., Purba, A. L., Sinurat, A. A. B., Hutauruk, K. R., ... & Permadi, S. (2025). E-Commerce dan V-Bisnis Perusahaan Digital di Abad Kedua Puluh Satu. Tangguh Denara Jaya Publisher.
[2] Raji, M. A., Olodo, H. B., Oke, T. T., Addy, W. A., Ofodile, O. C., & Oyewole, A. T. (2024). E-commerce and consumer behavior: A review of AI-powered personalization and market trends. GSC Advanced Research and Reviews, 18(3), 066-077.
[3] Koren, Y., Bell, R., & Volinsky, C. (2009). Matrix factorization techniques for recommender systems. Computer, 42(8), 30-37.

---

## Business Understanding

Bagian ini menguraikan proses klarifikasi masalah yang mendasari pengembangan sistem rekomendasi buku. Identifikasi masalah yang jelas merupakan langkah fundamental untuk memastikan bahwa solusi yang dibangun benar-benar relevan dan efektif dalam memenuhi kebutuhan pengguna.

### Problem Statements

Pernyataan masalah berikut menggarisbawahi tantangan utama yang dihadapi dalam ekosistem literatur digital, yang menjadi dasar perlunya sistem rekomendasi:

* **P1: Kesulitan Pengguna dalam Penemuan Buku yang Relevan (Information Overload):** Dalam era digital, pembaca dihadapkan pada volume buku yang sangat besar. Tanpa panduan yang efektif, mereka seringkali kesulitan menemukan buku-buku baru yang sesuai dengan minat dan preferensi mereka, yang dapat menyebabkan kelelahan informasi dan kurangnya eksplorasi genre atau penulis baru.
* **P2: Kurangnya Personalisasi dalam Rekomendasi Buku Konvensional:** Metode rekomendasi buku konvensional, seperti daftar *bestseller* atau kategori generik, seringkali tidak mencerminkan preferensi individu pembaca. Hal ini mengakibatkan rekomendasi yang kurang relevan dan potensi hilangnya pengalaman membaca yang menyenangkan.
* **P3: Visibilitas Rendah untuk Buku Baru atau Kurang Populer:** Buku-buku yang baru dirilis atau yang tidak memiliki popularitas massal cenderung sulit ditemukan oleh pembaca, meskipun mungkin sangat relevan dengan minat niche tertentu. Ini menghambat diversitas bacaan dan membatasi eksposur bagi penulis dan penerbit.

### Goals

Tujuan proyek ini dirumuskan untuk secara langsung menjawab pernyataan masalah yang telah diidentifikasi, dengan fokus pada pengembangan sistem rekomendasi yang efektif dan bermanfaat:

* **G1: Menyediakan Rekomendasi Buku yang Dipersonalisasi:** Tujuan utama adalah mengembangkan sistem yang mampu menganalisis pola interaksi dan preferensi membaca pengguna untuk menyajikan rekomendasi buku yang sangat relevan dan disesuaikan secara individual. Ini diharapkan dapat mengurangi *information overload* dan meningkatkan efisiensi penemuan buku.
* **G2: Meningkatkan Keterlibatan Pengguna dengan Konten Literatur:** Sistem ini bertujuan untuk meningkatkan frekuensi dan kualitas interaksi pengguna dengan platform buku. Dengan memberikan rekomendasi yang menarik, diharapkan dapat mendorong pengguna untuk membaca lebih banyak, menjelajahi genre yang lebih luas, dan merasa lebih puas dengan pengalaman penemuan buku mereka.
* **G3: Meningkatkan Visibilitas dan Aksesibilitas Buku:** Proyek ini bertujuan untuk memberikan eksposur yang lebih besar bagi buku-buku yang mungkin terlewatkan dalam pencarian konvensional. Dengan merekomendasikan judul-judul yang relevan berdasarkan preferensi yang teridentifikasi, sistem ini dapat membantu pembaca menemukan permata tersembunyi dan mendukung penulis maupun penerbit dari berbagai skala.

---

## Data Understanding

Bagian ini bertujuan untuk memberikan pemahaman menyeluruh tentang dataset yang digunakan dalam proyek sistem rekomendasi buku ini. Dataset ini diperoleh dari Kaggle dan dapat diunduh melalui tautan berikut: [Book-Recommendation-Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset). Dataset ini terdiri dari tiga tabel utama: `Books`, `Ratings`, dan `Users`, yang saling berhubungan melalui kolom `ISBN` dan `User-ID`.

### Gambaran Umum Dataset

Dataset `Books` berisi informasi dasar tentang buku, sementara `Ratings` mencatat interaksi pengguna dengan buku, dan `Users` menyimpan data demografi pengguna. Secara keseluruhan, dataset ini mencerminkan aktivitas membaca dan penilaian buku oleh berbagai pengguna. Kondisi awal data menunjukkan adanya *missing values* pada beberapa kolom di tabel `Books` dan `Users`, serta distribusi rating yang tidak merata, yang memerlukan tahap *data preparation* lebih lanjut.

### Deskripsi Variabel

Variabel-variabel yang terdapat dalam masing-masing dataset adalah sebagai berikut:

**1. Books Variable**
Dataset `Books` memiliki sekitar 271.360 entri dengan delapan kolom yang mencakup informasi penting tentang buku. Semua kolom bertipe objek, kecuali 'Year-Of-Publication' yang perlu dikonversi ke numerik.

* **ISBN**: *International Standard Book Number*, merupakan kode unik untuk setiap buku.
* **Book-Title**: Judul buku.
* **Book-Author**: Nama penulis buku.
* **Year-Of-Publication**: Tahun buku diterbitkan.
* **Publisher**: Nama penerbit buku.
* **Image-URL-S**: URL gambar sampul buku ukuran kecil.
* **Image-URL-M**: URL gambar sampul buku ukuran sedang.
* **Image-URL-L**: URL gambar sampul buku ukuran besar.

**2. Ratings Variable**
Dataset `Ratings` terdiri dari sekitar 1.149.780 entri yang merepresentasikan interaksi pengguna dengan buku.

* **User-ID**: Kode identifikasi unik untuk setiap pengguna.
* **ISBN**: Kode unik buku yang diberi rating oleh pengguna.
* **Book-Rating**: Rating numerik yang diberikan oleh pengguna untuk buku tertentu (skala 0-10).

**3. Users Variable**
Dataset `Users` berisi informasi demografi pengguna dengan sekitar 278.858 entri.

* **User-ID**: Kode identifikasi unik untuk setiap pengguna.
* **Location**: Lokasi geografis pengguna.
* **Age**: Usia pengguna.

---

## Data Preparation

Tahap *data preparation* merupakan langkah esensial dalam siklus proyek ilmu data, bertujuan untuk membersihkan, mengubah, dan memformat data agar siap digunakan untuk pemodelan. Dalam proyek ini, proses *data preparation* difokuskan pada penanganan *missing values* dan penyesuaian tipe data pada dataset `Books` dan `Users`, serta pemfilteran dan pembagian data pada dataset `Ratings`. Tahapan ini diperlukan untuk memastikan kualitas data, konsistensi, dan kesesuaian untuk pembangunan model sistem rekomendasi.

### 1. Menangani Missing Values pada Dataset `Books`

Dataset `Books` pada awalnya ditemukan memiliki beberapa *missing values* pada kolom `Book-Author`, `Publisher`, `Year-Of-Publication`, dan `Image-URL-L`. Penanganan nilai yang hilang ini dilakukan untuk mencegah masalah saat pemrosesan data dan pemodelan, karena nilai yang kosong dapat menyebabkan kesalahan atau bias dalam analisis.

* **Kolom `Book-Author` dan `Publisher`:**
    * **Proses:** Nilai kosong pada kolom `Book-Author` diisi dengan string 'Unknown Author', dan pada kolom `Publisher` diisi dengan 'Unknown Publisher'.
    * **Alasan:** Menggunakan label 'Unknown' merupakan pendekatan yang tepat ketika nilai yang hilang tidak dapat diimputasi dengan akurat dari data lain. Ini mempertahankan baris data yang relevan dan memberikan informasi bahwa penulis atau penerbit tidak tersedia, daripada menghapus baris yang mungkin memiliki informasi penting lainnya.

* **Kolom `Year-Of-Publication`:**
    * **Proses:** Kolom ini terlebih dahulu dikonversi ke tipe data numerik dengan *coerce* error (nilai tidak valid akan menjadi NaN), kemudian nilai kosong yang muncul diisi dengan nilai median dari kolom `Year-Of-Publication` yang valid, dan terakhir tipe datanya dikonversi menjadi integer (`int`).
    * **Alasan:** Pengisian *missing values* dengan median adalah metode yang robust terhadap *outlier* dibandingkan rata-rata, sehingga lebih representatif untuk distribusi data tahun terbit. Konversi ke tipe data numerik dan kemudian integer memastikan konsistensi format dan kesiapan untuk operasi numerik.

* **Kolom `Image-URL-L`:**
    * **Proses:** Nilai kosong pada kolom `Image-URL-L` diisi dengan string 'No Image'.
    * **Alasan:** Kolom ini berisi URL gambar, dan nilai yang hilang hanya menunjukkan bahwa URL gambar berukuran besar tidak tersedia. Mengisi dengan 'No Image' secara eksplisit menyatakan kondisi tersebut tanpa membuang informasi lain dari baris data.

Setelah semua langkah di atas, pengecekan ulang menunjukkan bahwa tidak ada lagi *missing values* pada dataset `Books`.

### 2. Menangani Missing Values pada Dataset `Ratings`

Dataset `Ratings` diperiksa untuk keberadaan *missing values* dan ditemukan bahwa tidak ada nilai yang hilang pada kolom `User-ID`, `ISBN`, maupun `Book-Rating`. Oleh karena itu, tidak ada tindakan khusus yang diperlukan untuk penanganan *missing values* pada dataset ini.

### 3. Menangani Missing Values pada Dataset `Users`

Dataset `Users` memiliki jumlah *missing values* yang signifikan pada kolom `Age`.

* **Kolom `Age`:**
    * **Proses:** Nilai kosong pada kolom `Age` diisi dengan nilai median dari kolom `Age` yang ada, kemudian tipe datanya dikonversi menjadi integer (`int`).
    * **Alasan:** Penggunaan median lebih cocok untuk data usia yang mungkin memiliki distribusi tidak normal atau *outlier* (misalnya, usia yang sangat muda atau sangat tua yang tidak representatif). Konversi ke integer menjaga integritas format data usia dan konsistensi tipe data.

Setelah langkah ini, pengecekan ulang menunjukkan bahwa tidak ada lagi *missing values* pada dataset `Users`.

### 4. Pemfilteran Data Rating dan Pembagian Dataset untuk Pemodelan

Sebelum model *collaborative filtering* dibangun, dataset `Ratings` menjalani pemfilteran dan persiapan khusus untuk framework Surprise.

* **Pemfilteran Rating Positif:**
    * **Proses:** Dataset `ratings` difilter untuk hanya menyertakan baris dengan nilai `Book-Rating` lebih besar dari 0. Hanya kolom `User-ID`, `ISBN`, dan `Book-Rating` yang dipilih untuk pemodelan.
    * **Alasan:** Mayoritas rating dalam dataset asli adalah 0, yang kemungkinan besar tidak merepresentasikan minat atau preferensi aktif pengguna terhadap buku. Rating 0 bisa berarti pengguna hanya melihat buku tersebut tanpa memberikan penilaian yang berarti, atau rating tersebut adalah nilai *default* untuk interaksi yang tidak jelas. Untuk model rekomendasi berbasis preferensi, rating positif (1-10) lebih informatif karena secara eksplisit menunjukkan tingkat kesukaan atau ketidaksukaan pengguna. Dengan memfilter rating 0, model dapat belajar dari interaksi yang lebih bermakna, sehingga diharapkan menghasilkan rekomendasi yang lebih relevan dan akurat.

* **Persiapan Data untuk Library Surprise:**
    * **Proses:** Skala rating didefinisikan dari 1 hingga 10 menggunakan objek `Reader`, dan data kemudian dimuat ke dalam objek `Dataset` yang sesuai dengan format library Surprise.
    * **Alasan:** Library Surprise membutuhkan data dalam format spesifik `(user_id, item_id, rating)` dan definisi skala rating untuk operasi internal serta normalisasi yang benar pada algoritma rekomendasi.

* **Pembagian Data Training dan Testing:**
    * **Proses:** Dataset yang sudah disiapkan kemudian dibagi menjadi *trainset* dan *testset* menggunakan fungsi `train_test_split`. Proporsi yang digunakan adalah 80% untuk *training* dan 20% untuk *testing*. Parameter `random_state=42` digunakan untuk memastikan reproduktibilitas pembagian data.
    * **Alasan:** Pembagian ini memungkinkan evaluasi objektif terhadap kinerja model pada data yang belum pernah dilihat sebelumnya, mencegah *overfitting*, dan memberikan indikasi seberapa baik model akan bekerja pada data dunia nyata.

## Modeling

Tahap ini membahas perancangan dan implementasi model sistem rekomendasi yang bertujuan untuk menyelesaikan permasalahan penemuan buku yang relevan bagi pengguna. Dalam proyek ini, pendekatan *collaborative filtering* digunakan sebagai dasar pembangunan sistem rekomendasi, dengan mengimplementasikan algoritma Singular Value Decomposition (SVD).

### 1. Pendekatan Collaborative Filtering

*Collaborative filtering* adalah teknik yang populer dalam sistem rekomendasi yang bekerja dengan mengidentifikasi pola preferensi dari banyak pengguna. Pendekatan ini secara fundamental terbagi menjadi dua kategori utama: *user-based* dan *item-based*. Model yang dibangun dalam proyek ini memanfaatkan prinsip-prinsip ini dengan menemukan pengguna dengan selera serupa (atau item yang dinilai serupa) untuk membuat rekomendasi.

### 2. Algoritma Singular Value Decomposition (SVD)

Singular Value Decomposition (SVD) adalah algoritma faktorisasi matriks yang digunakan untuk mengurangi dimensi matriks rating pengguna-item. Ini bekerja dengan mendekomposisi matriks rating besar menjadi komponen-komponen yang lebih kecil, yang memungkinkan model untuk menangkap preferensi implisit pengguna dan karakteristik buku secara lebih efisien. Dengan menemukan faktor-faktor ini, SVD dapat memprediksi rating untuk buku-buku yang belum pernah dinilai oleh pengguna, bahkan dalam kasus data yang sangat *sparse* (banyak nilai kosong).

### 3. Pembangunan dan Pelatihan Model SVD

Setelah proses *data preparation* selesai, model SVD diinisialisasi dan dilatih menggunakan *trainset* yang telah dipersiapkan sebelumnya.

* **Inisialisasi Model:** Model SVD diinisialisasi dengan parameter `n_factors=50` dan `n_epochs=30`. Parameter `n_factors` (jumlah faktor laten) menentukan kompleksitas model dan seberapa banyak fitur tersembunyi yang akan dipelajari dari data. Sementara `n_epochs` (jumlah iterasi pelatihan) mengontrol berapa kali algoritma akan mengulang proses pelatihan pada seluruh *trainset*. `random_state=42` digunakan untuk memastikan reproduktibilitas hasil pelatihan.
* **Proses Pelatihan:** Model dilatih dengan menggunakan `trainset` yang berisi data rating yang difilter (rating > 0). Proses `fit` ini memungkinkan SVD untuk mempelajari pola rating dari interaksi pengguna-buku yang sudah ada.

### 4. Fungsi Rekomendasi Buku untuk User

Sebuah fungsi (`recommend_books_for_user`) dikembangkan untuk menghasilkan rekomendasi buku berdasarkan model SVD yang telah dilatih. Fungsi ini bekerja dengan langkah-langkah berikut:

1.  **Identifikasi Buku yang Belum Dinilai:** Mengumpulkan semua ISBN buku yang ada dalam dataset dan membandingkannya dengan buku-buku yang telah dinilai oleh *user_id* yang diberikan.
2.  **Prediksi Rating:** Untuk setiap buku yang belum dinilai oleh pengguna, model SVD akan memprediksi rating yang kemungkinan akan diberikan oleh pengguna tersebut.
3.  **Pengurutan dan Pemilihan Top-N:** Hasil prediksi rating diurutkan secara menurun berdasarkan nilai prediksi rating (*estimated rating*). Fungsi kemudian memilih N buku teratas dengan prediksi rating tertinggi.
4.  **Penggabungan Informasi Buku:** Informasi detail seperti judul buku dan penulis dari dataset `Books` digabungkan dengan hasil prediksi untuk menyajikan rekomendasi yang lengkap.

#### Contoh Rekomendasi untuk Pengguna (User-ID 276772)

Untuk mendemonstrasikan kemampuan model, rekomendasi dihasilkan untuk `User-ID 276772`.

**Buku yang Sudah Dibaca oleh User-ID 276772:**
| Book-Title                                   | Book-Author             | Book-Rating |
| :------------------------------------------- | :---------------------- | :---------- |
| Pay Dirt (Mrs. Murphy Mysteries (Paperback)) | RITA MAE BROWN          | 7           |
| Adressat unbekannt.                          | Kathrine Kressmann Taylor | 10          |
| Henry der Held.                              | Roddy Doyle             | 10          |

**Rekomendasi Buku untuk User-ID 276772:**
| ISBN       | Book-Title                                          | Book-Author  | Estimated Rating |
| :--------- | :-------------------------------------------------- | :----------- | :--------------- |
| 0811824829 | 52 Deck Series: 52 Ways to Celebrate Friendship     | Lynn Gordon  | 9.766852         |
| 0743454529 | My Sister's Keeper : A Novel (Picoult, Jodi)      | Jodi Picoult | 9.746502         |
| 0385504209 | The Da Vinci Code                                   | Dan Brown    | 9.721862         |
| 0441172717 | Dune (Remembering Tomorrow)                         | Frank Herbert | 9.667607         |
| 0439136369 | Harry Potter and the Prisoner of Azkaban (Book 3)   | J. K. Rowling | 9.656759         |
| 0836213319 | Dilbert: A Book of Postcards                        | Scott Adams  | 9.652009         |
| 1880418568 | Wolves of the Calla (The Dark Tower, Book 5)        | Stephen King | 9.600803         |
| 0316779059 | The Baby Book: Everything You Need to Know Abo...   | Martha Sears | 9.549683         |

Hasil rekomendasi menunjukkan buku-buku dengan prediksi rating tinggi, yang meliputi karya-karya populer dari penulis terkenal. Ini mengindikasikan bahwa model SVD berhasil mengidentifikasi preferensi pengguna berdasarkan riwayat rating dan menyarankan buku yang relevan.

### 5. Kelebihan dan Kekurangan Pendekatan SVD

**Kelebihan:**

* **Mampu Menemukan Pola Tersembunyi (Latent Factors):** SVD sangat efektif dalam menemukan faktor-faktor laten yang tidak terduga antara pengguna dan item, yang mungkin tidak terlihat dari data mentah. Ini memungkinkan rekomendasi yang lebih cerdas dan personal.
* **Menangani Data Sparse:** SVD dapat bekerja dengan baik pada matriks rating yang *sparse* (banyak nilai kosong), umum terjadi pada sistem rekomendasi di mana pengguna hanya menilai sebagian kecil dari total item.
* **Personalisasi Tinggi:** Dengan memproyeksikan preferensi pengguna dan karakteristik item ke dalam ruang dimensi yang lebih rendah (faktor laten), SVD dapat memberikan rekomendasi yang sangat dipersonalisasi.

**Kekurangan:**

* **Masalah *Cold Start*:** SVD menghadapi masalah *cold start* untuk pengguna dan item baru. Pengguna baru tidak memiliki riwayat rating sehingga model tidak dapat memprediksi preferensinya, dan buku baru tidak memiliki rating sehingga tidak dapat direkomendasikan secara efektif.
* **Skalabilitas:** Meskipun SVD dapat menangani data *sparse*, komputasi untuk dekomposisi matriks besar dapat menjadi sangat mahal dan memakan waktu, terutama pada dataset dengan jutaan pengguna dan item.
* **Interpretasi Faktor Laten yang Sulit:** Faktor-faktor laten yang ditemukan oleh SVD seringkali abstrak dan sulit diinterpretasikan secara intuitif (misalnya, apa arti "faktor laten ke-3" pada preferensi buku?).
* **Ketergantungan pada Data Rating:** Akurasi model sangat bergantung pada kualitas dan kuantitas data rating. Jika ada bias dalam rating atau terlalu banyak rating nol yang tidak informatif, performa model dapat terpengaruh.

---

## Evaluation

Tahap evaluasi bertujuan untuk mengukur kinerja model sistem rekomendasi yang telah dibangun. Dalam proyek ini, metrik evaluasi yang digunakan adalah Root Mean Squared Error (RMSE).

### 1. Metrik Evaluasi: Root Mean Squared Error (RMSE)

Root Mean Squared Error (RMSE) adalah metrik yang umum digunakan untuk mengukur perbedaan antara nilai prediksi model dan nilai aktual. Dalam konteks sistem rekomendasi, RMSE mengukur seberapa akurat model dalam memprediksi rating buku yang diberikan oleh pengguna.

#### Formula RMSE

RMSE dihitung dengan formula berikut:

![RMSE Formula](https://miro.medium.com/v2/resize:fit:966/1*lqDsPkfXPGen32Uem1PTNg.png)

Di mana:
* n: Jumlah total data poin.
* yi: Nilai rating aktual (terobservasi).
* yi_bertopi: Nilai prediksi rating oleh model.

RMSE memberikan bobot yang lebih besar pada kesalahan prediksi yang besar, sehingga sangat sensitif terhadap *outlier*. Semakin kecil nilai RMSE, semakin baik performa model. Nilai RMSE 0 mengindikasikan bahwa model memprediksi rating dengan sempurna.

### 2. Hasil Evaluasi Model

Setelah model SVD dilatih, performanya dievaluasi menggunakan *testset* yang telah dipersiapkan sebelumnya. Evaluasi dilakukan dengan menghitung RMSE antara rating prediksi model dan rating aktual dalam *testset*.

Hasil evaluasi menunjukkan bahwa model SVD mencapai **RMSE sebesar 1.6401**.

### 3. Interpretasi Hasil

Nilai RMSE sebesar 1.6401 menunjukkan bahwa secara rata-rata, prediksi rating model memiliki kesalahan sekitar 1.64 poin dari rating aktual. Dalam konteks skala rating 1-10, tingkat kesalahan ini dapat diinterpretasikan sebagai moderat.

Beberapa faktor yang mungkin memengaruhi nilai RMSE ini:

* **Kompleksitas Dataset:** Dataset buku dan rating memiliki kompleksitas yang tinggi, dengan variasi preferensi pengguna yang luas dan distribusi rating yang tidak merata (banyak rating 0).
* **Keterbatasan Fitur:** Model *collaborative filtering* hanya menggunakan data interaksi pengguna-buku (rating) untuk membuat prediksi. Kurangnya informasi tambahan seperti genre buku, demografi pengguna, atau konteks interaksi dapat membatasi akurasi model.
* **Distribusi Rating:** Sebagian besar rating dalam dataset adalah 0, yang mungkin tidak mencerminkan preferensi pengguna yang sebenarnya. Meskipun rating 0 telah difilter dalam tahap *data preparation*, dampaknya pada model tetap ada.

### 4. Kesimpulan

Meskipun nilai RMSE sebesar 1.6401 menunjukkan adanya tingkat kesalahan moderat, model SVD yang dibangun telah berhasil mempelajari pola preferensi pengguna dan memberikan rekomendasi yang relevan, seperti yang ditunjukkan oleh contoh rekomendasi untuk User-ID 276772. Untuk meningkatkan performa model di masa mendatang, beberapa strategi dapat dipertimbangkan:

* **Penggunaan Informasi Tambahan:** Menggabungkan *collaborative filtering* dengan pendekatan *content-based filtering* (yang memanfaatkan informasi tentang buku itu sendiri, seperti genre, penulis, atau deskripsi) dapat meningkatkan akurasi dan mengatasi masalah *cold start*.
* **Tuning Hyperparameter:** Melakukan *tuning* parameter model SVD (seperti jumlah faktor laten atau *learning rate*) dapat menghasilkan konfigurasi model yang lebih optimal.
* **Penanganan Rating 0:** Mengeksplorasi cara yang lebih canggih untuk menangani rating 0, misalnya dengan menganggapnya sebagai *missing values* atau menggunakan metode *imputation* yang lebih kompleks.

---

**---Ini adalah bagian akhir laporan---**
