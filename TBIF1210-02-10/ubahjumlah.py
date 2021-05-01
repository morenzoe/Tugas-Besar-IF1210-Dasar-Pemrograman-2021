"""
Program F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory
Program ini akan menambah atau mengurangi jumlah gadget atau consumable
sesuai dengan input Admin.

Akses : Admin
"""

# KAMUS
# Daftar library
from constant import gadget, consumable, active_account
from login import cek_active_account

# Daftar variabel dan konstanta
# db_gadget, db_consumable    : list of list
# file_gadget, file_consumable: list of list
# isLoggedIn                  : bool
# pjg ID                      :int
# ID                          : chr+int
# jumlah                      : int


def cekid(ID, data):
    # KAMUS LOKAL
    # cek : int

    # ALGORITMA
    # Inisialisasi awal cek
    cek = 0
    for i in range(len(data)):  # Membaca panjang data
        if data[i][0] == ID:
            cek = 1             # ID ditemukan di database
    if cek == 1:
        return True             # Mengembalikan True apabila ID ditemukan
    else:
        return False            # Mengembalikan False apabila ID tidak ditemukan


def cekdelimit(cek):
	# KAMUS LOKAL
    # -

    # ALGORITMA
    # Mengecek ";"
    if ";" in cek:
        return True    # Mengembalikan True apabila ";" ditemukan
    else:
        return False   # Mengembalikan False apabila ";" ditemukan


def ubah(ID,data,jumlah):
    # KAMUS LOKAL
    # idx   : int
    # stok  : int
    # jumlah: int
    
    # ALGORITMA
    # Menemukan posisi ID
    for i in range (len(data)):
        if data[i][0] == ID:
            idx = i
            
    # Menambahkan jumlah item
    stok = data[idx][3] + jumlah
    
    # Mengubah jumlah item    
    if stok >= 0:
        data[idx][3] = stok
    else:
        data[idx][3] = stok - jumlah
    
    # Memastikan bahwa jumlah akhir lebih >= 0
    if stok < 0:
        # Beritahu pengguna gagal mengubah jumlah
        print()
        print("(/^-^)/:",jumlah, data[idx][1], "gagal dibuang karena stok kurang. Stok sekarang : ", (data[idx][3]))
    else: # stok >= 0
        # Beritahu pengguna telah berhasil mengubah jumlah
        if jumlah >= 0:
            print()
            print("(=^v^=):",jumlah , (data[idx][1]) , "berhasil ditambahkan. Stok sekarang : ",(data[idx][3]))
        else:
            print()
            print("(=^v^=):",jumlah , (data[idx][1]) , "berhasil dibuang. Stok sekarang : ",(data[idx][3]))

        
# ALGORITMA PROGRAM UTAMA
def ubahjumlah(databases):
    """
    Prosedur ini akan meminta input ID dan jumlah item yang ingin diubah, yaitu:
    Masukan ID    :
    Masukan Jumlah:
    """
    
    # Membuat list dari file yang akan diubah
    db_gadget = databases[gadget]
    file_gadget = db_gadget
    db_consumable = databases[consumable]
    file_consumable = db_consumable

    # Validasi login pengguna
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        username = databases[active_account][1]
        role = databases[active_account][5]
        
        # Validasi role pengguna
        if role == "Admin":
            # input ID gadget atau consumable
            ID = input("Masukan ID    : ")
            pjgID = len(ID)        
            if pjgID == 0:
                print()
                print("(/'o')/: Gagal mengubah jumlah karena ID tidak valid.")
                print()
                print("(^.~)/: Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                print("(^.~)/: Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
            else:
                # Identifikasi ID gadget
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
                        
                        # Memastikan bahwa ID tersedia
                        if cekid(ID,file_gadget):
                            # Input jumlah
                            jumlah = input("Masukan Jumlah: ")
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
                
                # Identifikasi ID consumable
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
                    
                        # Memastikan bahwa ID tersedia
                        if cekid(ID,file_consumable):
                            jumlah = input("Masukan Jumlah: ")
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
            print("(D_D): Maaf, role",username,"bukan Admin, silahkan login sebagai Admin untuk mengubah jumlah item.")
            return databases
    else:
        print("(^v^): Kamu belum login, silahkan login sebagai Admin untuk mengubah jumlah item.")
    
    return databases


