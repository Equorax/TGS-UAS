#rumus
from ui import *
def is_integer(char):
    return char.isdigit()  # Memeriksa apakah karakter adalah digit
def total():
    # Mengambil nilai dari entry untuk harga laptop, keyboard, accessory, serta pajak-pajak yang terkait
    

    # Menghitung total harga dari semua item dengan memperhatikan pajak yang berlaku
    total_harga = (input_asustuf+input_lenovoleg+input_msigam) + (input_royklud+input_zifrn+input_fanth) + (input_mouse+input_mousepad+input_coolfan) + (input_mouse+input_mousepad+input_coolfan)

    # Menampilkan total harga di dalam textarea
    textarea.insert(END, f"Total Harga: Rp {total_harga}\n")
