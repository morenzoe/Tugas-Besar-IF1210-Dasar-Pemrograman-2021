from constant import gadget,consumable,active_account
from login import cek_active_account

def cekid(ID,data):
    cek = 0
    for i in range(len(data)):
        if data[i][0] == ID:
            cek = 1
    if cek == 1:
        return True
    else:
        return False      

def cekdelimit(cek):
	if ";" in cek:
		return True
	else:
		return False

def ubah(ID,data,jumlah):
    for i in range (len(data)):
        if data[i][0] == ID:
            idx = i

    stok = data[idx][3] + jumlah
        
    if stok >= 0:
        data[idx][3] = stok
    else:
        data[idx][3] = stok - jumlah

    if stok < 0:
        print()
        print("(/^-^)/:",jumlah, data[idx][1], "gagal dibuang karena stok kurang. Stok sekarang : ", (data[idx][3]))
    else:
        if jumlah >= 0:
            print()
            print("(=^v^=):",jumlah , (data[idx][1]) , "berhasil ditambahkan. Stok sekarang : ",(data[idx][3]))
        else:
            print()
            print("(=^v^=):"jumlah , (data[idx][1]) , "berhasil dibuang. Stok sekarang : ",(data[idx][3]))

        
# prosedur akhir
def ubahjumlah(databases):
    """
    Prosedur ini akan meminta input ID dan jumlah item yang ingin diubah, yaitu:
    Masukan ID    :
    Masukan Jumlah:
    """
    db_gadget = databases[gadget]
    file_gadget = db_gadget
    db_consumable = databases[consumable]
    file_consumable = db_consumable

    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        if databases[active_account][5] == "Admin":
            ID = input("Masukan ID    : ")
            pjgID = len(ID)        
            if pjgID == 0:
                print()
                print("(/'o')/: Gagal mengubah jumlah karena ID tidak valid.")
                print()
                print("(^.~)/: Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                print("(^.~)/: Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
            else:
                if ID[0] == "G":
                    if pjgID == 1:
                        print()
                        print("(/'o')/: Gagal mengubah jumlah karena ID gadget tidak valid.")
                        print()
                        print("(^.~)/: Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                        return databases
                    else:
                        Id = ID[1:]
                        try:
                            Id = int(Id)
                        except BaseException:
                            print()
                            print("(/'o')/: Gagal mengubah jumlah karena ID gadget tidak valid.")
                            print()
                            print("(^.~)/: Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                            return databases
                            
                        if(Id <= 0):
                            print()
                            print("(/'o')/: Gagal mengubah jumlah karena ID gadget tidak valid.")
                            print()
                            print("(^.~)/: Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                            return databases
                        
                        if cekid(ID,file_gadget):
                            jumlah = input("Masukan Jumlah : ")
                            try:
                                jumlah = int(jumlah)
                            except BaseException:
                                print()
                                print("(^.~)/: Jumlah tidak valid. Jumlah harus berupa bilangan bulat.")
                                return databases
                            ubah(ID,file_gadget,jumlah)
                        else:
                            print()
                            print("(/'o')/: Gagal mengubah jumlah karena ID gadget tidak ditemukan.")
                            print()
                            print("(^.~)/: Pastikan gadget yang dimaksud sudah tersedia di database.")
                            return databases
                elif ID[0] == "C":
                    if pjgID == 1:
                        print()
                        print("(/'o')/: Gagal mengubah jumlah karena ID consumable tidak valid.")
                        print()
                        print("(^.~)/: Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
                        return databases
                    else:
                        Id = ID[1:]
                        try:
                            Id = int(Id)
                        except BaseException:
                            print()
                            print("(/'o')/: Gagal mengubah jumlah karena ID consumable tidak valid.")
                            print()
                            print("(^.~)/: Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
                            return databases
                            
                        if(Id <= 0):
                            print()
                            print("(/'o')/: Gagal mengubah jumlah karena ID consumable tidak valid.")
                            print()
                            print("(^.~)/: Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
                            return databases
                    
                        if cekid(ID,file_consumable):
                            jumlah = input("Masukan Jumlah : ")
                            try:
                                jumlah = int(jumlah)
                            except BaseException:
                                print()
                                print("(^.~)/: Jumlah tidak valid. Jumlah harus bilangan bulat.")
                            ubah(ID,file_consumable,jumlah)
                        else:
                            print()
                            print("(/'o')/: Gagal mengubah jumlah karena ID consumable tidak ditemukan.")
                            print()
                            print("(^.~)/: Pastikan bahwa consumable yang dimaksud sudah tersedia di database.")
                            return databases
               
                else:
                    print()
                    print("(/'o')/: Gagal mengubah jumlah karena ID tidak valid.")
                    print()
                    print("(^.~)/: Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                    print("(^.~)/: Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
                    
                return databases
        else:
            print("(D_D): Maaf, kamu bukan Admin, silahkan login sebagai Admin untuk mengubah jumlah item.")
            return databases
    else:
        print("(^v^): Kamu belum login, silahkan login sebagai Admin untuk mengubah jumlah item.")
    
    return databases


