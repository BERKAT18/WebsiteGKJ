from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.shortcuts import render
from .models import MGereja, MPendeta , MKhotbah,MWarta,MRenungan,MDokumentasi,MadminLog, MDokumentasi
from django.contrib.auth import authenticate, login
from .decorators import login_required
# Create your views here.


def home(request):
    return render(request, 'home.html')

@login_required()
def tambah_beranda(request):
    return render(request, 'tambah-beranda.html')


def postberanda(request):
    namagereja = request.POST['namagereja']
    alamatgereja = request.POST['alamatgereja']
    telepongereja = request.POST['telepongereja']
    tanggalberdiri = request.POST['tanggalberdiri']
    tema = request.POST['tema']
    ayatemas = request.POST['ayatemas']
    simpanberanda = MGereja(
        alamatgereja=alamatgereja,
        telepongereja=telepongereja,
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
        'databeranda': databeranda

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
    tanggalberdiri = request.POST['tanggalberdiri']
    tema = request.POST['tema']
    ayatemas = request.POST['ayatemas']

    updateberanda = MGereja.objects.get(id=id)

    updateberanda.namagereja = namagereja
    updateberanda.alamatgereja = alamatgereja
    updateberanda.telepongereja = telepongereja
    updateberanda.tanggalberdiri = tanggalberdiri
    updateberanda.tema = tema
    updateberanda.ayatemas = ayatemas

    updateberanda.save()

    messages.success(request, 'Data telah diperbarui.')
    return redirect('beranda')  # Menggunakan 'beranda' sebagai argumen untuk redirect

@login_required()
def profilpendeta(request):
    gereja = MPendeta.objects.all() # Mengambil objek berdasarkan id yang diberikan dalam URL
    context = {
       'gereja' : gereja 
    }
    
    return render(request, 'datapendeta/profilpendeta.html', context)

def postprofilpendeta(request):
    namapendeta = request.POST['namapendeta']
    fotopendeta = request.FILES['fotopendeta']
    visi = request.POST['visi']
    misi = request.POST['misi']
    jadwal = request.POST['jadwal']
    
    postprofil = MPendeta(
    namapendeta = namapendeta,
    fotopendeta = fotopendeta,
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
    namapendeta = request.POST['namapendeta']
    fotopendeta = request.FILES['fotopendeta']
    visi = request.POST['visi']
    misi = request.POST['misi']
    jadwal = request.POST['jadwal']
    
    postupdateprofilpendeta = MPendeta.objects.get(id=id)
    postupdateprofilpendeta.namapendeta = namapendeta
    postupdateprofilpendeta.fotopendeta = fotopendeta
    postupdateprofilpendeta.visi= visi
    postupdateprofilpendeta.misi = misi
    postupdateprofilpendeta.jadwal= jadwal
  
    postupdateprofilpendeta.save()
    messages.success(request, 'Data telah diperbarui.')
    return redirect('profilpendeta') 

def profil(request):
    return render(request,'datapendeta/tambah-profilpendeta.html')

@login_required()
def khotbah(request):
    data_khotbah = MKhotbah.objects.all()
    context = {
       'data_khotbah' : data_khotbah 
    }
    
    return render(request, 'datakhotbah/khotbah.html', context)

def tambah_khotbah(request):
    return render(request, 'datakhotbah/tambah-khotbah.html')

def posttambah_khotbah(request):
    id_khotbah = request.POST['id_khotbah']
    isi_khotbah = request.POST['isi_khotbah']
    tanggal = request.POST['tanggal']
    
    postkhotbah = MKhotbah(
    id_khotbah = id_khotbah,
    isi_khotbah = isi_khotbah,
    tanggal = tanggal
   
    )
    postkhotbah.save()
    messages.success(request, 'Data telah diperbarui.')
    return redirect('khotbah') 

def update_khotbah(request, id_khotbah):
    data_khotbah = MKhotbah.objects.get(id_khotbah=id_khotbah)
    context = {
        'data_khotbah': data_khotbah
    }
    return render(request, 'datakhotbah/update-khotbah.html', context) # Menggunakan 'khotbah.html' tanpa path ke folder 'templates'

def postupdate_khotbah(request, id_khotbah):  # Menambahkan id sebagai argumen
    id_khotbah = request.POST['id_khotbah']
    isi_khotbah = request.POST['isi_khotbah']
    tanggal = request.POST['tanggal']
  

    update_khotbah = MKhotbah.objects.get(id_khotbah=id_khotbah)

    update_khotbah.id_khotbah = id_khotbah
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
       'data_warta' : data_warta
    }
    
    return render(request, 'datawarta/warta.html', context)

def tambah_warta(request):
    return render(request, 'datawarta/tambah-warta.html')

def posttambah_warta(request):
    id_warta = request.POST['id_warta']
    isi_warta = request.POST['isi_warta']
    tanggal_warta = request.POST['tanggal_warta']
    
    postwarta = MWarta(
    id_warta = id_warta,
    isi_warta = isi_warta,
    tanggal_warta = tanggal_warta
   
    )
    postwarta.save()
    messages.success(request, 'Data telah diperbarui.')
    return redirect('warta') 

def update_warta(request, id_warta):
    data_warta = MWarta.objects.get(id_warta=id_warta)
    context = {
        'data_warta': data_warta
    }
    return render(request, 'datawarta/update-warta.html', context) # Menggunakan 'khotbah.html' tanpa path ke folder 'templates'


def postupdate_warta(request, id_warta):  # Menambahkan id sebagai argumen
    id_warta = request.POST['id_warta']
    isi_warta = request.POST['isi_warta']
    tanggal_warta = request.POST['tanggal_warta']
  

    update_warta = MWarta.objects.get(id_warta=id_warta)

    update_warta.id_warta = id_warta
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
       'data_renungan' : data_renungan
    }
    
    return render(request, 'datarenungan/renungan.html', context)

