# Tugas Besar IF1210 Dasar Pemrograman 2021
Sistem inventasisasi gadget dan consumables.

# Deskripsi Persoalan
Program pada tugas besar kali ini merupakan program inventarisasi gadget dan consumabledengan menggunakan bahasa python.Terdapat dua jenis role dalam program ini, 
yaitu Admin dan  User. Fitur –fitur pada  program  inijuga  terbagi  menjadi  beberapa  jenis,  yaitu fitur  untuk Admin  saja,  User  saja, serta fitur  Admin  dan 
User.  Fitur  untuk  Adminsaja adalah  registrasi, menambahkan  item  ke  databases,  mengubah  jumlahitem,  menghapus  item, melihatriwayat 
peminjamandanpengembaliangadget,danmelihat riwayatpermintaanconsumable.Fituryanghanyabolehdiakses olehUserdiantaranya fitur peminjamangadget, pengembaliangadget, dan 
permintaanconsumable.  Sedangkan  fitur  yang  dapat  diakses  oleh  keduanya  adalah  fitur pencarian gadget berdasarkan rarity dan tahun ditemukan, fitur save, 
fitur help dan exit.Untuk mengakses  aplikasi  ini, User  harus  diregistrasikan  terlebih  dahulu  oleh Adminmenggunakan fitur registrasi. Setelah diregistrasikan, 
Userharus login terlebih dahulu untukbisa mengakses  fitur user yang  tersedia.Setelah berhasillogin, baikUserataupunAdmin,riwayatlogin 
akanditambahkankeactive_accountdi database.Setiap fitur padaprogram akan mengidentifikasiroleakunterlebih dahulumelaluiriwayat login dari active_account di 
database.Sehinggapemilik akuntidak akan dapat mengakses fitur yang tidak sesuai dengan role nya. Pada setiap fitur, program akan meminta Admin atau User untuk 
memasukkaninputsesuai  dengan  kebutuhan pada  fitur. Setiap adanya  kesalahan  input,  atau input tidak valid, maka program akanlangsungditerminasikan.Untuk 
mengakhiri penggunaan program, gunakan fungsi exit. Pada fungsi ini, program akan bertanya padapemilik akunapakah ingin menyimpan perubahan data yang telah dilakukan, 
atau tidak.Apabila pemilik akun mengetik “Y”atau “y”, maka program akan menyimpan perubahan. Tetapi, apabila  pemilik  akun  mengetik “N”atau “n”,  maka  program  
tidak  akan  menyimpan perubahan data yang telah dilakukan.

# Desain Kamus Data
1.File User (user.csv)

 a. id: string
 
 b. username : string
 
 c. nama     : string
 
 d. alamat   : string
 
 e. password : string
 
 f. role     : string
 

2.File Gadget (gadget.csv)

 a. id              : string
 
 b. nama            : string
 
 c. deskripsi       : string
 
 d. jumlah          : integer
 
 e. rarity          : string
 
 f. tahun_ditemukan : integer


3.File Consumable (consumable.csv)

 a. id        : string
 
 b. nama      : string
 
 c. deskripsi : string
 
 d. jumlah    : integer
 
 e. rarity    : string
 

4.File Pengambilan Consumable(consumable_history.csv)

 a. id                  : string
 
 b. id_pengambil        : integer
 
 c. id_consumable       : string
 
 d. tanggal_pengambilan : string
 
 e. jumlah              : integer
 

5.File Riwayat Peminjaman Gadget (gadget_borrow_history.csv)

 a. id                 : string
 
 b. id_peminjam        : integer
 
 c. id_gadget          : string
 
 d. tanggal_peminjaman : string
 
 e. jumlah             : integer
 
 f. is_returned        : boolean
