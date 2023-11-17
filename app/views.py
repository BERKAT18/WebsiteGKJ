from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.shortcuts import render
from .models import MGereja, MPendeta , MKhotbah,MWarta,MRenungan,MDokumentasi,MadminLog, MDokumentasi,MKeluarga,MJemaat,MOrjem,MPengjem,MKategorial,MOrkat,MPengkat,MJenisibadah,MJnstgsibd,MJdwlibadah,MPtgsibadah,MJnskolekte,MKolekte,MHadir
from django.contrib.auth import authenticate, login
from .decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
import os
from django.http import JsonResponse
from django.shortcuts import render
# from .forms import KolekteForm
from .models import MKolekte


# Create your views here.
from django.urls import reverse


def home(request):
    return render(request, 'home.html')

@login_required()
def tambah_beranda(request):
    return render(request, 'tambah-beranda.html')


def postberanda(request):
    namagereja = request.POST['namagereja']
    alamatgereja = request.POST['alamatgereja']
    telepongereja = request.POST['telepongereja']
    emailgereja = request.POST['emailgereja']
    isi_ayatemas = request.POST['isi_ayatemas']
    tanggalberdiri = request.POST['tanggalberdiri']
    tema = request.POST['tema']
    ayatemas = request.POST['ayatemas']
    simpanberanda = MGereja(
        alamatgereja=alamatgereja,
        telepongereja=telepongereja,
        emailgereja = emailgereja,
        isi_ayatemas= isi_ayatemas,
        namagereja=namagereja,
        tanggalberdiri=tanggalberdiri,
        tema=tema,
        ayatemas=ayatemas
    )
    simpanberanda.save()
    messages.success(request, 'Data Beranda Berhasil DiTambah')
    return redirect('beranda')

@login_required()
def beranda(request):
    databeranda = MGereja.objects.all()
    context = {
        'databeranda': databeranda,
        'menu' : 'beranda'

    }
    return render(request, 'beranda.html', context)

def updateberanda(request, id):
    databeranda = MGereja.objects.get(id=id)
    context = {
        'databeranda': databeranda
    }
    return render(request, 'templates/update-beranda.html', context) # Menggunakan 'beranda.html' tanpa path ke folder 'templates'

def postupdate_beranda(request, id):  # Menambahkan id sebagai argumen
    namagereja = request.POST['namagereja']
    alamatgereja = request.POST['alamatgereja']
    telepongereja = request.POST['telepongereja']
    emailgereja =request.POST ['emailgereja']
    tanggalberdiri = request.POST['tanggalberdiri']
    tema = request.POST['tema']
    ayatemas = request.POST['ayatemas']
    isi_ayatemas = request.POST['isi_ayatemas']

    updateberanda = MGereja.objects.get(id=id)

    updateberanda.namagereja = namagereja
    updateberanda.alamatgereja = alamatgereja
    updateberanda.telepongereja = telepongereja
    updateberanda.emailgereja = emailgereja
    updateberanda.tanggalberdiri = tanggalberdiri
    updateberanda.tema = tema
    updateberanda.ayatemas = ayatemas
    updateberanda.isi_ayatemas =isi_ayatemas

    updateberanda.save()

    messages.success(request, 'Data telah diperbarui.')
    return redirect('beranda')  # Menggunakan 'beranda' sebagai argumen untuk redirect

@login_required()
def profilpendeta(request):
    gereja = MPendeta.objects.all() # Mengambil objek berdasarkan id yang diberikan dalam URL
    context = {
       'gereja' : gereja,
       'menu': 'profil'
    }
    
    return render(request, 'datapendeta/profilpendeta.html', context)

def postprofilpendeta(request):
    namapendeta = request.POST['namapendeta']
    fotopendeta = request.FILES['fotopendeta']
    tlpn_pendeta = request.POST['tlpn_pendeta']
    email_pendeta = request.POST['email_pendeta']
    pendidikan_pendeta = request.POST['pendidikan_pendeta']
    visi = request.POST['visi']
    misi = request.POST['misi']
    jadwal = request.POST['jadwal']
    
    postprofil = MPendeta(
    namapendeta = namapendeta,
    fotopendeta = fotopendeta,
    tlpn_pendeta = tlpn_pendeta,
    email_pendeta = email_pendeta,
    pendidikan_pendeta = pendidikan_pendeta,
    visi = visi,
    misi = misi,
    jadwal = jadwal
    )
    postprofil.save()
    messages.success(request, 'Data telah diperbarui.')
    return redirect('profilpendeta') 

def updateprofil_pendeta(request, id):
    datapendeta = MPendeta.objects.get(id=id)
    context = {
        'datapendeta': datapendeta
    }
    return render(request, 'datapendeta/update-profile-pendeta.html', context)

def postupdateprofil_pendeta(request, id):
    postupdateprofilpendeta = MPendeta.objects.get(id=id)

    if request.FILES.get('fotopendeta'):
        if postupdateprofilpendeta.fotopendeta:
            os.remove(postupdateprofilpendeta.fotopendeta.path)
        postupdateprofilpendeta.fotopendeta = request.FILES['fotopendeta']

    postupdateprofilpendeta.namapendeta = request.POST.get('namapendeta')
    postupdateprofilpendeta.tlpn_pendeta = request.POST.get('tlpn_pendeta')
    postupdateprofilpendeta.email_pendeta = request.POST.get('email_pendeta')
    postupdateprofilpendeta.pendidikan_pendeta = request.POST.get('pendidikan_pendeta')
    postupdateprofilpendeta.visi = request.POST.get('visi')
    postupdateprofilpendeta.misi = request.POST.get('misi')
    postupdateprofilpendeta.jadwal = request.POST.get('jadwal')

    postupdateprofilpendeta.save()
    messages.success(request, 'Data telah diperbarui.')
    return redirect('profilpendeta')


def profil(request):
    return render(request,'datapendeta/tambah-profilpendeta.html')

@login_required()
def khotbah(request):
    data_khotbah = MKhotbah.objects.all()
    context = {
       'data_khotbah' : data_khotbah,
       'menu': 'khotbah'
    }
    
    return render(request, 'datakhotbah/khotbah.html', context)

def tambah_khotbah(request):
    return render(request, 'datakhotbah/tambah-khotbah.html')

def posttambah_khotbah(request):
    
    judul_khotbah = request.POST['judul_khotbah']
    ayat_khotbah = request.POST['ayat_khotbah']
    isi_khotbah = request.POST['isi_khotbah']
    tanggal = request.POST['tanggal']

    postkhotbah = MKhotbah(
   
    judul_khotbah = judul_khotbah,
    ayat_khotbah = ayat_khotbah,
    isi_khotbah = isi_khotbah,
    tanggal = tanggal
   
    )
    postkhotbah.save()
    messages.success(request, 'Data khotbah berhasil ditambah.')
    return redirect('khotbah') 

def update_khotbah(request, id_khotbah):
    data_khotbah = MKhotbah.objects.get(id_khotbah=id_khotbah)
    context = {
        'data_khotbah': data_khotbah
    }
    return render(request, 'datakhotbah/update-khotbah.html', context) # Menggunakan 'khotbah.html' tanpa path ke folder 'templates'

def postupdate_khotbah(request, id_khotbah):  # Menambahkan id sebagai argumen
    id_khotbah = request.POST['id_khotbah']
    judul_khotbah = request.POST['judul_khotbah']
    ayat_khotbah = request.POST['ayat_khotbah']
    isi_khotbah = request.POST['isi_khotbah']
    tanggal = request.POST['tanggal']
  

    update_khotbah = MKhotbah.objects.get(id_khotbah=id_khotbah)

    update_khotbah.id_khotbah = id_khotbah
    update_khotbah.judul_khotbah = judul_khotbah
    update_khotbah.ayat_khotbah = ayat_khotbah
    update_khotbah.isi_khotbah = isi_khotbah
    update_khotbah.tanggal = tanggal
  

    update_khotbah.save()

    messages.success(request, 'Data telah diperbarui.')
    return redirect('khotbah')

def delete_khotbah(request, id_khotbah):
    khotbah = MKhotbah.objects.get(id_khotbah=id_khotbah).delete()
    messages.success(request, 'Berhasil hapus data khotbah')
    return redirect('khotbah')