def tambah_renungan(request):
    return render(request, 'datarenungan/tambah-renungan.html')

def posttambah_renungan(request):
    id_renungan = request.POST['id_renungan']
    isi_renungan = request.POST['isi_renungan']
    tanggal_renungan = request.POST['tanggal_renungan']
    
    postrenungan = MRenungan(
    id_renungan = id_renungan,
    isi_renungan = isi_renungan,
    tanggal_renungan = tanggal_renungan
   
    )
    postrenungan.save()
    messages.success(request, 'Data telah diperbarui.')
    return redirect('renungan') 

def update_renungan(request, id_renungan):
    data_renungan = MRenungan.objects.get(id_renungan=id_renungan)
    context = {
        'data_renungan': data_renungan
    }
    return render(request, 'datarenungan/update-renungan.html', context) # Menggunakan 'khotbah.html' tanpa path ke folder 'templates'

def postupdate_renungan(request, id_renungan):  # Menambahkan id sebagai argumen
    id_renungan = request.POST['id_renungan']
    isi_renungan = request.POST['isi_renungan']
    tanggal_renungan = request.POST['tanggal_renungan']
  

    update_renungan = MRenungan.objects.get(id_renungan=id_renungan)

    update_renungan.id_renungan = id_renungan
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
       'data_dokumentasi' : data_dokumentasi
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


def postupdate_dokumentasi(request,id_dokumentasi):
    id_dokumentasi = request.POST['id_dokumentasi']
    foto_dokumentasi = request.FILES['foto_dokumentasi']
    nama_kegiatan = request.POST['nama_kegiatan']
    tanggal_kegiatan = request.POST['tanggal_kegiatan']
    keterangan_kegiatan = request.POST['keterangan_kegiatan'] 
    
    update_dokumentasi = MDokumentasi.objects.get(id_dokumentasi=id_dokumentasi)

    update_dokumentasi.id_dokumentasi = id_dokumentasi
    update_dokumentasi.foto_dokumentasi = foto_dokumentasi
    update_dokumentasi.nama_kegiatan = nama_kegiatan
    update_dokumentasi.tanggal_kegiatan = tanggal_kegiatan
    update_dokumentasi.keterangan_kegiatan= keterangan_kegiatan


    update_dokumentasi.save()

    messages.success(request, 'Data telah diperbarui.')
    return redirect('dokumentasi')

def posttambah_dokumentasi(request):
    id_dokumentasi = request.POST['id_dokumentasi']
    foto_dokumentasi = request.FILES['foto_dokumentasi']
    nama_kegiatan = request.POST['nama_kegiatan']
    tanggal_kegiatan = request.POST['tanggal_kegiatan']
    keterangan_kegiatan = request.POST['keterangan_kegiatan'] 
    
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
    return render (request, 'profile/warta.html')

def renungan_page(request):
    return render (request, 'profile/renungan.html')

def khotbah_page(request):
    return render (request, 'profile/khotbah.html')

def document_page(request):
    data_document = MDokumentasi.objects.all()
    context = {
        'data_document' : data_document,
    }
    return render (request, 'profile/document.html', context)