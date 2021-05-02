# database id
user = 0
gadget = 1
consumable = 2
consumable_history = 3
gadget_borrow_history = 4
gadget_return_history = 5
active_account = 6

# nama-nama file CSV
nama_csv = ["user.csv",
            "gadget.csv",
            "consumable.csv",
            "consumable_history.csv",
            "gadget_borrow_history.csv",
            "gadget_return_history.csv"]

# data yang akan di convert
dikonversi = [# ['id', 'username', 'nama', 'alamat', 'password', 'role']
              [False, False, False, False, False, False],
              # ['id', 'nama', 'deskripsi', 'jumlah', 'rarity', 'tahun_ditemukan']
              [False, False, False, True, False, True],
              # ['id', 'nama', 'deskripsi', 'jumlah', 'rarity']
              [False, False, False, True, False],
              # ['id', 'id_pengambil', 'id_consumable', 'tanggal_pengambilan', 'jumlah']
              [False, True, False, False, True],
              # ['id', 'id_peminjam', 'id_gadget', 'tanggal_peminjaman', 'jumlah', 'is_returned']
             [False, True, False, False, True, False],
              # ['id', 'id_peminjaman', 'tanggal_pengembalian']
              [False, True, False]
             ]
