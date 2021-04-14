from cek_csv import cek_csv

# database id
user = 0
gadget = 1
consumable = 2
consumable_history = 3
gadget_borrow_history = 4
gadget_return_history = 5

databases = [
			 #user
			 [
			  ['id', 'username', 'nama', 'alamat', 'password', 'role'], 
			  [1, 'morenzoe', 'Eraraya Morenzo Muten', 'Depok', 'kucing123', 'Admin'], 
			  [2, 'nisa,Khafifanisa', 'Bukittinggi', '123sti', 'User'], 
			  [3, 'raihan', 'M. Raihan Aulia', 'Indonesia,kucing456,User'], 
			  [4, 'abik', 'Atabik Azfa', 'Rumah', 'inipass', 'User']
			 ], 
			 #gadget
			 [
			  ['id', 'nama', 'deskripsi', 'jumlah', 'rarity', 'tahun_ditemukan']
			 ], 
			 #consumable
			 [
			  ['id', 'nama', 'deskripsi', 'jumlah', 'rarity']
			 ], 
			 #consumable_history
			 [
			  ['id', 'id_pengambil', 'id_consumable', 'tanggal_peminjaman', 'jumlah']
			 ], 
			 #gadget_borrow_history
			 [
			  ['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah']
			 ], 
			 #gadget_return_history
			 [
			  ['id', 'id_peminjam', 'id_gadget', 'tanggal_pengembalian']
			 ]
			]

def to_str(array_word_int):
# menghasilkan word dalam type str

# KAMUS LOKAL
# Variabel
# array_word : array of string

# ALGORITMA
	array_word = [str(word) for word in array_word_int]
	return array_word

def array_word_to_row(array_word):
	# semicolon add
	row = ";".join(array_word) + "\n"
	return row

def array_to_csv(path, array):
	csv = []
	for array_word_int in database:
		array_word = to_str(array_word_int)
		row = ";".join(array_word) + "\n"
		csv.append(row)
	return csv
	
	csv_path = os.path.join(path,csv)
	f = open(csv_path,"w")
	f.write(array)
	f.close()

def save(databases,nama_csv):
	folder_save = input("Masukkan nama folder penyimpanan: ")
	#tulis csv
	print("Saving...")
	
	for database in databases:
		array_to_csv(database)
	