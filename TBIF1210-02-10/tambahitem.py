"""Program F05 - Menambah Item
Program akan menambahkan item gadget atau consumable ke database sesuai
dengan input Admin.
- Jika ID diawali huruf G, berarti Admin akan menambahkan gadget.
- Jika ID diawali huruf C, berarti Admin akan menambahkan consumable.
- Jika ID tidak diawali huruf G dan C, fungsi akan mengeluarkan fungsi error.
- Fungsi akan mengeluarkan fungsi error apabila input tidak valid.

Akses : Admin
"""

# KAMUS
# Daftar library
from constant import gadget, consumable, active_account
from login import cek_active_account

# Daftar konstanta
# gadget        : int
# consumable    : int
# active_account: int

# Daftar variabel
# databases                   : array of array of array
# db_gadget, db_consumable    : array of array
# file_gadget, file_consumable: array of array
# isLoggedIn                  : bool
# pjgID                       : int
# ID                          : str
# nama, deskripsi             : str
# jumlah, tahun               : int
# rarity                      : chr

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def cekid(ID, data):
    # KAMUS LOKAL
    # cek : int

    # ALGORITMA
    # Inisialisasi awal cek
    cek = 0
    # Membaca panjang data
    for i in range(len(data)):
        # ID ditemukan di databases
        if data[i][0] == ID:
            cek = 1
    if cek == 0:
        # Mengembalikan Tue apabila ID tidak ditemukan
        return True
    else:  # cek != 0
        # Mengembalikan False apabila ID ditemukan
        return False


def cekdelimit(cek):
    # KAMUS LOKAL
    # -

    # ALGORITMA
    # Mengecek ";"
    if ";" in cek:
        # Mengembalikan True apabila ";" ditemukan
        return True
    else:
        # Mengembalikan False apabila ";" ditemukan
        return False


