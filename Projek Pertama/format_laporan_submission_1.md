# Laporan Proyek Machine Learning - Rizki Surya Nugroho

---

## Domain Proyek

Kanker payudara merupakan salah satu penyakit kanker dengan tingkat prevalensi tertinggi di dunia dan menjadi penyebab utama kematian pada wanita secara global (World Health Organization, 2021). Deteksi dini kanker payudara sangat krusial untuk meningkatkan peluang kesembuhan dan menurunkan angka kematian (Marindrawati et al., 2023). Namun, proses diagnosis konvensional sering kali memerlukan pemeriksaan laboratorium dan citra medis yang memakan waktu dan biaya tinggi. Oleh karena itu, pengembangan metode prediksi berbasis data dan machine learning menjadi solusi potensial untuk mendukung diagnosis secara cepat dan akurat.

Proyek ini bertujuan mengimplementasikan predictive analytics menggunakan dataset kanker payudara untuk membangun model klasifikasi yang mampu membedakan antara jaringan jinak dan ganas secara otomatis. Pemanfaatan metode ini dapat membantu tenaga medis dalam pengambilan keputusan diagnosis yang lebih efisien, mengurangi beban kerja, dan meningkatkan akses layanan kesehatan terutama di daerah dengan keterbatasan sumber daya.

Berbagai penelitian terdahulu menunjukkan efektivitas penggunaan machine learning dalam menganalisis dataset kanker payudara, seperti yang dilakukan oleh Chazar dan Erawan (2020) yang menggunakan metode klasifikasi dengan akurasi tinggi. Oleh sebab itu, penelitian ini juga memanfaatkan dataset yang tersedia secara publik dari Kaggle yang telah terbukti menjadi benchmark dalam penelitian serupa.

**Referensi**:
- World Health Organization. (2021). Breast cancer. Online at https://www.who.int/news-room/fact-sheets/detail/breast-cancer, accessed 23 May 2025.
- Marindrawati, M., Ferdiana, F., Anandani, A., Oktarina, O., Chahyani, W. I., Ayu, F. H., & Dianita, D. (2021, October). Edukasi dan Pelatihan" Ayo Rutin Melakukan Periksa Payudara Sendiri (SADARI) Sebagai Metode Deteksi Dini Kanker Payudara. In Prosiding Seminar Nasional Pengabdian Masyarakat LPPM UMJ (Vol. 1, No. 1).
- Chazar, C., & Erawan, B. (2020). Machine Learning Diagnosis Kanker Payudara Menggunakan Algoritma Support Vector Machine. INFORMASI (Jurnal Informatika Dan Sistem Informasi), 12(1), 67-80.

---

## Business Understanding
### Problem Statements
- Kurangnya metode diagnosis kanker payudara yang cepat dan akurat:
    Diagnosis tradisional seperti biopsi dan mammografi membutuhkan waktu dan biaya yang relatif besar, serta keahlian khusus yang tidak selalu tersedia di semua fasilitas kesehatan.
- Kesulitan dalam membedakan jaringan payudara jinak dan ganas secara otomatis:
    Proses manual rentan terhadap kesalahan manusia dan keterbatasan interpretasi citra medis yang dapat mempengaruhi ketepatan diagnosis.
- Keterbatasan akses layanan kesehatan di daerah dengan sumber daya terbatas:
    Perlu solusi berbasis teknologi yang dapat membantu tenaga medis dan pasien dengan cara yang lebih efisien dan hemat biaya.

### Goals
- Mengembangkan model klasifikasi berbasis machine learning yang mampu membedakan jaringan payudara jinak dan ganas secara akurat:
    Dengan menggunakan dataset kanker payudara, model diharapkan dapat memberikan prediksi yang andal dengan metrik evaluasi seperti akurasi, precision, recall, dan F1-score.
- Menyediakan solusi yang dapat mempercepat proses diagnosis:
    Model prediksi ini dapat membantu mengurangi waktu tunggu diagnosis dan memudahkan tenaga medis dalam mengambil keputusan klinis.
- Memfasilitasi implementasi teknologi predictive analytics pada layanan kesehatan, khususnya untuk daerah dengan keterbatasan akses:
Memberikan alternatif diagnosis pendukung yang lebih mudah diakses dan digunakan secara luas.


