from constant import user

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
		databases.append(row)
		print("Login berhasil!")
	else:
		print("Login gagal! Username atau password salah.") 
		# mungkin nanti bisa dipisah. find buat username, setelah itu baru bandingin lagi passwordnya
		
	return databases
