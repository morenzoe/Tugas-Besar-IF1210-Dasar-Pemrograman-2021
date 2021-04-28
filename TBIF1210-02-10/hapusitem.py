from constant import gadget,consumable,active_account
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
    for row in range(len(db)):
        if id == db[row][0]:
            return True
    return False
    
def cek_idx(id, data, type):
    db = db_cek(data, type)
    for row in range(len(db)):
        if id == db[row][0]:
            idx = row
    return idx

def hapusitem(databases):
    isLoggedin = cek_active_account(databases)
    
    if isLoggedin:        
        if cek_role(databases):
            id = input("Masukan ID item: ")
            if id[0] == "G":
                type = "gadget"
                data = databases[gadget]
            elif id[0] == "C":
                type = "consumable"
                data = databases[consumable]
            else:
                print("Tidak ada item dengan ID tersebut.")
                return databases
            
            if cek_id(id, databases, type):
               idx = cek_idx(id, databases, type)
               name = data[idx][1]
               while True:
                   validation = input("Apakah anda yakin ingin menghapus "+name+" (Y/N)? ")
                   if validation in "YyNn" and len(validation) == 1 :
                       break
               if validation in "Yy":
                  #proses
                  del data[idx]
                  print("Item telah berhasil dihapus dari database")
               else:
                   print("Penghapusan item dibatalkan")
            else:
                print("Tidak ada item dengan ID tersebut.")
        else:
            print("Maaf, perintah ini hanya dapat diakses oleh Admin")
    else:
        print("Silahkan login terlebih dahulu")
    
    return databases