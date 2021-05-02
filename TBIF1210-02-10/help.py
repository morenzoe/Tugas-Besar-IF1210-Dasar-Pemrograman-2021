"""Program F16 - Help
Fungsi ini akan memberikan panduan penggunaan sistem.

Akses : Admin, User
"""

# KAMUS
# Daftar library lokal
from constant import user, active_account
from login import cek_active_account


def help(databases):
    isLoggedIn = cek_active_account(databases)
    if not isLoggedIn:
        print(
            """=================================== H E L P ===================================
register      : untuk melakukan registrasi user baru
login         : untuk melakukan login ke dalam sistem
carirariry    : untuk melakukan pencarian gadget dengan rarity tertentu
caritahun     : untuk melakukan pencarian gadget berdasarkan tahun ditemukan
tambahitem    : untuk menambahkan item ke dalam inventori
hapusitem     : untuk menghapus suatu item pada database
ubahjumlah    : untuk mengubah jumlah gadget dan consumable dalam sistem
pinjam        : untuk melakukan peminjaman gadget
kembalikan    : untuk melakukan pengembalian gadget
minta         : untuk meminta consumable yang tersedia
riwayatpinjam : untuk melihat riwayat peminjaman gadget
riwayatkembali: untuk melihat riwayat pengembalian gadget
riwayatambil  : untuk melihat riwayat pengembalian consumable
save          : untuk menyimpan data ke dalam file
exit          : untuk keluar dari aplikasi
===============================================================================""")

    else:
        role = databases[active_account][5]
        if role == "Admin":
            print(
                """=================================== H E L P ===================================
register      : untuk melakukan registrasi user baru
carirariry    : untuk melakukan pencarian gadget dengan rarity tertentu
caritahun     : untuk melakukan pencarian gadget berdasarkan tahun ditemukan
tambahitem    : untuk menambahkan item ke dalam inventori
hapusitem     : untuk menghapus suatu item pada database
ubahjumlah    : untuk mengubah jumlah gadget dan consumable dalam sistem
riwayatpinjam : untuk melihat riwayat peminjaman gadget
riwayatkembali: untuk melihat riwayat pengembalian gadget
riwayatambil  : untuk melihat riwayat pengembalian consumable
save          : untuk menyimpan data ke dalam file
exit          : untuk keluar dari aplikasi
===============================================================================""")
        else:
            print(
                """=================================== H E L P ===================================
carirariry    : untuk melakukan pencarian gadget dengan rarity tertentu
caritahun     : untuk melakukan pencarian gadget berdasarkan tahun ditemukan
pinjam        : untuk melakukan peminjaman gadget
kembalikan    : untuk melakukan pengembalian gadget
minta         : untuk meminta consumable yang tersedia
save          : untuk menyimpan data ke dalam file
exit          : untuk keluar dari aplikasi
===============================================================================""") 

    return databases            
