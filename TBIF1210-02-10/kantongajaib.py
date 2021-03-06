"""Program Inventarisasi Doraemonangis
Program ini akan membaca file berekstensi .csv dari suatu folder,
kemudian membaca atau mengubah data-data pada file tersebut sesuai
dengan input perintah dari pengguna.  Program ini dapat menyimpan
kembali data pada file berekstensi .csv pada folder yang diinginkan.
Program akan berhenti jika pengguna memanggil fungsi exit.
"""

# KAMUS
# Daftar library standar
import sys

# Daftar library lokal
from carirarity import carirarity
from caritahun import caritahun
from cek_csv import cek_csv
from exit import exit
from hapusitem import hapusitem
from help import help
from kembalikan import kembalikan
from load import load
from login import login
from minta import minta
from pinjam import pinjam
from register import register
from riwayatpinjam import riwayatpinjam
from riwayatkembali import riwayatkembali
from riwayatambil import riwayatambil
from save import save
from tambahitem import tambahitem
from ubahjumlah import ubahjumlah
from constant import *

# Daftar konstanta
# user, gadget, consumable, consumable_history, gadget_borrow_history : int
# gadget_return_history, active_account : int
# nama_csv : array of str
# konversi : array of array of bool

# Daftar variabel
# command : string
# dict_program : dictionary
# argumen : array of str
# csv_path : str
# databases : array of array of array
# dict_program : dictionary

# ALGORITMA
# Melakukan argument parsing
argumen = sys.argv

# Memeriksa kelengkapan csv pada folder yang diinput pengguna
csv_path = cek_csv(argumen)

# Csv tidak lengkap, terminasi seluruh program
if csv_path == 'csv tidak ada':
    sys.exit("\n(0.0) : File CSV tidak sesuai!\n"
             + "\n(^.^) : File CSV yang diperlukan adalah user.csv, "
             + "gadget.csv, consumable.csv, consumable_history.csv, "
             + "gadget_borrow_history.csv, gadget_return_history.csv")

# Folder tidak ada, terminasi seluruh program
elif csv_path == 'folder tidak ada':
    sys.exit("\n(O.o) : Folder tidak ada!")

# Folder ada dan csv lengkap, membaca seluruh csv ke dalam satu array
databases = load(csv_path)

# Inisialisasi variabel dictionary untuk pemanggilan fungsi
dict_program = {
    "register": register,
    "login": login,
    "carirarity": carirarity,
    "caritahun": caritahun,
    "exit": exit,
    "tambahitem": tambahitem,
    "hapusitem": hapusitem,
    "ubahjumlah": ubahjumlah,
    "pinjam": pinjam,
    "kembalikan": kembalikan,
    "minta": minta,
    "riwayatpinjam": riwayatpinjam,
    "riwayatkembali": riwayatkembali,
    "riwayatambil": riwayatambil,
    "save": save,
    "help": help,
}

# Menampilkan pesan selamat datang
print("\n(*^*)/ : Selamat datang di sistem inventarisasi Doraemonangis")

# Membuat infinite loop untuk program utama
while True:

    # # debugging
    # print("\nMode debugging:")
    # printSemua = input("Print databases sebagai array? (Y/N) ")
    # if printSemua in "Yy":
    # print(databases)
    # print()
    # printSebagian = input("Print databases per baris? (Y/N) ")
    # if printSebagian in "Yy":
    # for i in range(len(nama_csv)):
    # print(nama_csv[i])
    # for row in databases[i]:
    # print(row)
    # print()
    # print("active_account")
    # for row in databases[active_account]:
    # print(row)
    # # debugging

    # Menerima input perintah fungsi
    command = input("\n>>> ")
    print()

    # Memanggil fungsi sesuai input perintah fungsi
    try:
        databases = dict_program[command](databases)
    except KeyError:
        print("(O_o) : Perintah salah! Ketik help dan tekan enter untuk "
              + "menampilkan petunjuk.")
