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
    id_khotbah = models.AutoField(primary_key=True)
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
    foto_dokumentasi = models.ImageField(upload_to='static/dist/img')
    nama_kegiatan = models.CharField(max_length=100)
    tanggal_kegiatan = models.DateField()
    keterangan_kegiatan = models.CharField(max_length=500)
    
class MadminLog(models.Model):
    id_admin = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50, unique=True)
    password = models.CharField(max_length=20) 
    
    
class MKategorial(models.Model):
    kodekategorial = models.CharField(primary_key=True, max_length=10)
    namakategorial = models.CharField(max_length=50)
    

class MKeluarga(models.Model):
    kode_keluarga = models.CharField(primary_key=True,max_length=50)
    nama_kepala_keluarga = models.CharField(max_length=50)
    alamat_keluarga = models.CharField(max_length=100)
    jumlah_anggota_keluarga = models.IntegerField()
    foto_keluarga = models.ImageField(upload_to='static/dist/img')
    

class MJemaat(models.Model):
    kode_jemaat = models.CharField(primary_key=True,max_length=50)
    kode_keluarga = models.ForeignKey(MKeluarga, on_delete=models.CASCADE)
    nama_jemaat = models.CharField(max_length=50)
    status_dalam_keluarga = models.CharField(max_length=50)
    tanggal_lahir = models.DateField()
    jenis_kelamin = models.CharField(max_length=50)
    kodekategorial = models.ForeignKey(MKategorial, on_delete=models.CASCADE)
    status_baptis = models.CharField(max_length=50)
    status_sidi = models.CharField(max_length=50)
    nomor_telepon = models.CharField(max_length=20)
    pendidikan = models.CharField(max_length=50)
    pekerjaan = models.CharField(max_length=50)
    
class MOrjem(models.Model):
    kode_org_jemaat = models.CharField(primary_key=True, max_length=50)
    jabatan_org_jemaat = models.CharField(max_length=50)
    nomor_urut = models.CharField(max_length=50)
    
class MPengjem(models.Model):
    periode = models.CharField(max_length=50)
    kode_org_jemaat = models.ForeignKey(MOrjem, on_delete=models.CASCADE)
    kode_jemaat = models.ForeignKey(MJemaat, on_delete=models.CASCADE)
    kemajelisan = models.CharField(max_length=50)
    
class MOrkat(models.Model):
    kodekategorial = models.ForeignKey(MKategorial, on_delete=models.CASCADE)
    jabatan_kategorial = models.CharField(max_length=50)
    nomor_urut = models.CharField(max_length=50)
    
class MPengkat(models.Model):
    periode = models.CharField(max_length=50)
    kodekategorial = models.ForeignKey(MKategorial, on_delete=models.CASCADE)
    jabatan_kategorial = models.ForeignKey(MOrkat, on_delete=models.CASCADE )
    kode_jemaat = models.ForeignKey(MJemaat, on_delete=models.CASCADE)
    
class MJenisibadah(models.Model):
    kode_jenis_ibadah = models.CharField(primary_key=True, max_length=50)
    nama_jenis_ibadah = models.CharField(max_length=50)
    periode = models.CharField(max_length=50)
    
class MJnstgsibd(models.Model):
    kode_jenis_tugas_ibadah = models.CharField(primary_key=True, max_length=50)
    kode_jenis_ibadah =models.ForeignKey(MJenisibadah, on_delete=models.CASCADE)
    nomor_urut = models.CharField(max_length=50)
    jenis_tugas_ibadah = models.CharField(max_length=50)

class MJdwlibadah(models.Model):
    id_ibadah = models.CharField(primary_key=True,max_length=50)
    kode_jenis_ibadah =models.ForeignKey(MJenisibadah, on_delete=models.CASCADE)
    tanggal_ibadah =  models.DateTimeField()
    jam_ibadah = models.CharField(max_length=50)
    
class MPtgsibadah(models.Model):
    id_ibadah = models.ForeignKey(MJdwlibadah, on_delete=models.CASCADE)
    kode_jenis_tugas_ibadah = models.ForeignKey(MJnstgsibd, on_delete=models.CASCADE)
    kode_jemaat = models.ForeignKey(MJemaat, on_delete=models.CASCADE)
    nomor_urut = models.CharField(max_length=50)
    
class MJnskolekte(models.Model):
    kode_jenis_persembahan = models.CharField(primary_key=True,max_length=50)
    nama_jenis_persembahan = models.CharField(max_length=50)
    
class MKolekte(models.Model):
    id_ibadah = models.ForeignKey(MJdwlibadah, on_delete=models.CASCADE)
    kode_jenis_persembahan = models.ForeignKey(MJnskolekte, on_delete=models.CASCADE)
    jumlah_persembahan = models.CharField(max_length=50)

class MHadir(models.Model):
    id_ibadah = models.ForeignKey(MJdwlibadah, on_delete=models.CASCADE)
    kodekategorial = models.ForeignKey(MKategorial, on_delete=models.CASCADE)
    jumlah_kehadiran = models.CharField(max_length=50)

    
    

    
    
    

    
    

    
    
    
