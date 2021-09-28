# Deployment Model Support Vector Machine

## Deskripsi singkat

Repository ini berisi semua file yang dibutuhkan untuk melakukan deployment model Support Vector Machine dengan kernel Linier. Adapun model yang digunakan merupakan model untuk memprediksi pengukuran tingkat kepuasan lulusan:

-   `Jalur_Masuk` atau jalur masuk perguruan tinggi yaitu `Afirmasi`,`Sumikolah`,`Tumotou (T2)`,`SBMPTN`, `SNMPTN`
-   `Pilihan_Prodi_ke` atau pilihan program studi waktu mendaftar test yaitu `Ketiga`,`Kedua`,`Pertama`
-   `Organisasi_Intra_kampus` atau oraganisasi yang pernah diikuti di kampus yaitu `Tidak ada yang diikuti`,`Lainnya`,`Kemanusiaan`, 
                              `Lingkungan`, `Seni`, `Olahraga`, `Kerohanian`, `BEM/Senat`
-   `Organisasi_Ekstra_kampus` atau oraganisasi yang diikuti di luat dari kampus yaitu `Tidak ada yang diikuti`,`Lainnya`,`Kemanusiaan`,
                              `Lingkungan`, `Seni`, `Olahraga`, `Kerohanian`,
-   `Pekerjaan_Yang_di_Inginkan_Saat_Kuliah` atau pekerjaan yang diharapkan selama perkuliahan yaitu `Wiraswasta`,`Swasta (Manufaktur)`, 
                               `Swasta (Jasa)`,`Pemerintah (BUMN, BHMN)`, `Pemerintah (daerah)`, `Pemerintah (pusat/departemen)`
-   `IPK` atau indek prestasi komulasi tipe data fload (bilangan pecahan)        
-   `Yang_di_lakukan_kerjakan_saat_ini` atau yang dikerjakan saat ini yaitu `Masih kuliah/melanjutkan kuliah profesi atau pascasarjana`,
                               `Mencari/menunggu pekerjaan`, `Sudah bekerja`,`Kuliah dan bekerja`
-   `Lama_mencari_pekerjaan` atau lama mendapatkan pekerjaan yaitu `lebih dari 12 bulan sebelum lulus kuliah`,`6-12 bulan sebelum lulus 
                                kuliah`, `0-6 bulan sebelum lulus kuliah`,`0-3 bulan setelah lulus kuliah`, `3-6 bulan setelah lulus 
                                kuliah`, `6-12 bulan setelah lulus kuliah`, `12-24 bulan setelah lulus kuliah`
-   `Bidang_tempat_bekerja` atau bidang tempat bekerja saat ini yaitu `SAYA BELUM BEKERJA`, `Lainnya`, `Wiraswasta/perusahaan sendiri`,
                                `Perusahaan swasta`, `Organisasi non-profit/Lembaga Swadaya Masyarakat`, `Instansi pemerintah (termasuk 
                                BUMN)`
-   `Pendapatan_saat_pertama_kali_bekerja_bulan` atau pendapatan pertama kerja dengan tipe data integer (bilangan bulat)
-   `Pendapatan_utama_bulan` atau pendapatan utama saat ini dengan tipe data integer (bilangan bulat)
-   `Pendapatan_lembur_dan_tips_bulan` atau pendapatan lembur dengan tipe data integer (bilangan bulat)
-   `Pendapatan_pekerjaan_lainnya_bulan`  atau pendapatan pekerjaan lainnya dengan tipe data integer (bilangan bulat)
-   `Hubungan_antara_bidang_studi_dengan_pekerjaan` atau hubungan bidang studi dengan pekerjaan yaitu `Tidak Sama Skali`,`Kurang Erat`, 
                                `Cukup Erat`,`Erat`, `Sangat Erat`
-   `Tingkat_pendidikan_yang_paling_tepat_sesuai_untuk_pekerjaan_saat_ini` yaitu tingkat pendidikan yang paling sesuai dengan pekerjaan 
                                yaitu `Tidak Perlu Pendidikan Tinggi`,`Setingkat Lebih Rendah`, `Tingkat yang Sama`,`Setingkat Lebih 
                                Tinggi`
