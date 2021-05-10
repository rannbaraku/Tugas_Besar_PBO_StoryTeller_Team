import SQL as query
import Fungsi as fungsi
import mysql.connector #Memanggil mysql sebagai media pengolahan data


db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd="",
	database="Perpustakaan"
)


class Perpustakaan :
	def __init__(self,id_perpustakaan,nama_perpustakaan) :
		self.id_perpustakaan=id_perpustakaan
		self.nama_perpustakaan=nama_perpustakaan

class Item_Perpus (Perpustakaan):
	def __init__(self,data) :
		self.id_item=data[0]
		self.id_perpustakaan=data[1]
		self.kategori=data[2]
		self.judul=data[3]
		self.penulis=data[4]
		self.penerbit=data[5]
		self.tahun_produksi=data[6]
		self.salinan=data[7]
		#simpan menggunakan sql

class Pelanggan :
	def __init__(self,id_pelanggan,type,nama,alamat,no_hp,email):
		self.id_pelanggan=id_pelanggan
		self.type=type
		self.nama=nama
		self.alamat=alamat
		self.no_hp=no_hp
		self.email=email

class Peminjaman () :
	def __init__(self,id_pelanggan,tanggal_peminjaman,id_item,tanggal_pengembalian,biaya) :
		self.id_pelanggan=id_pelanggan
		self.tanggal_pengembalian=tanggal_pengembalian
		self.id_item=id_item
		self.tanggal_pengembalian=tanggal_pengembalian
		self.biaya=biaya

def Berakhir() :
	print("Program berakhir")

def menu(id_pustaka) :
	while(True):
		a=fungsi.menu()
		if a == "no" :
			a=True
			continue
		elif a == "yes" or a=="exit" : 
			a = False
			dashboard()
			break
		else : 
			print ("Menu Terpilih : ",a)
			b=a
			a=True
			menu_item(b,id_pustaka)
			break

def menu_item(b,id_pustaka) :
	while(True):
		if b == 1 :
			a=fungsi.Pilih_Item()
	#	elif b == 2
	#	elif b == 3
		if a == "no" :
			a=True
			continue
		elif a == "yes" or a=="exit" : 
			a = False
			dashboard()
			break
		else : 
			print ("Menu Terpilih : ",a)
			c=b
			b=a
			execute_item(b,c,id_pustaka)
			break

def Menambah_Item (id_pustaka):
    id_item=str(input("Masukkan ID Item  : "))    
    id_perpustakaan=id_pustaka
    kategori=str(input("Masukan kategori Item : "))
    judul=str(input("Masukan judul : "))
    penulis=str(input("Masukan penulis : "))
    penerbit=str(input("Masukan penerbit : "))
    tahun_produksi=str(input("tahun produksi : "))
    salinan=int(input("Salinan ke : "))
    return (id_item,id_perpustakaan,kategori,judul,penulis,penerbit,tahun_produksi,salinan)

def execute_item(b,c,id_pustaka):
	while(True):
		if c == 1 :
			if b == 1 :
				query.Tampil_Item(id_pustaka)
				dashboard()

			elif b == 2 :
				Item_Baru = Menambah_Item(id_pustaka)
				Item1 = Item_Perpus(Item_Baru)
				if query.Insert_item(Item_Baru) : print("Data Tersimpan")
				dashboard()

			elif b == 3 :
				id = str(input("Masukan ID dari item yang ingin dihapus : "))
				if query.Delete_item(id) : print ("data berhasil dihapus")
				else : print ("data yang ingin dihapus tidak tersedia")
				dashboard()
			
				#fungsi query

			elif b == 4 :
				id = str(input("Masukan ID dari item yang ingin diubah : "))
				if query.select_item(id) : 
					print("item ditemukan")
					query.Delete_item(id)
					print ("\nForm perubahan data\n")
					print ("\nData yang anda masukan akan menimpa data yang lama\n")
					Item = Menambah_Item(id_pustaka)
					if query.Insert_item(Item) : print ("Data Berhasil Diubah")
				dashboard()
			
			#fungsi query

def dashboard ():
	print("\n==== Pusat Perpustakaan ITERA ====")
	while(True):
		a=fungsi.intro()
		if a == "no" : continue
		elif a == "yes" or a == "exit" : 
			a = False
			Berakhir()
			break
		else : 
			print ("Perpustakaan terpilih : ", a)
			id_pustaka = str(a)
			#nama_pustaka = ambil dari databse
			#Perpustakaan1 = Perpustakaan(id_pustaka,nama_pustaka)
			menu(id_pustaka)
			break
dashboard()