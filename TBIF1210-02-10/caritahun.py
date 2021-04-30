from login import cek_active_account
from constant import gadget


def printdata(data):
    # meng-output setiap data yang terdapat pada array data

    # kamus
    # data : array of string and integer { array data yang ingin ditampilkan }
    print("\nNama            : ", data[1])
    print("Deskripsi       : ", data[2])
    print("Jumlah          : ", data[3], "buah")
    print("Rarity          : ", data[4])
    print("Tahun Ditemukan : ", data[5])

def ubahtahun(tahun_str):
    # mengubah input tahun menjadi integer jika bisa, jika tidak bisa akan diminta kembali dari input user

    # kamus
    # algoritma
    check = 0
    while check == 0:
        if len(tahun_str)==4:
            for i in range(len(tahun_str)):
                if tahun_str[i] in "0123456789":
                    check = 1
        else:
            tahun_str = input("Masukan salah! Masukkan tahun dengan benar!: ")
    return int(tahun_str)

def ubahkategori(kategori):
    # meminta input user untuk kategori jika input user salah

    #kamus
    #algoritma
    while not(kategori == ">" or kategori == "<" or kategori == "=" or kategori == ">=" or kategori == "<="):
        kategori = input("Masukan salah! Masukkan kategori dengan benar! : ")
    return kategori
def caritahun(database):
    # meng-output data gadget berdasarkan tahun ditemukannya

    # kamus
    # i : integer { indeks }
    # kategori : string { input kategori yang ingin ditampilkan oleh user }
    # tahun : integer { input tahun sebagai patokan }
    # array_data : array of array of string and integer { array yang berisi data-data tanpa header }
    # database : array of array of string and integer { array yang berisi data - data dengan header }
    
    # algoritma
    isLoggedIn = cek_active_account(database)
    if isLoggedIn:
        array_data = database[gadget]
        tahun_str = input("Masukkan tahun    : ")
        tahun = ubahtahun(tahun_str)
        kategori =  (input("Masukkan kategori : ")) # input user berupa ">" , "<" , "=" , "<=" , ">="
        kategori = ubahkategori(kategori)
        print("\nHasil pencarian :")
        if (kategori == ">"):
            for data in range(1,len(array_data)):
                if (int(array_data[data][5]) > tahun) :
                    printdata(array_data[data])
        elif (kategori == "="):
            for data in range(1,len(array_data)):
                if (int(array_data[data][5]) == tahun) :
                    printdata(array_data[data])
        elif (kategori == "<"):
            for data in range(1,len(array_data)):
                if (int(array_data[data][5]) < tahun) :
                    printdata(array_data[data])
        elif (kategori == ">="):
            for data in range(1,len(array_data)):
                if (int(array_data[data][5]) >= tahun) :
                    printdata(array_data[data])
        elif (kategori == "<="):
            for data in range(1,len(array_data)):
                if (int(array_data[data][5]) <= tahun) :
                    printdata(array_data[data])
    else:
        print("(+.+) : Anda belum login.")
    return database