import datetime

from constant import gadget_return_history,active_account
from riwayatpinjam import sortMaxMinTanggal
from login import cek_active_account

def print_baris(row):
	print("ID Pengambilan:",row[0])
	print("Nama Pengambil:",row[1])
	print("Nama Gadget:",row[2])
	print("Tanggal Pengambilan:",row[3])

def buat_list_tampilan(history, user, gadget):
	history_copy = []
	for row in history:
		row_copy = [row[0],user[row[1]][2],nama_gadget_id(gadget,row[2]),row[3]]
		# ['id', 'id_peminjam', 'id_gadget', 'tanggal_pengembalian']
		history_copy.append(row_copy)
	return history_copy

def riwayatkembali(databases):
	isLoggedIn = cek_active_account(databases)
	if isLoggedIn:
		role = databases[active_account][5]
		if role == "Admin":
			db_history = databases[gadget_return_history][1:]
			
			# cek db_history
			# for row in db_history:
				# print(row)
			
			sorted_db_history = sortMaxMinTanggal(db_history)
			
			# cek sorted
			# print()
			# print("hasil sorted")
			# for row in sorted_db_history:
				# print(row)
			
			list_tampilan = buat_list_tampilan(sorted_db_history,db_user,db_gadget)
			
			# cek list_tampilan 
			# print()
			# print("hasil ganti isi")
			# for row in list_tampilan:
				# print(row)
			
			username = databases[active_account][1]

			for i in range(len(list_tampilan)):
				print_baris(list_tampilan[i])

				if i!=len(list_tampilan)-1:
					print()
					
				if (i+1)%5==0 and i!=len(list_tampilan)-1:
					while True:
						lanjut = input("Apakah "+username+" mau melihat riwayat berikutnya? (Y/N) ")
						print()
						if lanjut in "YyNn" and len(lanjut)==1:
							break
						elif lanjut not in "YyNn" or len(lanjut)!=1:
							print("Input tidak sesuai. Ulangi!")
							print()
						
					if lanjut in "Nn":
						break	
					

			return databases
		else:
			username = databases[active_account][1]
			print("Role "+username+" bukan Admin, silahkan login akun Admin.")
			return databases
	else:
		print("Silahkan login terlebih dahulu.")
		return databases
		
# databases = [
			 # [
			  # ['id', 'username', 'nama', 'alamat', 'password', 'role'], 
			  # ['1', 'morenzoe', 'Eraraya Morenzo Muten', 'Depok', 'kucing123', 'Admin'], 
			  # ['2', 'nisa', 'Khafifanisa', 'Bukittinggi', '123sti', 'User'], 
			  # ['3', 'raihan', 'M. Raihan Aulia', 'Indonesia', 'kucing456,User'], 
			  # ['4', 'abik', 'Atabik Azfa', 'Rumah', 'inipass', 'User']
			 # ], 
			 # [
			  # ['id', 'nama', 'deskripsi', 'jumlah', 'rarity', 'tahun_ditemukan'], 
			  # ['G1', 'Kalung Kucing', 'Kalung untuk berubah menjadi kucing', 10, 'A', 2300], 
			  # ['G2', 'Scratch Post', 'Pengabul keinginan dengan dicakar', 2, 'S', 2500]
			 # ], 
			 # [
			  # ['id', 'nama', 'deskripsi', 'jumlah', 'rarity'], 
			  # ['C1', 'Catnip', 'Untuk party kucing', 100, 'B'], 
			  # ['C2', 'Ikan', 'Ikan', 200, 'C']
			 # ], 
			 # [
			  # ['id', 'id_pengambil', 'id_consumable', 'tanggal_peminjaman', 'jumlah'], 
			  # ['1', '1', 'C1', '17/04/2021', 5], ['2', '1', 'C2', '15/04/2021', 20]
			 # ], 
			 # [
			  # ['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah'], 
			  # ['1', '1', 'G1', '10/04/2021', 3], ['2', '1', 'G2', '20/04/2021', 1]
			 # ], 
			 # [
			  # ['id', 'id_peminjam', 'id_gadget', 'tanggal_pengembalian'], 
			  # ['1', '1', 'G1', '18/04/2021'], 
			  # ['2', '1', 'G2', '17/04/2021'], 
			  # ['3', '2', 'G1', '18/04/2021'], 
			  # ['4', '3', 'G2', '17/03/2019'], 
			  # ['5', '2', 'G1', '18/02/2020'], 
			  # ['6', '1', 'G2', '21/04/2018'], 
			  # ['7', '3', 'G1', '24/07/2021']
			 # ],
			 # ['1', 'morenzoe', 'Eraraya Morenzo Muten', 'Depok', 'kucing123', 'Admin']
			# ]

# riwayatkembali(databases)