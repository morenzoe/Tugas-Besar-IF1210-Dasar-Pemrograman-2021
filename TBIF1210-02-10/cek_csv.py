import sys
import os 
from constant import nama_csv

def cek_argumen(argumen):
	jumlah_argumen = len(argumen)
	if jumlah_argumen > 2:
		nama_folder_tujuan = " ".join(argumen[1:jumlah_argumen])
		return nama_folder_tujuan
	elif jumlah_argumen < 2:
		print("Tidak ada nama folder yang diberikan!")
		print(" Usage: \x1B[3mpython kantongajaib.py <nama_folder>\x1B[23m")
		sys.exit()
	elif jumlah_argumen == 2:
		nama_folder_tujuan = argumen[1]
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
			return folder_tujuan_dir, workspace
			break
		elif not folder_found:
			return 'folder tidak ada', workspace

def cek_csv(argumen):
	nama_folder_tujuan = cek_argumen(argumen)
	folder_tujuan_dir, workspace = cek_folder(nama_folder_tujuan)
	if folder_tujuan_dir == 'folder tidak ada':
		return 'folder tidak ada'
	files = os.listdir(folder_tujuan_dir)
	csv_found = all(item in files for item in nama_csv)
	if csv_found:
		return folder_tujuan_dir
	elif not csv_found:
		return 'csv tidak ada'