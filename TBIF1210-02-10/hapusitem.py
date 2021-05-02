from constant import gadget, consumable, active_account, gadget_borrow_history
from login import cek_active_account

def cek_role(data): #True jika admin, False jika user
    role = data[active_account][5]
    if role == "Admin":
        return True
    else:
        return False


def db_cek(data, type):
    db_gadget = data[gadget]
    db_consumable = data[consumable]
    if type == "gadget":
        return db_gadget
    elif type == "consumable":
        return db_consumable


def cek_id(id, data, type):
    db = db_cek(data, type)
    cek = 0
    for row in range(len(db)):
        if id == db[row][0]:
            cek = 1
    if cek == 0:
        return False
    elif cek == 1:
        return True
    
    
def cek_idx(id, data, type):
    db = db_cek(data, type)
    for row in range(len(db)):
        if id == db[row][0]:
            idx = row
    return idx
    

def cek_user_borrow_history(gadget_id, data): #mengecek apakah gadget sedang dipinjam oleh user , menghasilkan true jika sedang dipinjam
    f = data[gadget_borrow_history]
    if len(f) > 1:
        for row in range(len(f)):
            if gadget_id == f[row][2] and f[row][5] == "False":
                return True
    return False

    
def hapusitem(databases):
    isLoggedin = cek_active_account(databases)
    
    if isLoggedin:        
        if cek_role(databases):
            id = input("Masukan ID item: ")
            if len(id) == 0 :
                print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
                return databases
            else:
                if id[0] == "G":
                    type = "gadget"
                    data = databases[gadget]
                elif id[0] == "C":
                    type = "consumable"
                    data = databases[consumable]
                else:
                    print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
                    return databases
            
            if cek_id(id, databases, type):
                if type == "gadget" and cek_user_borrow_history(id, databases):
                    print("\n┐(´д`)┌ : Maaf, item sedang dipinjam oleh user. Tidak dapat menghapus item!")
                else:
                    idx = cek_idx(id, databases, type)
                    name = data[idx][1]
                    while True:
                        validation = input("\n(/_\) : Apakah anda yakin ingin menghapus "+name+" yang berharga ini? (Y/N) ")
                        if validation in "YyNn" and len(validation) == 1 :
                            break
                        else:
                            print("(^_^) : Maaf, silahkan masukan Y/y untuk yes dan N/n untuk no!")
                    if validation in "Yy":
                        #proses
                        del data[idx]
                        print("\n(>_<) : Item telah dihapus dari databases!")
                    else:
                        print("\n\(^ω^)/ : Penghapusan item dibatalkan!")
            else:
                print("\n┐(´д`)┌ : Maaf, tidak ada item dengan ID tersebut!")
        else:
            print("(^_^) : Maaf, perintah ini hanya dapat diakses oleh Admin!")
    else:
        print("(^_^) : Silahkan login terlebih dahulu!")
    
    return databases