@login_required()
def warta(request):
    data_warta = MWarta.objects.all()
    context = {
       'data_warta' : data_warta,
       'menu' : 'warta'
    }
    
    return render(request, 'datawarta/warta.html', context)

def tambah_warta(request):
    return render(request, 'datawarta/tambah-warta.html')

def posttambah_warta(request):
    id_warta = request.POST['id_warta']
    judul_warta = request.POST['judul_warta']
    isi_warta = request.POST['isi_warta']
    tanggal_warta = request.POST['tanggal_warta']
    
    if MWarta.objects.filter(id_warta=id_warta).exists():
        messages.error(request, 'ID warta Sudah Terdaftar ')
        return redirect('tambah_warta')
    
    postwarta = MWarta(
    id_warta = id_warta,
    judul_warta = judul_warta,
    isi_warta = isi_warta,
    tanggal_warta = tanggal_warta
   
    )
    postwarta.save()
    messages.success(request, 'Data warta berhasil ditambah.')
    return redirect('warta') 

def update_warta(request, id_warta):
    data_warta = MWarta.objects.get(id_warta=id_warta)
    context = {
        'data_warta': data_warta
    }
    return render(request, 'datawarta/update-warta.html', context) # Menggunakan 'khotbah.html' tanpa path ke folder 'templates'


def postupdate_warta(request, id_warta):  # Menambahkan id sebagai argumen
    id_warta = request.POST['id_warta']
    judul_warta = request.POST['judul_warta']
    isi_warta = request.POST['isi_warta']
    tanggal_warta = request.POST['tanggal_warta']
  

    update_warta = MWarta.objects.get(id_warta=id_warta)

    update_warta.id_warta = id_warta
    update_warta.judul_warta = judul_warta
    update_warta.isi_warta = isi_warta
    update_warta.tanggal_warta = tanggal_warta
  

    update_warta.save()

    messages.success(request, 'Data telah diperbarui.')
    return redirect('warta')

def delete_warta(request, id_warta):
    warta = MWarta.objects.get(id_warta=id_warta).delete()
    messages.success(request, 'Berhasil hapus data warta')
    return redirect('warta')


@login_required()
def renungan(request):
    data_renungan = MRenungan.objects.all()
    context = {
       'data_renungan' : data_renungan,
       'menu' : 'renungan'
    }
    
    return render(request, 'datarenungan/renungan.html', context)

def tambah_renungan(request):
    return render(request, 'datarenungan/tambah-renungan.html')

def posttambah_renungan(request):
    id_renungan = request.POST['id_renungan']
    judul_renungan = request.POST['judul_renungan']
    ayat_renungan = request.POST['ayat_renungan']
    isi_renungan = request.POST['isi_renungan']
    tanggal_renungan = request.POST['tanggal_renungan']
    
    if MRenungan.objects.filter(id_renungan=id_renungan).exists():
        messages.error(request, 'ID Renungan Sudah Terdaftar ')
        return redirect('tambah_renungan')
    
    postrenungan = MRenungan(
    id_renungan = id_renungan,
    judul_renungan = judul_renungan,
    ayat_renungan = ayat_renungan,
    isi_renungan = isi_renungan,
    tanggal_renungan = tanggal_renungan
   
    )
    postrenungan.save()
    messages.success(request, 'Data Renungan Berhasil Ditambah.')
    return redirect('renungan') 

def update_renungan(request, id_renungan):
    data_renungan = MRenungan.objects.get(id_renungan=id_renungan)
    context = {
        'data_renungan': data_renungan
    }
    return render(request, 'datarenungan/update-renungan.html', context) # Menggunakan 'khotbah.html' tanpa path ke folder 'templates'

def postupdate_renungan(request, id_renungan):  # Menambahkan id sebagai argumen
    id_renungan = request.POST['id_renungan']
    judul_renungan = request.POST['judul_renungan']
    ayat_renungan = request.POST['ayat_renungan']
    isi_renungan = request.POST['isi_renungan']
    tanggal_renungan = request.POST['tanggal_renungan']
  

    update_renungan = MRenungan.objects.get(id_renungan=id_renungan)

    update_renungan.id_renungan = id_renungan
    update_renungan.judul_renungan = judul_renungan
    update_renungan.ayat_renungan = ayat_renungan
    update_renungan.isi_renungan = isi_renungan
    update_renungan.tanggal_renungan = tanggal_renungan
  

    update_renungan.save()

    messages.success(request, 'Data telah diperbarui.')
    return redirect('renungan')

def delete_renungan(request, id_renungan):
    renungan = MRenungan.objects.get(id_renungan=id_renungan).delete()
    messages.success(request, 'Berhasil hapus data renungan')
    return redirect('renungan')

@login_required()
def dokumentasi(request):
    data_dokumentasi = MDokumentasi.objects.all()
    context = {
       'data_dokumentasi' : data_dokumentasi,
       'menu':'dokumentasi'
    }
    
    return render(request, 'datadokumentasi/dokumentasi.html', context)

def tambah_dokumentasi(request):
    return render(request, 'datadokumentasi/tambah-dokumentasi.html')

def update_dokumentasi(request, id_dokumentasi):
    data_dokumentasi = MDokumentasi.objects.get(id_dokumentasi=id_dokumentasi)
    context = {
        'data_dokumentasi': data_dokumentasi
    }
    return render(request, 'datadokumentasi/update-dokumentasi.html', context) # Menggunakan 'khotbah.html' tanpa path ke folder 'templates'

def postupdate_dokumentasi(request, id_dokumentasi):
    update_dokumentasi = MDokumentasi.objects.get(id_dokumentasi=id_dokumentasi)

    if request.FILES.get('foto_dokumentasi'):
        if update_dokumentasi.foto_dokumentasi:
            os.remove(update_dokumentasi.foto_dokumentasi.path)
        update_dokumentasi.foto_dokumentasi = request.FILES['foto_dokumentasi']

    # Hapus baris-baris berikut, karena Anda sudah mengambil 'id_dokumentasi' dan 'foto_dokumentasi' di atas.
    # id_dokumentasi = request.POST['id_dokumentasi']
    # foto_dokumentasi = request.FILES['foto_dokumentasi']

    # Gunakan request.POST.get() untuk mengambil nilai dari permintaan POST.
    nama_kegiatan = request.POST.get('nama_kegiatan')
    tanggal_kegiatan = request.POST.get('tanggal_kegiatan')
    keterangan_kegiatan = request.POST.get('keterangan_kegiatan')

    # Perbarui atribut-atribut objek 'update_dokumentasi'.
    # Tidak perlu mengatur 'id_dokumentasi' atau 'foto_dokumentasi' karena Anda sudah melakukannya di atas.
    update_dokumentasi.nama_kegiatan = nama_kegiatan
    update_dokumentasi.tanggal_kegiatan = tanggal_kegiatan
    update_dokumentasi.keterangan_kegiatan = keterangan_kegiatan

    update_dokumentasi.save()

    messages.success(request, 'Data Dokumentasi Berhasil DiUpdate.')
    return redirect('dokumentasi')


def posttambah_dokumentasi(request):
    id_dokumentasi = request.POST['id_dokumentasi']
    foto_dokumentasi = request.FILES['foto_dokumentasi']
    nama_kegiatan = request.POST['nama_kegiatan']
    tanggal_kegiatan = request.POST['tanggal_kegiatan']
    keterangan_kegiatan = request.POST['keterangan_kegiatan'] 
    
    if MDokumentasi.objects.filter(id_dokumentasi=id_dokumentasi).exists():
        messages.error(request, 'ID dokumentasi Sudah Terdaftar ')
        return redirect('tambah_dokumentasi')
    
    postdokumentasi = MDokumentasi(
    id_dokumentasi = id_dokumentasi,
    foto_dokumentasi = foto_dokumentasi,
    nama_kegiatan = nama_kegiatan,
    tanggal_kegiatan =tanggal_kegiatan,
    keterangan_kegiatan = keterangan_kegiatan
    
   
    )
    postdokumentasi.save()
    messages.success(request, 'Data telah ditambah.')
    return redirect('dokumentasi') 

def delete_dokumentasi(request, id_dokumentasi):
    dokumentasi = MDokumentasi.objects.get(id_dokumentasi=id_dokumentasi).delete()
    messages.success(request, 'Berhasil hapus data dokumentasi')
    return redirect('dokumentasi')



