from tkinter import *
from PIL import Image, ImageTk

window = Tk()
#test
window.title("POS Tech Store Hala Madrid")
window.geometry("965x722")
icon_image = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\pict.jpg")
#Ganti lokasi file di template, menjadi lokasi di mana kalian menyimpan file template ini: 
#1. Cari gambar "madrid.png" di folder uas, lalu klik kiri dan klik kanan pada gambar, pilih opsi "copy image path"
#3. Pastkekan path tersebut ke dalam kurung di sintaks line 181, jika ada "/", ditambah jadi "//"
icon_image = icon_image.resize((32, 32), Image.LANCZOS)  # Mengatur ulang ukuran gambar supaya fit to screen
icon_img = ImageTk.PhotoImage(icon_image)
window.iconphoto(False, icon_img)

# Heading
heading = Label(window, text="Tech Store Hala Madrid", font=("Times New Roman", 20), relief=GROOVE, bg="grey20", fg="gold")#menampilkan nama POS di window
heading.grid(row=0, column=0, columnspan=5, sticky="ew")

# Customer Details section
cust_detail = LabelFrame(window, text="Detail Customer", font=("Arial", 15), relief=GROOVE, bg="grey20", fg="gold")
cust_detail.grid(row=1, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

#create section
#nama
create_nama_label = Label(cust_detail, text="Name", font=("Arial", 15), bg="grey20", fg="gold")
create_nama_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
create_nama = Entry(cust_detail, width=15, borderwidth=5, relief=GROOVE)
create_nama.grid(row=0, column=1, padx=10, pady=10)

create_nohp_label = Label(cust_detail, text="No HP", font=("Arial", 15), bg="grey20", fg="gold")
create_nohp_label.grid(row=0, column=2, padx=5, pady=5, sticky="w")
create_nohp = Entry(cust_detail, width=15, borderwidth=5, relief=GROOVE, validate="key")
create_nohp.grid(row=0, column=3, padx=10, pady=10)

create_billnum_label = Label(cust_detail, text="Kode Tagihan", font=("Arial", 15), bg="grey20", fg="gold")
create_billnum_label.grid(row=0, column=4, padx=5, pady=5, sticky="w")
create_billnum = Entry(cust_detail, width=15, borderwidth=5, relief=GROOVE)
create_billnum.grid(row=0, column=5, padx=10, pady=10)

product = LabelFrame(window, text="Detail Produk", font=("Arial", 15), relief=GROOVE, bg="grey20", fg="gold")
product.grid(row=2, column=0, columnspan=5, padx=10, pady=10, sticky="ew")

# Laptop section
laptop = LabelFrame(product, text="Laptop", font=("Arial", 15), relief=GROOVE, bg="grey20", fg="gold")
laptop.grid(row=2, column=0, padx=2, pady=5, sticky="nw")

asustuf = Label(laptop, text="Asus TUF", font=("Arial", 15),bg="grey20", fg="gold")
asustuf.grid(row=0, column=0, padx=1, pady=5, sticky="w")
input_asustuf = Entry(laptop, width=5, borderwidth=5, relief=GROOVE)
input_asustuf.grid(row=0, column=1, padx=10, pady=10)
input_asustuf.insert(0, 0) #menentukan default value, supaya input tidak kosong (literal error "None")

lenovoleg = Label(laptop, text="Lenovo LEGION", font=("Arial", 15), bg="grey20", fg="gold")
lenovoleg.grid(row=1, column=0, padx=5, pady=5, sticky="w")
input_lenovoleg = Entry(laptop, width=5, borderwidth=5, relief=GROOVE)
input_lenovoleg.grid(row=1, column=1, padx=10, pady=10)
input_lenovoleg.insert(0, 0)

msigam = Label(laptop, text="MSI Gaming", font=("Arial", 15), bg="grey20", fg="gold")
msigam.grid(row=2, column=0, padx=5, pady=5, sticky="w")
input_msigam = Entry(laptop, width=5, borderwidth=5, relief=GROOVE)
input_msigam.grid(row=2, column=1, padx=10, pady=10)
input_msigam.insert(0, 0)

# Keyboard section
keyboard = LabelFrame(product, text="Keyboard", font=("Arial", 15), bg="grey20", fg="gold")
keyboard.grid(row=2, column=1, padx=2, pady=5, sticky="nw")

royklud = Label(keyboard, text="Royal Kludge", font=("Arial", 15), bg="grey20", fg="gold")
royklud.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_royklud = Entry(keyboard, width=5, borderwidth=5, relief=GROOVE)
input_royklud.grid(row=0, column=1, padx=10, pady=10)
input_royklud.insert(0, 0)

zifrn = Label(keyboard, text="Zif 90", font=("Arial", 15), bg="grey20", fg="gold")
zifrn.grid(row=1, column=0, padx=5, pady=5, sticky="w")
input_zifrn = Entry(keyboard, width=5, borderwidth=5, relief=GROOVE)
input_zifrn.grid(row=1, column=1, padx=10, pady=10)
input_zifrn.insert(0, 0)

fanth = Label(keyboard, text="Fanth 45", font=("Arial", 15), bg="grey20", fg="gold")
fanth.grid(row=2, column=0, padx=5, pady=5, sticky="w")
input_fanth = Entry(keyboard, width=5, borderwidth=5, relief=GROOVE)
input_fanth.grid(row=2, column=1, padx=10, pady=10)
input_fanth.insert(0, 0)

#Accessory section
accessory = LabelFrame(product, text="Accessory", font=("Arial", 15), relief=GROOVE, bg="grey20", fg="gold")
accessory.grid(row=2, column=2, padx=2, pady=5, sticky="nw")

mouse = Label(accessory, text="Mouse Gaming", font=("Arial", 15), bg="grey20", fg="gold")
mouse.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_mouse = Entry(accessory, width=5, borderwidth=5, relief=GROOVE)
input_mouse.grid(row=0, column=1, padx=10, pady=10)
input_mouse.insert(0, 0)

mousepad = Label(accessory, text="Mouse Pad", font=("Arial", 15), bg="grey20", fg="gold")
mousepad.grid(row=1, column=0, padx=5, pady=5, sticky="w")
input_mousepad = Entry(accessory, width=5, borderwidth=5, relief=GROOVE)
input_mousepad.grid(row=1, column=1, padx=10, pady=10)
input_mousepad.insert(0, 0)

coolfan = Label(accessory, text="Cooling Fan", font=("Arial", 15), bg="grey20", fg="gold")
coolfan.grid(row=2, column=0, padx=5, pady=5, sticky="w")
input_coolfan = Entry(accessory, width=5, borderwidth=5, relief=GROOVE)
input_coolfan.grid(row=2, column=1, padx=10, pady=10)
input_coolfan.insert(0, 0)

#billframe
billframe = Frame(product, bd=5, relief=GROOVE)
billframe.grid(row=2, column=3, padx=10, pady=5, sticky="nsew")

billareaLabel = Label(billframe, text="Tagihan", font=('Arial', 15), bd=7, relief=GROOVE, bg="grey20", fg="gold")
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=15, width=30, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview) #menampilkan scroll bar di tab tagihan

