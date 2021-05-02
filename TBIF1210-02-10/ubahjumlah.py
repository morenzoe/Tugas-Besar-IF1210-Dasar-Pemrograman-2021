"""Program F07 - Mengubah Jumlah Gadget atau Consumable pada Inventory
Program ini akan menambah atau mengurangi jumlah gadget atau consumable
sesuai dengan input Admin.

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
# pjg ID                      : int
# ID                          : str
# jumlah                      : int

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def cekid(ID, data):
    # KAMUS LOKAL
    # cek : int

    # ALGORITMA
    # Inisialisasi awal cek
    cek = 0
    # Membaca panjang data
    for i in range(len(data)):
        # ID ditemukan di database
        if data[i][0] == ID:
            cek = 1
    if cek == 1:
        # Mengembalikan True apabila ID ditemukan
        return True
    else:  # cek == 0
        # Mengembalikan False apabila ID tidak ditemukan
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


def ubah(ID, data, jumlah):
    # KAMUS LOKAL
    # idx   : int
    # stok  : int
    # jumlah: int

    # ALGORITMA
    # Menemukan posisi ID
    for i in range(len(data)):
        if data[i][0] == ID:
            idx = i

    # Menambahkan jumlah item
    stok = data[idx][3] + jumlah

    # Mengubah jumlah item
    if stok >= 0:
        data[idx][3] = stok
    else:
        data[idx][3] = stok - jumlah

    # Memastikan bahwa jumlah akhir lebih >= 0
    if stok < 0:
        # Beritahu pengguna gagal mengubah jumlah
        print(
            "\n(/^-^)/ :", jumlah, data[idx][1]
            + "gagal dibuang karena stok kurang. Stok sekarang : "
            + (data[idx][3]))
    else:  # stok >= 0
        # Beritahu pengguna telah berhasil mengubah jumlah
        if jumlah >= 0:
            print(
                "\n(=^v^=) :", jumlah, (data[idx][1])
                + " berhasil ditambahkan. Stok sekarang :", (data[idx][3]))
        else:
            print(
                "\n(=^v^=) :", jumlah, (data[idx][1])
                + " berhasil dibuang. Stok sekarang :", (data[idx][3]))


# ALGORITMA PROGRAM UTAMA
def ubahjumlah(databases):
    """
    Prosedur ini akan meminta input ID dan jumlah item yang ingin diubah, yaitu:
    Masukan ID    :
    Masukan Jumlah:
    """

    # Membuat list dari file yang akan diubah
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
            # Input ID gadget atau consumable
            ID = input("Masukan ID     : ")
            pjgID = len(ID)
            if pjgID == 0:
                print(
                    "\n(/'o')/ : Gagal mengubah jumlah karena ID tidak valid.")
                print(
                    "\n(^.~)/ : Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                print(
                    "(^.~)/ : Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
            else:
                # Identifikasi ID gadget
                if ID[0] == "G":
                    if pjgID == 1:
                        print(
                            "\n(/'o')/ : Gagal mengubah jumlah karena ID gadget tidak valid.")
                        print(
                            "\n(^.~)/ : Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                        return databases
                    else:
                        Id = ID[1:]
                        try:
                            Id = int(Id)
                        except BaseException:
                            print(
                                "\n(/'o')/ : Gagal mengubah jumlah karena ID gadget tidak valid.")
                            print(
                                "\n(^.~)/ : Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                            return databases

                        if(Id <= 0):
                            print(
                                "\n(/'o')/ : Gagal mengubah jumlah karena ID gadget tidak valid.")
                            print(
                                "\n(^.~)/ : Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                            return databases

                        # Memastikan bahwa ID tersedia
                        if cekid(ID, file_gadget):
                            # Input jumlah
                            jumlah = input("Masukan Jumlah : ")
                            try:
                                jumlah = int(jumlah)
                            except BaseException:
                                print(
                                    "\n(^.~)/ : Jumlah tidak valid. Jumlah harus berupa bilangan bulat.")
                                return databases
                            ubah(ID, file_gadget, jumlah)
                        else:
                            print(
                                "\n(/'o')/ : Gagal mengubah jumlah karena ID gadget tidak ditemukan.")
                            print(
                                "\n(^.~)/ : Pastikan gadget yang dimaksud sudah tersedia di database.")
                            return databases

                # Identifikasi ID consumable
                elif ID[0] == "C":
                    if pjgID == 1:
                        print(
                            "\n(/'o')/ : Gagal mengubah jumlah karena ID consumable tidak valid.")
                        print(
                            "\n(^.~)/ : Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
                        return databases
                    else:
                        Id = ID[1:]
                        try:
                            Id = int(Id)
                        except BaseException:
                            print(
                                "\n(/'o')/ : Gagal mengubah jumlah karena ID consumable tidak valid.")
                            print(
                                "\n(^.~)/ : Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
                            return databases

                        if(Id <= 0):
                            print(
                                "\n(/'o')/ : Gagal mengubah jumlah karena ID consumable tidak valid.")
                            print(
                                "\n(^.~)/ : Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")
                            return databases

                        # Memastikan bahwa ID tersedia
                        if cekid(ID, file_consumable):
                            jumlah = input("Masukan Jumlah : ")
                            try:
                                jumlah = int(jumlah)
                            except BaseException:
                                print(
                                    "\n(^.~)/ : Jumlah tidak valid. Jumlah harus bilangan bulat.")
                            ubah(ID, file_consumable, jumlah)
                        else:
                            print(
                                "\n(/'o')/ : Gagal mengubah jumlah karena ID consumable tidak ditemukan.")
                            print(
                                "\n(^.~)/ : Pastikan bahwa consumable yang dimaksud sudah tersedia di database.")
                            return databases

                else:
                    print(
                        "\n(/'o')/ : Gagal mengubah jumlah karena ID tidak valid.")
                    print(
                        "\n(^.~)/ : Gadget yang tersedia hanya memiliki ID dengan format (G<angka>)")
                    print(
                        "(^.~)/ : Consumable yang tersedia hanya memiliki ID dengan format (C<angka>)")

                return databases
        else:
            print(
                "\n(D_D) : Maaf, role" +
                username +
                "bukan Admin, silahkan login sebagai Admin untuk mengubah jumlah item.")
            return databases
    else:
        print(
            "\n(^v^) : Kamu belum login, silahkan login sebagai Admin untuk mengubah jumlah item.")

    return databases
