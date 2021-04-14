# import program lokal
from carirarity import carirarity
from caritahu import caritahu
from cek_csv import cek_csv
from hapusitem import hapusitem
from help import help
from kembalikan import kembalikan
from load import baca_csv
from login import login
from minta import minta
from pinjam import pinjam
#from register import register # register belum mengubah list
from riwayatpinjam import riwayatpinjam
from riwayatkembali import riwayatkembali
from riwayatambil import riwayatambil
from save import save
from tambahitem import tambahitem
from ubahjumlah import ubahjumlah

# nama-nama fungsi
dict_program = {'login' : login,
				'carirarity' : carirarity,
				'caritahu' : caritahu,
				'tambahitem' : tambahitem,
				'hapusitem' : hapusitem,
				'ubahjumlah' : ubahjumlah,
				'pinjam' : pinjam,
				'kembalikan' : kembalikan,
				'minta' : minta,
				'riwayatpinjam' : riwayatpinjam,
				'riwayatkembali' : riwayatkembali,
				'riwayatambil' : riwayatambil,
				'save' : save,
				'help' : help,
				'exit' : exit
				}