"""Program F01 - Register
Untuk menambahkan data pengguna pada file User.csv, pengguna dapat melakukan register.
Register hanya dapat diakses oleh Admin.

Akses : Admin
"""

# KAMUS
# Daftar library lokal
from constant import user, active_account
from login import cek_active_account

# Variabel dan konstanta
# isLoggedIn        : boolean
# check_role        : string
# data              : array of array
# Id                : string
# username          : string
# nama              : string
# alamat            : string
# password          : string
# role              : string
# new_data          : array of string


def check_username(username, data):
    # Mengecek apakah username input sudah ada atau belum pada data

    # KAMUS LOKAL
    # data          : array of array
    # username      : string
    # check         : integer

    # ALGORITMA
    check = 0
    for i in range(len(data)):
        if (data[i][1] == username):
            check = 1
    if (check == 0):
        return False
    else:  # check = 1
        return True


def checkdelimit(check):
    # Mengecek apakah dalam input pengguna terdapat ;.

    # KAMUS LOKAL
    # check            : string { yang ingin dicek }

    # ALGORITMA
    if ";" in check:
        return True
    else:
        return False


def register(databases):
    # Me-register akun pengguna
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        # Pengguna sudah login.
        check_role = databases[active_account][5]
        if check_role == "Admin":
            # Pengguna adalah Admin.
            data = databases[user][1:]

            # Memulai penginputan
            print("\\(>_<)/ : Dilarang menggunakan karakter ; dalam penginputan!\n")

            # Input nama
            nama = input("Masukkan nama     : ")
            if checkdelimit(nama) or nama == "":
                print("\n(*.*) : Kesalahan input, terminasi fungsi.")
                return databases
            nama = nama.title()

            # Input username
            username = input("Masukkan username : ")
            if checkdelimit(username) or check_username(username, data) or username == "":
                print("\n(*.*) : Kesalahan input, terminasi fungsi.")
                return databases

            # Input password
            password = input("Masukkan password : ")
            if checkdelimit(password) or password == "":
                print("\n(*.*) : Kesalahan input, terminasi fungsi.")
                return databases

            # Input alamat
            alamat = input("Masukkan alamat   : ")
            if checkdelimit(alamat) or alamat == "":
                print("\n(*.*) : Kesalahan input, terminasi fungsi.")
                return databases

            # Penetapan Id dan role secara otomatis dari sistem
            Id = str(len(data) + 1)
            role = "User"

            # Menggabungkan data menjadi array baru dan menggabungkannya dengan
            # databases
            new_data = [Id, username, nama, alamat, password, role]
            databases[user].append(new_data)
            print("\n\\('3')/ : User", username,
                  "telah berhasil register ke dalam Kantong Ajaib.")
        else:
            # Pengguna bukan Admin
            print(
                "(Q.Q) : Maafkan saya",
                databases[6][1] +
                "-san, anda bukan Admin.")
    else:
        # Pengguna belum login
        print("\n<('.')> : Maaf, anda belum login.")
    return databases
# python kantongajaib.py CSVs
