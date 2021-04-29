import os
from constant import *
from cek_csv import cek_folder


def to_str(array_word_int):
    # menghasilkan word dalam type str

    # KAMUS LOKAL
    # Variabel
    # array_word : array of string

    # ALGORITMA
    array_word = [str(word) for word in array_word_int]
    return array_word


def array_word_to_row(array_word):
    # semicolon add
    row = ";".join(array_word) + "\n"
    return row


def array_to_csv(csv, folder_path, database):
    save_csv = []
    for array_word_int in database:
        array_word = to_str(array_word_int)
        row = ";".join(array_word) + "\n"
        save_csv.append(row)
    csv_path = os.path.join(folder_path, csv)
    f = open(csv_path, "w")
    for row in save_csv:
        f.write(row)
    f.close()


def save(databases):
    folder_save = input("Masukkan nama folder penyimpanan: ")
    # cek foldernya ada dan csvnya ada atau ngga
    folder_path, workspace = cek_folder(folder_save)
    # kalo gaada folder , buat folder baru
    if folder_path == 'folder tidak ada':
        folder_path = os.path.join(workspace, folder_save)
        # buat folder, buat csv
        os.makedirs(folder_path)
    # kalo folder ada, overwrite
    print("Saving...")
    for i in range(len(databases)):
        csv = nama_csv[i]
        array_to_csv(csv, folder_path, databases[i])
    print("Data telah disimpan pada folder", folder_save + "!")
    return databases