#daftar menu
daftarmenu = LabelFrame(window, text="Detail Menu", font=("Arial", 15), bg="grey20", fg="gold")
daftarmenu.grid(row=3, column=0, columnspan=8, padx=8, pady=10, sticky="ew")

hargalaptop = Label(daftarmenu, text="Harga Laptop", font=("Arial", 15), bg="grey20", fg="gold")
hargalaptop.grid(row=3, column=0, padx=5, pady=5, sticky="w")
input_hargalaptop = Entry(daftarmenu, width=15, borderwidth=5, relief=GROOVE)
input_hargalaptop.grid(row=3, column=1, padx=5, pady=10)

hargakeyboard = Label(daftarmenu, text="Harga Keyboard", font=("Arial", 15),bg="grey20", fg="gold")
hargakeyboard.grid(row=4, column=0, padx=5, pady=5, sticky="w")
input_hargakeyboard = Entry(daftarmenu, width=15, borderwidth=5, relief=GROOVE)
input_hargakeyboard.grid(row=4, column=1, padx=5, pady=10)

hargaaccessory = Label(daftarmenu, text="Harga Accessory", font=("Arial", 15), bg="grey20", fg="gold")
hargaaccessory.grid(row=5, column=0, padx=5, pady=5, sticky="w")
input_hargaaccessory = Entry(daftarmenu, width=15, borderwidth=5, relief=GROOVE)
input_hargaaccessory.grid(row=5, column=1, padx=5, pady=10)