def registrasi(request):
    return render (request,'login/register.html')

def posttambah_registrasi(request):
    username  = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    
    if MadminLog.objects.filter(email=email).exists():
        messages.error(request, 'EMAIL REGISTERED')
        return redirect ('registrasi')
    
    simpan_registrasi = MadminLog(
        username = username,
        email = email,
        password = password
    )
    simpan_registrasi.save()
    messages.success(request, 'Data telah ditambah.')
    return redirect('login')

def login(request):
    return render(request,'login/login.html')


def form_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Mengambil nilai email dari tabel MadminLog yang cocok dengan email yang diberikan
        result = MadminLog.objects.filter(email=email, password=password).first()

        if result:
            request.session['id_admin'] = result.id_admin  # menyimpan id admin sbg session
            # Jika email cocok, Anda dapat melakukan autentikasi atau tindakan lain yang sesuai
            # Misalnya, autentikasi pengguna dan mengarahkannya ke halaman 'home' jika berhasil
            return redirect('home')  # Ganti 'home' dengan nama URL halaman setelah login berhasil
        else:
            # Jika email tidak cocok, Anda dapat menampilkan pesan kesalahan
            messages.error(request, 'Email is not registered.')
            return redirect('login')

    # Ganti 'login.html' dengan template halaman login Anda
    return render(request, 'login.html') 

def logout(request):
    # hapus data session
    request.session.flush()
    messages.success(request, 'BERHASIL LOGOUT')
    return redirect('login')



# VIEWS Profile Page``

def home_profile(request):
    data_gereja = MGereja.objects.all()
    data_pendeta = MPendeta.objects.all()
    context = {
        'data_gereja' : data_gereja,
        'data_pendeta' : data_pendeta,
    }
    return render (request, 'profile/index.html', context) 

def warta_page(request):
    data_warta = MWarta.objects.all().order_by('tanggal_warta')
    context = {'data_warta' : data_warta}
    return render (request, 'profile/warta.html', context)

def renungan_page(request):
    data_renungan = MRenungan.objects.all()
    data_pendeta = MPendeta.objects.all()
    context = {
        'data_pendeta' : data_pendeta,
        'data_renungan' : data_renungan,
    }
    return render (request, 'profile/renungan.html', context)

def khotbah_page(request):
    data_khotbah = MKhotbah.objects.all()
    data_pendeta = MPendeta.objects.all()
    context = {
        'data_pendeta' : data_pendeta,
        'data_khotbah' : data_khotbah,
    }
    return render (request, 'profile/khotbah.html', context)

def document_page(request):
    data_document = MDokumentasi.objects.all()
    context = {
        'data_document' : data_document,
    }
    return render (request, 'profile/document.html', context)

def detail_renungan(request, id_renungan):
    data_renungan = MRenungan.objects.get(id_renungan=id_renungan)
    data_pendeta = MPendeta.objects.all()
    context = {
        'data_renungan': data_renungan,
        'data_pendeta' : data_pendeta,
    }
    return render(request, 'profile/detailRenungan.html', context)

def detail_khotbah(request, id_khotbah):
    data_khotbah = MKhotbah.objects.get(id_khotbah=id_khotbah)
    data_pendeta = MPendeta.objects.all()
    context = {
        'data_khotbah': data_khotbah,
        'data_pendeta' : data_pendeta,
    }
    return render(request, 'profile/detailKhotbah.html', context)

def send_email(request):
    data_gereja = MGereja.objects.all()
    if request.method == 'POST':
        to_email = 'henochyanuar13@gmail.com' #Untuk Testing Pake Email Sendiri Dulu Aja
        # to_email = 'henochyanuar13@gmail.com'
        #Konfigurasi Email di settings.py
        sender_email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(subject, message, sender_email, [to_email])

        return HttpResponseRedirect(reverse('home_profile'))
    
    return render(request, 'profile/index.html')

#views data keluarga
@login_required()
def keluarga(request):
    datakeluarga = MKeluarga.objects.all().order_by('nama_kepala_keluarga')
    datajemaat = MJemaat.objects.all()
    context = {
        'datakeluarga': datakeluarga,
        'datajemaat': datajemaat,
        'menu': 'keluarga'

    }
    return render(request, 'datakeluarga/keluarga.html', context)

def tambah_keluarga(request):
    datajemaat = MJemaat.objects.all()
    context = {
        'keluarga': datajemaat,
        
    }
    return render(request, 'datakeluarga/tambah-keluarga.html',context)

def post_keluarga(request):
    if request.method == 'POST':
        kode_keluarga = request.POST.get('kode_keluarga')
        nama_kepala_keluarga = request.POST.get('nama_kepala_keluarga')
        alamat_keluarga = request.POST.get('alamat_keluarga')
        jumlah_anggota_keluarga = int(request.POST.get('jumlah_anggota_keluarga'))
        foto_keluarga = request.FILES.get('foto_keluarga')
        
        # if MKeluarga.objects.filter(kode_keluarga=kode_keluarga).exists():
        #     messages.error(request, 'Kode Keluarga Sudah Digunakan')
        #     return redirect('tambah_keluarga')
        first_letter = nama_kepala_keluarga[0].upper()
        # Cari semua kelompok yang memiliki huruf awal yang sama
        existing_kepala_kelarga = MKeluarga.objects.filter(kode_keluarga__startswith=first_letter)
        # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
        number = 1
        while existing_kepala_kelarga.filter(kode_keluarga=first_letter + str(number).zfill(3)).exists():
            number += 1
        # Setel kode_kelompok dengan format yang sesuai
        kode_keluarga = first_letter + str(number).zfill(3)

        simpankeluarga = MKeluarga(
            nama_kepala_keluarga=nama_kepala_keluarga,
            kode_keluarga=kode_keluarga,
            alamat_keluarga=alamat_keluarga,
            jumlah_anggota_keluarga=jumlah_anggota_keluarga,
            foto_keluarga=foto_keluarga,
        )
        simpankeluarga.save()
        messages.success(request, 'Data Keluarga Berhasil DiTambah')
        return redirect('keluarga')


def update_keluarga(request, kode_keluarga):
    datakeluarga = MKeluarga.objects.get(kode_keluarga=kode_keluarga)
    context = {
        'datakeluarga': datakeluarga
    }
    return render(request, 'datakeluarga/update-data-keluarga.html', context) # Menggunakan 'keluarga.html' tanpa path ke folder 'templates'

def postupdate_keluarga(request, kode_keluarga):
        
        kode_keluarga = request.POST['kode_keluarga']  
        nama_kepala_keluarga = request.POST['nama_kepala_keluarga']
        alamat_keluarga = request.POST['alamat_keluarga']
        jumlah_anggota_keluarga = int(request.POST['jumlah_anggota_keluarga'])
        foto_keluarga = request.FILES['foto_keluarga']

        updatekeluarga = MKeluarga.objects.get(kode_keluarga=kode_keluarga)

        # Perbarui nilai-nilai yang sesuai
        updatekeluarga.kode_keluarga = kode_keluarga
        updatekeluarga.nama_kepala_keluarga = nama_kepala_keluarga
        updatekeluarga.alamat_keluarga = alamat_keluarga
        updatekeluarga.jumlah_anggota_keluarga = jumlah_anggota_keluarga
        updatekeluarga.foto_keluarga = foto_keluarga

        updatekeluarga.save()

        messages.success(request, 'Data telah diperbarui.')
        return redirect('keluarga')  # Ganti dengan halaman yang sesuai
   
def delete_keluarga(request, kode_keluarga):
    keluarga = MKeluarga.objects.get(kode_keluarga=kode_keluarga).delete()
    messages.success(request, 'Berhasil hapus data keluarga')
    return redirect('keluarga')

#views jemaat

def kategorial(requset):
    datakategorial = MKategorial.objects.all()
    context = {
        'datakategorial' : datakategorial
    }
    return render ('kategorial',context)

@login_required()
def jemaat(request):
    # search_term = request.GET.get('search')
    datajemaat = MJemaat.objects.all()
    # if search_term:
    #     datajemaat = datajemaat.filter(nama_jemaat__icontains=search_term)
        
    context = {
        'datajemaat': datajemaat,
        #  'search_term' : search_term,
         'menu' : 'jemaat'

    }
    return render(request, 'datajemaat/jemaat.html', context)

