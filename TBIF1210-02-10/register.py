# Register

# meregister akun user ke dalam sistem

# Kamus
def check_username(username,data):
    # mengecek apakah username input sudah ada atau belum pada data
    # kamus
    # i : integer { indeks }
    # data : array of array of string and integer
    # username : string
    # check = integer
    check = 0
    for i in range(len(data)):
        if (data[i][1] == username):
            check = 1
    if (check == 0):
        return True
    else: #check = 1
        return False
def checkdelimit(check):
    # mengecek apakah dalam input user terdapat ; dalam input user
    
    # kamus
    # i : integer { indeks }
    # check : string { yang ingin dicek }
    # algoritma
	if ";" in check:
		return True
	else:
		return False
	


def register(databases):
    # Fungsi utama dari register

    # Kamus lokal
    # i : integer {sebagai indeks}
    # head : array of string { header pada file data }
    # nama, username, alamat, password : string {masukan nama user}
    # id : integer {dibuat otomatis oleh sistem}
    # role : string { dibuat secara default oleh sistem sebagai user. sehingga register hanya menghasilkan role user }
    # new_data : array of string
    # data : array of array of string and integer { data pada file data }

    # algoritma
	
	# cek dulu role akun aktif
	# di atas ketik from constant import user, active_account 
	#role = databases[active_account][5]
    role = databases[6][5]
    if role == "Admin":
        array_data = databases[0] # databases[user]
        head = array_data.pop(0)
        data = array_data
        print("dilarang menggunakan karakter ; dalam penginputan")
        nama = input("Masukkan nama: ")
        while checkdelimit(nama):
            print("umm.. b-baka (///).")
            nama = input("umm.. ma-masukkan namamu dengan benar : ")
        nama = nama.title()
        username = input("Masukkan username: ")
        while ((check_username(username,data) == False) or (checkdelimit(username))):
            print("username sudah diambil atau salah")
            username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        while checkdelimit(password):
            print("bu-bukannya aku perhatian dengan mu tapi")
            password = input("masukkan password mu tanpa ';' : ")
        alamat = input("Masukkan alamat: ")
        while checkdelimit(alamat):
            print("ara.. so you have chosen death", nama + "-san")
            alamat = input("masukkan alamat tanpa tanda ';' untuk menghindari serangan yandere: ")
        id = len(data) +1
        role = "User"
        new_data = [id,username,nama,alamat,password,role]
        data.append(new_data)
        array_data = [head] + data
        databases[0] = array_data
        print("User", username, "telah berhasil register ke dalam Kantong Ajaib")
        return databases
    else:
        print("maafkan saya", databases[6][1] + "-san, tetapi anda tidak berhak mengakses command ini")
        return databases