### Solution statements
- Mengimplementasikan dan membandingkan tiga algoritma machine learning yaitu Logistic Regression, Random Forest, dan Support Vector Machine (SVM) untuk membangun model klasifikasi kanker payudara.
- Melakukan reduksi dimensi menggunakan PCA untuk mengurangi kompleksitas data dan meningkatkan efisiensi proses training model.
- Menerapkan evaluasi model menggunakan metrik akurasi, precision, recall, dan F1-score untuk mengukur performa masing-masing model secara objektif dan memilih model terbaik.

---

## Data Understanding

Dataset yang digunakan dalam proyek ini adalah dataset kanker payudara yang tersedia secara publik di Kaggle dengan tautan berikut: [Breast Cancer Dataset - Kaggle](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset). Dataset ini berisi data klinis dan hasil pengukuran berbagai parameter morfologi dari jaringan payudara yang digunakan untuk klasifikasi apakah jaringan tersebut jinak atau ganas. Dataset ini terdiri dari 569 baris data dengan 32 kolom fitur yang meliputi data identifikasi, target klasifikasi, dan berbagai fitur numerik yang merepresentasikan karakteristik jaringan payudara.

### Kondisi Data  
- **Missing Value**: Tidak terdapat nilai yang hilang dalam dataset ini, sehingga semua data siap digunakan tanpa perlu proses imputasi.  
- **Duplikasi**: Tidak ditemukan data duplikat yang signifikan sehingga keunikan sampel terjaga.  
- **Outlier**: Teridentifikasi adanya nilai ekstrim (outlier) pada beberapa fitur numerik. Outlier ini tidak dihapus karena dapat mengandung informasi penting terkait karakteristik jaringan payudara.

### Uraian Seluruh Fitur  
- **id** : Nomor identifikasi unik untuk setiap sampel.  
- **diagnosis** : Kategori target yang menunjukkan jenis jaringan payudara, yaitu:  
  - *B* (Benign) - jaringan jinak  
  - *M* (Malignant) - jaringan ganas  
- **radius_mean** : Rata-rata jarak dari pusat ke tepi sel.  
- **texture_mean** : Rata-rata variasi tekstur sel.  
- **perimeter_mean** : Rata-rata keliling sel.  
- **area_mean** : Rata-rata luas sel.  
- **smoothness_mean** : Rata-rata kehalusan permukaan sel.  
- **compactness_mean** : Rata-rata kekompakan sel.  
- **concavity_mean** : Rata-rata tingkat cekungan pada sel.  
- **concave points_mean** : Rata-rata jumlah titik cekung pada sel.  
- **symmetry_mean** : Rata-rata simetri sel.  
- **fractal_dimension_mean** : Rata-rata dimensi fraktal sel.  
- **radius_se** : Standar deviasi jarak radius.  
- **texture_se** : Standar deviasi tekstur.  
- **perimeter_se** : Standar deviasi keliling.  
- **area_se** : Standar deviasi luas.  
- **smoothness_se** : Standar deviasi kehalusan permukaan.  
- **compactness_se** : Standar deviasi kekompakan.  
- **concavity_se** : Standar deviasi tingkat cekungan.  
- **concave points_se** : Standar deviasi jumlah titik cekung.  
- **symmetry_se** : Standar deviasi simetri.  
- **fractal_dimension_se** : Standar deviasi dimensi fraktal.  
- **radius_worst** : Nilai maksimum radius (terburuk).  
- **texture_worst** : Nilai maksimum tekstur (terburuk).  
- **perimeter_worst** : Nilai maksimum keliling (terburuk).  
- **area_worst** : Nilai maksimum luas (terburuk).  
- **smoothness_worst** : Nilai maksimum kehalusan (terburuk).  
- **compactness_worst** : Nilai maksimum kekompakan (terburuk).  
- **concavity_worst** : Nilai maksimum tingkat cekungan (terburuk).  
- **concave points_worst** : Nilai maksimum titik cekung (terburuk).  
- **symmetry_worst** : Nilai maksimum simetri (terburuk).  
- **fractal_dimension_worst** : Nilai maksimum dimensi fraktal (terburuk).

---

## Data Preparation

Tahap data preparation pada proyek ini dilakukan secara berurutan dan menyeluruh untuk memastikan data siap digunakan dalam pengembangan model machine learning dengan performa optimal.

