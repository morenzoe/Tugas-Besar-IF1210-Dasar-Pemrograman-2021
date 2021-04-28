from constant import gadget,consumable,active_account
from login import cek_active_account

def cekid(ID,data):
    cek = 0
    for i in range(len(data)):
        if data[i][0]==ID :
            cek = 1
    if cek == 1 :
        return True
    else:
        return False      

def cekdelimit(cek):
	if ";" in cek:
		return True
	else:
		return False

def ubah(ID,data,jumlah):
    for i in range (len(data)):
        if data[i][0] == ID :
            idx = i

    stok = data[idx][3] + jumlah
        
    if stok >= 0 :
        data[idx][3] = stok
    else :
        data[idx][3] = stok - jumlah

    if stok < 0 :
        print(jumlah, data[idx][1], "gagal dibuang karena stok kurang. Stok sekarang : ", (data[idx][3]))
    else :
        if jumlah >= 0 :
            print(jumlah , (data[idx][1]) , "berhasil ditambahkan. Stok sekarang : ",(data[idx][3]))
        else :
            print(jumlah , (data[idx][1]) , "berhasil dibuang. Stok sekarang : ",(data[idx][3]))

        
# prosedur akhir
def ubahjumlah(databases):
    db_gadget = databases[gadget]
    file_gadget = db_gadget
    db_consumable = databases[consumable]
    file_consumable = db_consumable

    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        if databases[active_account][5] == "Admin":
            ID = input("Masukan ID : ")
            pjgID = len(ID)        
            if pjgID == 0:
                print("Gagal mengubah jumlah karena ID tidak valid.")
            else :
                if ID[0] == "G" :
                    if pjgID == 1 :
                        print("Gagal mengubah jumlah karena ID gadget tidak valid.")
                        return databases
                    else :
                        Id = ID.replace('G','')
                        try :
                            Id = int(Id)
                        except :
                            print("Gagal mengubah jumlah karena ID gadget tidak valid.")
                            return databases
                        
                        if cekid(ID,file_gadget):
                            jumlah = input("Masukan Jumlah : ")
                            try :
                                jumlah = int(jumlah)
                            except :
                                print("Jumlah tidak valid. Jumlah harus bilangan bulat.")
                                return databases
                            ubah(ID,file_gadget,jumlah)
                        else :
                            print("Gagal mengubah jumlah karena ID gadget tidak ditemukan.")
                            return databases
                elif ID[0] == "C" :
                    if pjgID == 1 :
                        print("Gagal mengubah jumlah karena ID consumable tidak valid.")
                        return databases
                    else :
                        Id = ID.replace('C','')
                        try :
                            Id = int(Id)
                        except :
                            print("Gagal mengubah jumlah karena ID consumable tidak valid.")
                            return databases
                    
                        if cekid(ID,file_consumable):
                            jumlah = input("Masukan Jumlah : ")
                            try :
                                jumlah = int(jumlah)
                            except :
                                print("Jumlah tidak valid. Jumlah harus bilangan bulat.")
                            ubah(ID,file_consumable,jumlah)
                        else :
                            print("Gagal mengubah jumlah karena ID consumable tidak ditemukan.")
                            return databases
               
                else :
                    print("Gagal mengubah jumlah karena ID tidak valid.")
                return databases
        else :
            print("Maaf, kamu bukan Admin, silahkan login akun Admin.")
            return databases
    else :
        print("Silahkan login terlebih dahulu.")
    
    return databases