# ALGORITMA PROGRAM UTAMA
def tambahitem(databases):
    """Prosedur ini akan meminta input data item yang akan ditambahkan:
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

    # Membuat list untuk file yang akan diubah
    db_gadget = databases[gadget]
    file_gadget = db_gadget
    db_consumable = databases[consumable]
    file_consumable = db_consumable

    # Validasi login pengguna
    isLoggedIn = cek_active_account(databases)
    if isLoggedIn:
        username = databases[active_account][1]
        role = databases[active_account][5]

        # Validasi role pengguna
        if role == "Admin":
            # Input ID
            ID = input("Masukan ID              : ")
            pjgID = len(ID)

            # Validasi ID
            if pjgID == 0:
                # Beritahu pengguna bahwa ID tidak valid
                print("\n(;^_^): Gagal menambah item karena ID tidak valid.")
                print("\n(/'O'): Format ID gadget yang valid adalah (G<angka>)")
                print("(/'O'): Format ID consumable yang valid adalah (C<angka>)")
                return databases
            else:
                # Identifikasi gadget
                if ID[0] == "G":
                    # Validasi ID
                    if pjgID == 1:
                        # Beritahu pengguna bahwa ID tidak valid
                        print(
                            "\n(;^_^) : Gagal menambah item karena ID gadget tidak valid.")
                        print(
                            "\n(/'O') : Format ID gadget yang valid adalah (G<angka>)")
                    else:
                        Id = ID[1:]
                        try:
                            Id = int(Id)
                        except BaseException:
                            print(
                                "\n(;^_^) : Gagal menambah item karena ID gadget tidak valid.")
                            print(
                                "\n(/'O') : Format ID gadget yang valid adalah (G<angka>)")
                            return databases

                        if Id <= 0:
                            print()
                            print(
                                "(;^_^) : Gagal menambah item karena ID gadget tidak valid.")
                            print()
                            print(
                                "(/'O') : Format ID gadget yang valid adalah (G<angka>)")
                            return databases

                        # Memastikan ID tidak sama dengan ID gadget yang sudah
                        # ada di database
                        if cekid(ID, file_gadget):
                            # Input nama
                            nama = input("Masukan Nama            : ")
                            if len(nama) == 0:
                                print(
                                    "\n(/'O') : Nama tidak boleh kosong!")
                                return databases
                            else:
                                if cekdelimit(nama):
                                    print(
                                        "\n(/'O') : Nama tidak valid. Jangan gunakan ';' pada nama.")
                                    return databases

                            # Input deksripsi
                            deskripsi = input("Masukan Deskripsi       : ")
                            if len(deskripsi) == 0:
                                print(
                                    "\n(/'O') : Deskripsi tidak boleh kosong!")
                                return databases
                            else:
                                if cekdelimit(deskripsi):
                                    print(
                                        "\n(/'O') : Deskripsi tidak valid. Jangan gunakan ';' pada deksripsi.")
                                    return databases

                            # Input jumlah
                            jumlah = input("Masukan Jumlah          : ")
                            try:
                                jumlah = int(jumlah)
                            except BaseException:
                                print(
                                    "\n(/'O') : Jumlah harus berupa bilangan bulat positif.")
                                return databases
                            if jumlah <= 0:
                                print(
                                    "\n(/'O') : Jumlah harus berupa bilangan bulat positif.")
                                return databases

                            # Input rarity
                            rarity = input("Masukan Rarity          : ")
                            pjg = len(rarity)
                            while True:
                                if pjg == 1 and rarity in "CBAS":
                                    break
                                else:
                                    print(
                                        "\n(/'O') : Rarity tidak valid. Rarity hanya berupa 'C','B','A', dan 'S'.")
                                    return databases

                            # Input tahun ditemukannya gadget
                            tahun = input("Masukan tahun ditemukan : ")
                            thn = len(tahun)
                            try:
                                tahun = int(tahun)
                            except BaseException:
                                print(
                                    "\n(/'O') : Tahun tidak valid. Tahun harus berupa angka dalam format YYYY.")
                                return databases
                            while True:
                                if thn == 4 and tahun > 0:
                                    break
                                else:
                                    print(
                                        "\n(/'O') : Tahun tidak valid. Tahun harus dalam format YYYY.")
                                    return databases

                            # Menambahkan gadget ke database
                            new_gadget = [
                                ID, nama, deskripsi, jumlah, rarity, tahun]
                            file_gadget.append(new_gadget)
                            databases[gadget] = file_gadget

                            print(
                                "\n(b^_^)b : Item telah berhasil ditambahkan ke database.")

                        else:  # ID gadget sudah ada di database
                            # Beritahu pengguna bahwa ID gadget tidak dapat
                            # digunakan
                            print(
                                "\n(;^_^) : Gagal menambahkan gadget, karena ID sudah ada.")
                            print(
                                "\n(/^o^) : Gunakan ID lain. Format ID gadget yang valid adalah (G<angka>)")

                # Identifikasi consumable
                elif ID[0] == "C":
                    if pjgID == 1:
                        # Beritahu pengguna bahwa ID tidak valid
                        print(
                            "\n(;^_^) : Gagal menambah item karena ID consumable tidak valid.")
                        print(
                            "\n(/'O') : Format ID consumable yang valid adalah (C<angka>)")
                    else:
                        Id = ID[1:]
                        try:
                            Id = int(Id)
                        except BaseException:
                            print(
                                "\n(;^_^) : Gagal menambah item karena ID consumable tidak valid.")
                            print(
                                "\n(/'O') : Format ID consumable yang valid adalah (C<angka>)")
                            return databases

                        if Id <= 0:
                            print()
                            print(
                                "(;^_^) : Gagal menambah item karena ID gadget tidak valid.")
                            print()
                            print(
                                "(/'O') : Format ID consumable yang valid adalah (C<angka>)")
                            return databases

                        # Memastikan bahwa ID tidak sama dengan ID yang telah
                        # ada sebelumnya
                        if cekid(ID, file_consumable):
                            # Input nama
                            nama = input("Masukan Nama            : ")
                            if len(nama) == 0:
                                print(
                                    "\n(/'O') : Nama tidak boleh kosong!")
                                return databases
                            else:
                                if cekdelimit(nama):
                                    print(
                                        "\n(/'O') : Nama tidak valid. Jangan gunakan ';' pada nama.")
                                    return databases

                            # Input deksripsi
                            deskripsi = input("Masukan Deskripsi       : ")
                            if len(deskripsi) == 0:
                                print(
                                    "\n(/'O') : Deskripsi tidak boleh kosong!")
                                return databases
                            else:
                                if cekdelimit(deskripsi):
                                    print(
                                        "\n(/'O') : Deskripsi tidak valid. Jangan gunakan ';' pada deksripsi.")
                                    return databases

                            # Input jumlah
                            jumlah = input("Masukan Jumlah          : ")
                            try:
                                jumlah = int(jumlah)
                            except BaseException:
                                print(
                                    "\n(/'O') : Jumlah harus berupa bilangan bulat positif.")
                                return databases
                            if jumlah <= 0:
                                print(
                                    "\n(/'O') : Jumlah harus berupa bilangan bulat positif.")
                                return databases

                            # Input rarity
                            rarity = input("Masukan Rarity          : ")
                            pjg = len(rarity)
                            while True:
                                if pjg == 1 and rarity in "CBAS":
                                    break
                                else:
                                    print(
                                        "\n(/'O') : Rarity tidak valid. Rarity hanya berupa 'C','B','A', dan 'S'.")
                                    return databases

                            # Menambahkan consumable ke database
                            new_consumable = [
                                ID, nama, deskripsi, jumlah, rarity]
                            file_consumable.append(new_consumable)
                            databases[consumable] = file_consumable
                            print(
                                "\n(b^_^)b : Item telah berhasil ditambahkan ke database.")

                        else:
                            # Beritahu pengguna bahwa ID tidak dapat digunakan
                            print(
                                "\n(;^_^) : Gagal menambahkan consumable karena ID sudah ada.")
                            print(
                                "\n(/^O^) : Format ID consumable yang valid adalah (C<angka>)")

                else:
                    print(
                        "\n(;^_^) : Gagal menambahkan item karena ID tidak valid.")
                    print(
                        "\n(/'O') : Format ID gadget yang valid adalah (G<angka>)")
                    print("(/'O') : Format ID consumable yang valid adalah (C<angka>)")

        else:  # role != Admin
            print(
                "\n(D_D) : Maaf, role" +
                username +
                "bukan Admin, silahkan login sebagai Admin untuk mengubah jumlah item.")
            return databases
    else:  # not isLoggedIn
        print("(^v^) : Kamu belum login, silahkan login sebagai Admin untuk mengubah jumlah item.")

    return databases