def tambah_jemaat(request, kode_keluarga):
    dataanggotakeluarga = MKeluarga.objects.all()
    datakeluarga = MKeluarga.objects.get(kode_keluarga=kode_keluarga)
    dataanggota = MJemaat.objects.filter(kode_keluarga=kode_keluarga)
    datakategorial = MKategorial.objects.all()

    context = {
        'dataanggotakeluarga': dataanggotakeluarga,
        'datakeluarga' : datakeluarga,
        'dataanggota':dataanggota,
        'datakategorial' :datakategorial
        # 'ayahIsExist' : ayahIsExist,
    }
    return render(request, 'datajemaat/tambah-jemaat.html',context)


def post_jemaat(request):
    if request.method == 'POST':
        # kode_jemaat = request.POST['kode_jemaat']
        kode_keluarga = request.POST['kode_keluarga']
        kodekategorial = request.POST['kodekategorial']

        try:
            # Cari objek MKeluarga berdasarkan kode_keluarga
            keluarga = MKeluarga.objects.get(kode_keluarga=kode_keluarga)
        except MKeluarga.DoesNotExist:
            messages.error(request, 'MKeluarga tidak ditemukan')
            return redirect('tambah_jemaat')
        
        # if MJemaat.objects.filter(kode_jemaat=kode_jemaat).exists():
        #     messages.error(request, 'Kode jemaat Sudah Digunakan')
        #     return redirect('tambah_jemaat')
        # Ambil huruf pertama dari nama_kelompok
        first_letter = request.POST['nama_jemaat'][0].upper()
        # Cari semua kelompok yang memiliki huruf awal yang sama
        existing_jemaat = MJemaat.objects.filter(kode_jemaat__startswith=first_letter)
        # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
        number = 1
        while existing_jemaat.filter(kode_jemaat=first_letter + str(number).zfill(3)).exists():
            number += 1
        # Setel kode_kelompok dengan format yang sesuai
        kode_jemaat = first_letter + str(number).zfill(3)
    
    # jika ada kode kelompok yang sama maka akan ada pesan error

        m_kategorial = MKategorial.objects.get(kodekategorial=kodekategorial)

        # Buat objek MJemaat dengan objek MKeluarga yang sudah ditemukan
        simpanjemaat = MJemaat(
            kode_jemaat=kode_jemaat,
            kode_keluarga=keluarga,
            nama_jemaat=request.POST['nama_jemaat'],
            status_dalam_keluarga=request.POST['status_dalam_keluarga'],
            tanggal_lahir=request.POST['tanggal_lahir'],
            jenis_kelamin=request.POST['jenis_kelamin'],
            kodekategorial= m_kategorial,
            status_baptis=request.POST['status_baptis'],
            status_sidi=request.POST['status_sidi'],
            nomor_telepon=request.POST['nomor_telepon'],
            pendidikan=request.POST['pendidikan'],
            pekerjaan=request.POST['pekerjaan']
        )

        simpanjemaat.save()
        messages.success(request, 'Data jemaat Berhasil Ditambah')
        return redirect(reverse('detail_keluarga', args=[kode_keluarga]))
    else:
        return render(request, 'jemaat.html')
        # else:
        # # Tangani jika kode_keluarga tidak valid
        # messages.error(request, 'Kode keluarga tidak valid')
        # return redirect('/tambah_jemaat')

def update_jemaat(request, kode_jemaat):
    datajemaat= MJemaat.objects.get(kode_jemaat=kode_jemaat)
    datakeluarga = MKeluarga.objects.all()
    datakategorial = MKategorial.objects.all()
    
    context = {
        'datajemaat': datajemaat,
        'kode_keluarga': datakeluarga,
        'datakategorial' : datakategorial
    }
    
    return render(request, 'datajemaat/update-data-jemaat.html', context)
def postupdate_jemaat(request, kode_jemaat):
    try:
        datajemaat = MJemaat.objects.get(kode_jemaat=kode_jemaat)
    except MJemaat.DoesNotExist:
        return HttpResponse("MJemaat tidak ditemukan.")

    if request.method == 'POST':
        # Ambil kode_keluarga dari POST request
        kode_keluarga_id = request.POST['kode_keluarga']
        
        try:
            # Cari objek MKeluarga yang sesuai dengan kode_keluarga_id
            kode_keluarga = MKeluarga.objects.get(pk=kode_keluarga_id)
        except MKeluarga.DoesNotExist:
            return HttpResponse("Kode Keluarga tidak ditemukan.")
        
        # Setel MJemaat.kode_keluarga ke objek MKeluarga yang ditemukan
        datajemaat.kode_keluarga = kode_keluarga
        # Kemudian, Anda bisa mengatur atribut-atribut lain sesuai dengan data POST lainnya.
        
        kodekategorial = request.POST['kodekategorial']
        m_kategorial = MKategorial.objects.get(kodekategorial=kodekategorial)

        
        
        datajemaat.nama_jemaat = request.POST['nama_jemaat']
        datajemaat.status_dalam_keluarga = request.POST['status_dalam_keluarga']
        datajemaat.tanggal_lahir = request.POST['tanggal_lahir']
        datajemaat.jenis_kelamin = request.POST['jenis_kelamin']
        datajemaat.kodekategorial = m_kategorial
        datajemaat.status_baptis = request.POST['status_baptis']
        datajemaat.status_sidi = request.POST['status_sidi']
        datajemaat.nomor_telepon = request.POST['nomor_telepon']
        datajemaat.pendidikan = request.POST['pendidikan']
        datajemaat.pekerjaan = request.POST['pekerjaan']

        datajemaat.save()
        messages.success(request, 'Data jemaat Berhasil Diperbarui')
        return redirect('keluarga')

    return HttpResponse("Metode request tidak valid.")


def delete_jemaat(request, kode_jemaat):
    jemaat = MJemaat.objects.get(kode_jemaat=kode_jemaat).delete()
    messages.success(request, 'Berhasil hapus data jemaat')
    return redirect('jemaat')

@login_required()
def detail_keluarga(request, kode_keluarga):
    dataanggotakeluarga = MJemaat.objects.filter(kode_keluarga=kode_keluarga)
    datakeluarga = MKeluarga.objects.get(kode_keluarga=kode_keluarga)
    context = {
        'dataanggotakeluarga': dataanggotakeluarga,
        'datakeluarga' : datakeluarga

    }
    return render(request, 'datakeluarga/detailkeluarga.html', context)


#Pengurus Jemaat
@login_required()
def organisasi_jemaat(request):
    data_orjem = MOrjem.objects.all()
    context = {
        'data_orjem' : data_orjem
    }
    return render (request,'datapengurusjemaat/pengurus_jemaat.html', context)
@login_required()
def pengurus_jemaat(request):
    data_pengjem = MPengjem.objects.all()
    context = {
        'data_pengjem' : data_pengjem,
        'menu':'pengurus_jemaat',
    }
    return render(request, 'datapengurusjemaat/pengurus_jemaat.html', context)


def tambah_pengurus_jemaat(request):
    data_pengjem = MPengjem.objects.all()
    datajemaat= MJemaat.objects.all()
    data_orjem = MOrjem.objects.all()
    data_jemaat_penggurus = MPengjem.objects.values_list('kode_jemaat', flat=True)
    
    context ={
        'data_pengjem' : data_pengjem,
        'datajemaat' : datajemaat,
        'data_orjem' : data_orjem,
        'data_jemaat_penggurus' : data_jemaat_penggurus,
    }
    return render(request, 'datapengurusjemaat/tambah-pengurus-jemaat.html', context)
    
def post_pengurus_jemaat(request):
    periode = request.POST['periode']
    kode_org_jemaat = request.POST['kode_org_jemaat']
    kode_jemaat = request.POST['kode_jemaat']
    kemajelisan = request.POST['kemajelisan']
    
     # Dapatkan objek MOrjem berdasarkan kode_org_jemaat
    m_orjem = MOrjem.objects.get(kode_org_jemaat=kode_org_jemaat)
    m_jemaat = MJemaat.objects.get(kode_jemaat=kode_jemaat)
    post_pengurus = MPengjem(
         periode = periode,
         kode_org_jemaat = m_orjem,
         kode_jemaat = m_jemaat,
         kemajelisan = kemajelisan
    )
    post_pengurus.save()
    messages.success(request, 'Data pengurus telah ditambah.')
    return redirect('pengurus_jemaat')
    
