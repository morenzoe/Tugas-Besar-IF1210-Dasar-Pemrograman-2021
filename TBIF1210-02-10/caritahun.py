def printdata(data):
    # meng-output setiap data yang terdapat pada array data

    # kamus
    # data : array of string and integer { array data yang ingin ditampilkan }
    print("Nama: ", data[1])
    print("Deskripsi: ", data[2])
    print("Jumlah: ", data[3], "buah")
    print("Rarity: ", data[4])
    print("Tahun Ditemukan: ", data[5])

def caritahun(database):
    # meng-output data gadget berdasarkan tahun ditemukannya

    # kamus
    # i : integer { indeks }
    # kategori : string { input kategori yang ingin ditampilkan oleh user }
    # tahun : integer { input tahun sebagai patokan }
    # array_data : array of array of string and integer { array yang berisi data-data tanpa header }
    # database : array of array of string and integer { array yang berisi data - data dengan header }
    
    # algoritma

    array_data = database[1]
    tahun = int(input("Masukkan tahun: "))
    kategori =  (input("Masukkan kategori: ")) # input user berupa ">" , "<" , "=" , "<=" , ">="
    print("\n" + "Hasil pencarian: " + "\n")
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
    return database