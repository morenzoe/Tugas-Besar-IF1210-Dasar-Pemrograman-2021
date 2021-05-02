"""Program F08 - Meminjam Gadget
Fungsi ini akan meminta input id gadget yang ingin dipinjam,
jumlah dan tanggal. Peminjaman berhasil jika semua input valid.
Setelah melakukan peminjaman, jumlah id tersebut pada file gadget
akan diubah. Lalu, dibuat entri baru pada file riwayat pinjam.

Akses : User
"""

# KAMUS
# Daftar library standar
from datetime import datetime as dtm

# Daftar library lokal
from constant import gadget, active_account, gadget_borrow_history
from hapusitem import cek_role, cek_id, cek_idx, db_cek
from login import cek_active_account

# Daftar variabel
# databases     : array of array of array
# data          : array of array
# history	    : array of array
# isLoggedIn	: bool
# type          : str
# id            : str
# name          : str
# id_peminjam	: str
# idx           : int
# id_pinjam     : int
# stock			: int
# user          : array
# new_history	: array

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def cek_jumlah(id, type, jumlah, databases):
    """Fungsi ini akan menghasilkan True
    apabila jumlah id <= stok id
    pada databases[type].
    """

    # KAMUS LOKAL
    # db  : array of array
    # idx : int

    # ALGORITMA
    db = db_cek(databases, type)
    if cek_id(id, databases, type):
        idx = cek_idx(id, databases, type)
        if jumlah <= db[idx][3]:
            return True
        else:
            return False


def input_tanggal(transaksi):
    """Fungsi ini akan menghasilkan
    tanggal transkasi sesuai format
    dd/mm/yyyy menggunakan fungsi datetime.
    """

    # KAMUS LOKAL
    # date_input : str

    # ALGORITMA
    date_input = input("Tanggal " + transaksi + " : ")
    try:
        tanggal = dtm.strptime(date_input, '%d/%m/%Y')
        return date_input
    except BaseException:
        return 0


def input_jumlah(id, databases, type):
    """Fungsi ini akan menghasilkan
    jumlah yang valid dari id sesuai
    databases[type]. Jumlah valid,
    jumlah > 0, jumlah <= stok.

    """

    # KAMUS LOKAL

    # ALGORITMA
    while True:
        count_input = input("Jumlah               : ")
        try:
            count = int(count_input)
        except BaseException:
            return 0
        if count > 0:
            if cek_jumlah(id, type, count, databases):
                break
            else:
                print("Maaf, jumlah melebihi persediaan")
        else:
            print("Jumlah harus lebih besar dari 0!")
    return count


# mengecek apakah user pernah meminjam gadget yg sama, menghasilkan true
# jika sudah pernah meminjam
def cek_borrow_history(gadget_id, databases):
    id = databases[active_account][0]
    db = databases[gadget_borrow_history]
    if len(db) > 1:
        for row in range(len(db)):
            if int(
                    id) == db[row][1] and gadget_id == db[row][2] and db[row][5] == "False":
                return True
    return False


# ALGORITMA PROGRAM UTAMA
def pinjam(databases):
    isLoggedIn = cek_active_account(databases)
    type = "gadget"
    data = databases[gadget]
    history = databases[gadget_borrow_history]
    # Validasi login
    if isLoggedIn:
        user = databases[active_account]
        # Validasi role
        if cek_role(databases):
            print("(^_^) : Maaf, perintah ini hanya dapat diakses oleh User!")
        else:
            id = input("Masukan ID item      : ")
            # Validasi id
            if len(id) <= 1:
                print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
            else:
                if id[0] == "G":
                    if cek_id(id, databases, type):
                        if cek_borrow_history(id, databases):
                            print("\n(^o^) : Anda sedang meminjam gadget tersebut!")
                        else:
                            # Proses
                            idx = cek_idx(id, databases, type)
                            name = data[idx][1]
                            stock = data[idx][3]
                            if stock != 0:
                                tanggal = input_tanggal("peminjaman  ")
                                if tanggal != 0:
                                    jumlah = input_jumlah(id, databases, type)
                                    if jumlah != 0:
                                        # Proses rewrite gadget
                                        stock = stock - jumlah
                                        data[idx][3] = stock

                                        # proses write gadget_borrow_history
                                        id_pinjam = len(history)
                                        id_peminjam = user[0]
                                        is_returned = "False"
                                        new_history = [
                                            str(id_pinjam), int(id_peminjam), id, tanggal, jumlah, is_returned]
                                        history.append(new_history)

                                        # Output
                                        print(
                                            "\n\\(^ω^)/ : Item", name, "(" + str(jumlah) + ") telah berhasil dipinjam!")
                                    else:
                                        print(
                                            "\n┐(´д`)┌ : Maaf, input jumlah tidak valid!")
                                else:
                                    print(
                                        "\n┐(´д`)┌ : Maaf, input tanggal tidak sesuai format dd/mm/yyyy!")
                            else:
                                print("\n(>_<) : Maaf, persediaan habis!")
                    else:
                        print("\n┐(´д`)┌ : Maaf, tidak ada item dengan ID tersebut!")
                else:
                    print("\n┐(´д`)┌ : Maaf, input id tidak valid!")
    else:
        print("(^_^) : Silahkan login terlebih dahulu!")

    return databases
