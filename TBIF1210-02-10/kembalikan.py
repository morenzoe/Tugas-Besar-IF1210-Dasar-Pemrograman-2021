"""Program F09 - Mengembalikan Gadget
Fungsi ini akan menampilkan riwayat peminjaman gadget oleh
id active_account. Lalum meminta input nomor peminjaman dan tanggal.
Pengembalian berhasil jika input valid. Setelah melakukan
pengembalian, status pengembalian pada riwayat pinjam akan berubah.
Kemudian, jumlah pada file gadget akan dikembalikan.
Lalu, dibuat entri baru pada file riwayat pengembalian.

Akses : User
"""

# KAMUS
# Daftar library lokal
from constant import gadget, gadget_borrow_history, gadget_return_history, active_account
from hapusitem import cek_role, cek_idx
from login import cek_active_account
from pinjam import input_tanggal

# Daftar variabel
# databases     : array of array of array
# db_gadget     : array of array
# data          : array of array
# history		: array of array
# isLoggedIn	: bool
# type          : str
# id            : str
# name          : str
# id_peminjaman	: str
# idx           : int
# id_return 	: int
# user          : array
# new_history	: array

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def find_gadget_name(id_peminjaman, databases):
    """Fungsi ini akan menghasilkan
    nama gadget yang dipinjam dari
    id_peminjaman pada riwayat pinjam.
    """

    # KAMUS LOKAL
    # db        : array of array
    # id_gadget : str
    # name      : str

    # ALGORITMA
    db = databases[gadget]
    id_gadget = databases[gadget_borrow_history][id_peminjaman][2]
    if len(db) > 1:
        for row in range(len(db)):
            if id_gadget == db[row][0]:
                name = db[row][1]
    return name


# Mengecek apakah user pernah meminjam gadget atau tidak, true jika sudah,
# false jika belum
def cek_riwayat(databases):
    """Fungsi ini akan menghasilkan
    true jika user pernah meminjam
    gadget apapun.
    """

    # KAMUS LOKAL
    # db : array of array
    # id : str

    # ALGORITMA
    db = databases[gadget_borrow_history]
    id = databases[active_account][0]
    if len(db) > 1:
        for row in range(len(db)):
            if int(id) == db[row][1] and db[row][5] == "False":
                return True
    return False

# ALGORITMA PROGRAM UTAMA
def kembalikan(databases):
    isLoggedIn = cek_active_account(databases)
    type = "gadget"
    db_gadget = databases[gadget]
    data = databases[gadget_borrow_history]
    history = databases[gadget_return_history]
    # Validasi login
    if isLoggedIn:
        user = databases[active_account]
        id = user[0]
        # Validasi role
        if cek_role(databases):
            print("(^_^) : Maaf, perintah ini hanya dapat diakses oleh user!")
        else:
            # Menampilkan riwayat peminjaman user
            num = 0
            if cek_riwayat(databases):
                for row in range(len(data)):
                    if int(id) == data[row][1] and data[row][5] == "False":
                        num = num + 1
                        name = find_gadget_name(row, databases)
                        print(str(num) + ". " + name)
                print()
                # validasi no peminjaman
                try:
                    number = int(input("Masukan nomor        : "))
                except BaseException:
                    print("\n┐(´д`)┌ : Maaf, input tidak valid!")
                    return databases
                if number <= 0 or number > num:
                    print("\n┐(´д`)┌ : Maaf, nomor peminjaman di luar pilihan!")
                else:
                    idx_found = 0
                    row = 0
                    while row <= (len(data)):
                        if int(id) == data[row][1] and data[row][5] == "False":
                            idx_found = idx_found + 1
                        if idx_found == number:
                            idx_row = row
                            break
                        row = row + 1
                    # Input tanggal
                    tanggal = input_tanggal("pengembalian")
                    if tanggal != 0:
                        # Proses
                        borrow_history = data[idx_row]
                        # mencari id peminjaman
                        id_peminjaman = borrow_history[0]
                        id_gadget = borrow_history[2]  # mencari id gadget
                        jumlah = borrow_history[4]  # mencari jumlah peminjaman
                        # mencari idx gadget di db_gadget
                        idx = cek_idx(id_gadget, databases, type)
                        borrowed_gadget = db_gadget[idx]
                        gadget_name = borrowed_gadget[1]

                        # Prsoses rewrite db_gadget
                        borrowed_gadget[3] = borrowed_gadget[3] + jumlah

                        # Proses rewrite borrow_history
                        borrow_history[5] = "True"

                        # Proses append return_history
                        id_return = len(history)
                        new_data = [
                            str(id_return), int(id_peminjaman), tanggal]
                        history.append(new_data)

                        # output
                        print(
                            "\n\\(^ω^)/ : Item",
                            gadget_name,
                            "(" + str(jumlah) + ") telah dikembalikan!")
                    else:
                        print(
                            "\n┐(´д`)┌ : Maaf, input tanggal tidak sesuai format dd/mm/yyyy!")
            else:
                print("(^o^) : Anda sedang tidak meminjam gadget apapun!")
    else:
        print("(^_^) : Silahkan login terlebih dahulu!")
    return databases
