import mysql.connector #Memanggil mysql sebagai media pengolahan data

db = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd="",
	database="Perpustakaan"
)

if db.is_connected(): #Pengecekan python terhubung ke mysql
    print("Berhasil terhubung ke mysql\n")
else :
    print ("Gagal terhubung\n")
cursor = db.cursor()


def Tampil_Item (id_pustaka):        # Penampilan Tabel Motor
    sql = """SELECT * FROM item WHERE id_perpustakaan = "%s" """ % (id_pustaka)
    cursor.execute(sql)
    result = cursor.fetchall()
    count = 0
    for i in result:
        print (i)
        count += 1

    if (count == 0):
        print("\nTidak ada data Item\n")

def select_item (id_item):
    sql = """SELECT * FROM item WHERE id_item = "%s" """ % (id_item)
    cursor.execute(sql)
    result = cursor.fetchall()
    count = 0
    for i in result:
        count += 1

    if (count == 0):
        return False
    else : return True

def Delete_item (id_item):

    if select_item(id_item) :
        sql = """DELETE FROM item WHERE id_item = "%s" """ % (id_item)
        cursor.execute(sql)
        db.commit()
        return True
    else :return False

def Change_item (data) :

    if select_item(id_item) :
        sql = "INSERT INTO item (id_item, id_perpustakaan, kategori, judul, penulis, penerbit, tahun_produksi, salinan) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
        cursor.execute(sql, val)
        db.commit()
        print("Perubahan Tersimpan")
    
    else : print("item yang ingin diubah tidak tersedia")



def Insert_item (data) :
    sql = "INSERT INTO item (id_item, id_perpustakaan, kategori, judul, penulis, penerbit, tahun_produksi, salinan) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7])
    cursor.execute(sql, val)
    db.commit()
    return True

