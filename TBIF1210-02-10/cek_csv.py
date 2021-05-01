"""Program Cek CSV
Fungsi ini akan membaca dan memvalidasi argumen dari cmd, memeriksa
keberadaan folder yang diinput, dan kelengkapan csv di dalamnya.
Fungsi akan mengembalikan path directory folder jika semua valid
atau mengembalikan pesan eror jika tidak semua syarat terpenuhi.
"""

# KAMUS
# Daftar library standar
import os
import sys

# Daftar library lokal
from constant import nama_csv

# Daftar konstanta
# nama_csv : array of str

# Daftar variabel
# argumen, files : array of str
# nama_folder_tujuan, folder_tujuan_dir, workspace : str
# csv_found : bool

# Definisi, Spesifikasi, dan Realisasi Fungsi/Prosedur
def cek_argumen(argumen):
    """Fungsi ini membaca list of string yang berisi argumen dari cmd
    kemudian memvalidasi input nama folder penyimpanan.  Fungsi akan
    memberhentikan keseluruhan program jika nama folder tidak valid
    """

    # KAMUS LOKAL
    # argumen : array of str
    # jumlah_argumen : int
    # nama_folder_tujuan : str

    # ALGORITMA
    # Memeriksa jumlah kata pada input cmd
    jumlah_argumen = len(argumen)

    # Menggabungkan seluruh kata setelah kantongajaib.py sebagai nama folder
    if jumlah_argumen >= 2:
        nama_folder_tujuan = " ".join(argumen[1:jumlah_argumen])
        return nama_folder_tujuan

    # Input nama folder tidak ada, terminasi seluruh program
    elif jumlah_argumen < 2:
        print("\n(O.o): Tidak ada nama folder yang diberikan!")
        sys.exit("\nUsage: python kantongajaib.py <nama_folder>")


def cek_folder(nama_folder_tujuan):
    """Fungsi ini menerima nama folder tujuan dan memeriksa keberadaan
    folder tersebut di dalam workspace.  Fungsi akan mengembalikan
    path directory folder dan workspace jika folder tersebut ada dan
    mengembalikan pesan eror dan path directory workspace jika folder
    tidak ada.
    """

    # KAMUS LOKAL
    # folder_found : bool
    # nama_folder_tujuan, workspace, nama_folder, folder_tujuan_dir : str
    # root, dirs, files : array of str

    # ALGORITMA
    # Mendapatkan workspace file kantong_ajaib.py
    workspace = os.getcwd()

    # Inisialisasi variabel validasi nama folder
    folder_found = False

    # Mencari nama folder pada setiap folder dalam workspace
    for root, dirs, files in os.walk(workspace):
        for nama_folder in dirs:
            # Folder ditemukan, membuat variabel path directory folder
            if nama_folder == nama_folder_tujuan:
                folder_found = True
                folder_tujuan_dir = os.path.join(root, nama_folder_tujuan)
                break

        # Folder ditemukan, mengembalikan path directory folder dan workspace
        if folder_found:
            return folder_tujuan_dir, workspace
            break

        # Folder tidak ditemukan, mengembalikan pesan eror dan workspace
        elif not folder_found:
            return 'folder tidak ada', workspace


# ALGORITMA PROGRAM UTAMA
def cek_csv(argumen):
    # Memvalidasi nama folder dari argumen cmd
    nama_folder_tujuan = cek_argumen(argumen)

    # Memvalidasi keberadaan nama folder
    folder_tujuan_dir, workspace = cek_folder(nama_folder_tujuan)

    # Folder tidak ditemukan, mengembalikan pesan eror
    if folder_tujuan_dir == 'folder tidak ada':
        return folder_tujuan_dir

    # Folder ditemukan, memeriksa kelengkapan file csv
    files = os.listdir(folder_tujuan_dir)
    csv_found = all(item in files for item in nama_csv)

    # Semua file csv lengkap, mengembalikan path directory folder
    if csv_found:
        return folder_tujuan_dir

    # File csv tidak lengkap, mengembalikan pesan eror
    elif not csv_found:
        return 'csv tidak ada'
