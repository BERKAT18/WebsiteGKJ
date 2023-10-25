from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.shortcuts import render
from .models import MGereja, MPendeta , MKhotbah,MWarta,MRenungan,MDokumentasi,MadminLog, MDokumentasi,MKeluarga,MJemaat,MOrjem,MPengjem,MKategorial,MOrkat,MPengkat,MJenisibadah,MJnstgsibd
from django.contrib.auth import authenticate, login
from .decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse


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
       'gereja' : gereja 
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
    namapendeta = request.POST['namapendeta']
    fotopendeta = request.FILES['fotopendeta']
    tlpn_pendeta = request.POST['tlpn_pendeta']
    email_pendeta = request.POST['email_pendeta']
    pendidikan_pendeta = request.POST['pendidikan_pendeta']
    visi = request.POST['visi']
    misi = request.POST['misi']
    jadwal = request.POST['jadwal']
    
    postupdateprofilpendeta = MPendeta.objects.get(id=id)
    postupdateprofilpendeta.namapendeta = namapendeta
    postupdateprofilpendeta.fotopendeta = fotopendeta
    postupdateprofilpendeta.tlpn_pendeta = tlpn_pendeta
    postupdateprofilpendeta.email_pendeta = email_pendeta
    postupdateprofilpendeta.pendidikan_pendeta = pendidikan_pendeta
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
       'data_warta' : data_warta
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
       'data_renungan' : data_renungan
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

    messages.success(request, 'Data Dokumentasi Berhasil Ditambah.')
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

def keluarga(request):
    datakeluarga = MKeluarga.objects.all()
    datajemaat = MJemaat.objects.all()
    context = {
        'datakeluarga': datakeluarga,
        'datajemaat': datajemaat

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
        
        if MKeluarga.objects.filter(kode_keluarga=kode_keluarga).exists():
            messages.error(request, 'Kode Keluarga Sudah Digunakan')
            return redirect('tambah_keluarga')

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

def jemaat(request):
    datajemaat = MJemaat.objects.all()
    context = {
        'datajemaat': datajemaat

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
        kode_jemaat = request.POST['kode_jemaat']
        kode_keluarga = request.POST['kode_keluarga']
        kodekategorial = request.POST['kodekategorial']

        try:
            # Cari objek MKeluarga berdasarkan kode_keluarga
            keluarga = MKeluarga.objects.get(kode_keluarga=kode_keluarga)
        except MKeluarga.DoesNotExist:
            messages.error(request, 'MKeluarga tidak ditemukan')
            return redirect('tambah_jemaat')
        
        if MJemaat.objects.filter(kode_jemaat=kode_jemaat).exists():
            messages.error(request, 'Kode jemaat Sudah Digunakan')
            return redirect('tambah_jemaat')

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
            return HttpResponse("MKeluarga tidak ditemukan.")
        
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

def detail_keluarga(request, kode_keluarga):
    dataanggotakeluarga = MJemaat.objects.filter(kode_keluarga=kode_keluarga)
    datakeluarga = MKeluarga.objects.get(kode_keluarga=kode_keluarga)
    context = {
        'dataanggotakeluarga': dataanggotakeluarga,
        'datakeluarga' : datakeluarga

    }
    return render(request, 'datakeluarga/detailkeluarga.html', context)


#Pengurus Jemaat

def organisasi_jemaat(request):
    data_orjem = MOrjem.objects.all()
    context = {
        'data_orjem' : data_orjem
    }
    return render (request,'datapengurusjemaat/pengurus_jemaat.html', context)

def pengurus_jemaat(request):
    data_pengjem = MPengjem.objects.all()
    context = {
        'data_pengjem' : data_pengjem,
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

def pengurus_kategorial(request):
    data_kategorial = MKategorial.objects.all()
    data_pengkat = MPengkat.objects.all()
    context = {
        'data_pengkat' : data_pengkat,
        'data_kategorial' : data_kategorial
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

def jenis_ibadah(request):
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_ibadah': data_ibadah
    }
    return render(request, 'datajenisibadah/jenis_ibadah.html', context)

def tambah_jenis_ibadah(request):
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_ibadah': data_ibadah
    }
    return render(request, 'datajenisibadah/tambah_jenis_ibadah.html', context)
 
def post_jenis_ibadah(request):
    
    kode_jenis_ibadah = request.POST['kode_jenis_ibadah']
    nama_jenis_ibadah = request.POST['nama_jenis_ibadah']
    periode = request.POST['periode']    
  
  
    if MJenisibadah.objects.filter(kode_jenis_ibadah=kode_jenis_ibadah).exists():
        messages.error(request, 'Kode Jenis Ibadah Sudah Terdaftar ')
        return redirect('tambah_jenis_ibadah')
    
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

def jenis_tugas_ibadah(request):
    data_tugas_ibadah = MJnstgsibd.objects.all()
    data_ibadah = MJenisibadah.objects.all()
    context = {
        'data_tugas_ibadah': data_tugas_ibadah,
        'data_ibadah' : data_ibadah
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
    kode_jenis_tugas_ibadah = request.POST['kode_jenis_tugas_ibadah']
    kode_jenis_ibadah = request.POST['kode_jenis_ibadah']
    nomor_urut = request.POST['nomor_urut']
    jenis_tugas_ibadah = request.POST['jenis_tugas_ibadah']    
  
  
    if MJnstgsibd.objects.filter(kode_jenis_tugas_ibadah=kode_jenis_tugas_ibadah).exists():
        messages.error(request, 'Kode Tugas Ibadah Sudah Terdaftar ')
        return redirect('tambah_jenis_tugas_ibadah')
    
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
    
    