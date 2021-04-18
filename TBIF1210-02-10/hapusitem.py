from constant import gadget,consumable,active_account

def hapusitem(databases):
	# cek role
		# role = databases[active_account][5]
			# kalo bukan Admin, langsung selesai: return databases
			# kalo Admin, lanjut
	# minta ID
		# input("Masukan ID item: ")
	# cek ID
		# depannya bukan G atau C
		# karakter ke-2 dst harus integer
	# tentuin mau gadget atau consumable
	# cek ada ga ke databases
		# kalo gadget
			# db_gadget = databases[gadget]
		# kalo consumable
			# db_consumable = databases[consumable]
		# for indeks_baris in range(len(db_)):
			# if db_[indeks_baris][0] == ID:
				# ID ketemu, konfirmasi hapus
					# nama_gadget = databases[gadget][indeks_baris][1]
					# validasi YyNn
					# hapus barisnya berdasarkan indeks_baris
			# kalo gaada, fungsi selesai, tampilin pesan eror
		
	print("belum")
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
			  # ['1', 1, 'C1', '17/04/2021', 5], 
			  # ['2', 1, 'C2', '15/04/2021', 20]
			 # ], 
			 # [
			  # ['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah'], 
			  # ['1', 1, 'G1', '10/04/2021', 3], 
			  # ['2', 1, 'G2', '20/04/2021', 1]
			 # ], 
			 # [
			  # ['id', 'id_peminjam', 'id_gadget', 'tanggal_pengembalian'], 
			  # ['1', 1, 'G1', '18/04/2021'], 
			  # ['2', 1, 'G2', '17/04/2021'], 
			  # ['3', 2, 'G1', '18/04/2021'], 
			  # ['4', 3, 'G2', '17/03/2019'], 
			  # ['5', 2, 'G1', '18/02/2020'], 
			  # ['6', 1, 'G2', '21/04/2018'], 
			  # ['7', 3, 'G1', '24/07/2021']
			 # ],
			  # ['4', 'abik', 'Atabik Azfa', 'Rumah', 'inipass', 'User']
			# ]

# databases2 = hapusitem(databases)

# print(databases2)