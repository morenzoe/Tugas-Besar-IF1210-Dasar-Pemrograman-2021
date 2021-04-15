def caritahun(database):
    array_data = database.pop(0)
    def printdata(data):
        print("Nama: ", data[1])
        print("Deskripsi: ", data[2])
        print("Jumlah: ", data[3], "buah")
        print("Rarity: ", data[4])
        print("Tahun Ditemukan: ", data[5])
    tahun = int(input("Masukkan tahun: "))
    kategori = str(input("Masukkan kategori: "))
    print("\n" + "Hasil pencarian: " + "\n")
    if (kategori == ">"):
        for data in array_data:
            if ((array_data[data][5]) > tahun) :
                printdata(array_data[data])
    elif (kategori == "="):
        for data in array_data:
            if ((array_data[data][5]) == tahun) :
                printdata(array_data[data])
    elif (kategori == "<"):
        for data in array_data:
            if ((array_data[data][5]) < tahun) :
                printdata(array_data[data])
    elif (kategori == ">="):
        for data in array_data:
            if ((array_data[data][5]) >= tahun) :
                printdata(array_data[data])
    elif (kategori == "<="):
        for data in array_data:
            if ((array_data[data][5]) <= tahun) :
                printdata(array_data[data])