def update_pengurus_jemaat(request,id):
    datajemaat = MJemaat.objects.all()
    data_orjem = MOrjem.objects.all()
    data_pengjem = MPengjem.objects.get(id=id)
    data_jemaat_penggurus = MPengjem.objects.values_list('kode_jemaat', flat=True)

    context = {
        'data_pengjem' : data_pengjem,
        'datajemaat' : datajemaat,
        'data_orjem' : data_orjem,
        'data_jemaat_penggurus' : data_jemaat_penggurus
        
    }
    return render(request, 'datapengurusjemaat/update-pengurus-jemaat.html', context)

# def postupdate_pengurus_jemaat(request,id):
#     periode = request.POST['periode']
#     kode_org_jemaat = request.POST['kode_org_jemaat']
#     kode_jemaat = request.POST['kode_jemaat']
#     kemajelisan = request.POST['kemajelisan']
    
#     update_pengurus = MPengjem.objects.get(id=id)
    
#     update_pengurus.periode = periode
#     update_pengurus.kode_org_jemaat = kode_org_jemaat
#     update_pengurus.kode_jemaat = kode_jemaat
#     update_pengurus.kemajelisan = kemajelisan
    
#     update_pengurus.save()

#     messages.success(request, 'Data telah diperbarui.')
#     return redirect('pengurus_jemaat')
def postupdate_pengurus_jemaat(request, id):
    periode = request.POST['periode']
    kode_org_jemaat = request.POST['kode_org_jemaat']
    kode_jemaat = request.POST['kode_jemaat']
    kemajelisan = request.POST['kemajelisan']
    
    # Dapatkan instansi MOrjem yang sesuai berdasarkan kode_org_jemaat
    m_orjem = MOrjem.objects.get(kode_org_jemaat=kode_org_jemaat)
    
    # Dapatkan instansi MJemaat yang sesuai berdasarkan kode_jemaat
    m_jemaat = MJemaat.objects.get(kode_jemaat=kode_jemaat)
    
    update_pengurus = MPengjem.objects.get(id=id)
    
    update_pengurus.periode = periode
    update_pengurus.kode_org_jemaat = m_orjem  # Tetapkan instansi MOrjem
    update_pengurus.kode_jemaat = m_jemaat  # Tetapkan instansi MJemaat
    update_pengurus.kemajelisan = kemajelisan
    
    update_pengurus.save()

    messages.success(request, 'Data telah diperbarui.')
    return redirect('pengurus_jemaat')

def delete_pengurus_jemaat(request, id):
    MPengjem.objects.get(id=id).delete()
    messages.success(request, 'Berhasil hapus data pengurus jemaat')
    return redirect('pengurus_jemaat')

def organisasi_kategorial(request):
    data_organisasi = MOrkat.objects.all()
    context = {
        'data_organisasi' : data_organisasi
    }
    return render (request,'datapengurusjemaat/pengurus_kategorial.html', context)

@login_required()
def pengurus_kategorial(request):
    data_kategorial = MKategorial.objects.all()
    data_pengkat = MPengkat.objects.all()
    context = {
        'data_pengkat' : data_pengkat,
        'data_kategorial' : data_kategorial,
        'menu':'pengurus_kategorial'
    }
    return render (request,'datapenguruskategorial/pengurus_kategorial.html', context)

def tambah_pengurus_kategorial(request):
    
    data_pengkat = MPengkat.objects.all()
    datajemaat= MJemaat.objects.all()
    datakategorial = MKategorial.objects.all()
    data_organisasi = MOrkat.objects.all()
    
    
    context ={
        'data_pengkat' : data_pengkat,
        'datajemaat' : datajemaat,
        'datakategorial' : datakategorial,
        'data_organisasi' : data_organisasi

        
    }
    return render(request, 'datapenguruskategorial/tambah_pengurus_kategorial.html', context)
   
def post_pengurus_kategorial(request):
    
    periode = request.POST['periode']
    kodekategorial = request.POST['kodekategorial']
    kode_jemaat = request.POST['kode_jemaat']
    jabatan_kategorial = request.POST['jabatan_kategorial']
    
     # Dapatkan objek MOrjem berdasarkan kodekategorial
    m_kat = MKategorial.objects.get(kodekategorial=kodekategorial)
    m_jemaat = MJemaat.objects.get(kode_jemaat=kode_jemaat)
    m_orkat = MOrkat.objects.get(jabatan_kategorial=jabatan_kategorial)

    post_pengurus = MPengkat(
         periode = periode,
         kodekategorial = m_kat,
         kode_jemaat = m_jemaat,
         jabatan_kategorial = m_orkat
    )
    post_pengurus.save()
    messages.success(request, 'Data pengurus telah ditambah.')
    return redirect('pengurus_kategorial')

def update_pengurus_kategorial(request,id):
    data_pengkat = MPengkat.objects.get(id=id)
    datajemaat= MJemaat.objects.all()
    datakategorial = MKategorial.objects.all()
    data_organisasi = MOrkat.objects.all()
    
    
    context ={
        'data_pengkat' : data_pengkat,
        'datajemaat' : datajemaat,
        'datakategorial' : datakategorial,
        'data_organisasi' : data_organisasi

        
    }
    return render(request, 'datapenguruskategorial/update_pengurus_kategorial.html', context)

    
def postupdate_pengurus_kategorial(request,id):
    periode = request.POST['periode']
    kodekategorial = request.POST['kodekategorial']
    kode_jemaat = request.POST['kode_jemaat']
    jabatan_kategorial = request.POST['jabatan_kategorial']
    
     # Dapatkan objek MOrjem berdasarkan kodekategorial
    m_kat = MKategorial.objects.get(kodekategorial=kodekategorial)
    m_jemaat = MJemaat.objects.get(kode_jemaat=kode_jemaat)
    m_orkat = MOrkat.objects.get(jabatan_kategorial=jabatan_kategorial)
    
    update_pengurus = MPengkat.objects.get(id=id)

    update_pengurus.periode = periode 
    update_pengurus.kodekategorial = m_kat 
    update_pengurus.kode_jemaat = m_jemaat 
    update_pengurus.jabatan_kategorial = m_orkat 
   
    update_pengurus.save()
    messages.success(request, 'Data pengurus berhasil diubah.')
    return redirect('pengurus_kategorial')

def delete_pengurus_kategorial(request,id):
    MPengkat.objects.get(id=id).delete()
    messages.success(request, 'Berhasil hapus data pengurus kategorial')
    return redirect('pengurus_kategorial')

#view jenis ibadah
@login_required()
def jenis_ibadah(request):
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_ibadah': data_ibadah,
        'menu':'jenis_ibadah',
    }
    return render(request, 'datajenisibadah/jenis_ibadah.html', context)

def tambah_jenis_ibadah(request):
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_ibadah': data_ibadah
    }
    return render(request, 'datajenisibadah/tambah_jenis_ibadah.html', context)
 
def post_jenis_ibadah(request):
    
    kode_jenis_ibadah = request.POST.get('kode_jenis_ibadah')
    nama_jenis_ibadah = request.POST.get('nama_jenis_ibadah')
    periode = request.POST['periode']    
  
  
    # if MJenisibadah.objects.filter(kode_jenis_ibadah=kode_jenis_ibadah).exists():
    #     messages.error(request, 'Kode Jenis Ibadah Sudah Terdaftar ')
    #     return redirect('tambah_jenis_ibadah')
    first_letter = nama_jenis_ibadah[0].upper()
        # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_kepala_kelarga = MJenisibadah.objects.filter(kode_jenis_ibadah__startswith=first_letter)
        # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_kepala_kelarga.filter(kode_jenis_ibadah=first_letter + str(number).zfill(3)).exists():
        number += 1
        # Setel kode_kelompok dengan format yang sesuai
    kode_jenis_ibadah = first_letter + str(number).zfill(3)

    
    post_ibadah = MJenisibadah(
        kode_jenis_ibadah = kode_jenis_ibadah,
        nama_jenis_ibadah = nama_jenis_ibadah,
        periode = periode
        
    )
    post_ibadah.save()
    messages.success(request, 'Data ibadah berhasil ditambah.')
    return redirect('jenis_ibadah')