-   `Pengetahuan_di_luar_bidang_atau_disiplin_ilmu` atau pengetahuan diluar bidang ilmu yaitu `1`, `2`, `3`, `4`, `5` 
-   `Pengetahuan_umum` atau pengetahuan umum yaitu `1`, `2`, `3`, `4`, `5`
-   `Bahasa_Inggris` atau pengetahuan bahasa inggris yaitu `1`, `2`, `3`, `4`, `5`
-   `Keterampilan_internet_teknologi_informasi` atau keterampilan penguasaan internet yaitu `1`, `2`, `3`, `4`, `5`
-   `Keterampilan_komputer` atau keterampilan penguasaan komputer yaitu `1`, `2`, `3`, `4`, `5`
-   `Berpikir_kritis` atau berfikir kritis yaitu `1`, `2`, `3`, `4`, `5`
-   `Keterampilan_riset` atau keterampilan riset yaitu `1`, `2`, `3`, `4`, `5`
-   `Kemampuan_belajar` atau keterampilan belajar yaitu `1`, `2`, `3`, `4`, `5`
-   `Kemampuan_berkomunikasi` atau kemampuan berkomunikasi yaitu `1`, `2`, `3`, `4`, `5` 
-   `Bekerja_di_bawah_tekanan` atau kemampuan bekrja dibawah tekanan yaitu `1`, `2`, `3`, `4`, `5`
-   `Manajemen_waktu` atau kemampuan manajemen waktu yaitu `1`, `2`, `3`, `4`, `5`
-   `Bekerja_secara_mandiri` atau kemampuan bekerja mandiri yaitu `1`, `2`, `3`, `4`, `5`
-   `Bekerja_dalam_tim_bekerjasama_dengan_orang_lain` atau kemampuan bekerja dalam tim yaitu `1`, `2`, `3`, `4`, `5`
-   `Kemampuan_dalam_memecahkan_masalah` atau kemampuan memecahkan masalah yaitu `1`, `2`, `3`, `4`, `5`
-   `Negosiasi` atau kemampuan negosiasi yaitu `1`, `2`, `3`, `4`, `5`
-   `Kemampuan_analisis` atau kemampuan analisis yaitu `1`, `2`, `3`, `4`, `5`
-   `Toleransi` atau toleransi yaitu `1`, `2`, `3`, `4`, `5`
-   `Kemampuan_adaptasi` atau kemampuan adaptasi yaitu `1`, `2`, `3`, `4`, `5`
-   `Loyalitas` atau loyalitas yaitu `1`, `2`, `3`, `4`, `5`
-   `Integritas_etika` atau integritas dalam etika yaitu `1`, `2`, `3`, `4`, `5`
-   `Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang` atau kemampuan bekerja dengan orang beda budaya yaitu `1`, `2`, `3`, 
                                `4`, `5`
-   `Kemampuan_dalam_memegang_tanggungjawab` atau kemampuan dalam memegang tanggungjawab yaitu `1`, `2`, `3`, `4`, `5`
-   `Kepemimpinan` atau kepemimpinan yaitu `1`, `2`, `3`, `4`, `5`
-   `Inisiatif` atau inisiatif yaitu `1`, `2`, `3`, `4`, `5`
-   `Kemampuan_untuk_memresentasikan_ide_produk_laporan` atau kemampuan mempresentasikan ide/gagasan yaitu `1`, `2`, `3`, `4`, `5`
-   `Kemampuan_dalam_menulis_laporan_memo_dan_dokumen` atau kemampuan dalam menulis laporan yaitu `1`, `2`, `3`, `4`, `5`
-   `Manajemen_proyek_program` atau kemampuan manajemen proyek yaitu `1`, `2`, `3`, `4`, `5`


## Sekilas mengenai input model

Agar dapat mengukur tingkat kepuasan lulusan, data input model harus mengikuti format sebagai berikut:\
`[Jalur Masuk, Pilihan Prodi ke, Organisasi_Intra_kampus, Organisasi_Ekstra_kampus, Pekerjaan_Yang_di_Inginkan_Saat_Kuliah, IPK, Yang_di_lakukan_kerjakan_saat_ini, Lama_mencari_pekerjaan, Bidang_tempat_bekerja, Pendapatan_saat_pertama_kali_bekerja_bulan, Pendapatan_utama_bulan, Pendapatan_lembur_dan_tips_bulan, Pendapatan_pekerjaan_lainnya_bulan, Hubungan_antara_bidang_studi_dengan_pekerjaan, Tingkat_pendidikan_yang_paling_tepat_sesuai_untuk_pekerjaan_saat_ini, Pengetahuan_di_luar_bidang_atau_disiplin_ilmu, Pengetahuan_umum, Bahasa_Inggris, Keterampilan_internet_teknologi_informasi, Keterampilan_komputer, Berpikir_kritis, Keterampilan_riset, Kemampuan_belajar, Kemampuan_berkomunikasi, Bekerja_di_bawah_tekanan, Manajemen_waktu, Bekerja_secara_mandiri, Bekerja_dalam_tim_bekerjasama_dengan_orang_lain, Kemampuan_dalam_memecahkan_masalah, Negosiasi, Kemampuan_analisis, Toleransi, Kemampuan_adaptasi, Loyalitas, Integritas_etika, Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang, Kemampuan_dalam_memegang_tanggungjawab, Kepemimpinan, Inisiatif, Kemampuan_untuk_memresentasikan_ide_produk_laporan, Kemampuan_dalam_menulis_laporan_memo_dan_dokumen, Manajemen_proyek_program]`
`[5, 1, 7, 5, 5, 3.78, 3, 3, 4, 1500000, 3000000, 500000, 100000, 3, 3, 5, 5, 5, 4, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ]`