hargalaptoptax = Label(daftarmenu, text="Laptop Tax", font=("Arial", 15), bg="grey20", fg="gold")
hargalaptoptax.grid(row=3, column=3, padx=5, pady=5, sticky="w")
input_hargalaptoptax = Entry(daftarmenu, width=15, borderwidth=5, relief=GROOVE)
input_hargalaptoptax.grid(row=3, column=4, padx=5, pady=10)

hargakeyboardtax = Label(daftarmenu, text="Keyboard Tax", font=("Arial", 15), bg="grey20", fg="gold")
hargakeyboardtax.grid(row=4, column=3, padx=5, pady=5, sticky="w")
input_hargakeyboardtax = Entry(daftarmenu, width=15, borderwidth=5, relief=GROOVE)
input_hargakeyboardtax.grid(row=4, column=4, padx=5, pady=10)

hargaaccessorytax = Label(daftarmenu, text="Accessory Tax", font=("Arial", 15), bg="grey20", fg="gold")
hargaaccessorytax.grid(row=5, column=3, padx=5, pady=5, sticky="w")
input_hargaaccessorytax = Entry(daftarmenu, width=15, borderwidth=5, relief=GROOVE)
input_hargaaccessorytax.grid(row=5, column=4, padx=5, pady=10)

buttonframe = LabelFrame(daftarmenu, bd=8, relief=GROOVE, bg="gray20", fg="gold")
buttonframe.grid(row=4, column=6, columnspan=4, padx=8, pady=5, sticky="ew")

def total_laptop(): #fungsi untuk menampilkan total harga laptop ke entry box
    asus_tuf_price = int(input_asustuf.get())*15000000
    lenovo_leg_price = int(input_lenovoleg.get())*20000000
    msi_gam_price = int(input_msigam.get())*  18000000  

    total = asus_tuf_price + lenovo_leg_price + msi_gam_price
    total_formatted = "{:,.0f}".format(total)
    input_hargalaptop.delete(0, END)
    input_hargalaptop.insert(0, total_formatted)

totalButton = Button(buttonframe, text="Total", font=("Arial", 15), bg='gray20', fg='white', command=lambda:total_laptop()) #lambda untuk memberikan delay (the button will not be activated until the function is called or the button is cliked, event based)
totalButton.grid(row=0, column=7, padx=5,pady=5)


printButton = Button(buttonframe, text="Print", font=("Arial", 15), bg='gray20', fg='white')
printButton.grid(row=0, column=8, padx=5, pady=5)

control_image = Image.open('D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\madrid.png')
#Ganti lokasi file di template, menjadi lokasi di mana kalian menyimpan file template ini: 
#1. Cari gambar "madrid.png" di folder uas, lalu klik kiri dan klik kanan pada gambar, pilih opsi "copy image path"
#3. Pastkekan path tersebut ke dalam kurung di sintaks line 181, jika ada "/", ditambah jadi "//"
control_image = control_image.resize((75, 100), Image.LANCZOS)
control_img = ImageTk.PhotoImage(control_image)

image_label = Label(daftarmenu, image=control_img, bg="grey20")
image_label.grid(padx=10, column=12, row=4)

window.mainloop()