### 1. Pemilihan Fitur  
Pertama, dilakukan pemilihan fitur dengan menghapus kolom yang tidak digunakan sebagai input model, yaitu kolom `id` sebagai identifier unik dan kolom hasil encoding target `diagnosis_B` dan `diagnosis_M`. Variabel fitur (`X`) hanya berisi kolom numerik yang relevan untuk proses pelatihan.

### 2. Encoding Fitur Target  
Variabel target `diagnosis` yang awalnya berupa data kategorikal string (nilai *B* untuk benign dan *M* untuk malignant) diubah menjadi bentuk numerik menggunakan `LabelEncoder`. Proses ini mengkonversi label kategori menjadi nilai numerik (misalnya 0 dan 1) agar dapat diproses oleh algoritma machine learning.

### 3. Standarisasi Data  
Seluruh fitur numerik pada variabel `X` distandarisasi menggunakan *StandardScaler* untuk mengubah skala data agar memiliki mean nol dan standar deviasi satu. Standarisasi ini penting untuk mencegah fitur dengan rentang nilai besar mendominasi proses pelatihan, serta membantu algoritma seperti Logistic Regression dan SVM untuk mencapai konvergensi lebih cepat dan menghasilkan model yang stabil.

### 4. Reduksi Dimensi dengan PCA  
Setelah standarisasi, dilakukan reduksi dimensi menggunakan Principal Component Analysis (PCA) dengan mengambil dua komponen utama. PCA bertujuan mengurangi kompleksitas data dan multikolinearitas antar fitur, serta mempertahankan informasi sebanyak mungkin yang menjelaskan variasi data. Pengurangan dimensi ini juga mempercepat proses pelatihan dan membantu meningkatkan performa model dengan mengurangi noise.

### 5. Pemisahan Data Train dan Test  
Terakhir, data dibagi menjadi subset pelatihan dan pengujian dengan perbandingan 90% untuk training dan 10% untuk testing. Pembagian ini dilakukan dengan metode stratifikasi pada variabel target untuk menjaga proporsi kelas yang seimbang di kedua subset. Tahapan ini penting agar evaluasi model dilakukan pada data yang belum pernah dilihat, sehingga hasil evaluasi lebih valid dan representatif terhadap performa model sebenarnya.

---

## Modeling

Pada tahap modeling, tiga algoritma machine learning digunakan untuk mengatasi permasalahan klasifikasi kanker payudara, yaitu Logistic Regression, Random Forest, dan Support Vector Machine (SVM). Setiap model dilatih dengan parameter tertentu untuk memastikan konvergensi dan performa yang optimal.

### 1. Logistic Regression  
Logistic Regression merupakan model linier yang mengestimasi probabilitas kelas dengan fungsi logistik. Pada proyek ini, parameter utama yang digunakan adalah `max_iter=1000` untuk memberikan batas iterasi yang cukup agar proses optimasi konvergen dengan baik, terutama pada data yang telah melalui proses reduksi dimensi. Model ini mudah diinterpretasikan dan cepat dilatih. Namun, Logistic Regression kurang efektif jika hubungan antar fitur dan target bersifat non-linear serta rentan terhadap multikolinearitas antar fitur.

### 2. Random Forest  
Random Forest adalah ensemble learning yang menggabungkan banyak decision tree untuk meningkatkan akurasi dan mengurangi overfitting. Parameter penting yang digunakan meliputi:  
- `n_estimators=100` yang menentukan jumlah pohon dalam hutan; semakin banyak pohon, model cenderung lebih stabil dan akurat, namun memerlukan waktu komputasi lebih lama.  
- `random_state=42` untuk memastikan reproduksibilitas hasil.  

Random Forest mampu menangani data non-linear dan variabel yang kompleks, serta relatif tahan terhadap noise dan outlier. Kelemahannya, model ini kurang interpretatif dan sumber daya komputasi yang dibutuhkan lebih besar dibandingkan Logistic Regression.

### 3. Support Vector Machine (SVM)  
SVM menggunakan hyperplane dengan margin maksimum untuk memisahkan kelas. Pada proyek ini digunakan kernel `rbf` (Radial Basis Function) yang memungkinkan pemodelan pola non-linear. Parameter kunci yang digunakan adalah:  
- `kernel='rbf'` untuk pemetaan fitur ke ruang berdimensi lebih tinggi,  
- `probability=True` agar model dapat mengestimasi probabilitas kelas,  
- `random_state=42` untuk hasil yang konsisten.  

