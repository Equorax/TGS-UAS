from tkinter import *
from fungsi import total
from PIL import Image, ImageTk

# def limit_width(event, max_width):
#     if event.width > max_width:
#         window.grid_columnconfigure(0, minsize=max_width)
#     else:
#         window.grid_columnconfigure(0, minsize=event.width)

window = Tk()
#test
window.title("POS Tech Store Hala Madrid")
window.geometry("965x722")
icon_image = Image.open('D:\\Materi\\Kuliah\\Kerjaan\\Asisten Dosen\\Prinsip Pemrograman\\pythonwindows\\uas\\pict.jpg')
icon_image = icon_image.resize((32, 32), Image.LANCZOS)  # Resize image to fit as an icon
icon_img = ImageTk.PhotoImage(icon_image)
window.iconphoto(False, icon_img)

# Heading
heading = Label(window, text="Tech Store Hala Madrid", font=("Times New Roman", 20), relief=GROOVE, bg="grey20", fg="gold")
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

lenovoleg = Label(laptop, text="Lenovo LEGION", font=("Arial", 15), bg="grey20", fg="gold")
lenovoleg.grid(row=1, column=0, padx=5, pady=5, sticky="w")
input_lenovoleg = Entry(laptop, width=5, borderwidth=5, relief=GROOVE)
input_lenovoleg.grid(row=1, column=1, padx=10, pady=10)

msigam = Label(laptop, text="MSI Gaming", font=("Arial", 15), bg="grey20", fg="gold")
msigam.grid(row=2, column=0, padx=5, pady=5, sticky="w")
input_msigam = Entry(laptop, width=5, borderwidth=5, relief=GROOVE)
input_msigam.grid(row=2, column=1, padx=10, pady=10)

# Keyboard section
keyboard = LabelFrame(product, text="Keyboard", font=("Arial", 15), bg="grey20", fg="gold")
keyboard.grid(row=2, column=1, padx=2, pady=5, sticky="nw")

royklud = Label(keyboard, text="Royal Kludge", font=("Arial", 15), bg="grey20", fg="gold")
royklud.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_royklud = Entry(keyboard, width=5, borderwidth=5, relief=GROOVE)
input_royklud.grid(row=0, column=1, padx=10, pady=10)

zifrn = Label(keyboard, text="Zif 90", font=("Arial", 15), bg="grey20", fg="gold")
zifrn.grid(row=1, column=0, padx=5, pady=5, sticky="w")
input_zifrn = Entry(keyboard, width=5, borderwidth=5, relief=GROOVE)
input_zifrn.grid(row=1, column=1, padx=10, pady=10)

fanth = Label(keyboard, text="Fanth 45", font=("Arial", 15), bg="grey20", fg="gold")
fanth.grid(row=2, column=0, padx=5, pady=5, sticky="w")
input_fanth = Entry(keyboard, width=5, borderwidth=5, relief=GROOVE)
input_fanth.grid(row=2, column=1, padx=10, pady=10)

#Accessory section
accessory = LabelFrame(product, text="Accessory", font=("Arial", 15), relief=GROOVE, bg="grey20", fg="gold")
accessory.grid(row=2, column=2, padx=2, pady=5, sticky="nw")

mouse = Label(accessory, text="Mouse Gaming", font=("Arial", 15), bg="grey20", fg="gold")
mouse.grid(row=0, column=0, padx=5, pady=5, sticky="w")
input_mouse = Entry(accessory, width=5, borderwidth=5, relief=GROOVE)
input_mouse.grid(row=0, column=1, padx=10, pady=10)

mousepad = Label(accessory, text="Mouse Pad", font=("Arial", 15), bg="grey20", fg="gold")
mousepad.grid(row=1, column=0, padx=5, pady=5, sticky="w")
input_mousepad = Entry(accessory, width=5, borderwidth=5, relief=GROOVE)
input_mousepad.grid(row=1, column=1, padx=10, pady=10)

coolfan = Label(accessory, text="Cooling Fan", font=("Arial", 15), bg="grey20", fg="gold")
coolfan.grid(row=2, column=0, padx=5, pady=5, sticky="w")
input_coolfan = Entry(accessory, width=5, borderwidth=5, relief=GROOVE)
input_coolfan.grid(row=2, column=1, padx=10, pady=10)

#billframe
billframe = Frame(product, bd=5, relief=GROOVE)
billframe.grid(row=2, column=3, padx=10, pady=5, sticky="nsew")

billareaLabel = Label(billframe, text="Tagihan", font=('Arial', 15), bd=7, relief=GROOVE, bg="grey20", fg="gold")
billareaLabel.pack(fill=X)

scrollbar = Scrollbar(billframe, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)
textarea = Text(billframe, height=15, width=30, yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)

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

totalButton = Button(buttonframe, text="Total", font=("Arial", 15), bg='gray20', fg='white', command=total)
totalButton.grid(row=0, column=7, padx=5,pady=5)


printButton = Button(buttonframe, text="Print", font=("Arial", 15), bg='gray20', fg='white')
printButton.grid(row=0, column=8, padx=5, pady=5)

control_image = Image.open('D:\\Materi\\Kuliah\\Kerjaan\\Asisten Dosen\\Prinsip Pemrograman\\pythonwindows\\uas\\madrid.png')
control_image = control_image.resize((75, 100), Image.LANCZOS)
control_img = ImageTk.PhotoImage(control_image)

image_label = Label(daftarmenu, image=control_img, bg="grey20")
image_label.grid(padx=10, column=12, row=4)

window.mainloop()
