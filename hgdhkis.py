class snack:
    def __init__(self, Parent, nt):  # Parent = window utama
        self.snack = Parent
        self.akses_nota = nt
        self.Total_snck = None  # Initialize Total_snck

    def snack1(self, film_terpilih, kursi_terpilih):
        for i in self.snack.winfo_children():
            i.destroy()

        self.list_snack(film_terpilih, kursi_terpilih)  # Display the snack page

    def list_snack(self, film_terpilih, kursi_terpilih):  # Function to display the snack page
        # (Your existing code to create the UI)

        # Add the Entry widget for total snack price
        self.Total_snck = Entry(Frame5, width=10, borderwidth=5, relief=GROOVE)
        self.Total_snck.grid(row=6, column=0, padx=1, pady=0, columnspan=2)
        self.Total_snck.insert(0, 0)  # Display the initial price

        cek_harga_snack = Button(Frame5, text="Cek", command=lambda: self.total_harga_snack(input_fr_fries, input_htdg, input_pop, input_brgr, input_air, input_soda), bg="snow1", fg="black", relief=RAISED)
        cek_harga_snack.grid(row=7, column=0, padx=1, pady=10, sticky="n", columnspan=4)  # Button to check snack price

        del_harga_snack = Button(Frame5, text="Del", command=lambda: self.hapus_harga_snack(input_fr_fries, input_htdg, input_pop, input_brgr, input_air, input_soda), bg="snow1", fg="black", relief=RAISED)
        del_harga_snack.grid(row=7, column=1, padx=1, pady=10, sticky="n", columnspan=4)  # Button to delete snack price

        knfrm_flm = Button(self.snack, text="Konfirmasi", command=lambda: self.akses_nota.nota1(film_terpilih, kursi_terpilih, self.Total_snck))
        knfrm_flm.grid(row=7, column=0, padx=10, pady=10, columnspan=3)  # Confirmation button

    def total_harga_snack(self, input_fr_fries, input_htdg, input_pop, input_brgr, input_air, input_soda):
        harga_fr_fries = int(input_fr_fries.get()) * 20000
        harga_htdg = int(input_htdg.get()) * 25000
        harga_pop = int(input_pop.get()) * 20000
        harga_brgr = int(input_brgr.get()) * 30000
        harga_soda = int(input_soda.get()) * 15000
        harga_air = int(input_air.get()) * 10000

        total_snack = harga_fr_fries + harga_htdg + harga_pop + harga_brgr + harga_soda + harga_air

        total_formatted = "{:,.0f}".format(total_snack)
        self.Total_snck.delete(0, END)
        self.Total_snck.insert(0, total_formatted)

    def hapus_harga_snack(self, input_fr_fries, input_htdg, input_pop, input_brgr, input_air, input_soda):
        input_fr_fries.delete(0, END)
        input_fr_fries.insert(0, "0")

        input_htdg.delete(0, END)
        input_htdg.insert(0, "0")

        input_pop.delete(0, END)
        input_pop.insert(0, "0")

        input_brgr.delete(0, END)
        input_brgr.insert(0, "0")

        input_soda.delete(0, END)
        input_soda.insert(0, "0")

        input_air.delete(0, END)
        input_air.insert(0, "0")

        self.Total_snck.delete(0, END)
        self.Total_snck.insert(0, "0")

class nota:
    def __init__(self, Parent):
        self.nota = Parent

    def nota1(self, film_terpilih, kursi_terpilih, Total_snck):
        for i in self.nota.winfo_children():
            i.destroy()

        self.nota_bayar(film_terpilih, kursi_terpilih, Total_snck)  # Display the nota page

    def nota_bayar(self, film_terpilih, kursi_terpilih, Total_snck):  # Function to display the nota page
        # (Your existing code to create the UI)

        cek_flm = Button(Frame9, text="Cek", command=lambda: self.harga_total_nota(input_jmlh_kur, Total_snck, input_Harga_Total_nt))
        cek_flm.grid(row=6, column=1, padx=10, pady=10, columnspan=2)  # Check total price button

    def harga_total_nota(self, input_jmlh_kur, Total_snck, input_Harga_Total_nt):
        harga_kursi = int(input_jmlh_kur.get()) * 40000

        harga_snackies = int(Total_snck.get().replace(",", ""))

        harga_tiket = harga_kursi + harga_snackies

        hrg_tkt_formatted = "{:,.0f}".format(harga_tiket)
        input_Harga_Total_nt.delete(0, END)
        input_Harga_Total_nt.insert(0, hrg_tkt_formatted)

def main():
    win = tk.Tk()
    nt = nota(win)
    snck = snack(win, nt)
    # mn = menu(win, snck)
    # Log = Login(win, mn)
    # Log.Hal1()

    win.mainloop()

if __name__ == "__main__":
    main()
