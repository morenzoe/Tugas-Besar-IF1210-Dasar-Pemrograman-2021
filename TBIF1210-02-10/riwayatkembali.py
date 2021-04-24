import datetime

from constant import user,gadget,gadget_return_history,active_account
from login import cek_active_account
from riwayatpinjam import sortMaxMinTanggal
	

def print_baris(row):
	print("ID Pengambilan:",row[0])
	print("Nama Pengambil:",row[1])
	print("Nama Gadget:",row[2])
	print("Tanggal Pengembalian:",row[3])

def buat_list_tampilan(history, user, gadget):
	history_copy = []
	for row in history:
		id_pengambilan = row[1]
		nama_pengambil = 
		nama_gadget = 
		tanggal_pengembalian = 
		row_copy = [id_pengambilan, nama_pengambil, nama_gadget, tanggal_pengembalian]
		# ['id', 'id_peminjaman', 'tanggal_pengembalian']
		history_copy.append(row_copy)
	return history_copy

def riwayatkembali(databases):
	isLoggedIn = cek_active_account(databases)
	if isLoggedIn:
		role = databases[active_account][5]
		if role == "Admin":
			db_history = databases[gadget_return_history][1:]
			db_gadget = databases[gadget]
			db_user = databases[user]
			
			# cek db_history
			# for row in db_history:
				# print(row)
			
			sorted_db_history = sortMaxMinTanggal(db_history,2)
			
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
		
databases = [[['id', 'username', 'nama', 'alamat', 'password', 'role'], ['1', 'morenzoe', 'Eraraya Morenzo Muten', 'Depok', 'kucing123', 'Admin'], ['2', 'nisa', 'Khafifanisa', 'Bukittinggi', '123sti', 'User'], ['3', 'raihan', 'M. Raihan Aulia', 'Indonesia', 'kucing456,User'], ['4', 'abik', 'Atabik Azfa', 'Rumah', 'inipass', 'User']], [['id', 'nama', 'deskripsi', 'jumlah', 'rarity', 'tahun_ditemukan'], ['G1', 'Kalung Kucing', 'Kalung untuk berubah menjadi kucing.', 10, 'A', 1256], ['G2', 'Scratch Post', 'Pengabul keinginan dengan dicakar.', 2, 'S', 1527], ['G3', 'Cakar Kucing', 'Sarung tangan cakar kucing.', 26, 'C', 1870], ['G4', 'Kaki Kucing', 'Berjalan dengan senyap seperti kucing.', 15, 'B', 1990], ['G5', 'Ekor Kucing', 'Menjaga keseimbangan seperti kucing.', 55, 'C', 1998], ['G6', 'Cat Paw', 'Pemukul berbentuk tangan kucing.', 100, 'C', 1788], ['G7', 'Lidah Kucing', 'Pembersih rambut kucing.', 107, 'C', 1880]], [['id', 'nama', 'deskripsi', 'jumlah', 'rarity'], ['C1', 'Catnip', 'Untuk party kucing.', 100, 'B'], ['C2', 'Ikan', 'Ikan mentah.', 200, 'C'], ['C3', 'Gurame Bakar', 'Gurame bakar kecap.', 10, 'A'], ['C4', 'Vitamin Kucing', 'Suplemen kesehatan kucing.', 100, 'B'], ['C5', 'Air Liur Kucing', 'Menyembuhkan luka apapun.', 5, 'S'], ['C6', 'Rambut Kucing', 'Rambut kucing biasa.', 245, 'C'], ['C7', 'Dorayakin', 'Makanan kesukaan Doraemonangis.', 2, 'S']], [['id', 'id_pengambil', 'id_consumable', 'tanggal_pengambilan', 'jumlah'], ['1', 1, 'C1', '17/04/2021', 5], ['2', 1, 'C2', '15/04/2021', 20], ['2', 2, 'C5', '30/11/2002', 1], ['3', 3, 'C2', '28/31/2005', 50], ['4', 4, 'C3', '29/02/2004', 5], ['5', 4, 'C6', '29/06/2019', 300], ['6', 2, 'C1', '31/01/2001', 20], ['7', 3, 'C7', '17/10/2050', 1]], [['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah', 'is_returned'], ['1', 1, 'G1', '10/04/2021', 3, 'True'], ['2', 1, 'G2', '20/04/2021', 1, 'True'], ['3', 2, 'G4', '17/03/2020', 5, 'False'], ['4', 1, 'G7', '24/04/2021', 53, 'True'], ['5', 3, 'G4', '18/08/2021', 10, 'False'], ['6', 2, 'G3', '21/07/2078', 18, 'True'], ['7', 4, 'G5', '19/05/2012', 45, 'True'], ['8', 4, 'G6', '18/09/2021', 80, 'True'], ['9', 3, 'G3', '19/11/2011', 26, 'False']], [['id', 'id_peminjaman', 'tanggal_pengembalian'], ['1', 2, '18/04/2021'], ['2', 1, '17/04/2021'], ['3', 7, '18/04/2021'], ['4', 6, '17/03/2019'], ['5', 4, '18/02/2020'], ['6', 8, '21/04/2018'], ['7', 9, '24/07/2021']], ['1', 'morenzoe', 'Eraraya Morenzo Muten', 'Depok', 'kucing123', 'Admin']]

riwayatkembali(databases)