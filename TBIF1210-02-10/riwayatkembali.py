"""Program F12 - Melihat Riwayat Pengembalian Gadget
Fungsi ini akan menampilkan riwayat pengembalian gadget berisi data
ID Pengambil, Nama Pengambil, Nama Gadget, dan Tanggal Pengambilan.
Kemudian fungsi menampilkan riwayat pengembalian yang terurut menurun
dari yang paling terbaru.  Fungsi menampilkan tiap lima data sekali.

Akses : Admin
"""

# KAMUS
# Standard library imports
import datetime

# Local library imports
from constant import user, gadget, gadget_borrow_history, \
    gadget_return_history, active_account
from login import cek_active_account
from riwayatpinjam import sortMaxMinTanggal, nama_user_id, nama_gadget_id

# Variable
# isLoggedIn : bool
# username, role, : str
# db_gadget, db_kembali, db_pinjam : list of list
# db_user, sorted_db_kembali : list of list
# list_tampilan : list of list


def print_baris(row):
    """Prosedur ini akan menampilkan data pada list sesuai dengan
    tampilan berupa:
    ID Pengambilan      :
    Nama Pengambil      :
    Nama Gadget         :
    Tanggal Pengembalian:
    """

    # KAMUS LOKAL
    # -

    # ALGORITMA
    print("ID Pengambilan      :", row[0])
    print("Nama Pengambil      :", row[1])
    print("Nama Gadget         :", row[2])
    print("Tanggal Pengembalian:", row[3])


def tampilan(list_tampilan, username):
    """Prosedur ini akan membaca list of list berisi data yang
    akan ditampilkan per lima baris dan akan dilanjutkan sesuai
    keinginan user.
    """

    # KAMUS LOKAL
    # lanjut : str

    # ALGORITMA
    # Menampilkan sebanyak data pada list tampilan
    for i in range(len(list_tampilan)):
        print_baris(list_tampilan[i])

        # Menampilkan baris kosong sebagai pemisah antar data
        if i != len(list_tampilan) - 1:
            print()

        # Setelah menampilkan lima data, user memilih lanjut atau tidak
        if (i + 1) % 5 == 0 and i != len(list_tampilan) - 1:
            # Validasi input dari user
            while True:
                lanjut = input(
                    "^( '-' )^ : Apakah " +
                    username +
                    " mau melihat riwayat berikutnya? (Y/N) ")

                # Input valid, salah satu huruf Y/y/N/n
                if lanjut in "YyNn" and len(lanjut) == 1:
                    break
                # Input tidak valid, pengisian diulang
                elif lanjut not in "YyNn" or len(lanjut) != 1:
                    print("(>‘o’)> : Input tidak sesuai. Ulangi!")
                    print()

            # Tidak melanjutkan penampilan data berikutnya, terminasi loop
            if lanjut in "Nn":
                break
            # Melanjutkan penampilan lima data berikutnya
            elif lanjut in "Yy":
                print()


def buat_list_tampilan(kembali, pinjam, user, gadget):
    """Fungsi ini akan menerima input list berisi data pengembalian,
    peminjaman, user, dan gadget.  Kemudian fungsi mengembalikan
    sebuah list berisi data ID Pengambilan, Nama Pengambil, Nama
    Gadget, dan Tanggal Pengembalian yang sesuai pada tiap
    data pengembalian.
    """

    # KAMUS LOKAL
    # kembali_copy : list of list
    # row_copy : list of string and int
    # id_pengambilan, id_peminjam : int
    # nama_pengambil, id_gadget, nama_gadget, tanggal_pengembalian : str

    # ALGORITMA
    # inisialisasi list kosong
    kembali_copy = []

    # mencari data yang sesuai untuk tiap list pada riwayat pengembalian
    for row in kembali:
        id_pengambilan = row[1]
        id_peminjam = pinjam[id_pengambilan][1]
        nama_pengambil = nama_user_id(user, id_peminjam)
        id_gadget = pinjam[id_pengambilan][2]
        nama_gadget = nama_gadget_id(gadget, id_gadget)
        tanggal_pengembalian = row[2]

        # membuat list baru dengan data yang sesuai untuk satu peminjaman
        row_copy = [id_pengambilan, nama_pengambil,
                    nama_gadget, tanggal_pengembalian]

        # mengumpulkan list dengan data yang sesuai dari tiap peminjaman
        kembali_copy.append(row_copy)

    # mengembalikan list of list dengan data yang akan ditampilkan
    return kembali_copy


# ALGORITMA PROGRAM UTAMA
def riwayatkembali(databases):
    # Validasi user sudah login
    isLoggedIn = cek_active_account(databases)

    # User sudah login, validasi role
    if isLoggedIn:
        # Mendapatkan data terkait user
        username = databases[active_account][1]
        role = databases[active_account][5]

        # Role user adalah admin, jalankan prosedur riwayatkembali
        if role == "Admin":
            # Membuat list untuk tiap data yang dibutuhkan
            db_kembali = databases[gadget_return_history][1:]
            db_pinjam = databases[gadget_borrow_history]
            db_gadget = databases[gadget]
            db_user = databases[user]

            # Mengurutkan data pengembalian menurun berdasarkan tanggal
            sorted_db_kembali = sortMaxMinTanggal(db_kembali, 2)

            # Mencari data yang sesuai dan membuat list baru untuk ditampilkan
            list_tampilan = buat_list_tampilan(sorted_db_kembali, db_pinjam,
                                               db_user, db_gadget)

            # Menampilkan data yang sesuai dengan tampilan yang rapih
            tampilan(list_tampilan, username)

            # Mengembalikan databases yang sudah digunakan
            return databases

        # Role user bukan admin, terminate prosedur riwayatkembali
        else:
            print(
                "=^.^= : Role " +
                username +
                " bukan Admin, silahkan login akun Admin.")
            return databases
    # User belum login, terminate prosedur riwayatkembali
    else:
        print("^.^ : Silahkan login terlebih dahulu.")
        return databases