def update_jenis_ibadah(request,kode_jenis_ibadah):
    data_ibadah = MJenisibadah.objects.get(kode_jenis_ibadah=kode_jenis_ibadah)
    context = {
        'data_ibadah': data_ibadah
    }
    return render(request, 'datajenisibadah/update_jenis_ibadah.html', context)
 
def postupdate_jenis_ibadah(request,kode_jenis_ibadah):
    
    kode_jenis_ibadah = request.POST['kode_jenis_ibadah']
    nama_jenis_ibadah = request.POST['nama_jenis_ibadah']
    periode = request.POST['periode']
    
    update_ibadah = MJenisibadah.objects.get(kode_jenis_ibadah=kode_jenis_ibadah)   

    update_ibadah.kode_jenis_ibadah = kode_jenis_ibadah
    update_ibadah.nama_jenis_ibadah = nama_jenis_ibadah
    update_ibadah.periode = periode
 
    update_ibadah.save()
    messages.success(request, 'Data ibadah berhasil diupdate.')
    return redirect('jenis_ibadah')

def delete_jenis_ibadah(request,kode_jenis_ibadah):
    MJenisibadah.objects.get(kode_jenis_ibadah=kode_jenis_ibadah).delete()
    messages.success(request, 'Berhasil hapus data ibadah')
    return redirect('jenis_ibadah')
    
    
#view jenis tugas ibadah
@login_required()
def jenis_tugas_ibadah(request):
    data_tugas_ibadah = MJnstgsibd.objects.all().order_by('nomor_urut')
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_tugas_ibadah': data_tugas_ibadah,
        'data_ibadah' : data_ibadah,
        'menu':'jenis_tugas',
    }
    return render(request, 'datatugasibadah/jenis_tugas_ibadah.html', context)

def tambah_jenis_tugas_ibadah(request):
    data_tugas_ibadah = MJnstgsibd.objects.all()
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_ibadah': data_ibadah,
        'data_tugas_ibadah' : data_tugas_ibadah
    }
    return render(request, 'datatugasibadah/tambah_jenis_tugas_ibadah.html', context)
 
def post_jenis_tugas_ibadah(request):
    kode_jenis_tugas_ibadah = request.POST.get('kode_jenis_tugas_ibadah')
    kode_jenis_ibadah = request.POST['kode_jenis_ibadah']
    nomor_urut = request.POST['nomor_urut']
    jenis_tugas_ibadah = request.POST['jenis_tugas_ibadah']    
  
  
    # if MJnstgsibd.objects.filter(kode_jenis_tugas_ibadah=kode_jenis_tugas_ibadah).exists():
    #     messages.error(request, 'Kode Tugas Ibadah Sudah Terdaftar ')
    #     return redirect('tambah_jenis_tugas_ibadah')
    first_letter = jenis_tugas_ibadah[0].upper()
        # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_kepala_kelarga = MJnstgsibd.objects.filter(kode_jenis_tugas_ibadah__startswith=first_letter)
        # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_kepala_kelarga.filter(kode_jenis_tugas_ibadah=first_letter + str(number).zfill(3)).exists():
        number += 1
        # Setel kode_kelompok dengan format yang sesuai
    kode_jenis_tugas_ibadah = first_letter + str(number).zfill(3)
    
    m_jenisibadah = MJenisibadah.objects.get(kode_jenis_ibadah=kode_jenis_ibadah)
    
    post_ibadah = MJnstgsibd(
        kode_jenis_tugas_ibadah = kode_jenis_tugas_ibadah,
        kode_jenis_ibadah = m_jenisibadah,
        nomor_urut = nomor_urut,
        jenis_tugas_ibadah = jenis_tugas_ibadah
        
    )
    post_ibadah.save()
    messages.success(request, 'Data ibadah berhasil ditambah.')
    return redirect('jenis_tugas_ibadah')


def update_jenis_tugas_ibadah(request,kode_jenis_tugas_ibadah):
    data_tugas_ibadah = MJnstgsibd.objects.get(kode_jenis_tugas_ibadah=kode_jenis_tugas_ibadah)
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_tugas_ibadah': data_tugas_ibadah,
        'data_ibadah' :data_ibadah
    }
    return render(request, 'datatugasibadah/update_jenis_tugas_ibadah.html', context)

def postupdate_jenis_tugas_ibadah(request,kode_jenis_tugas_ibadah):
    kode_jenis_tugas_ibadah = request.POST['kode_jenis_tugas_ibadah']
    kode_jenis_ibadah = request.POST['kode_jenis_ibadah']
    nomor_urut = request.POST['nomor_urut']
    jenis_tugas_ibadah = request.POST['jenis_tugas_ibadah']    
    
    m_jenisibadah = MJenisibadah.objects.get(kode_jenis_ibadah=kode_jenis_ibadah)
    
    update_tugas = MJnstgsibd.objects.get(kode_jenis_tugas_ibadah=kode_jenis_tugas_ibadah)
    
    update_tugas.kode_jenis_tugas_ibadah = kode_jenis_tugas_ibadah
    update_tugas.kode_jenis_ibadah = m_jenisibadah
    update_tugas.nomor_urut = nomor_urut
    update_tugas.jenis_tugas_ibadah = jenis_tugas_ibadah
        
    update_tugas.save()
    messages.success(request, 'Data tugas ibadah berhasil diupdate.')
    return redirect('jenis_tugas_ibadah')


def delete_jenis_tugas_ibadah(request,kode_jenis_tugas_ibadah):
    MJnstgsibd.objects.get(kode_jenis_tugas_ibadah=kode_jenis_tugas_ibadah).delete()
    messages.success(request, 'Berhasil hapus data tugas ibadah')
    return redirect('jenis_tugas_ibadah')

#view jadwal ibadah
@login_required()
def jadwal_ibadah(request):
    data_jadwal = MJdwlibadah.objects.all()
    context = {
        'data_jadwal' : data_jadwal,
        'menu':'jadwal',
    }
    return render(request, 'datajadwalibadah/jadwal_ibadah.html', context)

def tambah_jadwal_ibadah(request):
    data_jadwal = MJdwlibadah.objects.all()
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_jadwal' : data_jadwal,
        'data_ibadah' : data_ibadah
    }
    return render(request, 'datajadwalibadah/tambah_jadwal_ibadah.html', context)

def post_jadwal_ibadah(request):
    id_ibadah = request.POST.get('id_ibadah')
    kode_jenis_ibadah = request.POST.get('kode_jenis_ibadah')
    tanggal_ibadah = request.POST['tanggal_ibadah']
    jam_ibadah = request.POST['jam_ibadah']    
  
  
    # if MJdwlibadah.objects.filter(id_ibadah=id_ibadah).exists():
    #     messages.error(request, 'ID Ibadah Sudah Terdaftar ')
    #     return redirect('tambah_jadwal_ibadah')
    first_letter = tanggal_ibadah[0].upper()
        # Cari semua kelompok yang memiliki huruf awal yang sama
    existing_kepala_kelarga = MJdwlibadah.objects.filter(id_ibadah__startswith=first_letter)
        # Tentukan nomor yang akan digunakan (misalnya, 001 jika belum ada yang sama)
    number = 1
    while existing_kepala_kelarga.filter(id_ibadah=first_letter + str(number).zfill(3)).exists():
        number += 1
        # Setel kode_kelompok dengan format yang sesuai
    id_ibadah = first_letter + str(number).zfill(3)
    if MJdwlibadah.objects.filter(id_ibadah=id_ibadah).exists():
        messages.error(request, 'ID Ibadah Sudah Terdaftar ')
        return redirect('tambah_jadwal_ibadah')
    
    m_jenisibadah = MJenisibadah.objects.get(kode_jenis_ibadah=kode_jenis_ibadah)
    
    post_ibadah = MJdwlibadah(
        id_ibadah = id_ibadah,
        kode_jenis_ibadah = m_jenisibadah,
        tanggal_ibadah = tanggal_ibadah,
        jam_ibadah = jam_ibadah
        
    )
    post_ibadah.save()
    messages.success(request, 'Jadwal ibadah berhasil ditambah.')
    return redirect('jadwal_ibadah')

