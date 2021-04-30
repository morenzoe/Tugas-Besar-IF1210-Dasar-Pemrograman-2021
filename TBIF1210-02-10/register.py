# program Register

# meregister akun user ke dalam databases

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
def inputkhusus(param,data):
    # meminta kembali input user yang benar

    # kamus lokal
    # masukan : string { jika input user salah, akan dicek kembali }
    # algoritma
    print("Masukkan", param, "anda : ", end ='')
    masukan = input()

    if param == "username":
        while not check_username(masukan,data) or checkdelimit(masukan):
            print("username tersebut sudah diambil atau salah (╥﹏╥)")
            masukan = input("berikan nama username yang belum ada dan benar (づ￣ ³￣)づ : ")
    else:
        while checkdelimit(masukan):
            print("masukan anda salah UwU")
            masukan = input("mohon beri masukan yang benar (9^-^)9 : ")
    if param == "nama":
        masukan = masukan.title()
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
            data = array_data[1:]
            print("dilarang menggunakan karakter ; dalam penginputan")
            nama = inputkhusus("nama",data)
            username = inputkhusus("username",data)
            password = inputkhusus("password",data)
            alamat = inputkhusus("alamat",data)
            Id = str(len(data) +1)
            role = "User"
            new_data = [Id,username,nama,alamat,password,role]
            databases[user].append(new_data)
            print("User", username, "telah berhasil register ke dalam Kantong Ajaib")
        else:
            print("maafkan saya", databases[6][1] + "-san, tetapi anda tidak berhak mengakses command ini (anda bukanlah Admin) 〒_〒")
    else:
        print("Maaf tapi anda belum login 〒_〒")
    return databases

#python kantongajaib.py CSVs