from constant import gadget, gadget_borrow_history, gadget_return_history, active_account
from hapusitem import cek_role, cek_idx
from login import cek_active_account
from minta import input_tanggal

def find_gadget_name(id_peminjaman, data):
    f = data[gadget]
    id_gadget = data[gadget_borrow_history][id_peminjaman][2]
    if len(f) != 0:
        for row in range(len(f)):
            if id_gadget == f[row][0]:
                name = f[row][1]
    return name


def cek_riwayat_peminjaman(data): #Mengecek apakah user pernah meminjam gadget atau tidak, true jika sudah, false jika belum
    f = data[gadget_borrow_history]
    id = data[active_account][0]
    cek = 0
    if len(f) > 1:
        for row in range(len(f)):
            if int(id) == f[row][1] and f[row][5] == "False":
                cek = 1
    if cek == 0:
        return False
    elif cek == 1:
        return True


def kembalikan(databases):
    isLoggedin = cek_active_account(databases)
    data = databases[gadget_borrow_history]
    history = databases[gadget_return_history]
    db_gadget = databases[gadget]
    type = "gadget"

    if isLoggedin:
        user = databases[active_account]
        id = user[0]
        if cek_role(databases):
            print("(^_^) : Maaf, perintah ini hanya dapat diakses oleh user!")
        else:
            # Menampilkan riwayat peminjaman user
            num = 0
            if cek_riwayat_peminjaman(databases):
                for row in range(len(data)):
                    if int(id) == data[row][1] and data[row][5] == "False":
                        num = num + 1
                        name = find_gadget_name(row, databases)
                        print(str(num)+". "+name)
                print()
                # Input no peminjaman
                try:
                    number = int(input("Masukan nomor        : "))
                except:
                    print("\n┐(´д`)┌ : Maaf, input tidak valid!")
                    return databases
                if number < 0 or number > num :
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
                        id_peminjaman = borrow_history[0] # mencari id peminjaman
                        id_gadget = borrow_history[2] # mencari id gadget
                        jumlah = borrow_history[4] # mencari jumlah peminjaman
                        idx = cek_idx(id_gadget, databases, type) # mencari idx gadget di db_gadget
                        borrowed_gadget = db_gadget[idx]
                        gadget_name = borrowed_gadget[1]
                        # Prsoses rewrite db_gadget
                        borrowed_gadget[3] = borrowed_gadget[3] + jumlah
                        # Proses rewrite borrow_history
                        borrow_history[5] = "True"
                        # Proses append return_history
                        id_return = len(history)
                        new_data = [str(id_return), int(id_peminjaman), tanggal]
                        history.append(new_data)
                        #output
                        print("\n\(^ω^)/ : Item", gadget_name, "("+str(jumlah)+") telah dikembalikan!")
                    else:
                        print("\n┐(´д`)┌ : Maaf, input tanggal tidak sesuai format dd/mm/yyyy!")
            else:
                print("\n(^o^) : Anda sedang tidak meminjam gadget apapun!")
    else:
        print("(^_^) : Silahkan login terlebih dahulu!")
    return databases
