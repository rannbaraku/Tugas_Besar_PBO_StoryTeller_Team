#Penerapan konsep modulariti 
from os import stat_result
import mysql.connector 
from datetime import datetime
from datetime import date
from threading import Thread
import Fungsi as Fungsi

#koneksi Database
db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd="",
	database="perpustakaan"
)
cursor = db.cursor()

#fungsi yang mengakhiri program
def finish():
    print("\n======== Proses Berakhir =========\n")

#fungsi utama
def menu_utama() :

	#tampilan dashboard
	print("\n==== Pusat Perpustakaan ITERA ===")
	print("1. Perpustakaan GKU")
	print("2. Perpustakaan Gedung E")
	print("3. Perpustakaan Labtek II")
	print("4. Data Pelanggan")
	print("5. Menu Peminjaman")
	print("6. Keluar")

	menu=int(input("Masukkan Pilihan : "))

	if (menu == 1 or menu == 2 or menu == 3) :

		#abstraksi
		if menu == 1 : 	perpustakaan= Fungsi.Perpustakaan("ITERA_001","Perpustakaan GKU")
		elif menu == 2 : perpustakaan= Fungsi.Perpustakaan("ITERA_002","Perpustakaan Gedung E")
		elif menu == 3 : perpustakaan= Fungsi.Perpustakaan("ITERA_003","Perpustakaan Labtek II")

		#abstraksi
		perpustakaan.Identitas()
		print("Manajemen Item Perpustakaan")
		print("1. Menampilakan Item")
		print("2. Menambah Item")
		print("3. Manghapus Item")
		print("4. Mengubah Item")
		print("5. kembali ke menu utama")
		pilihan=int(input("Aksi yang ingin ? : "))
		if (menu==1) :
			
			if(pilihan==1) :
				print("Menampilkan Item Perpustakaan GKU")
				#abstraksi
				perpustakaan.Tampil_item_perpus()			

			elif(pilihan==2) :
				print("Menambahkan Item Perpustakaan GKU")
				#abstraksi
				perpustakaan.Tambah_item_perpus()

			elif(pilihan==3) :
				#abstraksi
				perpustakaan.Hapus_item_perpus()

			elif(pilihan==4) :
				#astraksi
				perpustakaan.Ubah_item_perpus()
			elif(pilihan==5) :
				menu_utama()
		elif(menu==2) :
			if(pilihan==1) :
				print("Menampilkan Item Perpustakaan Gedung E")
				#abstraksi
				perpustakaan.Tampil_item_perpus()			

			elif(pilihan==2) :
				print("Menambahkan Item Perpustakaan Labtek II")
				#abstraksi
				perpustakaan.Tambah_item_perpus()

			elif(pilihan==3) :
				#abstraksi
				perpustakaan.Hapus_item_perpus()
			elif(pilihan==4) :

				#abstraksi
				perpustakaan.Ubah_item_perpus()
			elif(pilihan==5) :
				menu_utama()
		elif(menu==3) :
			if(pilihan==1) :
				print("Menampilkan Item Perpustakaan Labtek II")
				#abstraksi
				perpustakaan.Tampil_item_perpus()	

			elif(pilihan==2) :
				print("Menambahkan Item Perpustakaan Labtek II")
				#abstraksi
				perpustakaan.Tambah_item_perpus()

			elif(pilihan==3) :
				#abstraksi
				perpustakaan.Hapus_item_perpus()
			
			elif(pilihan==4) :
				#abstrkasi
				perpustakaan.Ubah_item_perpus()
			
			elif(pilihan==5) :
				menu_utama()

	elif (menu == 4) :
		print("\nData Pelanggan")
		print("1. Menampilkan Data Pelanggan") 
		print("2. Menambahkan Data Pelanggan")
		print("3. Menghapus Data Pelanggan")
		print("4. Mengubah Data Pelanggan")
		print("5. Kembali Ke Menu Utama")
		pilihan = int(input("Aksi yang ingin ? : "))
		if (pilihan==1) :
			sql = "SELECT * FROM pelanggan"
			cursor.execute(sql)
			result = cursor.fetchall()
			for basdat in result:
				#abstaksi
				pelanggan=Fungsi.Pelanggan(basdat)
				pelanggan.Identitas()

		elif (pilihan==2) :
			data=[" "," "," "," "," "," "," "," "]
			data[0]=str(input("Masukkan ID Pelanggan     : "))
			data[1]=str(input("Masukkan Type Pelanggan   : "))
			data[2]=str(input("Masukkan Nama Pelanggan   : "))
			data[3]=str(input("Masukkan Alamat Pelanggan : "))
			data[4]=str(input("Masukan No. Hp Pelanggan  : "))
			data[5]=str(input("Masukan E-mail Pelanggan  : "))
			#abstrkasi
			pelanggan_tambah=Fungsi.Pelanggan(data)
			pelanggan_tambah.tambahPelanggan()

		elif (pilihan==3) :
			id_pelanggan=str(input("Masukkan Id Pelanggan yang akan dihapus : "))
			sql = """SELECT * FROM pelanggan WHERE id_pelanggan = "%s" """ % (id_pelanggan)
			cursor.execute(sql)
			result = cursor.fetchall()
			count = 0
			for pelanggan in result:
				#abstraksi
				customer=Fungsi.Pelanggan(pelanggan)
				customer.hapusPelanggan()
				count += 1

			if (count == 0):
				print ("Data Tidak ada")

		elif (pilihan==4) :
			id_pelanggan=str(input("Masukkan Id Pelanggan yang akan diubah : "))
			sql = """SELECT * FROM pelanggan WHERE id_pelanggan = "%s" """ % (id_pelanggan)
			cursor.execute(sql)
			result = cursor.fetchall()
			count = 0
			for pelanggan in result:
				#abstraksi
				customer=Fungsi.Pelanggan(pelanggan)
				customer.UbahPelanggan()
				count += 1

			if (count == 0):
				print ("Data Tidak ada")

		elif (pilihan==5) :
			menu_utama()

	elif (menu == 5) :
		print("\nRekam Peminjaman")
		print("1. Menampilakan Data Peminjam")
		print("2. Melakukan peminjaman item")
		print("3. Manghapus Data Peminjam")
		print("4. Mengembalikan Pinjaman")
		print("5. Menampilakan peminjaman terdenda")
		print("6. Kembali ke Menu Utama")

		pilihan = int(input("Aksi yang ingin ? : "))
		if(pilihan==1) :
			sql= "SELECT * FROM peminjaman"
			cursor.execute(sql)
			result = cursor.fetchall()
			for basdat in result:
				#abstraksi
				peminjam=Fungsi.Peminjaman(basdat)
				print(peminjam)
		elif(pilihan==2) :
			data=[" "," "," "," "," "," "," "," "]
			data[0]=str(input("Masukkan Id Pelanggan         : "))
			data[1]=str(input("Masukkan Tanggal Peminjaman   : "))
			data[2]=str(input("Masukkan Id Item              : "))
			data[3]=str("0000-00-00")
			data[4]=int(0)
			data[5]="Dipinjam"

			sql= """SELECT status FROM peminjaman where id_item= "%s" && status ="Dipinjam" """ % (data[2])
			cursor.execute(sql)
			item = cursor.fetchall()
			if not item :
				item="none"

			sql= """SELECT status FROM peminjaman where id_pelanggan= "%s" && status ="Dipinjam" """ % (data[0])
			cursor.execute(sql)
			pelanggan = cursor.fetchall()
			if not pelanggan :
				pelanggan="none"

			if (item=="none" and pelanggan=="none") :
				peminjam_tambah=Fungsi.Peminjaman(data)
				peminjam_tambah.tambahPeminjam()
			else :
				if (item[0][0]=="Dipinjam") :
					print("Maaf Buku sedang dipinjam")

				if (pelanggan[0][0]=="Dipinjam") :
					print("Maaf batas meminjam hanya satu kali, silahkan kembalikan buku anda terlebih dahulu")
		
		elif(pilihan==3) :
			id_pelanggan=str(input("Masukkan Id Pelanggan yang akan dihapus : "))
			sql = """SELECT * FROM pelanggan WHERE id_pelanggan = "%s" """ % (id_pelanggan)
			cursor.execute(sql)
			result = cursor.fetchall()
			count = 0
			for pelanggan in result:
				#anstraksi
				peminjam=Fungsi.Peminjaman(pelanggan)
				peminjam.hapusPeminjam()
				count += 1

			if (count == 0):
				print ("Data Tidak ada")


		elif(pilihan==4) :
			id_item=str(input("Masukkan Id item yang akan dikembalikan : "))
			sql = """SELECT * FROM peminjaman WHERE id_item = "%s" && status="Dipinjam" """ % (id_item)
			cursor.execute(sql)
			result = cursor.fetchall()
			count = 0
			for pelanggan in result:
				peminjam=Fungsi.Peminjaman(pelanggan)
				peminjam.mengembalikanPeminjam()
				count += 1

			if (count == 0):
				print ("Data Tidak ada/Sudah dikembalikan")

		elif (pilihan==5) : 

			#Akses file.txt
			f = open("Terdenda.txt", "wt")
			f.write("Data peminjaman terdenda \n")
			f.write("========================================\n")

			sql = """SELECT * FROM peminjaman WHERE biaya <> "%s" """ % (0)
			cursor.execute(sql)
			result = cursor.fetchall()
			for basdat in result:
				#abstraksi
				peminjam=Fungsi.Peminjaman(basdat)
				print(peminjam)
				#oprasi write pada file
				f.write(str(peminjam))
			f.close()


		else :
			menu_utama()


	elif (menu == 6) : 
		finish()
#main os
if __name__ == '__main__':
	menu_utama()
	
