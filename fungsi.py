#rumus
from ui import *

input_asustuf = 0
input_lenovoleg = 0
input_msigam = 0
input_royklud = 0
input_zifrn = 0
input_fanth = 0
input_mouse = 0
input_mousepad = 0
input_coolfan = 0


def is_integer(char):
    return char.isdigit()  # Memeriksa apakah karakter adalah digit

def total_laptop(input_asustuf, input_lenovoleg, input_msigam):
    try:
        input_asustuf = int(input_asustuf) if input_asustuf else 0
        input_lenovoleg = int(input_lenovoleg) if input_lenovoleg else 0
        input_msigam = int(input_msigam) if input_msigam else 0

        total = (input_asustuf * 15000000) + (input_lenovoleg * 20000000) + (input_msigam * 18000000)
        input_hargalaptop.delete(0, 'end')
        input_hargalaptop.insert(0, str(total))
    except ValueError:
        input_hargalaptop.delete(0, 'end')
        input_hargalaptop.insert(0, "Error")

# def total():
#     # Mengambil nilai dari entry untuk harga laptop, keyboard, accessory, serta pajak-pajak yang terkait
#     # Menghitung total harga dari semua item dengan memperhatikan pajak yang berlaku
#     total_harga = (input_asustuf+input_lenovoleg+input_msigam) + (input_royklud+input_zifrn+input_fanth) + (input_mouse+input_mousepad+input_coolfan) + (input_mouse+input_mousepad+input_coolfan)

    # Menampilkan total harga di dalam textarea
    # textarea.insert(END, f"Total Harga: Rp {total_harga}\n")
