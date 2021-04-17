from constant import gadget
from constant import consumable

# prosedur akhir

def cekid(ID,data):
        cek = 0
        for i in range(len(data)):
                if data[i][0]==ID :
                        cek = 1
        if cek == 0 :
                return True
        else:
                return False


def tambahitem(databases):
        fileg = databases[gadget]
        datag = fileg
        filec = databases[consumable]
        datac = filec

        ID = input("Masukan ID : ")

        
        if ID[0]=="G" :
                if cekid(ID,datag)==False :
                        print("Gagal menambahkan item karena ID sudah ada.")
                else:
                        nama = input("Masukan Nama : ")
                        deskripsi = input("Masukan Deskripsi : ")
                        jumlah = input("Masukan Jumlah : ")
                        rarity = input("Masukan Rarity : ")
                        while rarity not in "CBAS":
                                print("Input rarity tidak valid")
                                rarity = input("Masukan rarity: ")
                        tahun = int(input("Masukan tahun ditemukan : "))
                        new_gadget = [ID,nama,deskripsi,jumlah,rarity,tahun]
                        datag.append(new_gadget)
                        databases[gadget]=datag
                        print("Item telah berhasil ditambahkan ke database.")
                        
        elif ID[0]=="C" :
                if cekid(ID,datac)==False :
                        print("Gagal menambahkan item karena ID sudah ada.")
                else:
                        nama = input("Masukan Nama : ")
                        deskripsi = input("Masukan Deskripsi : ")
                        jumlah = input("Masukan Jumlah : ")
                        rarity = input("Masukan Rarity : ")
                        while rarity not in "CBAS":
                                print("Input rarity tidak valid")
                                rarity = input("Masukan rarity: ")
                        new_consumable = [ID,nama,deskripsi,jumlah,rarity]
                        datac.append(new_consumable)
                        databases[consumable]=datac
                        print("Item telah berhasil ditambahkan ke database.")
        else:
                print("Gagal menambahkan item karena ID tidak valid.")


        return databases
