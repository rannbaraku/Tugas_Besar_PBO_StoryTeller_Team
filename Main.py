import Fungsi as fungsi
import Item as item
class Perpustakaan :
	def __init__(self,id_perpustakaan,nama_perpustakaan) :
		self.id_perpustakaan=id_perpustakaan
		self.nama_perpustakaan=nama_perpustakaan

class Item (Perpustakaan):
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



print("==== Pusat Perpustakaan ITERA ====")
while(True):
	a=fungsi.intro()
	if a == "no" : continue
	elif a == "yes" : 
		a = False
		print("Program Berakhir")
		break
	else : 
		print ("Perpustakaan terpilih : ", a)
		id_pustaka = str(a)
		#nama_pustaka = ambil dari databse
		#Perpustakaan1 = Perpustakaan(id_pustaka,nama_pustaka)
		a=True
		break

while(a):
	a=fungsi.menu()
	if a == "no" :
		a=True
		continue
	elif a == "yes" : 
		a = False
		print("Program Berakhir")
		break
	else : 
		print ("Menu Terpilih : ",a)
		b=a
		a=True
		break


while(a):
	if b == 1 :
		a=fungsi.Pilih_Item()
#	elif b == 2
#	elif b == 3
	if a == "no" :
		a=True
		continue
	elif a == "yes" : 
		a = False
		print("Program Berakhir")
		break
	else : 
		print ("Menu Terpilih : ",a)
		c=b
		b=a
		break


while(a):
	if c == 1 :
		if b == 1 :
			item.Tampilkan_Item(id_pustaka)
			break
		elif b == 2 :
			Item_Baru = item.Menambah_Item(id_pustaka)
			print(Item_Baru)
			Item1= Item(Item_Baru)
			print(Item_Baru)
			break

		elif b == 3 :
			id = str(input("Masukan ID dari item yang ingin dihapus : "))
			break
			#fungsi query

		elif b == 4 :
			id = str(input("Masukan ID dari item yang ingin diubah : "))
			break
			#fungsi query


		
	


# while(True) :

#     print("###")
#  	break
# 	a="Yes"
#     a = Fungsi.intro()
#      	if a == "yes" : 
#     	a = "program berakhir"
#         break
#     elif a == "no" : continue
#     else : break 
# print(a)