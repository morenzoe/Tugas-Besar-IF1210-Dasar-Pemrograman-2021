# Tugas Besar IF1210 Dasar Pemrograman 2021
Sistem inventasisasi _gadgets_ dan _consumables_.

# Deskripsi Persoalan
Program pada tugas besar kali ini merupakan program inventarisasi _gadget_ dan _consumable_ dengan menggunakan bahasa Python. Terdapat dua jenis _role_ dalam program ini, yaitu Admin dan User. Fitur–fitur pada program ini juga terbagi menjadi beberapa jenis, yaitu fitur untuk Admin saja, User saja, serta fitur Admin dan User. Fitur untuk Admin saja adalah registrasi, menambahkan _item_ ke _databases_, mengubah jumlah _item_, menghapus _item_, melihat riwayat peminjaman dan pengembalian gadget, dan melihat riwayat permintaan _consumable_. Fitur yang hanya boleh diakses oleh User di antaranya fitur peminjaman _gadget_, pengembalian _gadget_, dan permintaan _consumable_. Sedangkan fitur yang dapat diakses oleh keduanya adalah fitur pencarian _gadget_ berdasarkan _rarity_ dan tahun ditemukan, fitur _save_, fitur _help_ dan _exit_.


Untuk mengakses aplikasi ini, User harus diregistrasikan terlebih dahulu oleh Admin menggunakan fitur registrasi. Setelah diregistrasikan, User harus login terlebih 
dahulu untuk bisa mengakses fitur user yang tersedia. Setelah berhasil login, baik User ataupun Admin, riwayat login akan ditambahkan ke active_account di database.


Setiap fitur pada program akan mengidentifikasi role akun terlebih dahulu melalui riwayat login dari active_account di database. Sehingga pemilik akun tidak akan 
dapat mengakses fitur yang tidak sesuai dengan role nya. Pada setiap fitur, program akan meminta Admin atau User untuk memasukkan input sesuai dengan kebutuhan pada 
fitur. Setiap adanya kesalahan input, atau input tidak valid, maka program akan langsung diterminasikan. 


Untuk mengakhiri penggunaan program, gunakan fungsi exit. Pada fungsi ini, program akan bertanya pada pemilik akun apakah ingin menyimpan perubahan data yang telah 
dilakukan, atau tidak. Apabila pemilik akun mengetik “Y” atau “y”, maka program akan menyimpan perubahan. Tetapi, apabila pemilik akun mengetik “N” atau “n”, maka 
program tidak akan menyimpan perubahan data yang telah dilakukan.

# Desain Kamus Data
1. File User (user.csv)
- id       : string
- username : string
- nama     : string
- alamat   : string
- password : string
- role     : string
 
2. File Gadget (gadget.csv)
- id              : string
- nama            : string
- deskripsi       : string
- jumlah          : integer
- rarity          : string
- tahun_ditemukan : integer

3. File Consumable (consumable.csv)
- id        : string
- nama      : string
- deskripsi : string
- jumlah    : integer
- rarity    : string

4. File Pengambilan Consumable(consumable_history.csv)
- id                  : string
- id_pengambil        : integer
- id_consumable       : string
- tanggal_pengambilan : string
- jumlah              : integer

5. File Riwayat Peminjaman Gadget (gadget_borrow_history.csv)
- id                 : string
- id_peminjam        : integer
- id_gadget          : string
- tanggal_peminjaman : string
- jumlah             : integer
- is_returned        : boolean
