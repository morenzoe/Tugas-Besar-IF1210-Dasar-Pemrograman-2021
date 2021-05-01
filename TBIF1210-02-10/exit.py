"""Program F17 - Exit
Fungsi ini akan menawarkan pengguna untuk menyimpan data.  Jika 
pengguna ingin menyimpan data, fungsi akan memanggil fungsi save.  
Setelahnya, fungsi akan memberhentikan keseluruhan program.

Akses : -
"""

# KAMUS
# Daftar library standar
import sys

# Daftar library lokal
from save import save

# Daftar variabel
# save_option : str

# ALGORITMA
def exit(databases):
    # Memvalidasi input dari pengguna
    while True:
        save_option = input("Apakah Anda mau melakukan penyimpanan file "
                            + "yang sudah diubah? (Y/N) ")
        
        # Input valid, salah satu huruf Y/y/N/n
        if save_option in "YyNn" and len(save_option)==1:
            break
        # Input tidak valid, pengisian diulang
        print("\nm(><)m : Input tidak sesuai. Ulangi! \n")
    
    # Pengguna ingin menyimpan data, melakukan fungsi save
    if save_option in "Yy":
        save(databases)
    
    # Program selesai, terminasi loop program utama
    sys.exit("\n(^O^)/ : Sampai jumpa!")