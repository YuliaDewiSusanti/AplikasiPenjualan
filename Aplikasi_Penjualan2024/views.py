import json
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .models import *
from .decorators import ijinkan_pengguna, tolakhalaman_ini, pilihan_login
from django.conf import settings
from time import gmtime, strftime, time
import hashlib
import midtransclient
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import time 
import datetime

from midtransclient import Snap

# login sistem admin
def Login_sistem(request):
	context = {
	'page_title':'Login Sistem',
	}
	#print(request.user)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('Home')
		else:
			messages.info(request, 'Username & Password Tidak Sesuai Silakan Ulangi..?')
			return redirect('Login_Sistem')

	return render(request, 'login.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def HomeView(request):
	tanggal_sekarang = strftime('%d-%m-%Y')
	tahun_sekarang = strftime('%Y')
	jml_pelanggan = Model_pelanggans.objects.all().count()
	jml_pemesanan = Model_pemesanans.objects.all().count()
	Tampil = Model_pemesanans.objects.all()
	context = {
	'page_title':'Aplikasi Pengaduan',
	'tanggal_sekarang': tanggal_sekarang,
	'tahun_sekarang':tahun_sekarang,
	'jml_pelanggan':jml_pelanggan,
	'jml_pemesanan':jml_pemesanan,
	'Tampil':Tampil,
	}
	group_admin = Group.objects.get(name="Admin")
	group_user = Group.objects.get(name="User")
	admin_group = request.user.groups.all()

	template_name = None
	if group_admin in admin_group:
		template_name = 'index.html'
	elif group_user in admin_group:
		template_name = 'Master_atasan/halaman.html'
	else:
		template_name = 'index.html'

	return render(request, template_name,  context)

def LogoutView(request):
	context = {
	'page_title':'logout',
	}
	if request.method == "POST":
		if request.POST["logout"] == "Submit":	
			logout(request)

		return redirect('Login_Sistem')

	return render(request, 'logout.html',  context)	
# 
def lupa_pass(request):
	if 'cari_data' in request.GET:
		cari_data=request.GET['cari_data']
		Tampil = User.objects.filter(username=cari_data)
	else:
		Tampil = User.objects.filter(username=None)
	context = {
	'page_title':'Login Sistem',
	'Tampil': Tampil,
	}

	return render(request, 'lupa_pss.html',  context)
# 
@login_required(login_url=settings.LOGIN_URL)
def EditPetugasV(request, id_pt):		
	data = User.objects.get(id=id_pt)			
	if request.method == 'POST':		
			data.username = request.POST.get('username')
			data.email = request.POST.get('email')
			data.password = request.POST.get('password').strip()
			data.confirmPassword =request.POST.get('confirmPassword').strip()
			data.save()		
			messages.info(request, 'Data Berhasil..?')
			return redirect('/')

# master data pengaduan
# ----------------------data jenis--------------
@login_required(login_url=settings.LOGIN_URL)
def Data_jenis(request):
	Tampil = Model_jenis.objects.all()
	context = {	

	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_jenis/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Tambah_jenis(request):
	if request.method == 'POST':
		Model_jenis.objects.create(
			jenis = request.POST['jenis'],
			harga = request.POST['harga'],
			satuan = request.POST['satuan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..?')
		return HttpResponseRedirect("/Jenis/")	
	context = {	
	'Tambah': 'Tambah'
	}
	return render(request, 'Master_data/data_jenis/tambah.html', context)

@login_required(login_url=settings.LOGIN_URL)
def Edit_jenis(request, kode_p):		
	edit_data = Model_jenis.objects.get(id=kode_p)
	if request.method == 'POST':
			edit_data.jenis = request.POST.get('jenis')
			edit_data.harga = request.POST.get('harga')
			edit_data.satuan = request.POST.get('satuan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..?')
			return redirect('Jenis')

	context = {'edit_data': edit_data}
	return render(request, 'Master_data/data_jenis/edit.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Hapus_jenis(request, kode_p):
	Model_jenis.objects.filter(id=kode_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..?')
	return redirect('Jenis')

# ----------------------data kambing--------------
@login_required(login_url=settings.LOGIN_URL)
def Data_kambing(request):
	if 'cari_data' in request.POST:
		cari_data=request.POST.get('cari_data')
		Tampil = Model_kambingss.objects.filter(status=cari_data)
	else:
		Tampil = Model_kambingss.objects.all()
	
	context = {	

	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_kambing/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Tambah_kambing(request):
	select_jenis = Model_jenis.objects.all()
	if request.method == 'POST':
		Model_kambingss.objects.create(
			status = request.POST['status'],
			jenis = request.POST['jenis'],
			usia = request.POST['usia'],
			tinggi = request.POST['tinggi'],
			harga = request.POST['harga'],
			stock = request.POST['stock'],
			foto = request.FILES['foto'],
			keterangan = request.POST['keterangan'],
			)
		messages.info(request, 'Data Berhasil Di Simpan..?')
		return HttpResponseRedirect("/Kambing/")	
	context = {	
	'Tambah': 'Tambah',
	'select_jenis': select_jenis
	}
	return render(request, 'Master_data/data_kambing/tambah.html', context)

@login_required(login_url=settings.LOGIN_URL)
def Edit_kambing(request, kode_p):
	select_jenis = Model_jenis.objects.all()
	edit_data = Model_kambingss.objects.get(id=kode_p)
	if request.method == 'POST':
			edit_data.status = request.POST.get('status')
			edit_data.jenis = request.POST.get('jenis')
			edit_data.usia = request.POST.get('usia')
			edit_data.tinggi = request.POST.get('tinggi')
			edit_data.harga = request.POST.get('harga')
			edit_data.stock = request.POST.get('stock')
			edit_data.keterangan = request.POST.get('keterangan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..?')
			return redirect('Kambing')

	context = {'edit_data': edit_data, 'select_jenis': select_jenis}
	return render(request, 'Master_data/data_kambing/edit.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Edit_foto_kambing(request, kode_p):
	tampil = Model_kambingss.objects.get(id=kode_p)
	if request.method == 'POST':
			tampil.foto = request.FILES.get('foto')
			tampil.save()		
			messages.info(request, 'Data Berhasil Di Edit..?')
			return redirect('Kambing')

@login_required(login_url=settings.LOGIN_URL)
def Hapus_kambing(request, kode_p):
	Model_kambingss.objects.filter(id=kode_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..?')
	return redirect('Kambing')

# ----------------------data penjualan--------------
@login_required(login_url=settings.LOGIN_URL)
def Data_penjualan(request):
	select_pelanggan = Model_pelanggans.objects.all()
	Tampil = Model_penjualan.objects.all()	
	context = {	
	'select_pelanggan': select_pelanggan,
	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_penjualan/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Tambah_penjualan(request):
	select_jenis = Model_jenis.objects.all()
	tanggal_sekarang = strftime('%d-%m-%Y')
	if 'cari_jenis' in request.POST:
		cari_jenis=request.POST.get('cari_jenis')
		Tampil = Model_kambingss.objects.filter(jenis=cari_jenis)
	else:
		Tampil = Model_kambingss.objects.filter(jenis=None)
		

	context = {	
	'Tambah': 'Tambah',
	'select_jenis': select_jenis,
	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_penjualan/tambah.html', context)

@login_required(login_url=settings.LOGIN_URL)
def Proses_input_penjualan(request):
	if request.method == 'POST':
		tanggal_sekarang = strftime('%d-%m-%Y')
		Model_penjualan.objects.create(
			jenis = request.POST['jenis'],
			harga = request.POST['harga'],
			jumlah = request.POST['jumlah'],
			total = request.POST['total'],
			tgl_penjualan = tanggal_sekarang,
			)
	edit_stock = Model_kambingss.objects.get(id=request.POST.get('id'))
	if request.method == 'POST':
			edit_stock.stock = request.POST.get('stock')
			edit_stock.save()	
			messages.info(request, 'Data Berhasil Di Simpan..?')
			return HttpResponseRedirect("/Penjualan/")	

@login_required(login_url=settings.LOGIN_URL)
def Edit_penjualan(request, kode_p):
	select_jenis = Model_kambingss.objects.all()
	tanggal_sekarang = strftime('%d-%m-%Y')
	edit_data = Model_penjualan.objects.get(id=kode_p)
	if request.method == 'POST':
			edit_data.jenis = request.POST.get('jenis')
			edit_data.harga = request.POST.get('harga')
			edit_data.jumlah = request.POST.get('jumlah')
			edit_data.total = request.POST.get('total')
			edit_data.tgl_penjualan = tanggal_sekarang
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..?')
			return redirect('Penjualan')

	context = {'edit_data': edit_data, 'select_jenis': select_jenis}
	return render(request, 'Master_data/data_penjualan/edit.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Hapus_penjualan(request, kode_p):
	Model_penjualan.objects.filter(id=kode_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..?')
	return redirect('Penjualan')


# ----------------------data transaksi pembayaran--------------
@login_required(login_url=settings.LOGIN_URL)
def Data_transaksi(request):
	Tampil = Model_transaksis.objects.all()	
	context = {	

	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_transaksi/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Tambah_transaksi(request, kode_p):
	select_jenis = Model_jenis.objects.all()
	tampil = Model_penjualan.objects.get(id=kode_p)
	select_pelanggan = Model_pelanggans.objects.all()
	context = {	
	'Tambah': 'Tambah',
	'select_jenis': select_jenis,
	'tampil': tampil,
	'select_pelanggan': select_pelanggan,
	}
	return render(request, 'Master_data/data_transaksi/tambah.html', context)

@login_required(login_url=settings.LOGIN_URL)
def Proses_input_transaksi(request):
	if request.method == 'POST':
		tanggal_sekarang = strftime('%d-%m-%Y')
		Model_transaksis.objects.create(
			pelanggan = request.POST['pelanggan'],
			jenis = request.POST['jenis'],
			harga = request.POST['harga'],
			jumlah = request.POST['jumlah'],
			total = request.POST['total'],
			bayar = request.POST['bayar'],
			status_transfer = request.POST['status_transfer'],
			tgl_transaksi = tanggal_sekarang,
			)
		messages.info(request, 'Data Berhasil Di Simpan, silakan cetak nota.?')
		return HttpResponseRedirect("/Transaksi/")	

@login_required(login_url=settings.LOGIN_URL)
def Hapus_transaksi(request, kode_p):
	Model_transaksis.objects.filter(id=kode_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..?')
	return redirect('Transaksi')

@login_required(login_url=settings.LOGIN_URL)
def Cetak_nota(request, kode_p):
	tampil = Model_transaksis.objects.get(id=kode_p)
	tanggal_sekarang = strftime('%d-%m-%Y')
	context = {
	'tampil': tampil,
	'tanggal_sekarang': tanggal_sekarang,
	}
	return render(request, 'Master_data/data_transaksi/nota.html',  context)

# data pelanggan
@login_required(login_url=settings.LOGIN_URL)
def Data_pelanggan(request):
	Tampil = Model_pelanggans.objects.all()	
	context = {	

	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_pelanggan/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Hapus_pelanggan(request, kode_p):
	Model_pelanggans.objects.filter(id=kode_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..?')
	return redirect('Pelanggan')

# data pemesanan
@login_required(login_url=settings.LOGIN_URL)
def Data_pemesanan(request):
	Tampil = Model_pemesanans.objects.all()	
	context = {	

	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_pemesanan/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Hapus_dt_pemesanan(request, kode_p):
	Model_pemesanans.objects.filter(id=kode_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..?')
	return redirect('Pemesanan')

@login_required(login_url=settings.LOGIN_URL)
def Data_pembayaran(request):
	if 'cari' in request.POST:
		cari=request.POST.get('cari')
		Tampil = Model_pembayarans.objects.filter(noktp=cari)
	else:
		Tampil = Model_pembayarans.objects.filter(noktp=None)
	context = {	

	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_pemesanan/tabel_bayar.html',  context)

def simpan_pengiriman(request):
	if request.method == 'POST':
		tanggal_sekarang = strftime('%d-%m-%Y')
		Model_pengirimanss.objects.create(
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			jenis = request.POST['jenis'],
			jumlah = request.POST['jumlah'],
			harga = request.POST['harga'],
			total = request.POST['total'],
			tgl_pengiriman = request.POST['tgl_pengiriman'],
			pesan = request.POST['pesan'],
			status = 'Ter-kirim'
			)
		messages.info(request, 'Data Pengiriman Berhasil Tersimpan.?')
		return HttpResponseRedirect("/Pengiriman/")

@login_required(login_url=settings.LOGIN_URL)
def Data_pengiriman(request):
	Tampil = Model_pengirimanss.objects.all()	
	context = {	

	'Tampil': Tampil,
	}
	return render(request, 'Master_data/data_pengiriman/tabel.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def Edit_pengiriman(request, kode_p):
	edit_data = Model_pengirimanss.objects.get(id=kode_p)
	if request.method == 'POST':
			edit_data.tgl_pengiriman = request.POST.get('tgl_pengiriman')
			edit_data.pesan = request.POST.get('pesan')
			edit_data.save()		
			messages.info(request, 'Data Berhasil Di Edit..?')
			return redirect('Pengiriman')

@login_required(login_url=settings.LOGIN_URL)
def Hapus_pengiriman(request, kode_p):
	Model_pengirimanss.objects.filter(id=kode_p).delete()
	messages.info(request, 'Data Berhasil Di Hapus..?')
	return redirect('Pengiriman')

# halaman laporan
@login_required(login_url=settings.LOGIN_URL)
def Menu_laporan(request):
	Tampil = Model_pengirimanss.objects.all()	
	context = {	

	'Tampil': Tampil,
	}
	return render(request, 'Master_data/laporan/menu.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def lp_kambing(request):
	Tampil = Model_kambingss.objects.all()	
	tanggal_sekarang = strftime('%d-%m-%Y')	
	context = {	
	'Tampil': Tampil,
	'tanggal_sekarang': tanggal_sekarang,
	}
	return render(request, 'Master_data/laporan/lp_kambing.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def lp_pelanggan(request):
	Tampil = Model_pelanggans.objects.all()
	tanggal_sekarang = strftime('%d-%m-%Y')	
	context = {	
	'Tampil': Tampil,
	'tanggal_sekarang': tanggal_sekarang,
	}
	return render(request, 'Master_data/laporan/lp_pelanggan.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def lp_pemesanan(request):
	Tampil = Model_pemesanans.objects.all()	
	tanggal_sekarang = strftime('%d-%m-%Y')	
	context = {	
	'Tampil': Tampil,
	'tanggal_sekarang': tanggal_sekarang,
	}
	return render(request, 'Master_data/laporan/lp_pemesanan.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def lp_pengiriman(request):
	Tampil = Model_pengirimanss.objects.all()	
	tanggal_sekarang = strftime('%d-%m-%Y')	
	context = {	
	'Tampil': Tampil,
	'tanggal_sekarang': tanggal_sekarang,
	}
	return render(request, 'Master_data/laporan/lp_pengiriman.html',  context)

@login_required(login_url=settings.LOGIN_URL)
def lp_transaksi(request):
	Tampil = Model_transaksis.objects.all()
	tanggal_sekarang = strftime('%d-%m-%Y')	
	context = {	
	'Tampil': Tampil,
	'tanggal_sekarang': tanggal_sekarang,
	}
	return render(request, 'Master_data/laporan/lp_transaksi.html',  context)




# website pemesanan

def Website(request):
	select_jenis = Model_jenis.objects.all()
	if 'cari_jenis' in request.POST:
		cari_jenis=request.POST.get('cari_jenis')
		Tampil = Model_kambingss.objects.filter(jenis=cari_jenis)
	else:
		Tampil = Model_kambingss.objects.all()
	context = {	
	'Tampil': Tampil,
	'select_jenis': select_jenis,
	}
	return render(request, 'Website/index.html',  context)


def detail(request, kode_p):
	select_jenis = Model_jenis.objects.all()
	tampil = Model_kambingss.objects.get(id=kode_p)
	tanggal_sekarang = strftime('%d-%m-%Y')
	context = {
	'tampil': tampil,
	'tanggal_sekarang': tanggal_sekarang,
	'select_jenis': select_jenis,
	}
	return render(request, 'Website/detail.html',  context)


def registrasi(request):
	tanggal_sekarang = strftime('%d-%m-%Y')
	select_jenis = Model_jenis.objects.all()
	context = {
	'tanggal_sekarang': tanggal_sekarang,
	'select_jenis': select_jenis,
	}
	return render(request, 'Website/registrasi.html',  context)

def simpan_registrasi(request):
	if request.method == 'POST':
		tanggal_sekarang = strftime('%d-%m-%Y')
		Model_pelanggans.objects.create(
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			email = request.POST['email'],
			username = request.POST['username'],
			password = request.POST['password'],
			)
		messages.info(request, 'Registrasi Berhasil, Silakan Login Sekarang.?')
		return HttpResponseRedirect("/login/")

def login_data(request):
    if request.method == 'GET':
        return render(request, 'Website/login.html', {'select_jenis': Model_jenis.objects.all()})
    # login untuk user atau santri
    if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
    
            user=Model_pelanggans.objects.filter(username=username,password=password)
            if user.exists():
                # messages.success(request, 'Successfully Logged In')
                request.session["username"]=username
                return redirect('Halaman')
            else:            	
                return render(request, "Website/login.html", {
                "message": "Username dan password tidak sesuai, silakan Registrasi ulang..",'select_jenis': Model_jenis.objects.all()
            	})

    return render(request, 'Website/login.html', {'select_jenis': Model_jenis.objects.all()})

def Halaman(request):
	if 'cari_jenis' in request.GET:
		cari_jenis=request.GET['cari_jenis']
		Tampil = Model_kambingss.objects.filter(jenis=cari_jenis)
	else:
		Tampil = Model_kambingss.objects.all()
	if request.method == 'GET':
		username = request.session.get('username')
		data = Model_pelanggans.objects.filter(username=username)
		tanggal_sekarang = strftime('%d/%m/%Y')
		select_jenis = Model_jenis.objects.all()

	context = {	
	'Aplikasi':'Aplikasi',
	'username': username,
	'select_jenis': select_jenis,
	'Tampil': Tampil,
	}
	return render(request, 'Website/halaman.html',  context)

def logout_halaman(request):
    auth_logout(request)
    return redirect('/')

def detail_halaman(request, kode_p):
	select_jenis = Model_jenis.objects.all()
	tampil = Model_kambingss.objects.get(id=kode_p)
	tanggal_sekarang = strftime('%d-%m-%Y')
	if request.method == 'GET':
		username = request.session.get('username')
		data = Model_pelanggans.objects.filter(username=username)
	context = {
	'username': username,
	'tampil': tampil,
	'tanggal_sekarang': tanggal_sekarang,
	'select_jenis': select_jenis,
	}
	return render(request, 'Website/Master_pemesanan/detail.html',  context)

def tambah_pesanan(request, kode_p):
	select_jenis = Model_jenis.objects.all()
	tampil = Model_kambingss.objects.get(id=kode_p)
	tanggal_sekarang = strftime('%d-%m-%Y')
	if request.method == 'GET':
		username = request.session.get('username')
		data = Model_pelanggans.objects.filter(username=username)
	context = {
	'username': username,
	'tampil': tampil,
	'tanggal_sekarang': tanggal_sekarang,
	'select_jenis': select_jenis,
	'data': data,
	}
	return render(request, 'Website/Master_pemesanan/tambah_pesanan.html',  context)

def simpan_pemesanan(request):
	if request.method == 'POST':
		tanggal_sekarang = strftime('%d-%m-%Y')
		Model_pemesanans.objects.create(
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			alamat = request.POST['alamat'],
			nohp = request.POST['nohp'],
			jenis = request.POST['jenis'],
			jumlah = request.POST['jumlah'],
			harga = request.POST['harga'],
			total = request.POST['total'],
			tgl_pesanan = tanggal_sekarang,
			status = 'Belum Bayar'
			)
		messages.info(request, 'Pemesanan Berhasil Di Proses.?')
		return HttpResponseRedirect("/check_pemesanan/")


def check_pemesanan(request):
	select_jenis = Model_jenis.objects.all()
	tanggal_sekarang = strftime('%d-%m-%Y')
	if request.method == 'GET':
		username = request.session.get('username')
		data = Model_pelanggans.objects.filter(username=username)
		for tampil in data:
			noktp = tampil.noktp
			Tampil = Model_pemesanans.objects.filter(noktp=noktp)
    		
	context = {
	'username': username,
	'tanggal_sekarang': tanggal_sekarang,
	'select_jenis': select_jenis,
	'Tampil': Tampil,
	}
	return render(request, 'Website/Master_pemesanan/pemesanan.html',  context)

def Hapus_pesanan(request, kode_p):
	Model_pemesanans.objects.filter(id=kode_p).delete()
	messages.info(request, 'Pesanan Berhasil Di Hapus..?')
	return HttpResponseRedirect("/check_pemesanan/")

def proses_pembayaran(request, kode_p):
	select_jenis = Model_jenis.objects.all()
	tampil = Model_pemesanans.objects.get(id=kode_p)
	tanggal_sekarang = strftime('%d-%m-%Y')
	if request.method == 'GET':
		username = request.session.get('username')
		data = Model_pelanggans.objects.filter(username=username)
	context = {
	'username': username,
	'tampil': tampil,
	'tanggal_sekarang': tanggal_sekarang,
	'select_jenis': select_jenis,
	'data': data,
	}
	return render(request, 'Website/Master_pemesanan/proses_bayar.html',  context)

def simpan_pembayaran(request):
	if request.method == 'POST':
		tanggal_sekarang = strftime('%d-%m-%Y')
		Model_pembayarans.objects.create(
			noktp = request.POST['noktp'],
			nama_lengkap = request.POST['nama_lengkap'],
			jenis = request.POST['jenis'],
			jumlah = request.POST['jumlah'],
			harga = request.POST['harga'],
			total = request.POST['total'],
			tgl_pembayaran = tanggal_sekarang,
			bayar = request.POST['bayar'],
			keterangan = request.POST['keterangan'],
			file_tf = request.FILES['file_tf'],
			status = 'Terbayar'
			)
	edit_data = Model_pemesanans.objects.get(id=request.POST.get('id'))
	if request.method == 'POST':
			edit_data.status = 'Terbayar'
			edit_data.save()
			messages.info(request, 'Pembayaran Berhasil Ter-kirim ke Server Admin.?')
			return HttpResponseRedirect("/check_pemesanan/")

def check_pembayaran(request):
	select_jenis = Model_jenis.objects.all()
	tanggal_sekarang = strftime('%d-%m-%Y')
	if request.method == 'GET':
		username = request.session.get('username')
		data = Model_pelanggans.objects.filter(username=username)
		for tampil in data:
			noktp = tampil.noktp
			Tampil = Model_pembayarans.objects.filter(noktp=noktp)
    		
	context = {
	'username': username,
	'tanggal_sekarang': tanggal_sekarang,
	'select_jenis': select_jenis,
	'Tampil': Tampil
	}
	return render(request, 'Website/Master_pemesanan/check_pembayaran.html',  context)

def nota_pembayaran(request, kode_p):
	select_jenis = Model_jenis.objects.all()
	tampil = Model_pembayarans.objects.get(id=kode_p)
	tanggal_sekarang = strftime('%d-%m-%Y')
	if request.method == 'GET':
		username = request.session.get('username')
	context = {
	'username': username,
	'tampil': tampil,
	'tanggal_sekarang': tanggal_sekarang,
	}
	return render(request, 'Website/Master_pemesanan/nota.html',  context)

def check_pengiriman(request):
	select_jenis = Model_jenis.objects.all()
	tanggal_sekarang = strftime('%d-%m-%Y')
	if request.method == 'GET':
		username = request.session.get('username')
		data = Model_pelanggans.objects.filter(username=username)
		for tampil in data:
			noktp = tampil.noktp
			Tampil = Model_pengirimanss.objects.filter(noktp=noktp)
    		
	context = {
	'username': username,
	'tanggal_sekarang': tanggal_sekarang,
	'select_jenis': select_jenis,
	'Tampil': Tampil
	}
	return render(request, 'Website/Master_pemesanan/check_pengiriman.html',  context)

@csrf_exempt
def payment(request):
    if request.method == 'POST':
        snap = midtransclient.Snap(
            is_production=settings.MIDTRANS['IS_PRODUCTION'],
            server_key=settings.MIDTRANS['SERVER_KEY']
        )

        order_id = 'order-' + str(int(time.time()))
        gross_amount = int(request.POST.get('total', 0))

        transaction_data = {
            "transaction_details": {
                "order_id": order_id,
                "gross_amount": gross_amount
            },
            "credit_card": {
                "secure": True
            },
            "customer_details": {
                "first_name": request.POST.get('nama_lengkap'),
                "email": request.POST.get('email'),
                "phone": request.POST.get('telpon')
            }
        }

        try:
            transaction = snap.create_transaction(transaction_data)
            transaction_token = transaction.get('token', '')
            payment_url = transaction.get('redirect_url', '')

            if transaction_token:
                # Save to the database if needed
                transaksi = Model_pembayarans(
                    noktp=request.POST.get('noktp', ''),
                    nama_lengkap=request.POST.get('nama_lengkap', ''),
                    jenis=request.POST.get('jenis', ''),
                    jumlah=request.POST.get('jumlah', ''),
                    harga=request.POST.get('harga', ''),
                    total=request.POST.get('total', ''),
                    tgl_pembayaran=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    bayar=request.POST.get('bayar', ''),
                    keterangan=request.POST.get('keterangan', ''),
                    file_tf=request.FILES.get('file_tf', None),
                    status='Baru'
                )
                transaksi.save()

                return JsonResponse({"payment_url": payment_url})
            else:
                return JsonResponse({"error": "Failed to get transaction token"}, status=400)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return render(request, 'proses_pembayaran.html')

@csrf_exempt
def midtrans_notification(request):
    if request.method == "POST":
        data = json.loads(request.body) # Extract the order ID
        transaction_status = data.get('transaction_status', '')

        if transaction_status == 'settlement':
            return HttpResponse('OK')
    
    return HttpResponse('Error')
