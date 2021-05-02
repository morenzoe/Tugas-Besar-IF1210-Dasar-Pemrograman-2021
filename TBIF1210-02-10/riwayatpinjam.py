"""
Program F11 - Melihat Riwayat Peminjaman Gadget
Hanya dapat diakses oleh admin.
Digunakan oleh Admin sebagai bantuan untuk melihat riwayat peminjaman gadget.
Data bisa dibaca dari file yang tersedia. Bila terdapat lebih dari 5 entry, keluarkan
5 entry paling baru, dan pengguna dapat mengeluarkan 5 entry tambahan bila diinginkan.
Harus sorted descending berdasarkan tanggal
"""

# KAMUS
# Daftar library standar
import datetime

# Daftar library lokal
from constant import user, gadget, active_account, gadget_borrow_history
from login import cek_active_account
from carirarity import check_file_tidak_kosong
# Variabel dan konstanta
# isLoggedIn            : string
# sorted_history        : array of array
# db_gadget             : array of array
# db_user               : array of array
# username              : string
# awal                  : integer
# akhir                 : integer
# repeat                : string
# nama_user             : string
# nama_gadget           : string


def sortMaxMinTanggal(array, idx_tanggal):
    # mengurutkan array dari tanggal terbesar menuju tanggal terkecil

    # KAMUS LOKAL
    # pjg               : integer
    # imax              : integer
    # Pass              : integer

    # ALGORITMA
    pjg = len(array)
    if pjg > 1:
        # Panjang array >= 2
        for Pass in range(pjg - 1):
            imax = Pass
            for i in range(Pass, pjg):
                x = datetime.datetime.strptime(
                    array[imax][idx_tanggal], "%d/%m/%Y")
                y = datetime.datetime.strptime(
                    array[i][idx_tanggal], "%d/%m/%Y")
                if (x < y):
                    imax = i
            # Pertukaran terjadi
            array[imax], array[Pass] = array[Pass], array[imax]
    return array


def nama_user_id(database, id):
    # menghasilkan nama dari user dari id tersebut

    # ALGORITMA
    return database[id][2]


def nama_gadget_id(database, id):
    # menghasilkan nama gadget dari id tersebut

    # ALGORITMA
    for data in range(1, len(database)):
        if id == database[data][0]:
            return database[data][1]


def printdata(nama_user, nama_gadget, database):
    # mengoutput data yang bersangkutan

    # Algoritma
    print("\nID Peminjaman      : ", database[0])
    print("Nama Pengambil     : ", nama_user)
    print("Nama Gadget        : ", nama_gadget)
    print("Tanggal Peminjaman : ", database[3])
    print("Jumlah             : ", database[4])


def riwayatpinjam(databases):
    # menampilkan data pada "gadget_borrow_history.csv" secara berurutan
    # berdasarkan tanggal
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        # Pengguna sudah login
        if databases[active_account][5] != "Admin":
            # Pengguna bukan Admin
            print(
                "(;-;) : Maafkan saya",
                databases[active_account][1] + "-san",
                "Anda bukan Admin).")
        else:
            # Pengguna adalah Admin
            if check_file_tidak_kosong(databases[gadget_borrow_history]):
                sorted_history = sortMaxMinTanggal(
                    databases[gadget_borrow_history][1:], 3)
                db_gadget = databases[gadget]
                db_user = databases[user]
                username = databases[active_account][1]
                awal = 0
                akhir = 5
                repeat = "y"

                # Mulai Output
                print("(^.^)/ : Di bawah ini adalah data riwayat peminjaman gadget!")
                while (repeat == "Y") or (repeat == "y"):
                    if akhir < len(sorted_history):
                        # Jika data yang tersisa lebih dari 5
                        for data in range(awal, akhir):
                            nama_user = nama_user_id(
                                db_user, sorted_history[data][1])
                            nama_gadget = nama_gadget_id(
                                db_gadget, sorted_history[data][2])
                            printdata(nama_user, nama_gadget,
                                      sorted_history[data])
                        awal = akhir
                        akhir += 5
                        repeat = input(
                            "\n(^.^) : Apakah anda ingin melihat halaman selanjutnya? (Y/N): ")
                        while (not (repeat in "YyNn") or len(repeat) != 1):
                            repeat = input(
                                "\n(-.-') : Input salah mohon. Masukkan input yang benar. (Y/N): ")

                    elif akhir >= len(sorted_history):
                        # Jika data yang tersisa kurang dari sama dengan 5
                        for data in range(awal, len(sorted_history)):
                            nama_user = nama_user_id(
                                db_user, sorted_history[data][1])
                            nama_gadget = nama_gadget_id(
                                db_gadget, sorted_history[data][2])
                            printdata(nama_user, nama_gadget,
                                      sorted_history[data])
                        repeat = "N"
            else:
                # Jika tidak terdapat data pada gadget_borrow_history.csv
                print("(;_;) : Tidak terdapat data pada gadget_borrow_history.csv.")
    else:
        # Pengguna belum login
        print("(0_0): Anda belum login.")
    return databases
