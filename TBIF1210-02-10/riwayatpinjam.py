import datetime
from constant import user,gadget,active_account,gadget_borrow_history
from login import cek_active_account

def sortMaxMinTanggal(array,idx_tanggal):
    # mengurutkan array dari tanggal terbesar menuju tanggal terkecil

    # kamus

    pjg = len(array)
    if pjg > 1 :
        for Pass in range(pjg-1):
            imax = Pass
            for i in range (Pass, pjg):
                x = datetime.datetime.strptime(array[imax][idx_tanggal], "%d/%m/%Y")
                y = datetime.datetime.strptime(array[i][idx_tanggal], "%d/%m/%Y")
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
    print("\nID Peminjaman      : ", database[0])
    print("Nama Pengambil     : ", nama_user)
    print("Nama Gadget        : ", nama_gadget)
    print("Tanggal Peminjaman : ", database[3])
    print("Jumlah             : ", database[4])

def riwayatpinjam(databases):
    # menampilkan data pada "gadget_borrow_history.csv" secara berurutan berdasarkan tanggal
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        if databases[active_account][5] != "Admin" :
            print("(;-;) : Maafkan saya", databases[active_account][2] + "-san", "saya tidak dapat mengizinkan anda menggunakan command ini (anda bukan Admin).")
        else:
            print("(^.^)/ : Berikut adalah data riwayat peminjaman gadget : ")
            sorted_history = sortMaxMinTanggal(databases[gadget_borrow_history][1:],3)
            db_gadget = databases[gadget]
            db_user = databases[user]
            username = databases[active_account][1]
            awal = 0
            akhir = 5
            repeat = "y"
            while (repeat == "Y") or (repeat == "y"):
                if akhir < len(sorted_history):
                    for data in range(awal,akhir):
                        nama_user = nama_user_id(db_user, sorted_history[data][1])
                        nama_gadget = nama_gadget_id(db_gadget, sorted_history[data][2])
                        printdata(nama_user,nama_gadget,sorted_history[data])
                    awal = akhir
                    akhir += 5
                    repeat = input("(^.^) : Apakah anda ingin melihat halaman selanjutnya? (Y/N): ")
                    while (not (repeat in "YyNn") and len(repeat)!=1):
                        repeat = input("(-.-') : Input", username+"-san salah mohon masukkan input yang benar. (Y/N): ")
                elif akhir >= len(sorted_history):
                    for data in range(awal,len(sorted_history)):
                        nama_user = nama_user_id(db_user, sorted_history[data][1])
                        nama_gadget = nama_gadget_id(db_gadget, sorted_history[data][2])
                        printdata(nama_user,nama_gadget,sorted_history[data])
                    repeat = "N"
    else:
        print("(0_0): Anda belum login.")
    return databases