Sebagai contoh:\
Jalur_Masuk: SNMPTN\
Pilihan_Prodi_ke: Ketiga\
Organisasi_Intra_kampus: BEM/Senat\
Organisasi_Ekstra_kampus: Seni\
Pekerjaan_Yang_di_Inginkan_Saat_Kuliah: Pemerintah (daerah)\
IPK: 3.78\
Yang_di_lakukan_kerjakan_saat_ini: Sudah bekerja\
Lama_mencari_pekerjaan: 3-6 bulan setelah lulus kuliah\
Bidang_tempat_bekerja: Perusahaan swasta
Pendapatan_saat_pertama_kali_bekerja_bulan: 1500000\
Pendapatan_utama_bulan: 3000000\
Pendapatan_lembur_dan_tips_bulan: 500000\
Pendapatan_pekerjaan_lainnya_bulan: 100000\
Hubungan_antara_bidang_studi_dengan_pekerjaan: Cukup Erat\
Tingkat_pendidikan_yang_paling_tepat_sesuai_untuk_pekerjaan_saat_ini: Tingkat yang Sama\
Pengetahuan_di_luar_bidang_atau_disiplin_ilmu: 5\
Pengetahuan_umum: 5\
Bahasa_Inggris: 5\
Keterampilan_internet_teknologi_informasi: 4\
Keterampilan_komputer: 4\
Berpikir_kritis: 5\
Keterampilan_riset: 4\
Kemampuan_belajar: 4\
Kemampuan_berkomunikasi: 5
Bekerja_di_bawah_tekanan: 5\
Manajemen_waktu: 5\
Bekerja_secara_mandiri: 5\
Bekerja_dalam_tim_bekerjasama_dengan_orang_lain: 5\
Kemampuan_dalam_memecahkan_masalah: 5\
Negosiasi: 5\
Kemampuan_analisis: 5\
Toleransi: 5\
Kemampuan_adaptasi: 5\
Loyalitas: 5\
Integritas_etika: 5\
Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang: 5\
Kemampuan_dalam_memegang_tanggungjawab: 5\
Kepemimpinan: 5\
Inisiatif: 5\
Kemampuan_untuk_memresentasikan_ide_produk_laporan: 5\
Kemampuan_dalam_menulis_laporan_memo_dan_dokumen: 5\
Manajemen_proyek_program: 5\
    

Akan diubah menjadi:\
`[5, 1, 7, 5, 5, 3.78, 3, 3, 4, 1500000, 3000000, 500000, 100000, 3, 3, 5, 5, 5, 4, 4, 5, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ]`


## Folder, file, dan kegunaannya

-   templates/
-   index.html --> Berisi template website
-   app.py --> Berisi konfigurasi route untuk API
-   model.pkl --> Model Support Vector Machin yang sudah di-training
-   requirements.txt --> Berisi daftar dependency/package Python yang diperlukan untuk menjalankan API dan model Support Vector Machin


## Cara menjalankan API pada komputer Anda

### Menjalankan API

1. Pastikan Anda sudah menginstall Anaconda
1. Buka terminal/command prompt/power shell
1. Buat virtual environment dengan\
   `conda create -n <nama-environment> python=3.9`
1. Aktifkan virtual environment dengan\
   `conda activate <nama-environment>`
1. Install semua dependency/package Python dengan\
   `pip install -r requirements.txt`
1. Jalankan API menggunakan perintah\
   `python app.py`

### Akses melalui Website

Setelah API berjalan:

1. Anda akan diberikan URL untuk membuka website berupa `localhost:5000/` atau `127.0.0.1:5000/`
1. Buka URL dengan browser, coba masukkan data yang ingin di prediksi
1. Anda akan diberikan estimasi biaya asuransi pada sisi kanan halaman website


