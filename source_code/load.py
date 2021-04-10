# Program F14 - Load Data
# Input     :
# Output    :

# KAMUS
# CSVs : array of string
# databases : array of array of array of string and float

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

def to_float(array_word):
# menghasilkan word dalam type float jika word adalah angka

# KAMUS LOKAL
# Variabel
# array_word : array of string

# ALGORITMA
    for i in range(len(array_word)):
        try:
            array_word[i] = float(array_word[i])
        except ValueError:
            pass

def csv_to_array(filename):
# menghasilkan array berisi seluruh data pada csv

# KAMUS LOKAL
# Variabel
# f : file
# rows, array_word : array of string
# array_word_float : array of string and float
# database : array of array of string and float

# ALGORITMA
    f = open(filename+".csv","r")
    raw_rows = f.readlines()
    f.close()
    rows = [raw_row.replace("\n","") for raw_row in raw_rows]

    database = []
    for row in rows:
        array_word = row_to_array_word(row)
        array_word_float = to_float(array_word)
        database.append(array_word_float)
    return database

# PROGRAM UTAMA
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

# import program python

# loop program
# import sys
# print("Length of list:", len(sys.argv))
# print(sys.argv)