"""
Program F04 - Pencarian gadget berdasarkan tahun ditemukan
Dapat diakses oleh Admin dan User.
Pengguna dan admin dapat melakukan pencarian gadget berdasarakan tahun ditemukan.
pengguna memasukkan sebuah tahun, misalnya yyyy,dan kategori pencarian yaitu [=,<,>,<=,>=].
"""

# KAMUS
# Daftar library lokal
from login import cek_active_account
from constant import gadget
from carirarity import check_file_tidak_kosong, printdata

# Variabel dan konstanta
# isLoggedIn            : boolean
# array_data            : array of array
# tahun                 : integer
# tahun_str             : string
# kategori              : string


def ubahtahun(tahun_str):
    # mengubah input tahun menjadi integer jika bisa, jika tidak bisa akan
    # diminta kembali dari input user

    # KAMUS LOKAL
    # check : int

    # ALOGRITMA
    check = 0
    while check == 0:
        if len(tahun_str) == 4:
            check = 1
            try:
                tahun_int = int(tahun_str)
            except:
                # Jika tidak bisa dilakukan proses diatas
                check = 0
                tahun_str = input("\n(9*.*)9 : Masukan salah! Masukkan tahun dengan benar! (YYYY): ")
        else:
            check = 0
            tahun_str = input("\n(9*.*)9 : Masukan salah! Masukkan tahun dengan benar! (YYYY): ")
    return tahun_int


def ubahkategori(kategori):
    # Meminta input user untuk kategori jika input user salah

    # ALGORITMA
    while not(kategori == ">" or kategori == "<" or kategori ==
              "=" or kategori == ">=" or kategori == "<="):
        kategori = input("\n(9*.*)9 : Masukan salah! Masukkan kategori dengan benar! [>,<,=,>=,<=] : ")
    return kategori


def caritahun(database):
    # Meng-output data gadget berdasarkan tahun ditemukannya
    isLoggedIn = cek_active_account(database)
    if isLoggedIn:
        # Pengguna sudah login
        array_data = database[gadget]
        if check_file_tidak_kosong(array_data):
            # Terdapat gadget pada file gadget.csv

            # Input tahun
            tahun_str = input("Masukkan tahun    : ")
            tahun = ubahtahun(tahun_str)

            # Input kategori
            # input user berupa ">" , "<" , "=" , "<=" , ">="
            kategori = (input("Masukkan kategori : "))
            kategori = ubahkategori(kategori)

            # Menampilkan data
            print("\nHasil pencarian :")
            if (kategori == ">"):
                for data in range(1, len(array_data)):
                    if (int(array_data[data][5]) > tahun):
                        printdata(array_data[data])
            elif (kategori == "="):
                for data in range(1, len(array_data)):
                    if (int(array_data[data][5]) == tahun):
                        printdata(array_data[data])
            elif (kategori == "<"):
                for data in range(1, len(array_data)):
                    if (int(array_data[data][5]) < tahun):
                        printdata(array_data[data])
            elif (kategori == ">="):
                for data in range(1, len(array_data)):
                    if (int(array_data[data][5]) >= tahun):
                        printdata(array_data[data])
            elif (kategori == "<="):
                for data in range(1, len(array_data)):
                    if (int(array_data[data][5]) <= tahun):
                        printdata(array_data[data])
        else:
            # Tidak terdapat gadget pada file gadget.csv
            print("(;_;) : Tidak ada data pada gadget.csv, maafkan admin!")
    else:
        # Pengguna belum login
        print("(+.+) : Anda belum login.")
    return database
