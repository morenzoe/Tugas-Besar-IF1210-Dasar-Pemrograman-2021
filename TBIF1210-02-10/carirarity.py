"""
Program F03 - Pencarian gadget berdasarkan rarity
Dapat diakses oleh Admin dan User.
Pengguna dapat mencari gadget dengan rarity tertentu. Pengguna akan memasukkan
rarity (C, B, A, S), kemudian akan ditampilkan Gadget dengan rarity tersebut.

Akses : Admin, User
"""

# KAMUS
# Daftar library lokal
from constant import gadget
from login import cek_active_account

# Variabel dan konstanta
# isLoggedIn            : boolean
# array_data            : array of array
# rarity                : string

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def printdata(data):
    # meng-output setiap data yang terdapat pada array data

    # KAMUS LOKAL
    # data : array of string and integer { array data yang ingin ditampilkan }

    # ALGORITMA
    print("\nNama            : ", data[1])
    print("Deskripsi       : ", data[2])
    print("Jumlah          : ", data[3], "buah")
    print("Rarity          : ", data[4])
    print("Tahun Ditemukan : ", tahun_int_to_str(data[5]))


def tahun_int_to_str(tahun):
    # Menghasilkan tahun dalam bentuk string

    # ALGORITMA
    tahun_str = str(tahun)
    while len(tahun_str) < 4:
        tahun_str = "0" + tahun_str
    return tahun_str


def check_file_tidak_kosong(database):
    # menghasilkan nilai False jika gadget.csv kosong dan menghasilkan nilai
    # True jika gadget.csv tidak kosong

    # ALGORITMA
    if len(database) == 1:
        return False
    else:
        return True


# ALGORITMA PROGRAM UTAMA
def carirarity(database):
    # meng-output data berdasarkan rarity yang dipilih
    isLoggedIn = cek_active_account(database)
    if isLoggedIn:
        # Pengguna sudah login
        array_data = database[1]
        if check_file_tidak_kosong(array_data):
            # Terdapat gadget pada file gadget.csv
            rarity = input("Masukkan rarity : ")

            # Validasi rarity
            while rarity not in "CBAScbas" or len(rarity) != 1:
                rarity = input("\n(9*.*)9 : Masukkan rarity dengan benar! : ")
            rarity = rarity.title()

            # Memulai Output data
            print("\nHasil pencarian : ")
            for data in range(len(array_data)):
                if (array_data[data - 1][4] == rarity):
                    printdata(array_data[data - 1])
        else:
            # Tidak terdapat file gadget pada file gadget.csv
            print("(;_;) : Tidak ada data pada gadget.csv, maafkan admin!")
    else:
        # Pengguna belum login
        print("\\(>_<)/ : Anda belum login.")
    return database
