"""Program F06 - Menghapus Gadget atau Consumable
Fungsi ini akan meminta input id item (gadget atau consumable)
yang ingin dihapus. Lalu, meminta validasi penghapusan. Jika,
penghapusan dilakukan maka entri id tersebut pada file gadget
atau consumable akan dihapus.

Akses : Admin
"""

# KAMUS
# Daftar library lokal
from constant import gadget, consumable, active_account, gadget_borrow_history
from login import cek_active_account

# Daftar variabel
# databases  : array of array of array
# isLoggedIn : bool
# id         : str
# type       : str
# data	     : array of array
# idx		 : int
# name		 : str

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def cek_role(databases):
    """Fungsi ini akan menghasilkan True
    jika active_account adalah admin, dan
    False jika user.
    """
    
    # KAMUS LOKAL
    # role : str

    # ALGORITMA
    role = databases[active_account][5]
    if role == "Admin":
        return True
    else:
        return False


def db_cek(databases, type):
    """Fungsi ini akan menghasilkan databases[gadget] 
    apabila type “gadget”, dan menghasilkan 
    databases[consumable] apabila type “consumable”
    """
    
    # KAMUS LOKAL
    # db_gadget     : array of array
    # db_consumable : array of array

    # ALGORITMA
    db_gadget = databases[gadget]
    db_consumable = databases[consumable]
    if type == "gadget":
        return db_gadget
    elif type == "consumable":
        return db_consumable


def cek_id(id, databases, type):
    """Fungsi ini akan enghasilkan 
    True apabila id type terdapat 
    pada databases[type]
    """
    
    # KAMUS LOKAL
    # db  : array of array
    # row : int
    
    # ALGORITMA
    db = db_cek(databases, type)
    for row in range(len(db)):
        if id == db[row][0]:
            return True
    return False
    
    
def cek_idx(id, databases, type):
    """Fungsi ini akan menghasilkan 
    index baris dari databases[type] 
    yang memuat id yang sama
    """
    
    # KAMUS LOKAL
    # db  : array of array
    # row : int
    # idx : int
    
    # ALGORITMA
    db = db_cek(databases, type)
    for row in range(len(db)):
        if id == db[row][0]:
            idx = row
    return idx
    

def cek_user_borrow_history(gadget_id, databases):
    """Fungsi ini akan menghasilkan true 
    apabila terdapat gadget_id pada 
    databases[gadget_borrow_history]
    """
    
    # KAMUS LOKAL
    # db  : array of array
    # row : int
    
    # ALGORITMA
    db = databases[gadget_borrow_history]
    if len(db) > 1:
        for row in range(len(db)):
            if gadget_id == db[row][2] and db[row][5] == "False":
                return True
    return False

# ALGORITMA PROGRAM UTAMA    
def hapusitem(databases):
    isLoggedIn = cek_active_account(databases)
    # Validasi login
    if isLoggedIn:        
        # Validasi role
        if cek_role(databases):
            id = input("Masukan ID item : ")
            # Validasi id
            if len(id) <= 1 :
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
            # Pengecekan keberadaan id pada data
            if cek_id(id, databases, type):
                if type == "gadget" and cek_user_borrow_history(id, databases):
                    print("\n┐(´д`)┌ : Maaf, item sedang dipinjam oleh user. Tidak dapat menghapus item!")
                else:
                    idx = cek_idx(id, databases, type)
                    name = data[idx][1]
                    # Meminta validasi yes no untuk penghapusan
                    while True:
                        validation = input("\n(/_\) : Apakah anda yakin ingin menghapus "+name+" yang berharga ini? (Y/N) ")
                        if validation in "YyNn" and len(validation) == 1 :
                            break
                        else:
                            print("(^_^) : Maaf, silahkan masukan Y/y untuk yes dan N/n untuk no!")
                    if validation in "Yy":
                        
                        # Proses menghapus entri id pada database[type]
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