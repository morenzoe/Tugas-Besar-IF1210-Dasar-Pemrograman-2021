import sys
import os 
from constant import nama_csv

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

def cek_argumen(argument):
	jumlah_argumen = len(argument)
	if jumlah_argumen > 2:
		print("Argumen yang diberikan terlalu banyak!")
		print(" Usage: \x1B[3mpython kantongajaib.py <nama_folder>\x1B[23m")
	elif jumlah_argumen < 2:
		print("Tidak ada nama folder yang diberikan!")
		print(" Usage: \x1B[3mpython kantongajaib.py <nama_folder>\x1B[23m")
	elif jumlah_argumen == 2:
		nama_folder_tujuan = argument[1]
		return nama_folder_tujuan

def cek_folder(nama_folder_tujuan):
	workspace = os.getcwd() # workspace file kantong_ajaib.py
	folder_found = False
	for root, dirs, files in os.walk(workspace):
		for nama_folder in dirs:
			if nama_folder == nama_folder_tujuan:
				folder_found = True
				folder_tujuan_dir = os.path.join(root,nama_folder_tujuan)			
				break
		if folder_found:
			return folder_tujuan_dir
			break
		elif not folder_found:
			folder_tidak_ada()

def cek_csv(argumen):
	nama_folder_tujuan = cek_argumen(argumen)
	path = cek_folder(nama_folder_tujuan)
	files = os.listdir(path)
	csv_found = all(item in files for item in nama_csv)
	if csv_found:
		return path
	elif not csv_found:
		csv_tidak_ada()