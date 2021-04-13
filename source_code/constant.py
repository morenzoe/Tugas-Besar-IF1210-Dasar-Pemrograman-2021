# import fungsi
from carirarity import carirarity
from caritahu import caritahu
from hapusitem import hapusitem
from help import help
from kembalikan import kembalikan
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

# database id
user = 0
gadget = 1
consumable = 2
consumable_history = 3
gadget_borrow_history = 4
gadget_return_history = 5

# nama-nama file CSV
nama_csv = ["user.csv",
		"gadget.csv",
		"consumable.csv",
		"consumable_history.csv",
		"gadget_borrow_history.csv",
		"gadget_return_history.csv"]
		
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