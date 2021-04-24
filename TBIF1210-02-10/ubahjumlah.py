from constant import gadget
from constant import consumable

# prosedur akhir

def cekid(ID,data):
        cek = 0
        for i in range(len(data)):
                if data[i][0]==ID :
                        cek = 1
        if cek == 1 :
                return True
        else:
                return False

def ubah(ID,data, jumlah):
        for i in range (len(data)):
                if data[i][0] == ID :
                        idx = 1

        stok = data[idx][3] + jumlah
        
        if stok >= 0 :
                data[idx][3] = stok
        else :
                data[idx][3] = stok - jumlah
         
                

        if data[idx][3] >= 0 :
                if jumlah >= 0 :
                        print(jumlah , (data[idx][1]) , "berhasil ditambahkan. Stok sekarang : ",(data[idx][3]))
                else :
                        print(jumlah , (data[idx][1]) , "berhasil dibuang. Stok sekarang : ",(data[idx][3]))
        else :
                print(jumlah , (data[idx][1]) , "gagal dibuang karena stok kurang. Stok sekarang : ", (data[idx][3]))

        
        
        

def ubahjumlah(databases):
        fg = databases[gadget]
        datag = fg
        fc = databases[consumable]
        datac = fc

        ID = input("Masukan ID : ")
        jumlah = int(input("Masukan Jumlah : "))

        if ID[0] == "G" :
                if cekid(ID,datag) :
                        ubah(ID,datag,jumlah)
                else :
                        print("Gagal mengubah jumlah karena ID gadget tidak ditemukan.")
        elif ID[0] == "C" :
                if cekid(ID,datac) :
                        ubah(ID,datac,jumlah)
                else : print("Gagal mengubah jumlah karena ID consumable tidak ditemukan.")
        else :
                print("Gagal mengubah jumlah karena ID tidak valid.")
                        

        return databases