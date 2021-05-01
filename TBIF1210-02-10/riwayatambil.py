# prosedur akhir
import datetime
from riwayatpinjam import sortMaxMinTanggal
from login import cek_active_account
from constant import gadget,user,consumable_history,active_account,consumable
def nama_user_id(database,id):
    # menghasilkan nama dari user dari id tersebut
    return database[id][2]
def nama_consumeable_id(database,id):
	for data in range(1,len(database)):
		if id == database[data][0]:
			return database[data][1]
def printdata(nama_user,nama_consumeable,database):
    # mengoutput data yang bersangkutan
    print("\nID Peminjaman       : ", database[0])
    print("Nama Pengambil      : ", nama_user)
    print("Nama consumeable    : ", nama_consumeable)
    print("Tanggal Pengambilan : ", database[3])
    print("Jumlah              : ", database[4])

def riwayatambil(databases):
    # menampilkan data pada "consumeable_borrow_history.csv" secara berurutan berdasarkan tanggal
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        if databases[active_account][5] != "Admin" :
            print("(;-;) : Maafkan saya", databases[active_account][2] + "-san", "saya tidak dapat mengizinkan anda menggunakan command ini (anda bukan Admin).")
        else:
            print("(^.^)/ : Berikut adalah data riwayat peminjaman consumeable: ")
            sorted_history = sortMaxMinTanggal(databases[consumable_history][1:],3)
            db_consumeable = databases[consumable]
            db_user = databases[user]
            username = databases[active_account][1]
            awal = 0
            akhir = 5
            repeat = "y"
            while (repeat == "Y") or (repeat == "y"):
                if akhir < len(sorted_history):
                    for data in range(awal,akhir):
                        nama_user = nama_user_id(db_user, sorted_history[data][1])
                        nama_consumeable = nama_consumeable_id(db_consumeable, sorted_history[data][2])
                        printdata(nama_user,nama_consumeable,sorted_history[data])
                    awal = akhir
                    akhir += 5
                    repeat = input("('.') : Apakah anda ingin melihat halaman selanjutnya? (Y/N): ")
                    while (not (repeat in "YyNn") or len(repeat)!=1):
                        repeat = input("(-.-') : Input salah mohon. Masukkan input yang benar. (Y/N): ")
                elif akhir >= len(sorted_history):
                    for data in range(awal,len(sorted_history)):
                        nama_user = nama_user_id(db_user, sorted_history[data][1])
                        nama_consumeable = nama_consumeable_id(db_consumeable, sorted_history[data][2])
                        printdata(nama_user,nama_consumeable,sorted_history[data])
                    repeat = "N"
    else:
        print("(=_=) : Anda belum login.")
    return databases