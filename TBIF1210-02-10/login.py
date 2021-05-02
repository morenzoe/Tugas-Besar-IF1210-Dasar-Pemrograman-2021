"""Program F02 - Login
Untuk mengakses Inventarisasi Doremonangis, pengguna harus login terlebih
dahulu. Apabila pengguna memasukkan username dan password yang telah
terdaftar, maka pengguna berhasil login.
"""

# KAMUS
# Daftar library lokal
from constant import user, active_account

# Daftar konstanta
# user          : int
# active_account: int

# Daftar variabel
# databases    : array of array of array
# isLoggedIn   : bool
# username     : str
# password     : str
# file         : array of array
# find_username: bool
# find_password: bool


def cek_active_account(databases):
    # KAMUS LOKAL
    # jumlah_data : int

    # ALGORITMA
    # Membaca apakah active_account berisi atau tidak
    jumlah_data = len(databases[active_account])
    if jumlah_data != 0:
        return True
    else:
        return False


# ALGORITMA PROGRAM UTAMA
def login(databases):
    # Validasi login pengguna
    isLoggedIn = cek_active_account(databases)
    if not isLoggedIn:
        # Pengguna belum login, input username dan password
        username = input("Ketik username : ")
        password = input("Ketik password : ")

        # List dari user.csv
        file = databases[user]

        # Inisialisasi awal untuk mencari username
        find_username = False
        find_password = False

        # Mencari username dan password dari databases
        for row in file:
            if row[1] == username:
                # username ditemukan, lanjutkan program
                find_username = True
                if row[4] == password:
                    # password ditemukan, lanjutkan program
                    find_password = True
                    break
                else:
                    # password tidak cocok dengan database
                    find_password = False
                    break
            else:
                # username tidak terdapat dalam database
                find_username = False

        # username dan password cocok dengan database
        if find_username and find_password:
            # Tambahkan data login ke acctive_account
            databases[active_account] = row

            # Beritahu pengguna bahwa telah berhasil login
            print(
                "\n(=^.^=) : Selamat, "
                + username
                + " berhasil login!")

        # username tidak terdapat dalam databases
        elif find_username == False:
            # Beritahu pengguna bahwa username tidak ditemukan dan gagal login
            print(
                "\n('_') : Maaf, kamu belum berhasil login! Username kamu tidak ditemukan.")

        else:  # find_password == False
            # Beritahu pengguna bahwa masukan password salah
            print("\n('_') : Maaf, kamu belum berhasil login! Password kamu salah.")

    else:  # isLoggedIn
        # Membaca username dari active_account
        username = databases[active_account][1]

        # Beritahu pengguna mengenai akun yang sedang aktif
        print(
            "\n\\(>.<)/ : Saat ini kamu sedang login sebagai "
            + username
            + ".")

        # Minta pengguna untuk melakukan exit terlebih dahulu apabila ingin
        # menggunakan akun lain
        print(
            "\n\\(>.<)/ : Silakan exit terlebih dahulu apabila ingin login dengan akun lain.")
        return databases

    return databases
