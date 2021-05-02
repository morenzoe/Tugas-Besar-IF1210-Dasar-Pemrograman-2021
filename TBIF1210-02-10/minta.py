"""Program F10 - Mengambil Consumable
Fungsi ini akan mengambil input id consumable yang ingin diminta,
input jumlah dan tanggal. Pengambilan berhasil jika semua input
valid. Setelah melakukan pengambilan, jumlah id tersebut pada file 
consumable akan diubah. Lalu, dibuat entri baru pada file riwayat consumable.

Akses : User
"""

# KAMUS
# Daftar library lokal
from constant import consumable, consumable_history, active_account
from hapusitem import cek_role, cek_id, cek_idx
from pinjam import input_jumlah, input_tanggal
from login import cek_active_account

# Daftar variabel
# databases     : array of array of array
# data          : array of array
# history	    : array of array
# isLoggedIn	: bool
# type          : str
# id            : str		
# name          : str
# id_pengambil	: str
# idx           : int				
# id_ambil      : int
# stock			: int
# user          : array
# new_history	: array 

# ALGORITMA PROGRAM UTAMA
def minta(databases):
    isLoggedIn = cek_active_account(databases) 
    type = "consumable"    
    data = databases[consumable]
    history = databases[consumable_history]
    # Validasi login
    if isLoggedIn:
        user = databases[active_account]
        # Validasi role
        if cek_role(databases):
            print("(^_^) : Maaf, perintah ini hanya dapat diakses oleh User!")
        else:
            id = input("Masukan ID item      : ")
            # Validasi id
            if (len(id)) <= 1:
                print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
            else:
                if id[0] == "C":
                    if cek_id(id, databases, type):
                        idx = cek_idx(id, databases, type)
                        stock = data[idx][3]
                        name = data[idx][1]
                        if stock != 0:
                            jumlah = input_jumlah(id, databases, type)
                            if jumlah != 0:
                                tanggal = input_tanggal("permintaan  ")
                                if tanggal != 0:
                                    # Proses rewrite consumable                                    
                                    stock = stock - jumlah
                                    data[idx][3] = stock
                                    
                                    # Proses write consumable_history
                                    id_ambil = len(history)
                                    id_pengambil = user[0]
                                    new_history = [str(id_ambil), int(id_pengambil), id, tanggal, jumlah]
                                    history.append(new_history)
                                    
                                    # Output
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