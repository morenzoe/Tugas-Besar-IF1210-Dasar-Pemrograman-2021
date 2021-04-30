"""Program F15 - Save Data
Fungsi ini akan  menyimpan tiap list di dalam list yang diterima
sebagai file dengan ekstensi .csv yang dipisahkan semicolon.
Fungsi akan meminta input nama folder sebagai lokasi penyimpanan.

Akses : Admin, User
"""

# KAMUS
# Daftar library standar
import os

# Daftar library lokal
from login import cek_active_account
from cek_csv import cek_folder
from constant import user, gadget, consumable, consumable_history, \
    gadget_borrow_history, gadget_return_history, \
    active_account, nama_csv

# Daftar konstanta
# user : int
# gadget : int
# consumable : int
# consumable_history : int
# gadget_borrow_history : int
# gadget_return_history : int
# active_account : int
# nama_csv : list of str
# karakter_eror : list of str

# Daftar variabel
# folder_save, folder_path, workspace, csv : str
# isValid : bool


def to_str(array_word_int):
    """Fungsi ini membaca list dan merubah tipe data semua elemen menjadi
    tipe data string.  Kemudian fungsi mengembalikan list of string tersebut.
    """

    # KAMUS LOKAL
    # Variabel
    # array_word : list of str

    # ALGORITMA
    array_word = [str(word) for word in array_word_int]
    return array_word


def array_word_to_row(array_word):
    """Fungsi ini membaca list of string dan menggabungkan semua elemen
    dengan pemisah semicolon menjadi satu kalimat.  Kemudian fungsi
    mengembalikan string tersebut.
    """

    # KAMUS LOKAL
    # row : str

    # ALGORITMA
    row = ";".join(array_word) + "\n"
    return row


def array_to_csv(csv, folder_path, database):
    """Prosedur menerima nama file dengan ekstensi .csv, directory
    penyimpanan, dan list of list yang akan disimpan.  Prosedur
    menulis tiap list sebagai satu baris dalam file.
    """

    # KAMUS LOKAL
    # save_csv : list of str
    # array_word : list of list of str
    # row, csv_path : str
    # f : file

    # ALGORITMA
    save_csv = []
    for array_word_int in database:
        array_word = to_str(array_word_int)
        row = ";".join(array_word) + "\n"
        save_csv.append(row)
    csv_path = os.path.join(folder_path, csv)
    f = open(csv_path, "w")
    for row in save_csv:
        f.write(row)
    f.close()

# ALGORITMA PROGRAM UTAMA


def save(databases):
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
    if role != "Admin" and role != "User":
        # Role pengguna bukan admin atau user, terminate prosedur save
        print(
            "=^.^= : Role "
            + username
            + " bukan Admin atau User, silahkan login akun Admin atau "
            + "User.")
        return databases

    # Role pengguna adalah admin atau user, jalankan prosedur save
    karakter_eror = ['\\', '/', ':', '*', '&', '?', '"', '<', '>', '|']
    isValid = True

    # Meminta nama folder untuk penyimpanan data
    folder_save = input("(~ ^v^)~ : Masukkan nama folder penyimpanan: ")

    # Memvalidasi input nama folder
    if len(folder_save) == 0:
        print("\nm/(>.<)\\m : nama folder tidak boleh kosong!")
        isValid = False
    elif any(item in folder_save for item in karakter_eror):
        print("\nm/(>.<)\\m : nama folder tidak boleh mengandung karakter "
              + 'sebagai berikut: \\ / : * & ? " < > |')
        isValid = False

    # Nama folder tidak valid, terminasi fungsi
    if not isValid:
        return databases

    # Memeriksa ada tidaknya folder tersebut dalam workspace
    folder_path, workspace = cek_folder(folder_save)

    # Folder tidak ada, membuat folder baru dengan nama sesuai input
    if folder_path == 'folder tidak ada':
        folder_path = os.path.join(workspace, folder_save)
        try:
            os.makedirs(folder_path)
        except OSError:
            print("\n(╥_╥) : Data tidak berhasil disimpan, terjadi eror "
                  + "terkait sistem")
            return databases

    # Folder ada, simpan semua data dalam file berekstensi .csv
    print("\n( o _o) : Saving...")
    for i in range(len(databases) - 1):
        csv = nama_csv[i]
        array_to_csv(csv, folder_path, databases[i])

    # Penyimpanan selesai, menampilkan pesan konfirmasi
    print("\n( >_<)b : Data telah disimpan pada folder", folder_save + "!\n")
    return databases
