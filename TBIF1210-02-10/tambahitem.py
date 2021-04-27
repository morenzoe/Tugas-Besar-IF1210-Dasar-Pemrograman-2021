from constant import gadget,consumable,active_account
from login import cek_active_account


def cekid(ID,data):
    cek = 0
    for i in range(len(data)):
        if data[i][0]==ID :
            cek = 1
    if cek == 0 :
        return True
    else:
        return False       

def cekdelimit(cek):
    if ";" in cek:
        return True
    else:
        return False

# prosedur akhir
def tambahitem(databases):
    db_gadget = databases[gadget]
    file_gadget = db_gadget
    db_consumable = databases[consumable]
    file_consumable = db_consumable
        
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        if databases[active_account][5] == "Admin":
            ID = input("Masukan ID: ")
            pjgID = len(ID)
            if pjgID == 0 :
                 print("Gagal menambah item karena ID tidak valid.")
                 return databases
            else :
                if ID[0]=="G" :
                    if cekid(ID,file_gadget) :
                        nama = input("Masukan Nama : ")
                        if cekdelimit(nama):
                            print("Nama tidak valid.")
                            return databases
                            
                        deskripsi = input("Masukan Deskripsi : ")
                        if cekdelimit(deskripsi):
                            print("Deskripsi tidak valid.")
                            return databases
                            
                        jumlah = input("Masukan Jumlah : ")
                        if cekdelimit(jumlah):
                            print("Jumlah tidak valid.")
                            return databases
                        try :
                            jumlah = int(jumlah)
                        except :
                            print("Jumlah harus berupa bilanhan bulat positif.")
                            return databases
                        if jumlah <= 0 :
                            print("Jumlah harus bilangan bulat positif.")
                            return databases
                        
                        rarity = input("Masukan Rarity : ")
                        pjg = len(rarity)
                        if pjg == 1:
                            if rarity not in "CBAS" :
                                print("Rarity tidak valid.")
                                return databases
                        else :
                            print("Rarity tidak valid.")
                            return databases

                        tahun = input("Masukan tahun ditemukan : ")
                        if cekdelimit(tahun):
                            try :
                                tahun = int(tahun)
                            except :
                                print("Tahun tidak valid.")
                                return databases 
                        
                        new_gadget = [ID,nama,deskripsi,jumlah,rarity,tahun]
                        file_gadget.append(new_gadget)
                        databases[gadget] = file_gadget
                        print("Item telah berhasil ditambahkan ke database.")
                        
                    else :
                        print("Gagal menambahkan gadget, karena ID sudah ada.")
                        
                elif ID[0] == "C" :
                    if cekid(ID,file_consumable) :
                        nama = input("Masukan Nama : ")
                        if cekdelimit(nama):
                            print("Nama tidak valid.")
                            return databases
                            
                        deskripsi = input("Masukan Deskripsi : ")
                        if cekdelimit(deskripsi):
                            print("Deskripsi tidak valid.")
                            return databases
                            
                        jumlah = input("Masukan Jumlah : ")
                        if cekdelimit(jumlah):
                            print("Jumlah tidak valid.")
                            return databases
                        try :
                            jumlah = int(jumlah)
                        except :
                            print("Jumlah harus berupa bilanhan bulat positif.")
                            return databases
                        if jumlah <= 0 :
                            print("Jumlah harus bilangan bulat positif.")
                            return databases
                        
                        rarity = input("Masukan Rarity : ")
                        pjg = len(rarity)
                        if pjg == 1:
                            if rarity not in "CBAS" :
                                print("Rarity tidak valid.")
                                return databases
                        else :
                            print("Rarity tidak valid.")
                            return databases
                            
                        new_consumable = [ID,nama,deskripsi,jumlah,rarity]
                        file_consumable.append(new_consumable)
                        databases[consumable] = file_consumable
                        print("Item telah berhasil ditambahkan ke database.")
                    
                    else :
                        print("Gagal menambahkan consumable karena ID sudah ada.")                    

                else :
                    print("Gagal menambahkan item karena ID tidak valid.")

        else :
            print("Maaf, kamu bukan Admin, silahkan login akun Admin.")
            return databases
    else :
        print("Silahkan login terlebih dahulu.")
        return databases

    return databases 