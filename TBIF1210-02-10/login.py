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
	
    find_username = False
    find_password = False

    for row in file:
        if row[1] == username :
            find_username = True
            if row[4] == password:
                find_password = True
                break
            else :
                find_password = False
                break
        else:
            find_username = False
			
			
    if find_username == True and find_password == True :
        databases[active_account] = row
        print("Login berhasil!")
    elif find_username == False :
        print("Login gagal! Username kamu tidak ditemukan.")
               
    else :
        print("Login gagal! Password kamu salah.") 
		
	return databases
