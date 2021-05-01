"""Program F12 - Melihat Riwayat Pengembalian Gadget
Fungsi ini akan menampilkan riwayat pengembalian gadget berisi data
ID Pengambil, Nama Pengambil, Nama Gadget, dan Tanggal Pengambilan.
Kemudian fungsi menampilkan riwayat pengembalian yang terurut menurun
dari yang paling terbaru.  Fungsi menampilkan tiap lima entri sekali.

Akses : Admin
"""

# KAMUS
# Daftar library standar
import datetime

# Daftar library lokal
from login import cek_active_account
from riwayatpinjam import sortMaxMinTanggal, nama_user_id, nama_gadget_id
from constant import user, gadget, gadget_borrow_history, \
    gadget_return_history, active_account

# Daftar konstanta
# user : int
# gadget : int
# gadget_borrow_history : int
# gadget_return_history : int
# active_account : int

# Daftar variabel
# databases : array of array of array
# isLoggedIn : bool
# username, role, : str
# db_gadget, db_kembali, db_pinjam : array of array
# db_user, sorted_db_kembali : array of array
# list_tampilan : array of array

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur


def print_baris(row):
    """Prosedur ini akan menampilkan entri pada array sesuai dengan
    tampilan berupa:
    ID Pengambilan      :
    Nama Pengambil      :
    Nama Gadget         :
    Tanggal Pengembalian:
    """

    # KAMUS LOKAL
    # row : array of str and int

    # ALGORITMA
    print("ID Pengambilan      :", row[0])
    print("Nama Pengambil      :", row[1])
    print("Nama Gadget         :", row[2])
    print("Tanggal Pengembalian:", row[3])


def tampilan(list_tampilan, username):
    """Prosedur ini akan membaca array of array berisi entri yang
    akan ditampilkan per lima baris dan akan dilanjutkan sesuai
    keinginan pengguna.
    """

    # KAMUS LOKAL
    # list_tampilan : array of array
    # username, lanjut : str

    # ALGORITMA
    # Menampilkan sebanyak entri pada array tampilan
    for i in range(len(list_tampilan)):
        print_baris(list_tampilan[i])

        # Menampilkan baris kosong sebagai pemisah antar entri
        if i != len(list_tampilan) - 1:
            print()

        # Setelah menampilkan lima entri, pengguna memilih lanjut atau tidak
        if (i + 1) % 5 == 0 and i != len(list_tampilan) - 1:
            # Memvalidasi input dari pengguna
            while True:
                lanjut = input(
                    "^( '-' )^ : Apakah "
                    + username
                    + " mau melihat riwayat berikutnya? (Y/N) ")

                # Input valid, salah satu huruf Y/y/N/n
                if lanjut in "YyNn" and len(lanjut) == 1:
                    break
                # Input tidak valid, pengisian diulang
                print("\n(>‘o’)> : Input tidak sesuai. Ulangi!\n")

            # Tidak melanjutkan penampilan entri berikutnya, terminasi loop
            if lanjut in "Nn":
                break
            # Melanjutkan penampilan lima entri berikutnya
            elif lanjut in "Yy":
                print()


def buat_list_tampilan(kembali, pinjam, user, gadget):
    """Fungsi ini akan menerima input array berisi entri pengembalian,
    peminjaman, user, dan gadget.  Kemudian fungsi mengembalikan
    sebuah array berisi entri ID Pengambilan, Nama Pengambil, Nama
    Gadget, dan Tanggal Pengembalian yang sesuai pada tiap
    entri pengembalian.
    """

    # KAMUS LOKAL
    # kembali, pinjam, user, gadget, kembali_copy : array of array
    # row_copy : array of str and int
    # id_pengambilan, id_peminjam : int
    # nama_pengambil, id_gadget, nama_gadget, tanggal_pengembalian : str

    # ALGORITMA
    # inisialisasi array kosong
    kembali_copy = []

    # Mencari data yang sesuai untuk tiap array pada riwayat pengembalian
    for row in kembali:
        id_pengambilan = row[1]
        id_peminjam = pinjam[id_pengambilan][1]
        nama_pengambil = nama_user_id(user, id_peminjam)
        id_gadget = pinjam[id_pengambilan][2]
        nama_gadget = nama_gadget_id(gadget, id_gadget)
        tanggal_pengembalian = row[2]

        # Membuat array baru dengan data yang sesuai untuk satu peminjaman
        row_copy = [id_pengambilan, nama_pengambil,
                    nama_gadget, tanggal_pengembalian]

        # Mengumpulkan array dengan data yang sesuai dari tiap peminjaman
        kembali_copy.append(row_copy)

    # Mengembalikan array of array dengan entri yang akan ditampilkan
    return kembali_copy


# ALGORITMA PROGRAM UTAMA
def riwayatkembali(databases):
    # Memvalidasi pengguna sudah login
    isLoggedIn = cek_active_account(databases)
    if not isLoggedIn:
        # Pengguna belum login, terminate prosedur riwayatkembali
        print("^.^ : Silahkan login terlebih dahulu.")
        return databases

    # Pengguna sudah login, mendapatkan data terkait pengguna
    username = databases[active_account][1]
    role = databases[active_account][5]

    # Memvalidasi role pengguna
    if role != "Admin":
        # Role pengguna bukan admin, terminate prosedur riwayatkembali
        print(
            "=^.^= : Role "
            + username
            + " bukan Admin, silahkan login akun Admin.")
        return databases

    # Role pengguna adalah admin, jalankan prosedur riwayatkembali
    # Membuat array untuk tiap data yang dibutuhkan
    db_kembali = databases[gadget_return_history][1:]
    db_pinjam = databases[gadget_borrow_history]
    db_gadget = databases[gadget]
    db_user = databases[user]
    
    # Menangani kasus tidak ada entri riwayat kembali
    if len(db_kembali)==0:
        print("(O.o)? : Tidak ada riwayat pengembalian gadget!")
        return databases
    
    # Mengurutkan entri pengembalian menurun berdasarkan tanggal
    sorted_db_kembali = sortMaxMinTanggal(db_kembali, 2)
    
    # Mencari data yang sesuai dan membuat array baru untuk ditampilkan
    list_tampilan = buat_list_tampilan(sorted_db_kembali, db_pinjam,
                                       db_user, db_gadget)

    # Menampilkan entri yang sesuai dengan tampilan yang rapih
    tampilan(list_tampilan, username)

    # Mengembalikan databases yang sudah digunakan
    return databases
