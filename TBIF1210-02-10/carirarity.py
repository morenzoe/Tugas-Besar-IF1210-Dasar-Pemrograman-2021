"""
Program F03 - Pencarian gadget berdasarkan rarity
Dapat diakses oleh Admin dan User.
Pengguna dapat mencari gadget dengan rarity tertentu. Pengguna akan memasukkan
rarity (C, B, A, S), kemudian akan ditampilkan Gadget dengan rarity tersebut.
"""

# KAMUS
# Daftar library lokal
from constant import gadget,active_account
from login import cek_active_account

# Variabel dan konstanta
# isLoggedIn            : boolean
# username              : string
# array_data            : array of array
# rarity                : string

def printdata(data):
    # meng-output setiap data yang terdapat pada array data

    # KAMUS LOKAL
    # data : array of string and integer { array data yang ingin ditampilkan }

    # ALGORITMA
    print("\nNama            : ", data[1])
    print("Deskripsi       : ", data[2])
    print("Jumlah          : ", data[3], "buah")
    print("Rarity          : ", data[4])
    print("Tahun Ditemukan : ", data[5])

def check_file_tidak_kosong(database):
    # menghasilkan nilai False jika gadget.csv kosong dan menghasilkan nilai True jika gadget.csv tidak kosong

    # ALGORITMA
    if len(database) == 1:
        return False
    else:
        return True


def carirarity(database):
    # meng-output data berdasarkan rarity yang dipilih
    isLoggedIn = cek_active_account(database)
    if isLoggedIn:
        # Pengguna sudah login
        username = database[active_account][2]
        array_data = database[1]
        if check_file_tidak_kosong(array_data):
            # Terdapat gadget pada file gadget.csv
            rarity = input("Masukkan rarity : ")

            while rarity not in "CBAScbas" or len(rarity) != 1:         # Validasi rarity
                rarity = input("Masukkan rarity dengan benar! :")
            rarity = rarity.title()
            
            # Memulai Output data
            print("\nHasil pencarian : ")
            for data in range(len(array_data)):
                if (array_data[data-1][4] == rarity):
                    printdata(array_data[data-1])
        else:
            # Tidak terdapat file gadget pada file gadget.csv
            print("(;_;) : Tidak ada data pada gadget.csv, maafkan admin!")
    else:
        # Pengguna belum login
        print("\(>_<)/ : Anda belum login.")
    return database