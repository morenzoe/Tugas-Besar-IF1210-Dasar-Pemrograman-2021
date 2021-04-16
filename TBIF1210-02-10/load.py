# import library standar
import os
import sys

# import program lokal
from constant import nama_csv

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
		while i<len(row) and row[i]==';':          #  koma
			i+=1
		if i==len(row):                             # menangani kasus row == '', ','
			break
		
		j = i
		i+=1
		while i<len(row) and row[i]!=';':           # menangani selain koma
			i+=1
		
		if j==0 and i==len(row) and ';' not in row: # menangani kasus tidak ada koma dalam row
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
	raw_array_word = semicolon_split(row)                       # konversi row -> array of string
	array_word = [word.strip() for word in raw_array_word]  # membersihkan spasi awal dan akhir
	return array_word

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
	return array_word

def csv_to_array(path, csv):
# menghasilkan array berisi seluruh data pada csv

# KAMUS LOKAL
# Variabel
# f : file
# rows, array_word : array of string
# array_word_int : array of string and int
# database : array of array of string and int

# ALGORITMA
	csv_path = os.path.join(path,csv)
	f = open(csv_path,"r")
	raw_rows = f.readlines()
	f.close()
	rows = [raw_row.replace("\n","") for raw_row in raw_rows]

	database = []
	for row in rows:
		array_word = row_to_array_word(row)
		array_word_int = to_int(array_word)
		database.append(array_word_int)
	return database

def baca_csv(path):
	databases = []
	# file csv sesuai
	print("Loading...")
	for csv in nama_csv:
		databases.append(csv_to_array(path,csv))
	return databases