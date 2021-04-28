from constant import consumable, consumable_history, active_account
from hapusitem import cek_role, cek_id, cek_idx, db_cek
from login import cek_active_account

def cek_jumlah(id, type, jumlah, data):
    db = db_cek(data, type)
    if cek_id(id, data, type):
        idx = cek_idx(id, data, type)
        if jumlah <= db[idx][3]:
            return True
        else:
            return False

def cek_kabisat(tahun):
    if(tahun % 4)==0 :
        if (tahun % 100)==0 :
            if (tahun % 400)==0 :
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
def cek_tanggal(tanggal):
    if len(tanggal) == 10 : #DD/MM/YYYY
        d = int(tanggal[0]+tanggal[1])
        m = int(tanggal[3]+tanggal[4])
        y = int(tanggal[6]+tanggal[7]+tanggal[8]+tanggal[9])
        arr31 = [1,3,5,7,8,10,12]
        arr30 = [4,6,9,11]
        if m in arr31:
            if 0 < d <= 31:
                return True
            else:
                return False
        elif m in arr30:
            if 0 < d <= 30:
                return True
            else:
                return False
        elif m == 2:
            if cek_kabisat(y):
                if 0 < d <= 29:
                    return True
                else:
                    return False
            else:
                if 0 < d <= 28:
                    return True
                else:
                    return False
        else:
            return False
    else:
        return False
    
def input_tanggal(transaksi):
    while True:
        tanggal = input(("Tanggal "+transaksi+" : "))
        if cek_tanggal(tanggal):
            break
        else:
            print("Tanggal harus memenuhi kaidah penanggalan dengan format DD/MM/YYYY")
    return tanggal

def input_jumlah(id, data, type):
    while True:
        jumlah = int(input("Jumlah: "))
        if jumlah > 0:
            while True:
                if cek_jumlah(id, type, jumlah, data):
                    break
                else:
                    print("Maaf, jumlah permintaan melebihi persediaan")
                    jumlah = int(input("Jumlah: "))
            break
        else:
            print("Jumlah pengambilan harus lebih besar dari 0!")
    return jumlah

def minta(databases):
    isLoggedin = cek_active_account(databases) 
    data = databases[consumable]
    history = databases[consumable_history]
    type = "consumable"
    
    if isLoggedin:
        user = databases[active_account]
        if cek_role(databases):
            print("Maaf, perintah ini hanya dapat diakses oleh User")
        else:
            id = input("Masukan ID item(consumable) : ")
            if id[0] == "C":
                if cek_id(id, databases, type):
                    jumlah = input_jumlah(id, databases, type)
                    tanggal = input_tanggal("permintaan")
                    #proses rewrite consumable
                    idx = cek_idx(id, databases, type)
                    name = data[idx][1]
                    recent_consumable = data[idx]
                    new_data = [id, name, recent_consumable[2], (recent_consumable[3]-jumlah), recent_consumable[4]]
                    data[idx] = new_data
                    #proses write consumable_history
                    id_ambil = len(history)
                    id_pengambil = user[0]
                    new_history = [str(id_ambil), int(id_pengambil), id, tanggal, jumlah]
                    history.append(new_history)
                    #output
                    print("Item", name, "("+str(jumlah)+") telah berhasil diambil!")
                else:
                    print("Tidak ada item dengan ID tersebut.")
            else:
                print("Tidak ada item dengan ID tersebut.")
    else:
        print("Silahkan login terlebih dahulu")
    
    return databases