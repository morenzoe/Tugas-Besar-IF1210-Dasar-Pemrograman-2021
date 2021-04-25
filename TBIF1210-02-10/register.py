# program Register

# meregister akun user ke dalam sistem

# Kamus
from constant import user,active_account
from login import cek_active_account
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
    
    # kamus lokal
    # check : string { yang ingin dicek }
    # algoritma
	if ";" in check:
		return True
	else:
		return False
def ubahinput(masukan):
    # meminta kembali input user yang benar

    # kamus lokal
    # masukan : string { jika input user salah, akan dicek kembali }
    # algoritma
    while checkdelimit(masukan):
        print("masukan anda salah UwU")
        masukan = input("mohon beri masukan yang benar (9^-^)9 : ")
    return masukan

    


def register(databases):
    # Fungsi utama dari register

    # Kamus lokal
    # i : integer {sebagai indeks}
    # head : array of string { header pada file data }
    # nama, username, alamat, password : string {masukan nama user}
    # Id : integer {dibuat otomatis oleh sistem}
    # role : string { dibuat secara default oleh sistem sebagai user. sehingga register hanya menghasilkan role user }
    # new_data : array of string
    # data : array of array of string and integer { data pada file data }

    # algoritma
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        role = databases[active_account][5]
        if role == "Admin":
            array_data = databases[user]
            head = array_data.pop(0)
            data = array_data
            print("dilarang menggunakan karakter ; dalam penginputan")
            nama = input("Masukkan nama: ")
            nama = ubahinput(nama)
            nama = nama.title()
            username = input("Masukkan username: ")
            while ((check_username(username,data) == False) or (checkdelimit(username))):
                print("username sudah diambil atau salah")
                username = input("Masukkan username: ")
            password = input("Masukkan password: ")
            password = ubahinput(password)
            alamat = input("Masukkan alamat: ")
            alamat = ubahinput(alamat)
            Id = len(data) +1
            role = "User"
            new_data = [Id,username,nama,alamat,password,role]
            data.append(new_data)
            array_data = [head] + data
            databases[user] = array_data
            print("User", username, "telah berhasil register ke dalam Kantong Ajaib")
        else:
            print("maafkan saya", databases[6][1] + "-san, tetapi anda tidak berhak mengakses command ini")
    else:
        print("Maaf tapi anda belum login")
    return databases