SVM efektif pada dataset berukuran sedang dengan fitur yang tidak terlalu banyak dan margin pemisah yang jelas, tetapi bisa lambat pada dataset besar dan sangat bergantung pada pemilihan parameter kernel serta regularisasi.

### Pemilihan Model Terbaik  
Setelah pelatihan dan evaluasi menggunakan metrik akurasi, precision, recall, dan F1-score, model Random Forest menunjukkan performa terbaik secara keseluruhan. Hal ini dikarenakan kemampuannya dalam menangani pola data non-linear dan ketahanan terhadap outlier, sehingga model ini dipilih sebagai solusi utama untuk prediksi kanker payudara pada proyek ini.

---
## Evaluation

Pada proyek klasifikasi kanker payudara ini, evaluasi performa model dilakukan menggunakan metrik utama yaitu Accuracy, Precision, Recall, dan F1-Score. Metrik-metrik ini dihitung secara keseluruhan serta secara spesifik untuk masing-masing kelas (jinak dan ganas) agar memberikan gambaran yang lebih mendetail mengenai kemampuan model dalam mengklasifikasikan setiap kategori.

### Hasil Evaluasi Per Model dan Per Kelas

| Model               | Kelas   | Accuracy | Precision | Recall  | F1-Score |
|---------------------|---------|----------|-----------|---------|----------|
| Logistic Regression  | Benign  | 1.0000   | 1.0000    | 1.0000  | 1.0000   |
|                     | Malignant | 1.0000   | 1.0000    | 1.0000  | 1.0000   |
| Random Forest       | Benign  | 1.0000   | 1.0000    | 1.0000  | 1.0000   |
|                     | Malignant | 1.0000   | 1.0000    | 1.0000  | 1.0000   |
| Support Vector Machine (SVM) | Benign  | 0.9474   | 0.9167    | 1.0000  | 0.9565   |
|                     | Malignant | 0.9474   | 1.0000    | 0.8571  | 0.9231   |

Logistic Regression dan Random Forest menunjukkan performa sempurna pada seluruh metrik baik untuk kelas benign maupun malignant, yang berarti keduanya mampu mengklasifikasikan data tanpa kesalahan pada data uji. Sebaliknya, SVM memiliki performa sedikit lebih rendah, dengan recall pada kelas malignant turun menjadi 85.71%, menunjukkan beberapa kasus ganas gagal terdeteksi (false negative).

### Komparasi dan Pemilihan Model Terbaik

Berdasarkan metrik evaluasi, Logistic Regression dan Random Forest memiliki hasil yang identik dan sempurna, sementara SVM memiliki performa yang baik namun kurang sensitif pada kelas malignant. Pemilihan model terbaik jatuh pada **Random Forest** karena selain mencapai performa tinggi, model ini lebih kuat dalam menangani pola data yang kompleks dan non-linear serta tahan terhadap noise, sehingga lebih robust dan dapat diaplikasikan pada kondisi nyata yang bervariasi.

### Kaitan dengan Business Understanding

Model terbaik ini secara langsung menjawab masalah utama dalam business understanding, yaitu menyediakan metode diagnosis yang cepat dan akurat (Problem Statement 1) serta membantu membedakan jaringan jinak dan ganas secara otomatis (Problem Statement 2). Dengan performa yang sangat baik, model dapat mempercepat proses diagnosis dan membantu tenaga medis membuat keputusan yang lebih tepat dan efisien (Goal 1 dan Goal 2). 

Penggunaan Random Forest sebagai solusi juga mendukung goal ketiga yaitu memfasilitasi implementasi teknologi predictive analytics di daerah dengan keterbatasan sumber daya, karena model ini dapat dioptimalkan untuk berjalan secara efisien di berbagai platform.

### Dampak Solusi

Penerapan tiga algoritma dan evaluasi komparatif menunjukkan bahwa solusi yang diajukan efektif dan terukur (Solution Statement). Reduksi dimensi dengan PCA meningkatkan efisiensi tanpa mengorbankan akurasi, sementara evaluasi menyeluruh memastikan model yang dipilih memenuhi kriteria bisnis dan teknis.

Dengan demikian, model Random Forest yang dipilih tidak hanya memenuhi target metrik evaluasi, tetapi juga memberikan dampak signifikan dalam konteks kebutuhan bisnis dan klinis yang diidentifikasi di awal proyek.

---

**---Ini adalah bagian akhir laporan---**
