# Program F14 - Load Data
# Input     : 
# Output    :

# KAMUS
# databases : array of array of array of string and int
# command : string
# dict_program : dictionary

# import module
import sys

# import variabel konstan
from constant import *

# import program lokal
from carirarity import carirarity
from caritahun import caritahun
from cek_csv import cek_csv
from hapusitem import hapusitem
from help import help
from kembalikan import kembalikan
from load import baca_csv
from login import login
from minta import minta
from pinjam import pinjam
#from register import register # register belum mengubah list
from riwayatpinjam import riwayatpinjam
from riwayatkembali import riwayatkembali
from riwayatambil import riwayatambil
from save import save
from tambahitem import tambahitem
from ubahjumlah import ubahjumlah

# ALGORITMA
# argument parsing
argumen = sys.argv
csv_path = cek_csv(argumen)
if csv_path == 'csv tidak ada':
	pesan_error = '''
File CSV tidak sesuai!
File CSV yang diperlukan:
	user,
	gadget,
	consumable,
	consumable_history,
	gadget_borrow_history,
	gadget_return_history'''
	sys.exit(pesan_error)
elif csv_path == 'folder tidak ada':
	sys.exit("Folder tidak ada!")
# baca csv
databases = baca_csv(csv_path)
# kamus program
dict_program = {'login' : [login,databases[user]],	# [nama fungsi,input]
				'carirarity' : [carirarity,databases[gadget]],
				'caritahun' : [caritahun,databases[gadget]],
				'tambahitem' : [tambahitem,[databases[gadget],databases[consumable]]],
				'hapusitem' : [hapusitem,[databases[gadget],databases[consumable]]],
				'ubahjumlah' : [ubahjumlah,[databases[gadget],databases[consumable]]],
				'pinjam' : [pinjam,databases[gadget]],
				'kembalikan' : [kembalikan,databases[gadget]],
				'minta' : [minta,databases[consumable]],
				#'register' : [register,databases[user]]
				'riwayatpinjam' : [riwayatpinjam,databases[gadget_borrow_history]],
				'riwayatkembali' : [riwayatkembali,databases[gadget_return_history]],
				'riwayatambil' : [riwayatambil,databases[consumable_history]],
				'save' : [save,databases],
				'help' : [help,None]
				}
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
			dict_program['save'][fungsi](dict_program['save'][inputs])
			print("Save berhasil. Sampai jumpa!")
			break
		elif save_option in "Nn":
			print("Sampai jumpa!")
			break
		elif save_option not in "YyNn":
			print("Input tidak sesuai. Ulangi (Y/N) ")
			pass
	elif command!='exit':
		try:
			dict_program[command][fungsi](dict_program[command][inputs])
		except KeyError:
			print("Perintah salah! Ketik help dan tekan enter untuk menampilkan petunjuk.")
		

