"""
Program F02 - Login
Untuk mengakses Inventarisasi Doremonangis, pengguna harus login terlebih dahulu.
Apabila pengguna memasukkan username dan password yang telah terdaftar,
maka pengguna berhasil login.
"""

# KAMUS
# Daftar library lokal
from constant import user, active_account

# Variabel dan konstanta
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
        username = input("Ketik username: ")
        password = input("Ketik password: ")

        # list dari user.csv
        file = databases[user]

        # Inisialisasi awal untuk mencari username
        find_username = False
        find_password = False

        for row in file:                     # Mencari username dan password dari databases
            if row[1] == username:           # username ditemukan, lanjutkan program
                find_username = True
                if row[4] == password:       # password ditemukan, lanjutkan program
                    find_password = True
                    break
                else:
                    find_password = False    # password tidak cocok dengan database
                    break
            else:
                find_username = False        # username tidak terdapat dalam database

        # username dan password cocok dengan database
        if find_username and find_password:
            # tambahkan data login ke acctive_account
            databases[active_account] = row
            
            # Beritahu pengguna bahwa telah berhasil login
            print()
            print("(=^.^=): Selamat, " + str(username) + " berhasil login!")
        
        # username tidak terdapat dalam databases
        elif find_username == False:
            # Beritahu pengguna bahwa username tidak ditemukan dan gagal login
            print()
            print("('_'): Maaf, kamu belum berhasil login! Username kamu tidak ditemukan.")

        else: # find_password == False
            # Beritahu pengguna bahwa masukan password salah
            print()
            print("('_'): Maaf, kamu belum berhasil login! Password kamu salah.")

    else: # isLoggedIn
        # Membaca username dari active_account
        username = databases[active_account][1]
        
        # Beritahu pengguna mengenai akun yang sedang aktif
        print("\(>.<)/: Saat ini kamu sedang login sebagai " + username + ".")
        
        # Minta pengguna untuk melakukan exit terlebih dahulu apabila ingin menggunakan akun lain
        print("\(>.<)/: Silakan exit terlebih dahulu apabila ingin login dengan akun lain.")
        return databases

    return databases
