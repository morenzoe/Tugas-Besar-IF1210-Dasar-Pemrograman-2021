"""
Program F13 - Melihat Riwayat Pengambilan Consumable
Hanya dapat diakses oleh admin.
Digunakan oleh Admin sebagai bantuan untuk melihat riwayat pengambilan consumable.
Data bisa dibaca dari file yang tersedia. Bila terdapat lebih dari 5 entry, keluarkan
5 entry paling baru, dan pengguna dapat mengeluarkan 5 entry tambahan bila diinginkan.
Harus sorted descending berdasarkan tanggal
"""

# KAMUS
# Daftar library standar
import datetime

# Daftar library lokal
from riwayatpinjam import sortMaxMinTanggal
from login import cek_active_account
from constant import gadget, user, consumable_history, active_account, consumable
from carirarity import check_file_tidak_kosong

# Variabel dan konstanta
# isLoggedIn            : boolean
# sorted_history        : array of array
# db_consumeable        : array of array
# db_user               : array of array
# username              : string
# awal                  : integer
# akhir                 : integer
# repeat                : string
# nama_user             : string
# nama_consumeable      : string


def nama_user_id(database, id):
    # Menghasilkan nama dari user dari id tersebut

    # ALGORITMA
    return database[id][2]


def nama_consumeable_id(database, id):
    # Menghasilkan nama dari consumable dengan id tersebut

    # ALGORITMA
    for data in range(1, len(database)):
        if id == database[data][0]:
            return database[data][1]


def printdata(nama_user, nama_consumeable, database):
    # Mengoutput data yang bersangkutan

    # ALGORITMA
    print("\nID Peminjaman       : ", database[0])
    print("Nama Pengambil      : ", nama_user)
    print("Nama consumeable    : ", nama_consumeable)
    print("Tanggal Pengambilan : ", database[3])
    print("Jumlah              : ", database[4])


def riwayatambil(databases):
    # Menampilkan data pada "consumeable_borrow_history.csv" secara berurutan
    # berdasarkan tanggal
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        # Pengguna sudah login
        if databases[active_account][5] != "Admin":
            # Pengguna bukan admin
            print(
                "(;-;) : Maafkan saya",
                databases[active_account][2] + "-san",
                "saya tidak dapat mengizinkan anda menggunakan command ini (anda bukan Admin).")
        else:
            # Pengguna adalah admin
            if check_file_tidak_kosong(databases[consumable_history]):
                # Terdapat data pada file consumable_history.csv

                sorted_history = sortMaxMinTanggal(
                    databases[consumable_history][1:], 3)
                db_consumeable = databases[consumable]
                db_user = databases[user]
                username = databases[active_account][1]
                awal = 0
                akhir = 5
                repeat = "y"

                # Mulai Output
                print("(^.^)/ : Berikut adalah data riwayat pengambilan consumeable: ")
                while (repeat == "Y") or (repeat == "y"):
                    if akhir < len(sorted_history):
                        # Jika data yang tersisa lebih dari 5
                        for data in range(awal, akhir):
                            nama_user = nama_user_id(
                                db_user, sorted_history[data][1])
                            nama_consumeable = nama_consumeable_id(
                                db_consumeable, sorted_history[data][2])
                            printdata(
                                nama_user, nama_consumeable, sorted_history[data])
                        awal = akhir
                        akhir += 5
                        repeat = input(
                            "('.') : Apakah anda ingin melihat halaman selanjutnya? (Y/N): ")
                        while (not (repeat in "YyNn") or len(repeat) != 1):
                            repeat = input(
                                "(-.-') : Input salah mohon. Masukkan input yang benar. (Y/N): ")
                    elif akhir >= len(sorted_history):
                        # Jika data yang tersisa kurang dari sama dengan 5
                        for data in range(awal, len(sorted_history)):
                            nama_user = nama_user_id(
                                db_user, sorted_history[data][1])
                            nama_consumeable = nama_consumeable_id(
                                db_consumeable, sorted_history[data][2])
                            printdata(
                                nama_user, nama_consumeable, sorted_history[data])
                        repeat = "N"
            else:
                # Tidak terdapat data pada file consumable_history
                print("(;_;) : Tidak ada data pada gadget.csv, maafkan admin!")
    else:
        # Pengguna belum login
        print("(=_=) : Anda belum login.")
    return databases