def update_jadwal_ibadah(request,id_ibadah):
    data_jadwal = MJdwlibadah.objects.get(id_ibadah=id_ibadah)
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_jadwal': data_jadwal,
        'data_ibadah' :data_ibadah
    }
    return render(request, 'datajadwalibadah/update_jadwal_ibadah.html', context)

def postupdate_jadwal_ibadah(request,id_ibadah):
    id_ibadah = request.POST['id_ibadah']
    kode_jenis_ibadah = request.POST['kode_jenis_ibadah']
    tanggal_ibadah = request.POST['tanggal_ibadah']
    jam_ibadah = request.POST['jam_ibadah'] 
           
    m_jenisibadah = MJenisibadah.objects.get(kode_jenis_ibadah=kode_jenis_ibadah)
    update_jadwal = MJdwlibadah.objects.get(id_ibadah=id_ibadah)
    
    update_jadwal.id_ibadah = id_ibadah
    update_jadwal.kode_jenis_ibadah = m_jenisibadah
    update_jadwal.tanggal_ibadah = tanggal_ibadah
    update_jadwal.jam_ibadah = jam_ibadah
        
    update_jadwal.save()
    messages.success(request, 'Jadwal ibadah berhasil diupdate.')
    return redirect('jadwal_ibadah')
     
def delete_jadwal_ibadah(request,id_ibadah):
    MJdwlibadah.objects.get(id_ibadah=id_ibadah).delete()
    messages.success(request, 'Berhasil hapus jadwal ibadah')
    return redirect('jadwal_ibadah')

@login_required()
def petugas_ibadah(request):
    data_petugas = MPtgsibadah.objects.all()
    data_jadwal = MJdwlibadah.objects.all()
    data_tugas_ibadah = MJnstgsibd.objects.all()
    data_ibadah = MJenisibadah.objects.all()
    datajemaat = MJemaat.objects.all()
    context = {
        'data_petugas' : data_petugas,
        'data_jadwal' : data_jadwal,
        'data_tugas_ibadah' : data_tugas_ibadah,
        'data_ibadah': data_ibadah,
        'datajemaat' :datajemaat,
        'menu':'petugas',
    }
    return render(request, 'datapetugasibadah/petugas_ibadah.html', context)

def select_ibadah(request):
    data_jadwal_ibadah = MJdwlibadah.objects.all()
    data_tugas_ibadah = MJnstgsibd.objects.all()
    
    context = {
        'data_jadwal_ibadah' : data_jadwal_ibadah,
        'data_tugas_ibadah': data_tugas_ibadah
    }
    
    return render(request, 'datapetugasibadah/select_ibadah.html', context)

# def post_selected_ibadah(request):
#     if request.method == 'POST':
#         selected_ibadah = request.POST.get('id_ibadah')
        
#         return render(request, 'datapetugasibadah/tambah_petugas_ibadah.html', {'selected_ibadah' : selected_ibadah})
# from django.http import JsonResponse

# def get_kode_jenis_tugas_ibadah(request):
#     if request.is_ajax() and request.method == 'GET':
#         id_ibadah = request.GET.get('id_ibadah')
#         # Ambil data kode_jenis_tugas_ibadah dari MJnstgsibd berdasarkan id_ibadah yang dipilih
#         kode_jenis_tugas_ibadah = list(
#             MJnstgsibd.objects.filter(id_ibadah=id_ibadah).values('kode_jenis_tugas_ibadah')
#         )
#         return JsonResponse({'kode_jenis_tugas_ibadah': kode_jenis_tugas_ibadah}, safe=False)
#     return JsonResponse({}, status=400)

def tambah_petugas_ibadah(request):
    if request.method == 'POST':
        selected_ibadah = request.POST.get('id_ibadah')
        
        data_petugas = MPtgsibadah.objects.all()
        data_jadwal = MJdwlibadah.objects.all()
        data_tugas_ibadah = MJnstgsibd.objects.all()
        data_ibadah = MJenisibadah.objects.all()
        datajemaat = MJemaat.objects.all()
        context = {
            'selected_ibadah' : selected_ibadah,
            'data_petugas' : data_petugas,
            'data_jadwal' : data_jadwal,
            'data_tugas_ibadah' : data_tugas_ibadah,
            'data_ibadah': data_ibadah,
            'datajemaat' :datajemaat
        }
        return render(request, 'datapetugasibadah/tambah_petugas_ibadah.html', context)

def post_petugas_ibadah(request):

    id_ibadah = request.POST['id_ibadah']
    kode_jenis_tugas_ibadah = request.POST['kode_jenis_tugas_ibadah'] 
    kode_jemaat = request.POST['kode_jemaat']
    nomor_urut = request.POST['nomor_urut']
  
  
    m_jdwl = MJdwlibadah.objects.get(id_ibadah=id_ibadah)
    m_jns = MJnstgsibd.objects.get(kode_jenis_tugas_ibadah=kode_jenis_tugas_ibadah)
    m_jemaat = MJemaat.objects.get(kode_jemaat=kode_jemaat)
    post_petugas = MPtgsibadah(
        id_ibadah = m_jdwl,
        kode_jenis_tugas_ibadah = m_jns,
        kode_jemaat = m_jemaat,
        nomor_urut = nomor_urut
        
    )
    post_petugas.save()
    messages.success(request, 'Petugas ibadah berhasil ditambah.')
    return redirect('petugas_ibadah')

def update_petugas_ibadah(request,id):
    data_petugas = MPtgsibadah.objects.get(id=id)
    data_jadwal = MJdwlibadah.objects.all()
    data_tugas_ibadah = MJnstgsibd.objects.all()
    data_ibadah = MJenisibadah.objects.all()
    datajemaat = MJemaat.objects.all()
    context = {
        'data_petugas' : data_petugas,
        'data_jadwal' : data_jadwal,
        'data_tugas_ibadah' : data_tugas_ibadah,
        'data_ibadah': data_ibadah,
        'datajemaat' :datajemaat
    }
    return render(request, 'datapetugasibadah/update_petugas_ibadah.html', context)

def postupdate_petugas_ibadah(request,id):
    id_ibadah = request.POST['id_ibadah']
    kode_jenis_tugas_ibadah = request.POST['kode_jenis_tugas_ibadah']
    kode_jemaat = request.POST['kode_jemaat']
    nomor_urut = request.POST['nomor_urut'] 
       
    m_jdwl = MJdwlibadah.objects.get(id_ibadah=id_ibadah)
    m_jns = MJnstgsibd.objects.get(kode_jenis_tugas_ibadah=kode_jenis_tugas_ibadah)
    m_jemaat = MJemaat.objects.get(kode_jemaat=kode_jemaat)
    
    update_ptgs = MPtgsibadah.objects.get(id=id)
    
    update_ptgs.id_ibadah = m_jdwl
    update_ptgs.kode_jenis_tugas_ibadah = m_jns
    update_ptgs.kode_jemaat = m_jemaat
    update_ptgs.nomor_urut = nomor_urut
        
    update_ptgs.save()
    messages.success(request, 'Petugas ibadah berhasil diupdate.')
    return redirect('petugas_ibadah')

def delete_petugas_ibadah(request,id):
    MPtgsibadah.objects.get(id=id).delete()
    messages.success(request, 'Berhasil hapus petugas ibadah')
    return redirect('petugas_ibadah')

    
#persembahan
@login_required()
def jenis_kolekte(request):
    data_jkolekte = MJnskolekte.objects.all()
    context = {
        'data_jkolekte' : data_jkolekte
    }
    return redirect(request, 'kolekte', context)

def kolekte(request):
    data_kolekte = MKolekte.objects.all()
    data_jadwal = MJdwlibadah.objects.all()
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_kolekte' : data_kolekte,
        'data_jadwal': data_jadwal,
        'data_ibadah' : data_ibadah, 
        'menu' : 'persembahan'
    }
    return render(request, 'datakolekte/kolekte.html', context)

