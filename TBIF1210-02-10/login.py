from constant import user,active_account

def cek_active_account(databases):
	jumlah_data = len(databases[active_account])
	if jumlah_data != 0:
		return True
	else:
		return False
		
# prosedur akhir
def login(databases):
	username = input("Ketik username : ")
	password = input("Ketik password : ")

	file = databases[user]

	find = False

	for row in file:
		if row[1] == username and row[4] == password:
			find = True
			break
		else:
			find = False
	if find == True :
		databases[active_account] = row
		print("Login berhasil!")
	else:
		print("Login gagal! Username atau password salah.") 
		# mungkin nanti bisa dipisah. find buat username, setelah itu baru bandingin lagi passwordnya
		
	return databases
