# Program F14 - Load Data
# Input     : 
# Output    :

# KAMUS
# databases : array of array of array of string and int
# command : string
# dict_program : dictionary

# import module
import sys

# import program lokal
from constant import *
from functions import *

# ALGORITMA
# argument parsing
argument = sys.argv
csv_path = cek_csv(argument)
# baca csv
databases = baca_csv(csv_path)
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
		

