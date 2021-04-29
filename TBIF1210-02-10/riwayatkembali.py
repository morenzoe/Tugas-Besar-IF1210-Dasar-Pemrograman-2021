"""Program F12 - Melihat Riwayat Pengembalian Gadget 
Prosedur ini akan menampilkan riwayat pengembalian gadget berisi data 
ID Pengambil, Nama Pengambil, Nama Gadget, dan Tanggal Pengambilan.
Prosedur ini akan menampilkan riwayat pengembalian yang terurut menurun
dari yang paling terbaru. Prosedur menampilkan 5 data sekali keluaran.
"""

# KAMUS
# standard library imports
import datetime

# local library imports
from constant import user,gadget,gadget_borrow_history, \
                     gadget_return_history,active_account
from login import cek_active_account
from riwayatpinjam import sortMaxMinTanggal,nama_user_id,nama_gadget_id	

# variable
#

# function and procedure
#

# ALGORITMA PROGRAM UTAMA
def riwayatkembali(databases):
	isLoggedIn = cek_active_account(databases)
	if isLoggedIn:
		username = databases[active_account][1]
		role = databases[active_account][5]
		if role == "Admin":
			db_kembali = databases[gadget_return_history][1:]
			db_pinjam = databases[gadget_borrow_history]
			db_gadget = databases[gadget]
			db_user = databases[user]
		
			sorted_db_kembali = sortMaxMinTanggal(db_kembali,2)
			
			list_tampilan = buat_list_tampilan(sorted_db_kembali,db_pinjam,db_user,db_gadget)
			
			tampilan(list_tampilan,username)
						
			return databases
			
		else:
			print("Role "+username+" bukan Admin, silahkan login akun Admin.")
			return databases
	else:
		print("Silahkan login terlebih dahulu.")
		return databases

# REALISASI FUNGSI DAN PROSEDUR

def print_baris(row):
	print("ID Pengambilan:",row[0])
	print("Nama Pengambil:",row[1])
	print("Nama Gadget:",row[2])
	print("Tanggal Pengembalian:",row[3])

def buat_list_tampilan(kembali, pinjam, user, gadget):
	kembali_copy = []
	for row in kembali:
		id_pengambilan = row[1]
		id_peminjam = pinjam[id_pengambilan][1]
		nama_pengambil = nama_user_id(user,id_peminjam)
		id_gadget = pinjam[id_pengambilan][2]
		nama_gadget = nama_gadget_id(gadget,id_gadget)
		tanggal_pengembalian = row[2]
		
		row_copy = [id_pengambilan, nama_pengambil, nama_gadget, tanggal_pengembalian]
		kembali_copy.append(row_copy)
	return kembali_copy

def tampilan(list_tampilan,username):
	for i in range(len(list_tampilan)):
				print_baris(list_tampilan[i])

				if i!=len(list_tampilan)-1:
					print()
					
				if (i+1)%5==0 and i!=len(list_tampilan)-1:
					while True:
						lanjut = input("Apakah "+username+" mau melihat riwayat berikutnya? (Y/N) ")
						if lanjut in "YyNn" and len(lanjut)==1:
							break
						elif lanjut not in "YyNn" or len(lanjut)!=1:
							print("Input tidak sesuai. Ulangi!")
							print()
						
					if lanjut in "Nn":
						break
					elif lanjut in "Yy":
						print()