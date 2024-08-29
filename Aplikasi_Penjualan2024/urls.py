from django.contrib import admin
from django.urls import path
from Aplikasi_Penjualan2024 import settings
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,include

urlpatterns = [
      # halaman untuk admin
    path('Login_Sistem/', Login_sistem, name='Login_Sistem'),
    path('Home/', HomeView, name="Home"),
    path('logout/',LogoutView, name="logout"),
    # data jenis pengaduan
    path('Jenis/',Data_jenis, name="Jenis"),
    path('Tambah_jenis/',Tambah_jenis, name="Tambah_jenis"),
    path('edit_jenis/<str:kode_p>',Edit_jenis, name="edit_jenis"),
    path('hapus_jenis/<str:kode_p>',Hapus_jenis, name="hapus_jenis"),
    # data kambing
    path('Kambing/',Data_kambing, name="Kambing"),
    path('Tambah_kambing/',Tambah_kambing, name="Tambah_kambing"),
    path('edit_kambing/<str:kode_p>',Edit_kambing, name="edit_kambing"),
    path('Edit_foto_kambing/<str:kode_p>',Edit_foto_kambing, name="Edit_foto_kambing"),
    path('hapus_kambing/<str:kode_p>',Hapus_kambing, name="hapus_kambing"),
    # data penjualan
    path('Penjualan/',Data_penjualan, name="Penjualan"),
    path('Tambah_penjualan/',Tambah_penjualan, name="Tambah_penjualan"),
    path('Proses_input_penjualan/',Proses_input_penjualan, name="Proses_input_penjualan"),
    path('edit_penjualan/<str:kode_p>',Edit_penjualan, name="edit_penjualan"),
    path('hapus_penjualan/<str:kode_p>',Hapus_penjualan, name="hapus_penjualan"),
    # data transaksi
    path('Transaksi/',Data_transaksi, name="Transaksi"),
    path('Tambah_transaksi/<str:kode_p>',Tambah_transaksi, name="Tambah_transaksi"),
    path('Proses_input_transaksi/',Proses_input_transaksi, name="Proses_input_transaksi"),
    path('Cetak_nota/<str:kode_p>',Cetak_nota, name="Cetak_nota"),
    path('hapus_transaksi/<str:kode_p>',Hapus_transaksi, name="hapus_transaksi"),
    # data pelanggan
    path('Pelanggan/',Data_pelanggan, name="Pelanggan"),
    path('hapus_pelanggan/<str:kode_p>',Hapus_pelanggan, name="hapus_pelanggan"),
    # data pemesanan
    path('Pemesanan/',Data_pemesanan, name="Pemesanan"),
    path('Hapus_dt_pemesanan/<str:kode_p>',Hapus_dt_pemesanan, name="Hapus_dt_pemesanan"),
    # chek pembayaran
    path('Data_pembayaran/',Data_pembayaran, name="Data_pembayaran"),
    path('simpan_pengiriman/',simpan_pengiriman, name="simpan_pengiriman"),
    # data pengiriman
    path('Pengiriman/',Data_pengiriman, name="Pengiriman"),
    path('Edit_pengiriman/<str:kode_p>',Edit_pengiriman, name="Edit_pengiriman"),
    path('Hapus_pengiriman/<str:kode_p>',Hapus_pengiriman, name="Hapus_pengiriman"),
    # buat laporan
    path('Menu_laporan/',Menu_laporan, name="Menu_laporan"),

    path('lp_kambing/',lp_kambing, name="lp_kambing"),
    path('lp_pelanggan/',lp_pelanggan, name="lp_pelanggan"),
    path('lp_pemesanan/',lp_pemesanan, name="lp_pemesanan"),
    path('lp_pengiriman/',lp_pengiriman, name="lp_pengiriman"),
    path('lp_transaksi/',lp_transaksi, name="lp_transaksi"),


    # website
    path('',Website, name="Website"),
    path('detail/<str:kode_p>',detail, name="detail"),
    path('registrasi/',registrasi, name="registrasi"),
    path('simpan_registrasi/',simpan_registrasi, name="simpan_registrasi"),
    # 
    path('login/',login_data, name="login"),
    path('Halaman/',Halaman, name="Halaman"),
    path('logout_halaman', logout_halaman, name='logout_halaman'),
    path('detail_halaman/<str:kode_p>',detail_halaman, name="detail_halaman"),
    # proses pesanan
    path('tambah_pesanan/<str:kode_p>',tambah_pesanan, name="tambah_pesanan"),

    path('simpan_pemesanan/',simpan_pemesanan, name="simpan_pemesanan"),
    path('check_pemesanan/',check_pemesanan, name="check_pemesanan"),
    path('Hapus_pesanan/<str:kode_p>',Hapus_pesanan, name="Hapus_pesanan"),

    # pembayaran
    path('proses_pembayaran/<str:kode_p>',proses_pembayaran, name="proses_pembayaran"),
    path('simpan_pembayaran/',simpan_pembayaran, name="simpan_pembayaran"),
    path('check_pembayaran/',check_pembayaran, name="check_pembayaran"),
    path('nota_pembayaran/<str:kode_p>',nota_pembayaran, name="nota_pembayaran"),

    path('paymant', payment, name='payment'),
    path('midtrans_notification/', midtrans_notification, name='midtrans_notification'),
    # 
    path('check_pengiriman/',check_pengiriman, name="check_pengiriman"),

    path('admin/', admin.site.urls),
]
if settings.DEBUG:    
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)