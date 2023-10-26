from django.urls import path
# from .  views import tambah_beranda,home,postberanda,beranda,postupdate_beranda,updateberanda,profilpendeta,postprofilpendeta,profil,updateprofil_pendeta
from . views import * 
urlpatterns = [
    path('',home,name='home'),
    
    path('tambah_beranda',tambah_beranda,name='tambahberanda'),
    path('postberanda',postberanda,name='postberanda'),
    path('beranda',beranda,name='beranda'),
    path('updateberanda/<str:id>',updateberanda,name='updateberanda',),
    path('postupdate_beranda/<str:id>', postupdate_beranda, name='postupdate_beranda'),
    
    path('profilpendeta', profilpendeta, name='profilpendeta'),
    path('postprofil_pendeta',postprofilpendeta,name='postprofil_pendeta'),
    path('profil',profil,name='profil'),
    path('updateprofil_pendeta/<str:id>',updateprofil_pendeta,name='updateprofilpendeta'),
    path('postupdate_profil_pendeta/<str:id>', postupdateprofil_pendeta, name='postupdateprofilpendeta'),
    
    path ('khotbah',khotbah,name='khotbah'),
    path('tambah_khotbah',tambah_khotbah,name='tambah_khotbah'),
    path('posttambah_khotbah',posttambah_khotbah,name='posttambah_khotbah'),
    path('update_khotbah/<int:id_khotbah>',update_khotbah,name='update_khotbah'),
    path('postupdate_khotbah/<int:id_khotbah>',postupdate_khotbah,name='postupdate_khotbah'),
    path('delete_khotbah/<int:id_khotbah>',delete_khotbah,name='delete_khotbah'),
    
    path('warta',warta,name='warta'),
    path('tambah_warta',tambah_warta,name='tambah_warta'),
    path('posttambah_warta',posttambah_warta,name='posttambah_warta'),
    path('update_warta/<str:id_warta>',update_warta,name='update_warta'),
    path('postupdate_warta/<str:id_warta>',postupdate_warta,name='postupdate_warta'),
    path('delete_warta/<str:id_warta>',delete_warta,name='delete_warta'),
  
    path('renungan',renungan,name='renungan'),
    path('tambah_renungan',tambah_renungan,name='tambah_renungan'),
    path('posttambah_renungan',posttambah_renungan,name='posttambah_renungan'),
    path('update_renungan/<str:id_renungan>',update_renungan,name='update_renungan'),
    path('postupdate_renungan/<str:id_renungan>',postupdate_renungan,name='postupdate_renungan'),
    path('delete_renungan/<str:id_renungan>',delete_renungan,name='delete_renungan'),
  
    path('dokumentasi',dokumentasi,name='dokumentasi'),
    path('tambah_dokumentasi',tambah_dokumentasi,name='tambah_dokumentasi'),
    path('posttambah_dokumentasi',posttambah_dokumentasi,name='posttambah_dokumentasi'),
    path('update_dokumentasi/<str:id_dokumentasi>',update_dokumentasi,name='update_dokumentasi'),
    path('postupdate_dokumentasi/<str:id_dokumentasi>',postupdate_dokumentasi,name='postupdate_dokumentasi'),
    path('delete_dokumentasi/<str:id_dokumentasi>',delete_dokumentasi,name='delete_dokumentasi'),
    
    path('registrasi',registrasi,name='registrasi'),
   # path('tambah_registrasi',tambah_registrasi,name='tambah_registrasi'),
    path('posttambah_registrasi',posttambah_registrasi,name='posttambah_registrasi'),
    
    path('login',login,name='login'),
    path('form_login',form_login,name='form_login'),
    path('logout',logout,name='logout'),


    # URLS Profile Page
    path('home_profile', home_profile, name='home_profile'),
    path('document_page', document_page, name='document_page'),
    path('warta_page', warta_page, name='warta_page'),
    path('renungan_page', renungan_page, name='renungan_page'),
    path('khotbah_page', khotbah_page, name='khotbah_page'),
    path('detail_renungan/<str:id_renungan>', detail_renungan, name='detail_renungan'),
    path('detail_khotbah/<str:id_khotbah>', detail_khotbah, name='detail_khotbah'),
    path('send_email', send_email, name="send_email"),
    
    #URL Data Keluarga
    path('keluarga',keluarga,name='keluarga'),
    path('tambah_keluarga',tambah_keluarga,name='tambah_keluarga'),
    path('post_keluarga',post_keluarga,name='post_keluarga'),
    path('update_keluarga/<str:kode_keluarga>',update_keluarga,name='update_keluarga'),
    path('postupdate_keluarga/<str:kode_keluarga>',postupdate_keluarga,name='postupdate_keluarga'),
    path('delete_keluarga/<str:kode_keluarga>',delete_keluarga,name='delete_keluarga'),
    
    
    path('kategorial',kategorial,name='kategorial'),
    #URL Data  jemaat
    path('jemaat',jemaat,name='jemaat'),
    path('tambah_jemaat/<str:kode_keluarga>',tambah_jemaat,name='tambah_jemaat'),
    path('post_jemaat',post_jemaat,name='post_jemaat'),
    path('update_jemaat/<str:kode_jemaat>',update_jemaat,name='update_jemaat'),
    path('postupdate_jemaat/<str:kode_jemaat>',postupdate_jemaat,name='postupdate_jemaat'),
    path('delete_jemaat/<str:kode_jemaat>',delete_jemaat,name='delete_jemaat'),
    
    path('detail_keluarga/<str:kode_keluarga>',detail_keluarga,name='detail_keluarga'),
    
    #pengurus jemaat
    path('pengurus_jemaat',pengurus_jemaat,name='pengurus_jemaat'),
    path('tambah_pengurus_jemaat',tambah_pengurus_jemaat,name='tambah_pengurus_jemaat'),
    path('post_pengurus_jemaat',post_pengurus_jemaat,name='post_pengurus_jemaat'),
    path('update_pengurus_jemaat/<int:id>',update_pengurus_jemaat,name='update_pengurus_jemaat'),
    path('postupdate_pengurus_jemaat/<int:id>',postupdate_pengurus_jemaat,name='postupdate_pengurus_jemaat'),
    path('delete_pengurus_jemaat/<int:id>',delete_pengurus_jemaat,name='delete_pengurus_jemaat'),
    
    path('organisasi_jemaat',organisasi_jemaat,name='organisasi_jemaat'),
    
    path('organisasi_kategorial',organisasi_kategorial,name='organisasi_kategorial'),
    
    #pengurus kategorial
    path('pengurus_kategorial',pengurus_kategorial,name='pengurus_kategorial'),
    path('tambah_pengurus_kategorial',tambah_pengurus_kategorial,name='tambah_pengurus_kategorial'),
    path('post_pengurus_kategorial',post_pengurus_kategorial,name='post_pengurus_kategorial'),
    path('update_pengurus_kategorial/<int:id>',update_pengurus_kategorial,name='update_pengurus_kategorial'),
    path('postupdate_pengurus_kategorial/<int:id>',postupdate_pengurus_kategorial,name='postupdate_pengurus_kategorial'),
    path('delete_pengurus_kategorial/<int:id>',delete_pengurus_kategorial,name='delete_pengurus_kategorial'),
    
    #jenis ibadah
    path('jenis_ibadah',jenis_ibadah,name='jenis_ibadah'),
    path('tambah_jenis_ibadah',tambah_jenis_ibadah,name='tambah_jenis_ibadah'),
    path('post_jenis_ibadah',post_jenis_ibadah,name='post_jenis_ibadah'),
    path('update_jenis_ibadah/<str:kode_jenis_ibadah>',update_jenis_ibadah,name='update_jenis_ibadah'),
    path('postupdate_jenis_ibadah/<str:kode_jenis_ibadah>',postupdate_jenis_ibadah,name='postupdate_jenis_ibadah'),
    path('delete_jenis_ibadah/<str:kode_jenis_ibadah>',delete_jenis_ibadah,name='delete_jenis_ibadah'),
    
    #jenis  tugas ibadah
    path('jenis_tugas_ibadah',jenis_tugas_ibadah,name='jenis_tugas_ibadah'),
    path('tambah_jenis_tugas_ibadah',tambah_jenis_tugas_ibadah,name='tambah_jenis_tugas_ibadah'),
    path('post_jenis_tugas_ibadah',post_jenis_tugas_ibadah,name='post_jenis_tugas_ibadah'),
    path('update_jenis_tugas_ibadah/<str:kode_jenis_tugas_ibadah>',update_jenis_tugas_ibadah,name='update_jenis_tugas_ibadah'),
    path('postupdate_jenis_tugas_ibadah/<str:kode_jenis_tugas_ibadah>',postupdate_jenis_tugas_ibadah,name='postupdate_jenis_tugas_ibadah'),
    path('delete_jenis_tugas_ibadah/<str:kode_jenis_tugas_ibadah>',delete_jenis_tugas_ibadah,name='delete_jenis_tugas_ibadah'),
    
    #jadwal ibadah
    path('jadwal_ibadah',jadwal_ibadah,name='jadwal_ibadah'),
    path('tambah_jadwal_ibadah',tambah_jadwal_ibadah,name='tambah_jadwal_ibadah'),
    path('post_jadwal_ibadah',post_jadwal_ibadah,name='post_jadwal_ibadah'),
    path('update_jadwal_ibadah/<str:id_ibadah>',update_jadwal_ibadah,name='update_jadwal_ibadah'),
    path('postupdate_jadwal_ibadah/<str:id_ibadah>',postupdate_jadwal_ibadah,name='postupdate_jadwal_ibadah'),
    # path('delete_jadwal_ibadah/<str:id_ibadah>',delete_jadwal_ibadah,name='delete_jenis_tugas_ibadah'),
    
    
]