def tambah_kolekte(request):
    data_jkolekte = MJnskolekte.objects.all()
    data_kolekte = MKolekte.objects.all()
    data_jadwal = MJdwlibadah.objects.all()

    selected_id_ibadah = request.GET.get('id_ibadah')

    # Filter data_jkolekte based on selected_id_ibadah and existing data_kolekte
    if selected_id_ibadah:
        existing_kolekte = data_kolekte.filter(id_ibadah=selected_id_ibadah).values_list('kode_jenis_persembahan', flat=True)
        data_jkolekte = data_jkolekte.exclude(kode_jenis_persembahan__in=existing_kolekte)

    context = {
        'data_jkolekte': data_jkolekte,
        'data_kolekte': data_kolekte,
        'data_jadwal': data_jadwal,
        'selected_id_ibadah': selected_id_ibadah,
    }
    return render(request, 'datakolekte/tambah_kolekte.html', context)

def post_kolekte(request):
    if request.method == 'POST':
        id_ibadah = request.POST['id_ibadah']
        kode_jenis_persembahan = request.POST['kode_jenis_persembahan']
        jumlah_persembahan = request.POST['jumlah_persembahan']
        
        # Pengecekan apakah kombinasi id_ibadah dan kode_jenis_persembahan sudah ada di MKolekte
        # if MKolekte.objects.filter(id_ibadah=id_ibadah, kode_jenis_persembahan=kode_jenis_persembahan).exists():
        #     messages.error(request, 'Kombinasi ID Ibadah dan Kode Jenis Persembahan sudah terdaftar.')
        #     return redirect('tambah_kolekte')

        m_jdwl = MJdwlibadah.objects.get(id_ibadah=id_ibadah)
        m_jk = MJnskolekte.objects.get(kode_jenis_persembahan=kode_jenis_persembahan)
        
        post_kolekte = MKolekte(
            id_ibadah=m_jdwl,
            kode_jenis_persembahan=m_jk,
            jumlah_persembahan=jumlah_persembahan
        )
        post_kolekte.save()
        messages.success(request, 'Data kolekte ibadah berhasil ditambah.')
        return redirect('kolekte')

    return render(request, 'datakolekte/tambah_kolekte.html', {'data_jkolekte': MJnskolekte.objects.all()})

def update_kolekte(request,id):
    data_jkolekte = MJnskolekte.objects.all()
    data_kolekte = MKolekte.objects.get(id=id)
    data_jadwal = MJdwlibadah.objects.all()
    context = {
        'data_jkolekte': data_jkolekte,
        'data_kolekte': data_kolekte,
        'data_jadwal': data_jadwal
    }
    return render(request, 'datakolekte/update_kolekte.html', context)
    
def postupdate_kolekte(request,id):
    id_ibadah = request.POST['id_ibadah']
    kode_jenis_persembahan = request.POST['kode_jenis_persembahan']
    jumlah_persembahan = request.POST['jumlah_persembahan']
       
    m_jdwl = MJdwlibadah.objects.get(id_ibadah=id_ibadah)
    m_jns = MJnskolekte.objects.get(kode_jenis_persembahan=kode_jenis_persembahan)
    
    update_kolekte = MKolekte.objects.get(id=id)
    
    update_kolekte.id_ibadah = m_jdwl
    update_kolekte.kode_jenis_persembahan = m_jns
    update_kolekte.jumlah_persembahan = jumlah_persembahan
        
    update_kolekte.save()
    messages.success(request, 'Data kolekte berhasil diupdate.')
    return redirect('kolekte')

def delete_kolekte(request,id):
    MKolekte.objects.get(id=id).delete()
    messages.success(request, 'Berhasil hapus data kolekte ')
    return redirect('kolekte')
    
    
    
#kehadiran
def kehadiran(request):
    data_kehadiran = MHadir.objects.all()
    data_jadwal = MJdwlibadah.objects.all()
    data_kategorial = MKategorial.objects.all()
    
    context = {
        'data_kehadiran' :data_kehadiran,
        'data_jadwal' : data_jadwal,
        'datakategorial' : data_kategorial,
        'menu':'kehadiran'
        
    }
    return render(request, 'datakehadiran/kehadiran.html', context)

def tambah_kehadiran(request):
    data_kehadiran = MHadir.objects.all()
    data_jadwal = MJdwlibadah.objects.all()
    data_kategorial = MKategorial.objects.all()

    context = {
        'data_kehadiran' :data_kehadiran,
        'data_jadwal' : data_jadwal,
        'datakategorial' : data_kategorial   
    }
    return render(request, 'datakehadiran/tambah_kehadiran.html', context)

def post_kehadiran(request):
    id_ibadah = request.POST['id_ibadah']
    kodekategorial = request.POST['kodekategorial']
    jumlah_kehadiran = request.POST['jumlah_kehadiran']
    
    m_jdwl = MJdwlibadah.objects.get(id_ibadah=id_ibadah)
    m_kategorial = MKategorial.objects.get(kodekategorial=kodekategorial)
    
    post_hadir =MHadir (
        id_ibadah =m_jdwl,
        kodekategorial=m_kategorial,
        jumlah_kehadiran=jumlah_kehadiran
    )
    post_hadir.save()
    messages.success(request, 'data kehadiran ibadah berhasil ditambah.')
    return redirect('kehadiran') 



def update_kehadiran(request,id):
    data_kehadiran = MHadir.objects.get(id=id)
    data_jadwal = MJdwlibadah.objects.all()
    data_kategorial = MKategorial.objects.all()

    context = {
        'data_kehadiran' :data_kehadiran,
        'data_jadwal' : data_jadwal,
        'datakategorial' : data_kategorial   
    }
    return render(request, 'datakehadiran/update_kehadiran.html', context)
    
def postupdate_kehadiran(request,id):
    id_ibadah = request.POST['id_ibadah']
    kodekategorial = request.POST['kodekategorial']
    jumlah_kehadiran = request.POST['jumlah_kehadiran']
       
    m_jdwl = MJdwlibadah.objects.get(id_ibadah=id_ibadah)
    m_kategorial = MKategorial.objects.get(kodekategorial=kodekategorial)
    
    update_kehadiran = MHadir.objects.get(id=id)
    
    update_kehadiran.id_ibadah = m_jdwl
    update_kehadiran.kodekategorial = m_kategorial
    update_kehadiran.jumlah_kehadiran = jumlah_kehadiran
        
    update_kehadiran.save()
    messages.success(request, 'Data kehadiran berhasil diupdate.')
    return redirect('kehadiran')

def delete_kehadiran(request,id):
    MHadir.objects.get(id=id).delete()
    messages.success(request, 'Berhasil hapus data kehadiran ')
    return redirect('kehadiran')


   

from xhtml2pdf import pisa
from django.template.loader import get_template
def export_pdf(request):
    # Ambil data penjualan dari database atau sumber lainnya
    datajemaat = MJemaat.objects.all().order_by('-kode_jemaat')
    context = {
        'datajemaat': datajemaat
    }

    # Render template
    template = get_template('datajemaat/exportPDF.html')
    rendered_template = template.render(context)

    # Buat objek HttpResponse dengan tipe konten application/pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data_jemaat.pdf"'

    # Buat PDF menggunakan HTML yang dirender
    pisa_status = pisa.CreatePDF(rendered_template, dest=response)

    # Jika pembuatan PDF gagal, kirimkan tanggapan error
    if pisa_status.err:
        return HttpResponse('Error generating PDF')
    return response

# views.py


# def check_existing_combinations(request):
#     if request.method == 'GET' and request.is_ajax():
#         id_ibadah = request.GET.get('id_ibadah', None)
#         kode_jenis_persembahan = request.GET.get('kode_jenis_persembahan', None)

#         if id_ibadah and kode_jenis_persembahan:
#             existing_combination = MKolekte.objects.filter(
#                 id_ibadah=id_ibadah,
#                 kode_jenis_persembahan=kode_jenis_persembahan
#             ).exists()

#             return JsonResponse({'exists': existing_combination})

#     return JsonResponse({'exists': False})


from django.http import JsonResponse

def get_existing_combinations(request):
    existing_combinations = list(MKolekte.objects.values_list('id_ibadah', 'kode_jenis_persembahan'))
    existing_combinations = [f"{id_ibadah}|{kode_jenis_persembahan}" for id_ibadah, kode_jenis_persembahan in existing_combinations]
    return JsonResponse({'combinations': existing_combinations})





    

    


    
    




