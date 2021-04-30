"""Program F14 - Load Data
Fungsi ini akan membaca semua data dalam enam file dengan ekstensi 
.csv, mengubah tipe data setiap kolom tertentu, dan menggabungkannya 
dalam satu list databases.  Fungsi kemudian menambahkan satu list 
kosong pada akhir list databases untuk diisi data login.  Fungsi 
mengembalikan list databases tersebut.

Akses : -
"""

# KAMUS
# Daftar library standar
import os
import sys

# import program lokal
from constant import nama_csv, dikonversi

# PROCEDURE DAN FUNCTION


def semicolon_split(row):
    # menghasilkan array of string tiap string (kata) antara koma

    # KAMUS LOKAL
    # Variabel
    # array_word : array of string
    # row : string
    # i, j : int

    # ALGORITMA
    array_word = []                                 # inisialisasi
    i = j = 0
    while True:                                     # loop sampai seluruh character dalam row
        while i < len(row) and row[i] == ';':  # koma
            i += 1
        if i == len(row):  # menangani kasus row == '', ','
            break

        j = i
        i += 1
        while i < len(row) and row[i] != ';':           # menangani selain koma
            i += 1

        if j == 0 and i == len(
                row) and ';' not in row:  # menangani kasus tidak ada koma dalam row
            return [row]

        array_word.append(row[j:i])
    return array_word


def row_to_array_word(row):
    # menghasilkan array of string tiap string (kata) antara koma tanpa spasi
    # di awal dan akhir

    # KAMUS LOKAL
    # Variabel
    # raw_array_word, array_word : array of string
    # row : string

    # ALGORITMA
    # konversi row -> array of string
    raw_array_word = semicolon_split(row)
    # membersihkan spasi awal dan akhir
    array_word = [word.strip() for word in raw_array_word]
    return array_word


def to_int(array_word, konversi):
    # menghasilkan word dalam type int jika word adalah angka

    # KAMUS LOKAL
    # Variabel
    # array_word : array of string

    # ALGORITMA
    for i in range(len(array_word)):
        if konversi[i]:
            array_word[i] = int(array_word[i])
    return array_word


def csv_to_array(path, csv, konversi):
    # menghasilkan array berisi seluruh data pada csv

    # KAMUS LOKAL
    # Variabel
    # f : file
    # rows, array_word : array of string
    # array_word_int : array of string and int
    # database : array of array of string and int

    # ALGORITMA
    csv_path = os.path.join(path, csv)
    f = open(csv_path, "r")
    raw_rows = f.readlines()
    f.close()
    rows = [raw_row.replace("\n", "") for raw_row in raw_rows]

    database = []
    for i in range(len(rows)):
        array_word = row_to_array_word(rows[i])
        if i != 0:
            array_word = to_int(array_word, konversi)
        database.append(array_word)
    return database


def load(path):
    databases = []
    # file csv sesuai
    print("Loading...")
    for i in range(len(nama_csv)):
        databases.append(csv_to_array(path, nama_csv[i], dikonversi[i]))
    active_account = []
    databases.append(active_account)
    return databases
