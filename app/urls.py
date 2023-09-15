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
  
 
]

