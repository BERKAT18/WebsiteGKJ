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
    path('update_khotbah/<str:id_khotbah>',update_khotbah,name='update_khotbah'),
    path('postupdate_khotbah/<str:id_khotbah>',postupdate_khotbah,name='postupdate_khotbah'),
    path('delete_khotbah/<str:id_khotbah>',delete_khotbah,name='delete_khotbah'),
    
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


    # URLS Proile Page
    path('home_profile', home_profile, name='home_profile'),
    path('document_page', document_page, name='document_page'),
    path('warta_page', warta_page, name='warta_page'),
    path('renungan_page', renungan_page, name='renungan_page'),
    path('khotbah_page', khotbah_page, name='khotbah_page'),
 
]

