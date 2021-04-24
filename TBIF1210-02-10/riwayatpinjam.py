import datetime


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
    # menghasilkan nama dari user dari id tersebut
    return database[id][2]
def nama_gadget_id(database,id):
    # menghasilkan nama gadget dari id tersebut
    for data in range(1,len(database)):
        if id == database[data][0]:
            return database[data][1]
def printdata(nama_user,nama_gadget,database):
    # mengoutput data yang bersangkutan
    print("ID Peminjaman:", database[0])
    print("Nama Pengambil:", nama_user)
    print("Nama Gadget:", nama_gadget)
    print("Tanggal Peminjaman:", database[3])
    print("Jumlah:", database[4])

def riwayatpinjam(databases):
    # menampilkan data pada "gadget_borrow_history.csv" secara berurutan berdasarkan tanggal
    if databases[6][5] == "User" :
        print("maafkan saya", databases[6][2] + "-san", "saya tidak dapat mengizinkan anda menggunakan command ini")
        return databases
    else:
        print("selamat datang", databases[6][2] + "-san", "berikut adalah data riwayat peminjaman gadget")
        print()
        sorted_history = sortMaxMinTanggal(databases[4][1:])
        db_gadget = databases[1]
        db_user = databases[0]
        username = databases[6][1]
        awal = 0
        akhir = 5
        repeat = "y"
        while (repeat == "Y") or (repeat == "y"):
            if akhir < len(sorted_history):
                for data in range(awal,akhir):
                    nama_user = nama_user_id(db_user, sorted_history[data][1])
                    nama_gadget = nama_gadget_id(db_gadget, sorted_history[data][2])
                    printdata(nama_user,nama_gadget,sorted_history[data])
                    print()
                awal = akhir
                akhir += 5
                repeat = input("Apakah anda ingin melihat halaman selanjutnya? (Y/N): ")
                print()
                while (not (repeat in "YyNn") and len(repeat)!=1):
                    repeat = input("input", username+"-san salah mohon masukkan input yang benar (Y/N): ")
                    print()
            elif akhir >= len(sorted_history):
                for data in range(awal,len(sorted_history)):
                    nama_user = nama_user_id(db_user, sorted_history[data][1])
                    nama_gadget = nama_gadget_id(db_gadget, sorted_history[data][2])
                    printdata(nama_user,nama_gadget,sorted_history[data])
                    print()
                repeat = "N"
    return databases
