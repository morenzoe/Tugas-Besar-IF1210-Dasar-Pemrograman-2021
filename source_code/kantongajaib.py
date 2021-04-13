# Program F14 - Load Data
# Input     : 
# Output    :

# KAMUS
# databases : array of array of array of string and int
# command : string
# dict_program : dictionary

# import library standar
import os
import sys

# import program lokal
from constant import *

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

def folder_tidak_ada():
	sys.exit("Folder tidak ada!")

def csv_tidak_ada():
	pesan_error = '''
File CSV tidak sesuai!
File CSV yang diperlukan:
	user,
	gadget,
	consumable,
	consumable_history,
	gadget_borrow_history,
	gadget_return_history
'''
	sys.exit(pesan_error)

def cek_csv(path):
	files = os.listdir(path)
	csv_found = all(item in files for item in nama_csv)
	if csv_found:
		baca_csv(path)
	elif not csv_found:
		csv_tidak_ada()

def cek_folder(nama_folder_tujuan):
	workspace = os.getcwd() # workspace file kantong_ajaib.py
	folder_found = False
	for root, dirs, files in os.walk(workspace):
		for nama_folder in dirs:
			if nama_folder == nama_folder_tujuan:
				folder_found = True
				folder_tujuan_dir = os.path.join(root,nama_folder_tujuan)			
		if folder_found:
			cek_csv(folder_tujuan_dir)
			break
		elif not folder_found:
			folder_tidak_ada()

def cek_argumen():
	jumlah_argumen = len(sys.argv)
	if jumlah_argumen > 2:
		print("Argumen yang diberikan terlalu banyak!")
		print(" Usage: \x1B[3mpython kantongajaib.py <nama_folder>\x1B[23m")
	elif jumlah_argumen < 2:
		print("Tidak ada nama folder yang diberikan!")
		print(" Usage: \x1B[3mpython kantongajaib.py <nama_folder>\x1B[23m")
	elif jumlah_argumen == 2:
		folder_load = sys.argv[1]
		cek_folder(folder_load)

def cetak_database(database):
	print(databases[database])

def baca_csv(path):
	global databases
	# file csv sesuai
	print("Loading...")
	for csv in nama_csv:
		databases.append(csv_to_array(path,csv))
	return databases
# PROGRAM UTAMA
# inisialisasi
databases = []
# argument parsing
cek_argumen()
# pesan selamat datang
print()
print("Selamat datang di inventarisasi Doraemonangis")
print()
# loop program
while True:
	command = input(">>> ")
	if command=='exit':
		save_option = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (Y/N) ")
		if save_option in "Yy":
			dict_program[save]()
			print("Save berhasil. Sampai jumpa!")
			break
		elif save_option in "Nn":
			print("Sampai jumpa!")
			break
		elif save_option not in "YyNn":
			print("Input tidak sesuai. (Y/N) ")
			pass
	elif command!='exit':
		try:
			dict_program[command]()
		except KeyError:
			print("Perintah salah! Ketik help dan tekan enter untuk menampilkan petunjuk.")
		

