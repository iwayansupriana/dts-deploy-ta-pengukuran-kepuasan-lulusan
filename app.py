from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

model_file = open('model.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', tinggkat_kepuasan=0)
    


@app.route('/predict', methods=['POST'])
def predict():
    '''
    Tracer Studi untuk mengukur tingkat kepuasan lulusan prodi management Fakultas Ekonomi dan Bisnis 
    Universitas Sam Ratulangi Tahun 2020 berdasarkan input pengguna dan render hasilnya ke halaman html
    '''

    Jalur_Masuk = [x for x in request.form.values()]
    Pilihan_Prodi_ke = [X for X in request.form.values()]
    Organisasi_Intra_kampus= [X for X in request.form.values()]
    Organisasi_Ekstra_kampus= [X for X in request.form.values()]
    Pekerjaan_Yang_di_Inginkan_Saat_Kuliah= [X for X in request.form.values()]
    IPK= request.form["IPK"]        
    Yang_di_lakukan_kerjakan_saat_ini=[X for X in request.form.values()]
    Lama_mencari_pekerjaan= [X for X in request.form.values()]
    Bidang_tempat_bekerja= [X for X in request.form.values()]
    Pendapatan_saat_pertama_kali_bekerja_bulan= request.form["Pendapatan_saat_pertama_kali_bekerja_bulan"]
    Pendapatan_utama_bulan= request.form["Pendapatan_utama_bulan"]
    Pendapatan_lembur_dan_tips_bulan= request.form["Pendapatan_lembur_dan_tips_bulan"]
    Pendapatan_pekerjaan_lainnya_bulan= request.form["Pendapatan_pekerjaan_lainnya_bulan"]
    Hubungan_antara_bidang_studi_dengan_pekerjaan= [X for X in request.form.values()]
    Tingkat_pendidikan_yang_paling_tepat_sesuai_untuk_pekerjaan_saat_ini= [X for X in request.form.values()]
    Pengetahuan_di_luar_bidang_atau_disiplin_ilmu= [X for X in request.form.values()]
    Pengetahuan_umum= [X for X in request.form.values()]
    Bahasa_Inggris= [X for X in request.form.values()]
    Keterampilan_internet_teknologi_informasi= [X for X in request.form.values()]
    Keterampilan_komputer= [X for X in request.form.values()]
    Berpikir_kritis= [X for X in request.form.values()]
    Keterampilan_riset= [X for X in request.form.values()]
    Kemampuan_belajar= [X for X in request.form.values()]
    Kemampuan_berkomunikasi= [X for X in request.form.values()]
    Bekerja_di_bawah_tekanan= [X for X in request.form.values()]
    Manajemen_waktu= [X for X in request.form.values()]
    Bekerja_secara_mandiri= [X for X in request.form.values()]
    Bekerja_dalam_tim_bekerjasama_dengan_orang_lain= [X for X in request.form.values()]
    Kemampuan_dalam_memecahkan_masalah= [X for X in request.form.values()]
    Negosiasi= [X for X in request.form.values()]
    Kemampuan_analisis= [X for X in request.form.values()]
    Toleransi= [X for X in request.form.values()]
    Kemampuan_adaptasi= [X for X in request.form.values()]
    Loyalitas= [X for X in request.form.values()]
    Integritas_etika= [X for X in request.form.values()]
    Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang= [X for X in request.form.values()]
    Kemampuan_dalam_memegang_tanggungjawab= [X for X in request.form.values()]
    Kepemimpinan= [X for X in request.form.values()]
    Inisiatif= [X for X in request.form.values()]
    Kemampuan_untuk_memresentasikan_ide_produk_laporan= [X for X in request.form.values()]
    Kemampuan_dalam_menulis_laporan_memo_dan_dokumen= [X for X in request.form.values()]
    Manajemen_proyek_program= [X for X in request.form.values()]
          
    data = []

    if Jalur_Masuk == "SNMPTN":
        data.extend([5])
    else:
        if Jalur_Masuk == 'SBMPTN':
            data.extend([4])
        else:    
            if Jalur_Masuk == 'Tumotou (T2)':
                data.extend([3])
            else:
                if Jalur_Masuk == 'Sumikolah':
                    data.extend([2])
                else:
                    if Jalur_Masuk == 'Afirmasi':
                        data.extend([1])
                    else:
                        data.extend([0])
              
    if Pilihan_Prodi_ke == 'Pertama':
        data.extend([3])
    else:
        if Pilihan_Prodi_ke == 'Kedua':
            data.extend([2])
        else:
            if Pilihan_Prodi_ke == 'Ketiga':
                data.extend([1])
            else:
                data.extend([0])

    
    if Organisasi_Intra_kampus == 'BEM / Senat':
        data.extend([8])
    else:
        if Organisasi_Intra_kampus == 'Kerohanian':
            data.extend([7])
        else:
            if Organisasi_Intra_kampus == 'Olahraga':
                data.extend([6])
            else:
                if Organisasi_Intra_kampus == 'Seni':
                    data.extend([5])
                else:
                    if Organisasi_Intra_kampus == 'Lingkungan':
                        data.extend([4])
                    else:
                        if Organisasi_Intra_kampus == 'Kemanusiaan':
                            data.extend([3])
                        else:
                            if Organisasi_Intra_kampus == 'Lainnya':
                                data.extend([2])
                            else:
                                if Organisasi_Intra_kampus == 'Tidak ada yang diikuti':
                                    data.extend([1])        
                                else:
                                    data.extend([0])
 
    
    
            
    if Organisasi_Ekstra_kampus == 'Kerohanian':
        data.extend([7])
    else:
        if Organisasi_Ekstra_kampus == 'Olahraga':
            data.extend([6])
        else:
            if Organisasi_Ekstra_kampus == 'Seni':
                data.extend([5])
            else:
                if Organisasi_Ekstra_kampus == 'Lingkungan':
                    data.extend([4])
                else:
                    if Organisasi_Ekstra_kampus == 'Kemanusiaan':
                        data.extend([3])
                    else:
                        if Organisasi_Ekstra_kampus == 'Lainnya':
                            data.extend([2])
                        else:
                            if Organisasi_Ekstra_kampus == 'Tidak ada yang diikuti':
                                data.extend([1])        
                            else:
                                data.extend([0])
                                             
        
    if Pekerjaan_Yang_di_Inginkan_Saat_Kuliah == 'Pemerintah (pusat/departemen)':
        data.extend([6])
    else:
        if Pekerjaan_Yang_di_Inginkan_Saat_Kuliah == 'Pemerintah (daerah)':
            data.extend([5])
        else:
            if Pekerjaan_Yang_di_Inginkan_Saat_Kuliah == 'Pemerintah (BUMN, BHMN)':
                data.extend([4])
            else:
                if Pekerjaan_Yang_di_Inginkan_Saat_Kuliah == 'Swasta (Jasa)':
                    data.extend([3])
                else:
                    if Pekerjaan_Yang_di_Inginkan_Saat_Kuliah == 'Swasta (Manufaktur)':
                        data.extend([2])
                    else:
                        if Pekerjaan_Yang_di_Inginkan_Saat_Kuliah == 'Wiraswasta':
                            data.extend([1])  
                        else:
                            data.extend([0])
    
    data.append(np.asarray([IPK]))
        
    
    if Yang_di_lakukan_kerjakan_saat_ini == 'Kuliah dan bekerja':
        data.extend([4])
    else:
        if Yang_di_lakukan_kerjakan_saat_ini == 'Sudah bekerja':
            data.extend([3])
        else:
            if Yang_di_lakukan_kerjakan_saat_ini == 'Mencari/menunggu pekerjaan':
                data.extend([2])
            else:
                if Yang_di_lakukan_kerjakan_saat_ini == 'Masih kuliah/melanjutkan kuliah profesi atau pascasarjana':
                    data.extend([1]) 
                else:
                    data.extend([0])



    if Lama_mencari_pekerjaan == '12-24 bulan setelah lulus kuliah':
        data.extend([7])
    else:
        if Lama_mencari_pekerjaan == '6-12 bulan setelah lulus kuliah':
            data.extend([6])
        else:
            if Lama_mencari_pekerjaan == '3-6 bulan setelah lulus kuliah':
                data.extend([5])
            else:
                if Lama_mencari_pekerjaan == '0-3 bulan setelah lulus kuliah':
                    data.extend([4])
                else:
                    if Lama_mencari_pekerjaan == '0-6 bulan sebelum lulus kuliah':
                        data.extend([3])
                    else:
                        if Lama_mencari_pekerjaan == '6-12 bulan sebelum lulus kuliah':
                            data.extend([2])
                        else:
                            if Lama_mencari_pekerjaan == 'lebih dari 12 bulan sebelum lulus kuliah':
                                data.extend([1])     
                            else:
                                data.extend([0])
                                
    
    if Bidang_tempat_bekerja == 'Instansi pemerintah (termasuk BUMN)':
        data.extend([6])
    else:
        if Bidang_tempat_bekerja == 'Organisasi non-profit/Lembaga Swadaya Masyarakat':
            data.extend([5])
        else:
            if Bidang_tempat_bekerja == 'Perusahaan swasta':
                data.extend([4])
            else:
                if Bidang_tempat_bekerja == 'Wiraswasta/perusahaan sendiri':
                    data.extend([3])
                else:
                    if Bidang_tempat_bekerja == 'Lainnya':
                        data.extend([2])
                    else:
                        if Bidang_tempat_bekerja == 'SAYA BELUM BEKERJA':
                            data.extend([1])      
                        else:
                            data.extend([0])
                            
    
    data.append(np.asarray([Pendapatan_saat_pertama_kali_bekerja_bulan]))
    
    data.append(np.asarray([Pendapatan_utama_bulan]))
   
    data.append(np.asarray([Pendapatan_lembur_dan_tips_bulan]))
    
    data.append(np.asarray([Pendapatan_pekerjaan_lainnya_bulan]))    
    
    
    if Hubungan_antara_bidang_studi_dengan_pekerjaan == 'Sangat Erat':
        data.extend([5])
    else:
        if Hubungan_antara_bidang_studi_dengan_pekerjaan == 'Erat':
            data.extend([4])
        else:
            if Hubungan_antara_bidang_studi_dengan_pekerjaan == 'Cukup Erat':
                data.extend([3])
            else:
                if Hubungan_antara_bidang_studi_dengan_pekerjaan == 'Kurang Erat':
                    data.extend([2])
                else:
                    if Hubungan_antara_bidang_studi_dengan_pekerjaan == 'Tidak Sama Skali':
                        data.extend([1])  
                    else:
                        data.extend([0])

    
    if Tingkat_pendidikan_yang_paling_tepat_sesuai_untuk_pekerjaan_saat_ini == 'Setingkat Lebih Tinggi':
        data.extend([4])
    else:
        if Tingkat_pendidikan_yang_paling_tepat_sesuai_untuk_pekerjaan_saat_ini == 'Tingkat yang Sama':
            data.extend([3])
        else:
            if Tingkat_pendidikan_yang_paling_tepat_sesuai_untuk_pekerjaan_saat_ini == 'Setingkat Lebih Rendah':
                data.extend([2])
            else:
                if Tingkat_pendidikan_yang_paling_tepat_sesuai_untuk_pekerjaan_saat_ini == 'Tidak Perlu Pendidikan Tinggi':
                    data.extend([1])     
                else:
                    data.extend([0])

        
    if Pengetahuan_di_luar_bidang_atau_disiplin_ilmu == 5:
        data.extend([5])
    else:
        if Pengetahuan_di_luar_bidang_atau_disiplin_ilmu == 4:
            data.extend([4])
        else:
            if Pengetahuan_di_luar_bidang_atau_disiplin_ilmu == 3:
                data.extend([3])
            else:
                if Pengetahuan_di_luar_bidang_atau_disiplin_ilmu == 2:
                    data.extend([2])
                else:
                    if Pengetahuan_di_luar_bidang_atau_disiplin_ilmu == 1:
                        data.extend([1])               
                    else:
                        data.extend([0])
                     
                     
    if Pengetahuan_umum == 5:
        data.extend([5])
    else:
        if Pengetahuan_umum == 4:
            data.extend([4])
        else:
            if Pengetahuan_umum == 3:
                data.extend([3])
            else:
                if Pengetahuan_umum == 2:
                    data.extend([2])
                else:
                    if Pengetahuan_umum == 1:
                        data.extend([1])    
                    else:
                        data.extend([0])
 
                     
    if Bahasa_Inggris == 5:
        data.extend([5])
    else:
        if Bahasa_Inggris == 4:
            data.extend([4])
        else:
            if Bahasa_Inggris == 3:
                data.extend([3])
            else:
                if Bahasa_Inggris == 2:
                    data.extend([2])
                else:
                    if Bahasa_Inggris == 1:
                        data.extend([1])    
                    else:
                        data.extend([0])
 
                     
    
    if Keterampilan_internet_teknologi_informasi == 5:
        data.extend([5])
    else:
        if Keterampilan_internet_teknologi_informasi == 4:
            data.extend([4])
        else:
            if Keterampilan_internet_teknologi_informasi == 3:
                data.extend([3])
            else:
                if Keterampilan_internet_teknologi_informasi == 2:
                    data.extend([2])
                else:
                    if Keterampilan_internet_teknologi_informasi == 1:
                        data.extend([1])     
                    else:
                        data.extend([0])
  
 
                     
    if Keterampilan_komputer == 5:
        data.extend([5])
    else:
        if Keterampilan_komputer == 4:
            data.extend([4])
        else:
            if Keterampilan_komputer == 3:
                data.extend([3])
            else:
                if Keterampilan_komputer == 2:
                    data.extend([2])
                else:
                    if Keterampilan_komputer == 1:
                        data.extend([1])  
                    else:
                        data.extend([0])

                     
    if Berpikir_kritis == 5:
        data.extend([5])
    else:
        if Berpikir_kritis == 4:
            data.extend([4])
        else:
            if Berpikir_kritis == 3:
                data.extend([3])
            else:
                if Berpikir_kritis == 2:
                    data.extend([2])
                else:
                    if Berpikir_kritis == 1:
                        data.extend([1])  
                    else:
                        data.extend([0])

                     

    if Keterampilan_riset == 5:
        data.extend([5])
    else:
        if Keterampilan_riset == 4:
            data.extend([4])
        else:
            if Keterampilan_riset == 3:
                data.extend([3])
            else:
                if Keterampilan_riset == 2:
                    data.extend([2])
                else:
                    if Keterampilan_riset == 1:
                        data.extend([1])  
                    else:
                        data.extend([0])


                     
    if Kemampuan_belajar == 5:
        data.extend([5])
    else:
        if Kemampuan_belajar == 4:
            data.extend([4])
        else:
            if Kemampuan_belajar == 3:
                data.extend([3])
            else:
                if Kemampuan_belajar == 2:
                    data.extend([2])
                else:
                    if Kemampuan_belajar == 1:
                        data.extend([1])  
                    else:
                        data.extend([0])


    if Kemampuan_berkomunikasi == 5:
        data.extend([5])
    else:
        if Kemampuan_berkomunikasi == 4:
            data.extend([4])
        else:
            if Kemampuan_berkomunikasi == 3:
                data.extend([3])
            else:
                if Kemampuan_berkomunikasi == 2:
                    data.extend([2])
                else:
                    if Kemampuan_berkomunikasi == 1:
                        data.extend([1]) 
                    else:
                        data.extend([0])

                     

    if Bekerja_di_bawah_tekanan == 5:
        data.extend([5])
    else:
        if Bekerja_di_bawah_tekanan == 4:
            data.extend([4])
        else:
            if Bekerja_di_bawah_tekanan == 3:
                data.extend([3])
            else:
                if Bekerja_di_bawah_tekanan == 2:
                    data.extend([2])
                else:
                    if Bekerja_di_bawah_tekanan == 1:
                        data.extend([1]) 
                    else:
                        data.extend([0])

                     
    if Manajemen_waktu == 5:
        data.extend([5])
    else:
        if Manajemen_waktu == 4:
            data.extend([4])
        else:
            if Manajemen_waktu == 3:
                data.extend([3])
            else:
                if Manajemen_waktu == 2:
                    data.extend([2])
                else:
                    if Manajemen_waktu == 1:
                        data.extend([1]) 
                    else:
                        data.extend([0])

                     
        
    if Bekerja_secara_mandiri == 5:
        data.extend([5])
    else:
        if Bekerja_secara_mandiri == 4:
            data.extend([4])
        else:
            if Bekerja_secara_mandiri == 3:
                data.extend([3])
            else:
                if Bekerja_secara_mandiri == 2:
                    data.extend([2])
                else:
                    if Bekerja_secara_mandiri == 1:
                        data.extend([1])         
                    else:
                        data.extend([0])
        
        
    if Bekerja_dalam_tim_bekerjasama_dengan_orang_lain == 5:
        data.extend([5])
    else:
        if Bekerja_dalam_tim_bekerjasama_dengan_orang_lain == 4:
            data.extend([4])
        else:
            if Bekerja_dalam_tim_bekerjasama_dengan_orang_lain == 3:
                data.extend([3])
            else:
                if Bekerja_dalam_tim_bekerjasama_dengan_orang_lain == 2:
                    data.extend([2])
                else:
                    if Bekerja_dalam_tim_bekerjasama_dengan_orang_lain == 1:
                        data.extend([1])        
                    else:
                        data.extend([0])

                     
                     
        
    if Kemampuan_dalam_memecahkan_masalah == 5:
        data.extend([5])
    else:
        if Kemampuan_dalam_memecahkan_masalah == 4:
            data.extend([4])
        else:
            if Kemampuan_dalam_memecahkan_masalah == 3:
                data.extend([3])
            else:
                if Kemampuan_dalam_memecahkan_masalah == 2:
                    data.extend([2])
                else:
                    if Kemampuan_dalam_memecahkan_masalah == 1:
                        data.extend([1])         
                    else:
                        data.extend([0])

                     
        
    if Negosiasi == 5:
        data.extend([5])
    else:
        if Negosiasi == 4:
            data.extend([4])
        else:
            if Negosiasi == 3:
                data.extend([3])
            else:
                if Negosiasi == 2:
                    data.extend([2])
                else:
                    if Negosiasi == 1:
                        data.extend([1])         
                    else:
                        data.extend([0])

                     
        
    if Kemampuan_analisis == 5:
        data.extend([5])
    else:
        if Kemampuan_analisis == 4:
            data.extend([4])
        else:
            if Kemampuan_analisis == 3:
                data.extend([3])
            else:
                if Kemampuan_analisis == 2:
                    data.extend([2])
                else:
                    if Kemampuan_analisis == 1:
                        data.extend([1])  
                    else:
                        data.extend([0])
                     

    if Toleransi == 5:
        data.extend([5])
    else:
        if Toleransi == 4:
            data.extend([4])
        else:
            if Toleransi == 3:
                data.extend([3])
            else:
                if Toleransi == 2:
                    data.extend([2])
                else:
                    if Toleransi == 1:
                        data.extend([1])  
                    else:
                        data.extend([0])
                     
        
    if Kemampuan_adaptasi == 5:
        data.extend([5])
    else:
        if Kemampuan_adaptasi == 4:
            data.extend([4])
        else:
            if Kemampuan_adaptasi == 3:
                data.extend([3])
            else:
                if Kemampuan_adaptasi == 2:
                    data.extend([2])
                else:
                    if Kemampuan_adaptasi == 1:
                        data.extend([1])  
                    else:
                        data.extend([0])
                     
        
    if Loyalitas == 5:
        data.extend([5])
    else:
        if Loyalitas == 4:
            data.extend([4])
        else:
            if Loyalitas == 3:
                data.extend([3])
            else:
                if Loyalitas == 2:
                    data.extend([2])
                else:
                    if Loyalitas == 1:
                        data.extend([1])         
                    else:
                        data.extend([0])
                     
        
    if Integritas_etika == 5:
        data.extend([5])
    else:
        if Integritas_etika == 4:
            data.extend([4])
        else:
            if Integritas_etika == 3:
                data.extend([3])
            else:
                if Integritas_etika == 2:
                    data.extend([2])
                else:
                    if Integritas_etika == 1:
                        data.extend([1])          
                    else:
                        data.extend([0])
                     
        
    if Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang == 5:
        data.extend([5])
    else:
        if Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang == 4:
            data.extend([4])
        else:
            if Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang == 3:
                data.extend([3])
            else:
                if Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang == 2:
                    data.extend([2])
                else:
                    if Bekerja_dengan_orang_yang_berbeda_budaya_maupun_latar_belakang == 1:
                        data.extend([1])            
                    else:
                        data.extend([0])
                     
        
    if Kemampuan_dalam_memegang_tanggungjawab == 5:
        data.extend([5])
    else:
        if Kemampuan_dalam_memegang_tanggungjawab == 4:
            data.extend([4])
        else:
            if Kemampuan_dalam_memegang_tanggungjawab == 3:
                data.extend([3])
            else:
                if Kemampuan_dalam_memegang_tanggungjawab == 2:
                    data.extend([2])
                else:
                    if Kemampuan_dalam_memegang_tanggungjawab == 1:
                        data.extend([1])            
                    else:
                        data.extend([0])
                     
                     
     
    if Kepemimpinan == 5:
        data.extend([5])
    else:
        if Kepemimpinan == 4:
            data.extend([4])
        else:
            if Kepemimpinan == 3:
                data.extend([3])
            else:
                if Kepemimpinan == 2:
                    data.extend([2])
                else:
                    if Kepemimpinan == 1:
                        data.extend([1])            
                    else:
                        data.extend([0])
                     
                     

    if Inisiatif == 5:
        data.extend([5])
    else:
        if Inisiatif == 4:
            data.extend([4])
        else:
            if Inisiatif == 3:
                data.extend([3])
            else:
                if Inisiatif == 2:
                    data.extend([2])
                else:
                    if Inisiatif == 1:
                        data.extend([1])            
                    else:
                        data.extend([0])
                     
        
    if Kemampuan_untuk_memresentasikan_ide_produk_laporan == 5:
        data.extend([5])
    else:
        if Kemampuan_untuk_memresentasikan_ide_produk_laporan == 4:
            data.extend([4])
        else:
            if Kemampuan_untuk_memresentasikan_ide_produk_laporan == 3:
                data.extend([3])
            else:
                if Kemampuan_untuk_memresentasikan_ide_produk_laporan == 2:
                    data.extend([2])
                else:
                    if Kemampuan_untuk_memresentasikan_ide_produk_laporan == 1:
                        data.extend([1])  
                    else:
                        data.extend([0])
                     

    if Kemampuan_dalam_menulis_laporan_memo_dan_dokumen == 5:
        data.extend([5])
    else:
        if Kemampuan_dalam_menulis_laporan_memo_dan_dokumen == 4:
            data.extend([4])
        else:
            if Kemampuan_dalam_menulis_laporan_memo_dan_dokumen == 3:
                data.extend([3])
            else:
                if Kemampuan_dalam_menulis_laporan_memo_dan_dokumen == 2:
                    data.extend([2])
                else:
                    if Kemampuan_dalam_menulis_laporan_memo_dan_dokumen == 1:
                        data.extend([1])   
                    else:
                        data.extend([0])
                        

    if Manajemen_proyek_program == 5:
        data.extend([5])
    else:
        if Manajemen_proyek_program == 4:
            data.extend([4])
        else:
            if Manajemen_proyek_program == 3:
                data.extend([3])
            else:
                if Manajemen_proyek_program == 2:
                    data.extend([2])
                else:
                    if Manajemen_proyek_program == 1:
                        data.extend([1])
                    else:
                        data.extend([0])
    
   
    prediction = model.predict([data])
    output = round(prediction[0], 2)
   
    return render_template('index.html', tinggkat_kepuasan=output)
   

if __name__ == '__main__':
    app.run(debug=True)