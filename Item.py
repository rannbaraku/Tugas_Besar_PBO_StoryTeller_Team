
def Tampilkan_Item (id_pustaka):
    #query
    print("nanti makai query")

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





