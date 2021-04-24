from constant import user
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

	find_u = False
	find_p = False

	for row in file:
		if row[1] == username :
                        find_u = True
                        if row[4] == password:
                                find_p = True
                                break
                        else :
                                find_p = False
		else:
			find_u = False
			break
			
	if find_u == True and find_p == True :
		databases.append(row)
		print("Login berhasil!")
	elif find_u == False :
                print("Login gagal! Username kamu tidak ditemukan.")
                
	else :
		print("Login gagal! Password kamu salah.") 
		# mungkin nanti bisa dipisah. find buat username, setelah itu baru bandingin lagi passwordnya
		
	return databases
