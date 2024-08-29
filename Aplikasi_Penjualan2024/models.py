from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from django.contrib.auth.models import User
# Create your models here.
class Model_jenis(models.Model):	
	jenis	= models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 1200)
	satuan	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.jenis)

class Model_kambingss(models.Model):	
	status	=models.CharField(max_length = 1200)	
	jenis	= models.CharField(max_length = 1200)
	usia	= models.CharField(max_length = 1200)
	tinggi	=models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 1200)
	stock	=models.CharField(max_length = 1200)
	foto	= models.ImageField(upload_to ='Berkas/', null=True)
	keterangan	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.status)

class Model_pelanggans(models.Model):
	noktp	= models.CharField(max_length = 1200)
	nama_lengkap	= models.CharField(max_length = 1200)
	alamat	=models.CharField(max_length = 1200)
	nohp	=models.CharField(max_length = 1200)
	jk	=models.CharField(max_length = 1200)
	email	=models.CharField(max_length = 1200)
	username	=models.CharField(max_length = 1200)
	password	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.noktp)

class Model_penjualan(models.Model):	
	jenis	= models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 1200)
	jumlah	=models.CharField(max_length = 1200)
	total	=models.CharField(max_length = 1200)
	tgl_penjualan	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.jenis)

class Model_transaksis(models.Model):	
	pelanggan	= models.CharField(max_length = 1200)
	jenis	= models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 1200)
	jumlah	=models.CharField(max_length = 1200)
	total	=models.CharField(max_length = 1200)
	bayar	=models.CharField(max_length = 1200)
	status_transfer	=models.CharField(max_length = 1200)
	tgl_transaksi	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.jenis)


class Model_pemesanans(models.Model):
	noktp	= models.CharField(max_length = 1200)
	nama_lengkap	= models.CharField(max_length = 1200)
	alamat	=models.CharField(max_length = 1200)
	nohp	=models.CharField(max_length = 1200)
	jenis	=models.CharField(max_length = 1200)
	jumlah	=models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 1200)
	total	=models.CharField(max_length = 1200)
	tgl_pesanan	=models.CharField(max_length = 1200)
	status	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.noktp)

class Model_pembayarans(models.Model):
	noktp	= models.CharField(max_length = 1200)
	nama_lengkap	= models.CharField(max_length = 1200)
	jenis	=models.CharField(max_length = 1200)
	jumlah	=models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 1200)
	total	=models.CharField(max_length = 1200)
	tgl_pembayaran	=models.CharField(max_length = 1200)
	bayar	=models.CharField(max_length = 1200)
	keterangan	=models.CharField(max_length = 1200)
	file_tf	= models.ImageField(upload_to ='Berkas/', null=True)
	status	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.noktp)

class Model_pengirimanss(models.Model):
	noktp	= models.CharField(max_length = 1200)
	nama_lengkap	= models.CharField(max_length = 1200)
	alamat	=models.CharField(max_length = 1200)
	nohp	=models.CharField(max_length = 1200)
	jenis	=models.CharField(max_length = 1200)
	jumlah	=models.CharField(max_length = 1200)
	harga	=models.CharField(max_length = 1200)
	total	=models.CharField(max_length = 1200)
	tgl_pengiriman	=models.CharField(max_length = 1200)
	pesan	=models.CharField(max_length = 1200)
	status	=models.CharField(max_length = 1200)

	published = models.DateTimeField(auto_now_add = True)
	updated = models.DateTimeField(auto_now = True)
			
	def __str__(self):
		return "{}.{}".format(self.id, self.noktp)