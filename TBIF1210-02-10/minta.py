from datetime import datetime as dtm
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

    
def input_tanggal(transaksi):
    date_input = input("Tanggal "+transaksi+" : ")
    try:
        tanggal = dtm.strptime(date_input , '%d/%m/%Y' )
        return date_input
    except:
        return 0
 
 
def input_jumlah(id, data, type):
    while True:
        count_input = input("Jumlah               : ")
        try:
            count = int(count_input)
        except:
            return 0
        if count > 0:
            if cek_jumlah(id, type, count, data):
                break
            else:
                print("Maaf, jumlah melebihi persediaan")
        else:
            print("Jumlah harus lebih besar dari 0!")
    return count


def minta(databases):
    isLoggedin = cek_active_account(databases) 
    data = databases[consumable]
    history = databases[consumable_history]
    type = "consumable"
    
    if isLoggedin:
        user = databases[active_account]
        if cek_role(databases):
            print("(^_^) : Maaf, perintah ini hanya dapat diakses oleh User!")
        else:
            id = input("Masukan ID item      : ")
            if (len(id)) == 0 :
                print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
            else:
                if id[0] == "C" and len(id) != 1:
                    if cek_id(id, databases, type):
                        idx = cek_idx(id, databases, type)
                        stock = data[idx][3]
                        name = data[idx][1]
                        if stock != 0:
                            jumlah = input_jumlah(id, databases, type)
                            if jumlah != 0:
                                tanggal = input_tanggal("permintaan  ")
                                if tanggal != 0:
                                    #proses rewrite consumable                                    
                                    stock = stock - jumlah
                                    data[idx][3] = stock
                                    #proses write consumable_history
                                    id_ambil = len(history)
                                    id_pengambil = user[0]
                                    new_history = [str(id_ambil), int(id_pengambil), id, tanggal, jumlah]
                                    history.append(new_history)
                                    #output
                                    print("\n\(^ω^)/ : Item", name, "("+str(jumlah)+") telah berhasil diambil!")
                                else:
                                    print("\n┐(´д`)┌ : Maaf, input tanggal tidak sesuai format dd/mm/yyyy!")
                            else:
                                print("\n┐(´д`)┌ : Maaf, input jumlah tidak valid!")
                        else:
                            print("\n(>_<) : Maaf, persediaan habis!")
                    else:
                        print("\n┐(´д`)┌ : Maaf, tidak ada item dengan ID tersebut!")
                else:
                    print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
    else:
        print("(^_^) : Silahkan login terlebih dahulu!")
    
    return databases