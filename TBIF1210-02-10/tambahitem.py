from constant import gadget, consumable, active_account
from login import cek_active_account


def cekid(ID, data):
    cek = 0
    for i in range(len(data)):
        if data[i][0] == ID:
            cek = 1
    if cek == 0:
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
    """Prosedur ini akan meminta input data item yang akan ditambahkan, yaitu:
    Untuk gadget:
    Masukan ID             :
    Masukan Nama           :
    Masukan Deskripsi      :
    Masukan Jumlah         :
    Masukan Rarity         :
    Masukan tahun ditemukan:

    Untuk consumable:
    Masukan ID             :
    Masukan Nama           :
    Masukan Deskripsi      :
    Masukan Jumlah         :
    Masukan Rarity         :
    """

    db_gadget = databases[gadget]
    file_gadget = db_gadget
    db_consumable = databases[consumable]
    file_consumable = db_consumable

    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        if databases[active_account][5] == "Admin":
            ID = input("Masukan ID             : ")
            pjgID = len(ID)
            if pjgID == 0:
                print()
                print("(;^_^): Gagal menambah item karena ID tidak valid.")
                print()
                print("(/'O'): Format ID gadget yang valid adalah (G<angka>)")
                print("(/'O'): Format ID consumable yang valid adalah (C<angka>)")
                return databases
            else:
                if ID[0] == "G":
                    if pjgID == 1:
                        print()
                        print("(;^_^): Gagal menambah item karena ID gadget tidak valid.")
                        print()
                        print("(/'O'): Format ID gadget yang valid adalah (G<angka>)")
                    else:
                        Id = ID[1:]
                        try:
                            Id = int(Id)
                        except BaseException:
                            print()
                            print("(;^_^): Gagal menambah item karena ID gadget tidak valid.")
                            print()
                            print("(/'O'): Format ID gadget yang valid adalah (G<angka>)")
                            return databases

                        if Id <= 0:
                            print()
                            print("(;^_^): Gagal menambah item karena ID gadget tidak valid.")
                            print()
                            print("(/'O'): Format ID gadget yang valid adalah (G<angka>)")
                            return databases

                        if cekid(ID, file_gadget):
                            nama = input("Masukan Nama           : ")
                            if len(nama) == 0:
                                print()
                                print("(/'O'): Nama tidak boleh kosong!")
                                return databases
                            else:
                                if cekdelimit(nama):
                                    print()
                                    print("(/'O'): Nama tidak valid. Jangan gunakan ';' pada nama.")
                                    return databases

                            deskripsi = input("Masukan Deskripsi      : ")
                            if len(deskripsi) == 0:
                                print()
                                print("(/'O'): Deskripsi tidak boleh kosong!")
                                return databases
                            else:
                                if cekdelimit(deskripsi):
                                    print()
                                    print("(/'O'): Deskripsi tidak valid. Jangan gunakan ';' pada deksripsi.")
                                    return databases

                            jumlah = input("Masukan Jumlah         : ")
                            try:
                                jumlah = int(jumlah)
                            except BaseException:
                                print()
                                print("(/'O'): Jumlah harus berupa bilangan bulat positif.")
                                return databases
                            if jumlah <= 0:
                                print()
                                print("(/'O'): Jumlah harus berupa bilangan bulat positif.")
                                return databases

                            rarity = input("Masukan Rarity         : ")
                            pjg = len(rarity)
                            while True:
                                if pjg == 1 and rarity in "CBAS":
                                    break
                                else:
                                    print()
                                    print("(/'O'): Rarity tidak valid. Rarity hanya berupa 'C','B','A', dan 'S'.")
                                    return databases

                            tahun = input("Masukan tahun ditemukan: ")
                            thn = len(tahun)
                            try:
                                tahun = int(tahun)
                            except BaseException:
                                print()
                                print("(/'O'): Tahun tidak valid. Tahun harus berupa angka dalam format YYYY.")
                                return databases
                            while True:
                                if thn == 4 and tahun > 0:
                                    break
                                else:
                                    print()
                                    print("(/'O'): Tahun tidak valid. Tahun harus dalam format YYYY.")
                                    return databases

                            new_gadget = [
                                ID, nama, deskripsi, jumlah, rarity, tahun]
                            file_gadget.append(new_gadget)
                            databases[gadget] = file_gadget
                            print()
                            print("(b^_^)b: Item telah berhasil ditambahkan ke database.")

                        else:
                            print()
                            print("(;^_^): Gagal menambahkan gadget, karena ID sudah ada.")
                            print()
                            print("(/^o^): Gunakan ID lain. Format ID gadget yang valid adalah (G<angka>)")

                elif ID[0] == "C":
                    if pjgID == 1:
                        print()
                        print("(;^_^): Gagal menambah item karena ID consumable tidak valid.")
                        print()
                        print("(/'O'): Format ID consumable yang valid adalah (C<angka>)")
                    else:
                        Id = ID[1:]
                        try:
                            Id = int(Id)
                        except BaseException:
                            print()
                            print("(;^_^): Gagal menambah item karena ID consumable tidak valid.")
                            print()
                            print("(/'O'): Format ID consumable yang valid adalah (C<angka>)")
                            return databases

                        if Id <= 0:
                            print()
                            print("(;^_^): Gagal menambah item karena ID gadget tidak valid.")
                            print()
                            print("(/'O'): Format ID consumable yang valid adalah (C<angka>)")
                            return databases

                        if cekid(ID, file_gadget):
                            nama = input("Masukan Nama           : ")
                            if len(nama) == 0:
                                print()
                                print("(/'O'): Nama tidak boleh kosong!")
                                return databases
                            else:
                                if cekdelimit(nama):
                                    print()
                                    print("(/'O'): Nama tidak valid. Jangan gunakan ';' pada nama.")
                                    return databases

                            deskripsi = input("Masukan Deskripsi      : ")
                            if len(deskripsi) == 0:
                                print()
                                print("(/'O'): Deskripsi tidak boleh kosong!")
                                return databases
                            else:
                                if cekdelimit(deskripsi):
                                    print()
                                    print("(/'O'): Deskripsi tidak valid. Jangan gunakan ';' pada deksripsi.")
                                    return databases

                            jumlah = input("Masukan Jumlah         : ")
                            try:
                                jumlah = int(jumlah)
                            except BaseException:
                                print()
                                print("(/'O'): Jumlah harus berupa bilangan bulat positif.")
                                return databases
                            if jumlah <= 0:
                                print()
                                print("(/'O'): Jumlah harus berupa bilangan bulat positif.")
                                return databases

                            rarity = input("Masukan Rarity         : ")
                            pjg = len(rarity)
                            while True:
                                if pjg == 1 and rarity in "CBAS":
                                    break
                                else:
                                    print()
                                    print("(/'O'): Rarity tidak valid. Rarity hanya berupa 'C','B','A', dan 'S'.")
                                    return databases

                            new_consumable = [
                                ID, nama, deskripsi, jumlah, rarity]
                            file_consumable.append(new_consumable)
                            databases[consumable] = file_consumable
                            print()
                            print("(b^_^)b: Item telah berhasil ditambahkan ke database.")

                        else:
                            print()
                            print("(;^_^): Gagal menambahkan consumable karena ID sudah ada.")
                            print()
                            print("(/^O^): Format ID consumable yang valid adalah (C<angka>)")

                else:
                    print()
                    print("(;^_^): Gagal menambahkan item karena ID tidak valid.")
                    print()
                    print("(/'O'): Format ID gadget yang valid adalah (G<angka>)")
                    print("(/'O'): Format ID consumable yang valid adalah (C<angka>)")

        else:
            print("(D_D): Maaf, kamu bukan Admin, silahkan login sebagai Admin untuk mengubah jumlah item.")
            return databases
    else:
        print("(^v^): Kamu belum login, silahkan login sebagai Admin untuk mengubah jumlah item.")

    return databases
