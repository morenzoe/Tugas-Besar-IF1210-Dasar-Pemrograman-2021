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
    array_data = databases[0]
    head = array_data.pop(0)
    data = array_data
    nama = input("Masukkan nama: ")
    nama = nama.title()
    username = input("Masukkan username: ")
    while (check_username(username,data) == False):
        print("username sudah diambil")
        username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    alamat = input("Masukkan alamat: ")
    id = len(data) +1
    role = "User"
    new_data = [id,username,nama,alamat,password,role]
    data.append(new_data)
    array_data = [head] + data
    databases[0] = array_data
    print("User", username, "telah berhasil register ke dalam Kantong Ajaib")
    return databases
