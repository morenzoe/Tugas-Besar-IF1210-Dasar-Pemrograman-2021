# Program F14 - Load Data
# Input     :
# Output    :

# KAMUS
# databases : list of list of list
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
from load import load
from login import login
from minta import minta
from pinjam import pinjam
from register import register
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
databases = load(csv_path)
# kamus program
dict_program = {
	'register': register,
    'login': login,
    'carirarity': carirarity,
    'caritahun': caritahun,
    'tambahitem': tambahitem,
    'hapusitem': hapusitem,
    'ubahjumlah': ubahjumlah,
    'pinjam': pinjam,
    'kembalikan': kembalikan,
    'minta': minta,
    'riwayatpinjam': riwayatpinjam,
    'riwayatkembali': riwayatkembali,
    'riwayatambil': riwayatambil,
    'save': save,
    'help': help,
    }
# pesan selamat datang
print()
print("Selamat datang di inventarisasi Doraemonangis")
# loop program
while True:

	# debugging
	print("\nMode debugging:")
	printSemua = input("Print databases sebagai list? (Y/N) ")
	if printSemua in "Yy":
		print(databases)
		print()
	printSebagian = input("Print databases per baris? (Y/N) ")
	if printSebagian in "Yy":
		for i in range(len(nama_csv)):
			print(nama_csv[i])
			for row in databases[i]:
				print(row)
			print()
		print("active_account")
		for row in databases[active_account]:
			print(row)
	# debugging

	command = input("\n>>> ")
	print()
	if command == 'exit':
		while True:
			save_option = input("Apakah Anda mau melakukan penyimpanan file " +
                                "yang sudah diubah? (Y/N) ")
			print()
			if save_option in "YyNn" and len(save_option)==1:
				break
			print("m(><)m : Input tidak sesuai. Ulangi! \n")
		if save_option in "Yy":
			dict_program['save'](databases)
		print("(^O^)/ : Sampai jumpa!")
		break
        
	elif command!='exit':
		try:
			databases = dict_program[command](databases)
		except KeyError:
			print("O_o : Perintah salah! Ketik help dan tekan enter untuk menampilkan petunjuk.")
		

'''
user.csv
['id', 'username', 'nama', 'alamat', 'password', 'role']
['1', 'morenzoe', 'Eraraya Morenzo Muten', 'Depok', 'kucing123', 'Admin']
['2', 'nisa', 'Khafifanisa', 'Bukittinggi', '123sti', 'User']
['3', 'raihan', 'M. Raihan Aulia', 'Indonesia', 'kucing456,User']
['4', 'abik', 'Atabik Azfa', 'Rumah', 'inipass', 'User']

gadget.csv
['id', 'nama', 'deskripsi', 'jumlah', 'rarity', 'tahun_ditemukan']
['G1', 'Kalung Kucing', 'Kalung untuk berubah menjadi kucing.', 10, 'A', 1256]
['G2', 'Scratch Post', 'Pengabul keinginan dengan dicakar.', 2, 'S', 1527]
['G3', 'Cakar Kucing', 'Sarung tangan cakar kucing.', 26, 'C', 1870]
['G4', 'Kaki Kucing', 'Berjalan dengan senyap seperti kucing.', 15, 'B', 1990]
['G5', 'Ekor Kucing', 'Menjaga keseimbangan seperti kucing.', 55, 'C', 1998]
['G6', 'Cat Paw', 'Pemukul berbentuk tangan kucing.', 100, 'C', 1788]
['G7', 'Lidah Kucing', 'Pembersih rambut kucing.', 107, 'C', 1880]

consumable.csv
['id', 'nama', 'deskripsi', 'jumlah', 'rarity']
['C1', 'Catnip', 'Untuk party kucing.', 100, 'B']
['C2', 'Ikan', 'Ikan mentah.', 200, 'C']
['C3', 'Gurame Bakar', 'Gurame bakar kecap.', 10, 'A']
['C4', 'Vitamin Kucing', 'Suplemen kesehatan kucing.', 100, 'B']
['C5', 'Air Liur Kucing', 'Menyembuhkan luka apapun.', 5, 'S']
['C6', 'Rambut Kucing', 'Rambut kucing biasa.', 245, 'C']
['C7', 'Dorayakin', 'Makanan kesukaan Doraemonangis.', 2, 'S']

consumable_history.csv
['id', 'id_pengambil', 'id_consumable', 'tanggal_pengambilan', 'jumlah']
['1', 1, 'C1', '17/04/2021', 5]
['2', 1, 'C2', '15/04/2021', 20]
['2', 2, 'C5', '30/11/2002', 1]
['3', 3, 'C2', '28/31/2005', 50]
['4', 4, 'C3', '29/02/2004', 5]
['5', 4, 'C6', '29/06/2019', 300]
['6', 2, 'C1', '31/01/2001', 20]
['7', 3, 'C7', '17/10/2050', 1]

gadget_borrow_history.csv
['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah', 'is_returned']
['1', 1, 'G1', '10/04/2021', 3, 'True']
['2', 1, 'G2', '20/04/2021', 1, 'True']
['3', 2, 'G4', '17/03/2020', 5, 'False']
['4', 1, 'G7', '24/04/2021', 53, 'True']
['5', 3, 'G4', '18/08/2021', 10, 'False']
['6', 2, 'G3', '21/07/2078', 18, 'True']
['7', 4, 'G5', '19/05/2012', 45, 'True']
['8', 4, 'G6', '18/09/2021', 80, 'True']
['9', 3, 'G3', '19/11/2011', 26, 'False']

gadget_return_history.csv
['id', 'id_peminjaman', 'tanggal_pengembalian']
['1', 2, '18/04/2021']
['2', 1, '17/04/2021']
['3', 7, '18/04/2021']
['4', 6, '17/03/2019']
['5', 4, '18/02/2020']
['6', 8, '21/04/2018']
['7', 9, '24/07/2021']
'''
