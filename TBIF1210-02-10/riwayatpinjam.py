# prosedur akhir
def sortMaxMinTanggal(array):
    # mengurutkan array dari tanggal terbesar menuju tanggal terkecil

    # kamus

    pjg = len(array)
    if pjg > 1 :
        for Pass in range(pjg-1):
            imax = Pass
            for i in range (Pass, pjg):
                x = datetime.datetime.strptime(array[imax][3], "%d/%m/%Y")
                y = datetime.datetime.strptime(array[i][3], "%d/%m/%Y")
                if (x < y):
                    imax = i
            array[imax],array[Pass]=array[Pass],array[imax]
    return array
def nama_user_id(database,id):
    for data in range(1,len(database)):
        if id == database[data][0]:
            return database[data][2]
def nama_gadget_id(database,id):
    for data in range(1,len(database)):
        if id == database[data][0]:
            return database[data][1]
def printdata(nama_user,nama_gadget,database):
    print("ID Peminjaman:", database[0])
    print("Nama Pengambil:", nama_user)
    print("Nama Gadget:", nama_gadget)
    print("Tanggal Peminjaman:", database[3])
    print("Jumlah:", database[4])
def riwayatpinjam(databases):
    if databases[6][5] == "User" :
        print("maafkan saya", databases[6][2] + "-san", "saya tidak dapat mengizinkan anda menggunakan command ini")
        return databases
    else:
        print("selamat datang", databases[6][2] + "-san", "berikut adalah data riwayat peminjaman gadget")
        data_sorted = sortMaxMinTanggal(databases[1])
        awal = 1
        akhir = 6
        repeat = "y"
        while ((repeat == "y") or (repeat == "Y")):
            if akhir < len(data_sorted):
                for data in range(awal,akhir):
                    printdata(nama_user_id(databases[0],data_sorted[i][0]),(nama_gadget_id(databases[0],data_sorted[i][0])), data_sorted)
                repeat = input("apakah anda ingin melihat selanjutnya 5 data selanjutnya", database[6][2] + "-san ?")
                if (repeat == "y") or (repeat == "Y"):
                    awal = akhir
                    akhir = akhir + 5
            elif akhir >= len(data_sorted):
                for data in range(awal,len(data_sorted)):
                    printdata(nama_user_id(databases[0],data_sorted[i][0]),(nama_gadget_id(databases[0],data_sorted[i][0])), data_sorted)
    return databases