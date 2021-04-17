def printdata(data):
    # meng-output setiap data yang terdapat pada array data

    # kamus
    # data : array of string and integer { array data yang ingin ditampilkan }
    print("Nama: ", data[1])
    print("Deskripsi: ", data[2])
    print("Jumlah: ", data[3], "buah")
    print("Rarity: ", data[4])
    print("Tahun Ditemukan: ", data[5])

def carirarity(database):
    # meng-output data berdasarkan rarity yang dipilih

    # kamus
    # i : integer { indeks }
    # rarity : string { input rarity yang ingin ditampilkan oleh user }
    # array_data : array of array of string and integer { array yang berisi data-data tanpa header }
    # database : array of array of string and integer { array yang berisi data - data dengan header }

    # algoritma
    array_data = database[1]
    rarity = input("Masukkan rarity: ")
    print("\n" + "Hasil pencarian: " + "\n")
    if len(array_data) == 1:
        print("Tidak ada data pada gadget.csv, maafkan admin hu-hu~")
    else:
        for data in range(len(array_data)):
            if (array_data[data-1][4] == rarity):
                printdata(array_data[data-1])
    return database