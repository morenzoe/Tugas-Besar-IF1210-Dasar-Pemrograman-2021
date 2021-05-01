"""Program F14 - Load Data
Fungsi ini akan membaca path directory folder kemudian membaca semua
data dalam enam file dengan ekstensi .csv, mengubah tipe data setiap
kolom tertentu, dan menggabungkannya dalam satu list databases.
Fungsi kemudian menambahkan satu list kosong pada akhir list databases
untuk diisi data login.  Fungsi mengembalikan list databases tersebut.

Akses : -
"""

# KAMUS
# Daftar library standar
import os

# Daftar library lokal
from constant import nama_csv, dikonversi

# Daftar konstanta
# nama_csv : array of str
# dikonversi : array of array of bool

# Daftar variabel
# databases : array of array of array
# database : array of array
# active_account : list

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def semicolon_split(row):
    """Fungsi ini membaca string dan menghasilkan list of string tiap
    kata antara titik koma (semicolon). Fungsi kemudian mengembalikan
    list tesebut.

    Ide algoritma dari documentation fungsi bawaan Python split().
    """

    # KAMUS LOKAL
    # Variabel
    # array_word : array of str
    # row : str
    # i, j : int

    # ALGORITMA
    # Inisialisasi variabel array dan counter
    array_word = []
    i = j = 0

    # Loop untuk seluruh karakter dalam row
    while True:
        # Melongkapi semicolon ketika belum mencapai karakter terakhir
        while i < len(row) and row[i] == ';':
            i += 1

        # Seluruh karakter sudah di proses
        if i == len(row):
            break

        # Menangani kasus ada karakter selain semicolon
        j = i
        i += 1
        while i < len(row) and row[i] != ';':
            i += 1

        # Menangani kasus tidak ada semicolon dalam row
        if j == 0 and i == len(
                row) and ';' not in row:
            return [row]

        # Menambahkan data antara semicolon sebagai string
        array_word.append(row[j:i])
    return array_word


def space_strip(array_word):
    """Fungsi membaca string, mengubah menjadi array of string,
    menghasilkan array of string tiap string (kata) antara koma tanpa
    spasi di awal dan akhir.  Fungsi kemudian mengembalikan array
    dengan data yang bersih.
    """

    # KAMUS LOKAL
    # array_word, clean_array_word : array of string

    # ALGORITMA
    # Membersihkan spasi awal dan akhir tiap elemen
    clean_array_word = [word.strip() for word in array_word]
    return clean_array_word


def to_int(array_word, konversi):
    """Fungsi ini membaca array of string dan mengubah tipe data tiap
    elemen menjadi integer sesuai ketentuan konversi.  Fungsi kemudian
    mengembalikan array dengan tipe data yang sesuai.
    """

    # KAMUS LOKAL
    # array_word : array of str
    # konversi : array of array of bool

    # ALGORITMA
    # Memproses semua data pada entri
    for i in range(len(array_word)):
        # Mengubah tipe data menjadi integer pada kolom yang sesuai
        if konversi[i]:
            array_word[i] = int(array_word[i])
    return array_word


def csv_to_array(path, csv, konversi):
    """Fungsi ini membaca satu csv pada suatu path directory dan
    mengubah bentuk entri sesuai dengan konversi.  Fungsi kemudian
    mengembalikan seluruh entri sebagai satu array.
    """

    # KAMUS LOKAL
    # path, csv : str
    # konversi : array of array of bool
    # f : file
    # rows, array_word : array of string
    # array_word_int : array of string and int
    # database : array of array of string and int

    # ALGORITMA
    # Membuat path directory penyimpanan
    csv_path = os.path.join(path, csv)

    # Membaca tiap entri pada file
    f = open(csv_path, "r")
    raw_rows = f.readlines()
    f.close()

    # Menghapus new line character
    rows = [raw_row.replace("\n", "") for raw_row in raw_rows]

    # Inisialisasi array penyimpanan
    database = []

    # Memproses semua entri dari csv
    for i in range(len(rows)):
        # Mengubah bentuk entri dari string menjadi array
        array_word = semicolon_split(rows[i])
        clean_array_word = space_strip(array_word)

        # Mengubah tipe data selain entri pertama
        if i != 0:
            clean_array_word = to_int(clean_array_word, konversi)

        # Menggabungkan entri
        database.append(clean_array_word)
    return database


# ALGORITMA PROGRAM UTAMA
def load(path):
    # Inisialisasi array penyimpanan
    databases = []

    # Menampilkan pesan proses pembacaan
    print("\n(o.O): Loading...")

    # Membaca dan mengolah semua file csv
    for i in range(len(nama_csv)):
        database = csv_to_array(path, nama_csv[i], dikonversi[i])
        databases.append(database)

    # Menambahkan array kosong untuk data akun aktif satelah login
    active_account = []
    databases.append(active_account)
    return databases
