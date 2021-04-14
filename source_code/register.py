# nanti tolong diedit ya fungsinya
# jadi edit list aja di dalem fungsi ini
# trus jangan ada def di dalem def, taro di luar aja 
# fungsi input() udah otomatis string, jadi gausah pake str()

def split(string, delimiters):
    result = []
    word = ''
    for c in string:
        if c not in delimiters:
            word += c
        elif word:
            result.append(word)
            word = ''

    if word:
        result.append(word)

    return result
def check_username(username,data):
    check = 0
    for i in range(len(data)):
        if (data[i][1] == username):
            check = 1
    if (check == 0):
        return True
    else: #check = 1
        return False
def data_user():
    f=open("user.csv","r")
    raw_lines = f.readlines()
    f.close()
    lines = [raw_line.replace("\n","") for raw_line in raw_lines]
    array_of_data_user = [split(line,",;") for line in lines]
    header = array_of_data_user[0]
    array_of_data_user.pop(0)
    return header, array_of_data_user
def conv_data_string(header,data):
    string_data = ",".join(header) + "\n"
    for arr_data in data:
        arr_data_all_string = [str(var) for var in arr_data]
        string_data += ",".join(arr_data_all_string)
        string_data += "\n"
    return string_data
def register(array_data): # array data nanti bisa diganti jadi user
    def register_save(new_data):
        f = open("user.csv","w")
        f.write(new_data)
        f.close()
    def check_username(username,data):
        check = 0
        for i in range(len(data)):
            if (data[i][1] == username):
                check = 1
        if (check == 0):
            return True
        else: #check = 1
            return False
    head, data = array_data
    nama = str(input("Masukkan nama: "))
    nama = nama.title()
    username = str(input("Masukkan username: "))
    while (check_username(username,data) == False):
        print("username sudah diambil")
        username = str(input("Masukkan username: "))
    password = str(input("Masukkan password: "))
    alamat = str(input("Masukkan alamat: "))
    id = len(data) +1
    role = "User"
    new_data = [id,username,nama,alamat,password,role]
    data.append(new_data)
    print("User", username, "telah berhasil register ke dalam Kantong Ajaib")
    register_save(conv_data_string(head,data))

register(data_user())