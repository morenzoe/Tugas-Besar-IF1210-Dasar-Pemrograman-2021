from constant import gadget, active_account, gadget_borrow_history
from hapusitem import cek_role, cek_id, cek_idx
from minta import input_jumlah, input_tanggal
from login import cek_active_account

def cek_borrow_history(gadget_id, data): #mengecek apakah user pernah meminjam gadget yg sama, menghasilkan true jika sudah pernah meminjam
    id = data[active_account][0]
    f = data[gadget_borrow_history]
    for row in range(len(f)):
        if int(id) == f[row][1] and gadget_id == f[row][2] and f[row][5] == "False":
            return True
    return False
    
    
def pinjam(databases):
    isLoggedin = cek_active_account(databases)
    data = databases[gadget]
    history = databases[gadget_borrow_history]
    type = "gadget"
    
    if isLoggedin:
        user = databases[active_account]
        if cek_role(databases):
            print("(^_^) : Maaf, perintah ini hanya dapat diakses oleh User!")
        else:
            id = input("Masukan ID item      : ")
            if len(id) == 0:
                print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
            else:
                if id[0] == "G" and len(id) != 1 :
                    if cek_id(id, databases, type):
                        if cek_borrow_history(id, databases):
                            print("\n(^o^) : Anda sedang meminjam gadget tersebut!")
                        else:
                            #proses
                            tanggal = input_tanggal("peminjaman  ")
                            if tanggal != 0:
                                jumlah = input_jumlah(id, databases, type)
                                if jumlah != 0:
                                    #proses rewrite gadget
                                    idx = cek_idx(id, databases, type)
                                    name = data[idx][1]
                                    recent_gadget = data[idx]
                                    new_data = [id, name, recent_gadget[2], (recent_gadget[3]-jumlah), recent_gadget[4], recent_gadget[5]]
                                    data[idx] = new_data
                                    #proses write consumable_history
                                    id_pinjam = len(history)
                                    id_peminjam = user[0]
                                    is_returned = "False"
                                    new_history = [str(id_pinjam), int(id_peminjam), id, tanggal, jumlah, is_returned]
                                    history.append(new_history)
                                    #output
                                    print("\n\(^ω^)/ : Item", name, "("+str(jumlah)+") telah berhasil dipinjam!")
                                else:
                                    print("\n┐(´д`)┌ : Maaf, input jumlah tidak valid!")
                            else:
                                print("\n┐(´д`)┌ : Maaf, input tanggal tidak sesuai format dd/mm/yyyy!")
                    else:
                        print("\n┐(´д`)┌ : Maaf, tidak ada item dengan ID tersebut!")
                else:
                    print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
    else:
        print("(^_^) : Silahkan login terlebih dahulu!")
    
    return databases