# Laporan Proyek Machine Learning - Rizki Surya Nugroho

## Domain Proyek

Kanker payudara merupakan salah satu penyakit kanker dengan tingkat prevalensi tertinggi di dunia dan menjadi penyebab utama kematian pada wanita secara global (World Health Organization, 2021). Deteksi dini kanker payudara sangat krusial untuk meningkatkan peluang kesembuhan dan menurunkan angka kematian (Marindrawati et al., 2023). Namun, proses diagnosis konvensional sering kali memerlukan pemeriksaan laboratorium dan citra medis yang memakan waktu dan biaya tinggi. Oleh karena itu, pengembangan metode prediksi berbasis data dan machine learning menjadi solusi potensial untuk mendukung diagnosis secara cepat dan akurat.

Proyek ini bertujuan mengimplementasikan predictive analytics menggunakan dataset kanker payudara untuk membangun model klasifikasi yang mampu membedakan antara jaringan jinak dan ganas secara otomatis. Pemanfaatan metode ini dapat membantu tenaga medis dalam pengambilan keputusan diagnosis yang lebih efisien, mengurangi beban kerja, dan meningkatkan akses layanan kesehatan terutama di daerah dengan keterbatasan sumber daya.

Berbagai penelitian terdahulu menunjukkan efektivitas penggunaan machine learning dalam menganalisis dataset kanker payudara, seperti yang dilakukan oleh Chazar dan Erawan (2020) yang menggunakan metode klasifikasi dengan akurasi tinggi. Oleh sebab itu, penelitian ini juga memanfaatkan dataset yang tersedia secara publik dari Kaggle yang telah terbukti menjadi benchmark dalam penelitian serupa.

**Referensi**:
- World Health Organization. (2021). Breast cancer. Online at https://www.who.int/news-room/fact-sheets/detail/breast-cancer, accessed 23 May 2025.
- Marindrawati, M., Ferdiana, F., Anandani, A., Oktarina, O., Chahyani, W. I., Ayu, F. H., & Dianita, D. (2021, October). Edukasi dan Pelatihan" Ayo Rutin Melakukan Periksa Payudara Sendiri (SADARI) Sebagai Metode Deteksi Dini Kanker Payudara. In Prosiding Seminar Nasional Pengabdian Masyarakat LPPM UMJ (Vol. 1, No. 1).
- Chazar, C., & Erawan, B. (2020). Machine Learning Diagnosis Kanker Payudara Menggunakan Algoritma Support Vector Machine. INFORMASI (Jurnal Informatika Dan Sistem Informasi), 12(1), 67-80.

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

## Data Understanding

