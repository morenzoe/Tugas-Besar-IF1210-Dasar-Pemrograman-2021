# Program F14 - Load Data
# Input     : 
# Output    :

# KAMUS
# CSVs : array of string
# databases : array of array of array of string and int
# command : string
# dict_program : dictionary

# import library standar
import os
import sys

# import program lokal
import carirarity
import caritahu
import constant
import exit
import hapusitem
import help
import kembalikan
import login
import minta
import pinjam
import riwayatpinjam
import riwayatkembali
import riwayatambil
import save
import tambahitem
import ubahjumlah

# PROCEDURE DAN FUNCTION
def comma_split(row):
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
        while i<len(row) and row[i]==',':          #  koma
            i+=1
        if i==len(row):                             # menangani kasus row == '', ','
            break
        
        j = i
        i+=1
        while i<len(row) and row[i]!=',':           # menangani selain koma
            i+=1
        
        if j==0 and i==len(row) and ',' not in row: # menangani kasus tidak ada koma dalam row
            return [row]
        
        array_word.append(row[j:i])
    return array_word

def row_to_array_word(row):
# menghasilkan array of string tiap string (kata) antara koma tanpa spasi di awal dan akhir

# KAMUS LOKAL
# Variabel
# raw_array_word, array_word : array of string
# row : string

# ALGORITMA
    raw_array_word = comma_split(row)                       # konversi row -> array of string
    array_word = [word.strip() for word in raw_array_word]  # membersihkan spasi awal dan akhir
    return array_word

def pathmaker(filename):
    path = csv_directory+"\\"+filename+".csv"
    return path

def to_int(array_word):
# menghasilkan word dalam type int jika word adalah angka

# KAMUS LOKAL
# Variabel
# array_word : array of string

# ALGORITMA
    for i in range(len(array_word)):
        try:
            array_word[i] = int(array_word[i])
        except ValueError:
            pass

def csv_to_array(filename):
# menghasilkan array berisi seluruh data pada csv

# KAMUS LOKAL
# Variabel
# f : file
# rows, array_word : array of string
# array_word_int : array of string and int
# database : array of array of string and int

# ALGORITMA
    path = pathmaker(filename)
    f = open(path,"r")
    raw_rows = f.readlines()
    f.close()
    rows = [raw_row.replace("\n","") for raw_row in raw_rows]

    database = []
    for row in rows:
        array_word = row_to_array_word(row)
        array_word_int = to_int(array_word)
        database.append(array_word_int)
    return database

# PROGRAM UTAMA
# loading
print("Loading...")
# current working directory file kantong_ajaib.py
current_working_directory = os.getcwd()
# parent directory
parent_directory = os.path.abspath(os.path.join(current_working_directory, os.pardir))
# CSV directory
csv_directory = parent_directory + "\external_files"
# mengubah semua csv menjadi array dalam database
CSVs = ["user",
        "gadget",
        "consumable",
        "consumable_history",
        "gadget_borrow_history",
        "gadget_return_history"]
databases = []
for csv in CSVs:
    databases.append(csv_to_array(csv))

# dictionary program
dict_program = {
    'login' : login,
    'carirarity' : carirarity,
    'caritahu' : caritahu,
    'tambahitem' : tambahitem,
    'hapusitem' : hapusitem,
    'ubahjumlah' : ubahjumlah,
    'pinjam' : pinjam,
    'kembalikan' : kembalikan,
    'minta' : minta,
    'riwayatpinjam' : riwayatpinjam,
    'riwayatkembali' : riwayatkembali,
    'riwayatambil' : riwayatambil,
    'save' : save,
    'help' : help,
    'exit' : exit
    }

# loop program
print()
print("Selamat datang di inventarisasi Doraemonangis")
print()

while True:
    command = input(">>> ")
    if command=='exit':
        break    
    dict_program[command]()

