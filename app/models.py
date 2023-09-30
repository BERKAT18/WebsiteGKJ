from django.db import models

# Create your models here.
class MGereja(models.Model):
    namagereja = models.CharField(max_length=20)
    alamatgereja = models.CharField(max_length=100)
    telepongereja = models.CharField(max_length=15)
    emailgereja = models.EmailField(max_length=225, blank=True, unique=True)
    tanggalberdiri = models.DateField()
    tema = models.CharField(max_length=100)
    ayatemas = models.CharField(max_length=50)
    isi_ayatemas = models.CharField(max_length=500, blank=True)
    
class MPendeta(models.Model):
    namapendeta = models.CharField(max_length=50)
    fotopendeta = models.ImageField(upload_to='static/dist/img', blank=True, null=True)
    tlpn_pendeta = models.CharField(max_length=20, blank=True)
    email_pendeta = models.EmailField(max_length=225, unique=True, blank=True)
    pendidikan_pendeta = models.CharField(max_length=225, blank=True)
    visi = models.CharField(max_length=500)
    misi = models.CharField(max_length=1000)
    jadwal = models.CharField(max_length=100)
    

class MKhotbah (models.Model):
    id_khotbah = models.CharField(primary_key=True, max_length=10)
    judul_khotbah = models.CharField(max_length=225, blank=True)
    ayat_khotbah = models.CharField(max_length=225, blank=True)
    isi_khotbah = models.CharField(max_length=1000)
    tanggal = models.DateField()
    
    
class MWarta(models.Model):
    id_warta = models.CharField(primary_key=True, max_length=10)
    judul_warta = models.CharField(max_length=225, blank=True)
    isi_warta = models.CharField(max_length=1000)
    tanggal_warta = models.DateField()
    
class MRenungan(models.Model):
    id_renungan = models.CharField(primary_key=True, max_length=50)   
    judul_renungan = models.CharField(max_length=225, blank=True)
    ayat_renungan = models.CharField(max_length=225, blank=True)
    isi_renungan = models.CharField(max_length=1000)
    tanggal_renungan = models.DateField()

class MDokumentasi(models.Model):
    id_dokumentasi = models.CharField(primary_key=True, max_length=50)
    foto_dokumentasi = models.ImageField(upload_to='static/dist/img', blank=True, null=True)
    nama_kegiatan = models.CharField(max_length=100)
    tanggal_kegiatan = models.DateField()
    keterangan_kegiatan = models.CharField(max_length=500)
    
class MadminLog(models.Model):
    id_admin = models.AutoField(primary_key=True, max_length=10)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20) 
    # class MKategorial(models.Model):
#     kodekategorial = models.CharField(primary_key=True, max_length=10)
#     namakategorial = models.CharField(max_length=10)
    
# class MKeluarga(models.Model):
#     kodekeluarga =models.CharField(primary_key=True, max_length=50)
#     nama_kepala_keluarga = models.CharField(max_length=50)
#     alamat_keluarga = models.CharField(max_length=10)
#     jumlah_anggota_keluarga = models.IntegerField(max_length=50)
#     foto_keluarga = models.ImageField(upload_to='static/dist/img', blank=True, null=True)
       
    