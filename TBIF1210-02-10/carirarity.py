from constant import gadget,active_account
from login import cek_active_account

def printdata(data):
    # meng-output setiap data yang terdapat pada array data

    # kamus
    # data : array of string and integer { array data yang ingin ditampilkan }
    print("\nNama            : ", data[1])
    print("Deskripsi       : ", data[2])
    print("Jumlah          : ", data[3], "buah")
    print("Rarity          : ", data[4])
    print("Tahun Ditemukan : ", data[5])

def carirarity(database):
    # meng-output data berdasarkan rarity yang dipilih

    # kamus
    # i : integer { indeks }
    # rarity : string { input rarity yang ingin ditampilkan oleh user }
    # array_data : array of array of string and integer { array yang berisi data-data tanpa header }
    # database : array of array of string and integer { array yang berisi data - data dengan header }

    # algoritma
    isLoggedIn = cek_active_account(database)
    if isLoggedIn:
        username = database[active_account][2]
        array_data = database[1]
        rarity = input("Masukkan rarity : ")
        while rarity not in "CBAScbas" or len(rarity) != 1:
            rarity = input("Masukkan rarity dengan benar! :")
        rarity = rarity.title()
        print("\nHasil pencarian : ")
        if len(array_data) == 1:
            print("Tidak ada data pada gadget.csv, maafkan admin!")
        else:
            for data in range(len(array_data)):
                if (array_data[data-1][4] == rarity):
                    printdata(array_data[data-1])
    else:
        print("\(>_<)/ : Anda belum login.")
    return database