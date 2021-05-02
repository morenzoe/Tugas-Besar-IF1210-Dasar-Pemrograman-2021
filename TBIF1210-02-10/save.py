"""Program F15 - Save Data
Fungsi ini akan  menyimpan tiap array di dalam array yang diterima
sebagai file dengan ekstensi .csv yang dipisahkan semicolon.
Fungsi akan meminta input nama folder sebagai lokasi penyimpanan.
data
Akses : Admin, User
"""

# KAMUS
# Daftar library standar
import os

# Daftar library lokal
from login import cek_active_account
from cek_csv import cek_folder, get_cwd_folder_name, cek_file_csv
from carirarity import tahun_int_to_str
from constant import user, gadget, consumable, consumable_history, \
    gadget_borrow_history, gadget_return_history, \
    active_account, nama_csv

# Daftar konstanta
# user, gadget, consumable, consumable_history, gadget_borrow_history : int
# gadget_return_history, active_account : int
# nama_csv : array of str
# karakter_eror : array of str

# Daftar variabel
# databases : array of array of array
# folder_save, folder_path, workspace, csv : str
# isValid : bool

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def to_str(array_word_int):
    """Fungsi ini membaca array dan merubah tipe data semua elemen menjadi
    tipe data string.  Kemudian fungsi mengembalikan array of string tersebut.
    """

    # KAMUS LOKAL
    # array_word_int : array of str and int
    # array_word : array of str

    # ALGORITMA
    array_word = [str(word) for word in array_word_int]
    return array_word


def array_word_to_row(array_word):
    """Fungsi ini membaca array of string dan menggabungkan semua elemen
    dengan pemisah semicolon menjadi satu kalimat.  Kemudian fungsi
    mengembalikan string tersebut.
    """

    # KAMUS LOKAL
    # array_word : array of str
    # row : str

    # ALGORITMA
    row = ";".join(array_word) + "\n"
    return row


def array_to_csv(csv, folder_path, database):
    """Prosedur ini menerima nama file dengan ekstensi .csv, directory
    penyimpanan, dan array of array yang akan disimpan.  Prosedur
    menulis tiap array sebagai satu baris dalam file.
    """

    # KAMUS LOKAL
    # database : array of array
    # save_csv : array of str
    # array_word : array of array of str
    # row, csv, csv_path, folder_path : str
    # f : file

    # ALGORITMA
    # Inisialisasi variabel array yang akan disimpan
    save_csv = []

    # Gabungkan semua array dalam database
    for array_word_int in database:
        # Melengkapi format tahun YYYY untuk data gadget
        if csv == "gadget.csv":
            # Konversi hanya untuk baris dengan tipe data integer
            if isinstance(array_word_int[5], int):
                array_word_int[5] = tahun_int_to_str(array_word_int[5])

        # Mengubah isi array menjadi string dan menggabungkan semuanya
        array_word = to_str(array_word_int)

        # Menggabungkan tiap baris menjadi satu string
        row = ";".join(array_word) + "\n"
        save_csv.append(row)

    # Membuat path directory penyimpanan
    csv_path = os.path.join(folder_path, csv)

    # Menulis semua entri pada array save_csv
    f = open(csv_path, "w")
    for row in save_csv:
        f.write(row)
    f.close()


def validasi_folder(folder_save):

    # Inisialisasi validasi nama folder
    karakter_eror = ['\\', '/', ':', '*', '&', '?', '"', '<', '>', '|']

    # Memvalidasi input nama folder
    if len(folder_save) == 0:
        print("\nm/(>.<)\\m : Nama folder tidak boleh kosong!")
        return False
    elif any(item in folder_save for item in karakter_eror):
        print("\nm/(>.<)\\m : Nama folder tidak boleh mengandung karakter "
              + 'sebagai berikut: \\ / : * & ? " < > |')
        return False
    else:
        return True

# ALGORITMA PROGRAM UTAMA
def save(databases):
    # Memvalidasi pengguna sudah login
    isLoggedIn = cek_active_account(databases)
    if not isLoggedIn:
        # Pengguna belum login, terminate prosedur riwayatkembali
        print("(^.^) : Silahkan login terlebih dahulu.")
        return databases

    # Pengguna sudah login, mendapatkan data terkait pengguna
    username = databases[active_account][1]
    role = databases[active_account][5]

    # Memvalidasi role pengguna
    if role != "Admin" and role != "User":
        # Role pengguna bukan admin atau user, terminate prosedur save
        print(
            "=(^.^)= : Role "
            + username
            + " bukan Admin atau User, silahkan login akun Admin atau "
            + "User.")
        return databases

    # Role pengguna adalah admin atau user, jalankan prosedur save
    # Memvalidasi input nama folder
    while True:
        # Meminta nama folder untuk penyimpanan data
        folder_save = input("(~ ^v^)~ : Masukkan nama folder penyimpanan : ")

        # Memvalidasi nama folder
        isValid = validasi_folder(folder_save)

        if isValid:
            break

        while True:
            lanjut = input("\n(^-^) : Apakah "
                           + username
                           + " ingin melanjutkan penyimpanan? (Y/N) ")

            # Input valid, salah satu huruf Y/y/N/n
            if lanjut in "Yy" and len(lanjut) == 1:
                print()
                break
            elif lanjut in "Nn" and len(lanjut) == 1:
                return databases
            # Input tidak valid, pengisian diulang
            else:
                print("\nm(><)m : Input tidak sesuai. Ulangi! \n")

    # Mendapatkan nama folder workspace
    folder_workspace, cwd = get_cwd_folder_name()

    # Memeriksa memeriksa kelengkapan file csv dalam folder workspace
    if folder_save == folder_workspace:
        csv_found = cek_file_csv(cwd)
        if csv_found:
            folder_path = cwd

    else:
        # Memeriksa ada tidaknya folder tersebut dalam workspace
        folder_path, workspace = cek_folder(folder_save)

        # Folder tidak ada, membuat folder baru dengan nama sesuai input
        if folder_path == 'folder tidak ada':
            folder_path = os.path.join(workspace, folder_save)
            try:
                os.makedirs(folder_path)
            except OSError:
                print("\n(╥_╥) : Data tidak berhasil disimpan, terjadi eror "
                      + "terkait sistem.")
                return databases

    # Folder ada, simpan semua data dalam file berekstensi .csv
    print("\n( o _o) : Saving...")
    for i in range(len(databases) - 1):
        csv = nama_csv[i]
        array_to_csv(csv, folder_path, databases[i])

    # Penyimpanan selesai, menampilkan pesan konfirmasi
    print("\n( >_<)b : Data telah disimpan di folder", folder_save + "!")
    return databases
