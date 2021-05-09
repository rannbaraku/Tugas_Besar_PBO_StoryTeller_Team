class Konfirmasi_ID :
    def __init__ (self,number) :
	    self.number = number
		
    def __str__ (self) :
        if self.number == 1 :
            return "ITERA_001"
        elif self.number == 2 :
            return "ITERA_002"
        else :
            return "ITERA_003"


def intro ():
    print("Pilih perpustakaan yang ingin diakses")
    print("1. Perpustakaan GKU")
    print("2. Perpustakaan Gedung E")
    print("3. Perpustakaan LabTek II")
    pilihan=int(input("Perpustakaan yang ingin diakses ? : "))
    if pilihan >=1 and pilihan <4 : 
        return Konfirmasi_ID(pilihan)
    
    else : 
        print("Pilihan tidak diketahui")
        Yes = str(input("keluar (Y/N) ? : "))
        if Yes=='Y' : return "yes"
        else : return "no"

def menu ():
    print("Menu yang tersedia")
    print("1. Manegement Item")
    print("2. Management subscriber")
    print("3. Rekam peminjaman")
    pilihan=int(input("Aksi yang ingin dilakukan ? : "))
    if pilihan >=1 and pilihan <4 : 
        return pilihan
    
    else : 
        print("Pilihan tidak diketahui")
        Yes = str(input("keluar (Y/N) ? : "))
        if Yes=='Y' : return "yes"
        else : return "no"

def Pilih_Item ():
    print("Management Item")
    print("1. Menampilakan Item")
    print("2. Menambah Item")
    print("3. Manghapus Item")
    print("4. Merubah Item")
    pilihan=int(input("Aksi yang ingin ? : "))
    if pilihan >=1 and pilihan <5 : 
        return pilihan
    
    else : 
        print("Pilihan tidak diketahui")
        Yes = str(input("keluar (Y/N) ? : "))
        if Yes=='Y' : return "yes"
        else : return "no"