Dataset yang digunakan dalam proyek ini adalah dataset kanker payudara yang tersedia secara publik di Kaggle dengan tautan berikut: [Breast Cancer Dataset - Kaggle](https://www.kaggle.com/datasets/yasserh/breast-cancer-dataset). Dataset ini berisi data klinis dan hasil pengukuran berbagai parameter morfologi dari jaringan payudara yang digunakan untuk klasifikasi apakah jaringan tersebut jinak atau ganas.

Dataset ini terdiri dari 32 kolom dengan 569 baris data. Berikut adalah penjelasan variabel-variabel utama dalam dataset:

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

Selain variabel-variabel di atas, terdapat fitur dengan akhiran `_se` yang merepresentasikan standar deviasi dari fitur tersebut, dan fitur dengan akhiran `_worst` yang menunjukkan nilai terburuk (maksimum) dari fitur tersebut dalam pengukuran sampel.

### Exploratory Data Analysis (EDA)

Dalam tahap pemahaman data, beberapa proses eksplorasi dan pembersihan data dilakukan untuk memastikan kualitas dan karakteristik dataset, yaitu:
- **Penanganan Missing Values**  
  Data dicek untuk nilai yang hilang (missing values). Pada dataset ini, tidak ditemukan missing value, sehingga semua data dapat digunakan tanpa proses imputasi.
- **Penanganan Outlier**  
  Visualisasi boxplot digunakan untuk mendeteksi outlier pada masing-masing fitur. Meskipun outlier ditemukan pada beberapa variabel, data tersebut tidak dihapus atau dibersihkan karena dalam konteks data kesehatan, nilai ekstrim dapat mengandung informasi penting yang relevan untuk diagnosis penyakit.
- **Univariate Analysis**  
  Analisis distribusi tiap variabel dilakukan dengan visualisasi histogram dan countplot (untuk fitur kategorikal), guna memahami penyebaran data, pola, serta frekuensi masing-masing kelas.
- **Multivariate Analysis**  
  Analisis hubungan antar variabel dilakukan menggunakan pairplot dan heatmap korelasi. Ini membantu dalam mengidentifikasi fitur-fitur yang berkorelasi kuat dan potensi multikolinearitas, yang sangat berguna dalam tahap pemodelan dan reduksi dimensi.

Proses EDA ini menjadi fondasi penting untuk tahap selanjutnya yaitu data preparation dan pengembangan model machine learning yang efektif dan akurat.

---

*Catatan:* Seluruh tahapan di atas dilaksanakan dengan tujuan untuk memastikan data siap pakai dan model yang dibangun dapat memberikan hasil prediksi yang dapat dipercaya dalam konteks diagnosis kanker payudara.

## Data Preparation

Proses data preparation pada proyek ini dilakukan secara berurutan untuk memastikan data siap digunakan dalam pengembangan model machine learning dengan performa optimal.

### 1. Encoding Fitur Kategorikal  
Variabel target `diagnosis` yang awalnya berupa kategori string (*B* untuk benign dan *M* untuk malignant) diubah menjadi representasi numerik menggunakan one-hot encoding. Proses ini mengubah variabel kategori menjadi format numerik yang dapat dipahami oleh algoritma machine learning. Encoding ini penting untuk memisahkan kelas target dan memudahkan proses pelatihan model.

### 2. Standarisasi Data  
Seluruh fitur numerik distandarisasi menggunakan *StandardScaler* untuk mengubah skala data sehingga memiliki mean nol dan standar deviasi satu. Standarisasi diperlukan agar fitur dengan rentang nilai berbeda tidak mendominasi proses training dan membantu algoritma yang sensitif terhadap skala, seperti Logistic Regression dan SVM, untuk konvergen lebih cepat dan menghasilkan model yang lebih stabil.

### 3. Reduksi Dimensi dengan PCA  
Setelah standarisasi, diterapkan Principal Component Analysis (PCA) untuk mereduksi dimensi data menjadi dua komponen utama. PCA membantu mengurangi kompleksitas data dan potensi multikolinearitas antar fitur, sekaligus mempertahankan informasi sebanyak mungkin yang menjelaskan variasi data. Pengurangan dimensi ini mempercepat proses training dan dapat meningkatkan performa model dengan mengurangi noise.

### 4. Pemisahan Data Train dan Test  
Data kemudian dibagi menjadi data pelatihan dan pengujian dengan perbandingan 90% untuk training dan 10% untuk testing, menggunakan stratifikasi pada variabel target untuk menjaga proporsi kelas yang seimbang. Tahapan ini penting untuk mengevaluasi kemampuan model secara objektif pada data yang belum pernah dilihat sebelumnya, sehingga hasil evaluasi lebih representatif terhadap performa model sesungguhnya.

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

Dalam proyek klasifikasi kanker payudara ini, digunakan beberapa metrik evaluasi utama untuk mengukur performa model, yaitu:

- **Accuracy**: Persentase prediksi yang benar dari seluruh data yang diuji. Rumusnya adalah:  
  ![Accuracy](https://cdn.prod.website-files.com/660ef16a9e0687d9cc27474a/662c426738658d748af1b1e5_644af6a24701d43aaecd8771_classification_guide_apc09.png)
  dimana TP, TN, FP, dan FN adalah true positive, true negative, false positive, dan false negative.

- **Precision**: Proporsi prediksi positif yang benar-benar positif. Formula precision:  
  ![Precision](https://miro.medium.com/v2/resize:fit:1240/1*DoGL8YNxBOwkX_gd9P_CEA.png)
  Precision tinggi berarti model minim kesalahan positif palsu.

- **Recall** (Sensitivity): Proporsi data positif yang berhasil terdeteksi oleh model. Formula recall:  
  ![Recall](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRM2acxu2473I4yGB81jakKqtDXwVgb4XDtB6cJmcOKvsMdmRQYWgPOdtluZ7IoTFbqmbg&usqp=CAU)
  Recall tinggi penting untuk meminimalisir false negative, sangat krusial dalam diagnosis penyakit.

- **F1-Score**: Harmonik rata-rata dari precision dan recall, memberikan keseimbangan antara keduanya. Formula F1-score:  
  ![F1-Score](https://ilmudatapy.com/wp-content/uploads/2021/01/confusion-matrix-5.png)

### Hasil Evaluasi

Berdasarkan hasil evaluasi pada data uji, didapatkan performa sebagai berikut:

| Model               | Accuracy | Precision | Recall  | F1-Score |
|---------------------|----------|-----------|---------|----------|
| Logistic Regression  | 1.0000   | 1.0000    | 1.0000  | 1.0000   |
| Random Forest       | 1.0000   | 1.0000    | 1.0000  | 1.0000   |
| Support Vector Machine (SVM) | 0.9474   | 1.0000    | 0.8571  | 0.9231   |

Model Logistic Regression dan Random Forest mencapai hasil sempurna pada metrik evaluasi yang digunakan dengan nilai 1.0 untuk semua metrik, menunjukkan bahwa kedua model tersebut mampu melakukan klasifikasi secara akurat tanpa kesalahan pada data uji yang digunakan. Sementara model SVM menunjukkan performa sedikit lebih rendah dengan akurasi 94,74%, meskipun precision-nya tetap sempurna, recall-nya sedikit menurun, yang berarti ada beberapa data positif yang tidak terdeteksi (false negative), namun nilai F1-score yang cukup tinggi menunjukkan keseimbangan yang baik antara precision dan recall.

### Interpretasi

- Nilai **Accuracy** dan **F1-Score** yang sempurna pada Logistic Regression dan Random Forest mengindikasikan kedua model tersebut sangat andal untuk tugas klasifikasi ini dalam dataset yang digunakan.  
- Performa **Recall** yang sedikit menurun pada SVM perlu diperhatikan karena dalam konteks diagnosis kanker, false negative dapat berakibat fatal, sehingga recall menjadi metrik penting.  
- Hasil ini mendukung pemilihan Random Forest sebagai model terbaik karena selain performa, model ini juga lebih robust terhadap data non-linear dan noise.

---

**---Ini adalah bagian akhir laporan---**
