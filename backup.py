
import os
import tkinter as tk
import PIL
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

win = Tk()
win.title("cineBOX")
win.geometry("1400x1200")  # variabel
win.configure(bg="snow1")
# gambar logo
logo_image = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\10140537.jpg")
logo_image = logo_image.resize((32, 32), Image.LANCZOS)
logo_img = ImageTk.PhotoImage(logo_image)
win.iconphoto(False, logo_img)


class Login:  # modul 9 class
    def __init__(self, Parent, mn):
        self.Login = Parent
        self.akses_mn = mn
        self.Create_usrm = None
        self.Create_pswd = None

    def Hal1(self):  # modul 8 fungsi
        def Konfirmasi():  # simpan value dari entry dipanggil pake tombol
            username = Create_usrm.get()
            password = Create_pswd.get()
            if username == "" and password == "":  # pemilihan 6
                messagebox.showinfo("Peringatan", "Silahkan Masukan Nama dan Password")
            elif username == "admin" and password == "admin123":
                self.akses_mn.menu_film(username)
            else:
                messagebox.showinfo("Peringatan", "Silahkan Masukan Username atau Password")

        # Heading hal Login
        log = Label(self.Login, text="CineBOX\t\t\t\t\t\t\t\t", font=("Perpetua", 40), relief=FLAT, bg="#5E0101",
                    fg="#BE965A")  # character escape modul 3
        log.grid(row=0, column=0, columnspan=4, sticky=N)

        lg_bawah = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\movie roll .png")
        lg_bawah = lg_bawah.resize((55, 55), Image.LANCZOS)
        self.lg_bawah = ImageTk.PhotoImage(lg_bawah)
        lg_bawahS = Label(self.Login, image=self.lg_bawah, bg="#5E0101")
        lg_bawahS.grid(row=0, column=0, sticky="n", padx=10)

        # Frame
        Frame1 = LabelFrame(self.Login, text="Login", font=("Times New Roman", 20), relief=FLAT, bg="#5E0101",
                            fg="white")
        Frame1.grid(row=1, column=0, columnspan=4, pady=120, sticky=NS)

        # Username
        usrnm = Label(Frame1, text="Username", font=("Times New Roman", 10), relief=FLAT, bg="#5E0101", fg="white")
        usrnm.grid(row=1, column=0, columnspan=1, sticky="w", pady=2, padx=2)

        Create_usrm = Entry(Frame1, width=40, borderwidth=3, relief=SUNKEN)
        Create_usrm.grid(row=2, column=0, padx=1, pady=2, sticky="ns")

        # Password
        pswd = Label(Frame1, text="Password", font=("Times New Roman", 10), relief=FLAT, bg="#5E0101", fg="white")
        pswd.grid(row=3, column=0, columnspan=1, sticky="w", pady=2, padx=1)

        Create_pswd = Entry(Frame1, width=40, borderwidth=3, relief=SUNKEN, show="*")
        Create_pswd.grid(row=4, column=0, padx=1, pady=2, sticky="ns")

        # Tombol Konfirmasi halaman login bolo
        tmbl_kon = Button(Frame1, text="Konfirmasi", bg="snow1", command=lambda: Konfirmasi())
        tmbl_kon.grid(row=5, column=0, pady=10, padx=1)


class menu:
    def __init__(self, Parent, snck):  # Parent = window utama buat akses window
        self.film = Parent
        self.akses_snck = snck
        self.pilih_kursi = [] # di append dari var di checkbutton jadi bisa di update terus list  
        self.jmlh_kursi = 0

    def menu_film(self, username):
        for i in self.film.winfo_children():  # lacak widget dihalaman lalu dibersihin bikin halaman baru intinya # perulangan 7
            i.destroy()  # hancurkan hahaha

        self.list_film() 
        

        nama = Label(self.film, text=f"Selamat Datang di CineBOX, {username}!", font=("Times New Roman", 20),
                     relief=FLAT, bg="snow1", fg="black")
        nama.grid(row=1, column=0, columnspan=3, sticky="w", pady=0, padx=10)

        nama = Label(self.film, text="Pilih Film:", font=("Times New Roman", 15), relief=FLAT, bg="snow1", fg="black")
        nama.grid(row=6, column=0, columnspan=3, sticky="w", pady=0, padx=5)


    #geser kehalaman snack

    def cek_film_kursi(self, pilih_film, kursi_terpilih,): #periksa film berlaku sebagai update fungsi tombol cek
        if not pilih_film.curselection():
            messagebox.showwarning("Peringatan", "Silahkan Pilih Film")
            return

        kursi_terpilih = [var.get() for var in self.pilih_kursi if var.get() != ""]

        if not kursi_terpilih:
            messagebox.showwarning("Peringatan", "Silahkan Pilih Kursi")
            return
        
        if self.jmlh_kursi <= 0:
            messagebox.showwarning("Peringatan", "Silahkan Masukan Jumlah Kursi")
            return

        index_film_terpilih = pilih_film.curselection()[0]
        film_terpilih = pilih_film.get(index_film_terpilih)
        messagebox.showinfo("Film dan Kursi", f"Film: {film_terpilih}\nKursi: {', '.join(kursi_terpilih)}")

    def konfirmasi_input(self, pilih_film, kursi_terpilih): #fungsi konfirmasi halaman film + geser ke menu snack
        if not pilih_film.curselection():
            messagebox.showwarning("Peringatan", "Silahkan h Film")
            return
        
        film_terpilih = pilih_film.curselection()
        kursi_terpilih = [var.get() for var in self.pilih_kursi if var.get() != ""]

        if not kursi_terpilih:
            messagebox.showwarning("Peringatan", "Silahkan Pilih Kursi")
            return
        if self.jmlh_kursi <= 0:
            messagebox.showwarning("Peringatan", "Silahkan Jumlah Kursi")
            return

        index_film_terpilih = pilih_film.curselection()[0]
        film_terpilih = pilih_film.get(index_film_terpilih)
        messagebox.showinfo("Film dan Kursi", f"Film: {film_terpilih}\nKursi: {', '.join(kursi_terpilih)}")

        harga_kursi_rp = self.jmlh_kursi * 40000
      
        self.akses_snck.snack1(film_terpilih,kursi_terpilih)


    def okefilm(self, pilih_film,kursi_terpilih): #nahan checkButton
        if not pilih_film.curselection():
            messagebox.showwarning("Peringatan", "Silahkan Pilih Film")
            return
        
        film_terpilih = pilih_film.curselection()
        kursi_terpilih = [var.get() for var in self.pilih_kursi if var.get() != ""]

        if not kursi_terpilih:
            messagebox.showwarning("Peringatan", "Silahkan Pilih Kursi")
            return
        
        if self.jmlh_kursi <= 0:
            messagebox.showwarning("Peringatan", "Silahkan Jumlah Kursi")
            return
        
        index_film_terpilih = pilih_film.curselection()[0]
        film_terpilih = pilih_film.get(index_film_terpilih)
        messagebox.showinfo("Film dan Kursi", f"Film: {film_terpilih}\nKursi: {', '.join(kursi_terpilih)}")


    def list_film(self):  # fungsi listbox pilih film
        pilih_film = Listbox(self.film, bg="white", font=("Times New Roman", 12), fg="black", width=30, height=6)
        pilih_film.grid(row=7, column=0, columnspan=1, sticky="w", padx=10, pady=10)
        film = ["Spider-Man: Across the Spider-Verse","La La Land","Oppenheimer","Whisper of the Heart","Avengers: Endgame","American Psycho"]

        kursi_terpilih = [var.get() for var in self.pilih_kursi if var.get() != ""]
        
        for item in film:
            pilih_film.insert(tk.END, item) # buat nampilin film urut dari spiderman ke american psycho tiap ,fungsi dari insert habis itu tk.End fungsinya buat naruh film di akhir film lain

       
        knfrm_flm = Button(self.film, text="Konfirmasi", command=lambda: self.konfirmasi_input(pilih_film,kursi_terpilih))
        knfrm_flm.grid(row=7, column=0, padx=10, pady=10,columnspan=3) #tombol konfirmasi film 
        
        cek_flm = Button(self.film, text="Cek", command=lambda: self.cek_film_kursi(pilih_film,kursi_terpilih))
        cek_flm.grid(row=7, column=0, padx=10, pady=10,columnspan=2)  #tombol cek film
        
        FrameJum = LabelFrame(self.film, text="Jumlah", font=("Perpetua", 10), relief=FLAT, bg="#5E0101", fg="#BE965A")
        FrameJum.grid(row=3, column=0, columnspan=1)

        jmlh_kur = Label(FrameJum, text="Jumlah Kursi", font=("Times New Roman", 15),bg="azure4", fg="black")
        jmlh_kur.grid(row=2, column=0, padx=1, pady=5, sticky="w")


        input_jmlh_kur = Entry(FrameJum, width=5, borderwidth=5, relief=GROOVE)
        input_jmlh_kur.grid(row=2, column=1, padx=5, pady=5)
        input_jmlh_kur.insert(0, 0)

        def update_jmlh_kursi():
            try:
                self.jmlh_kursi = int(input_jmlh_kur.get())
            except ValueError: # kalok ada yang enter huruf atau angka selain integer ke di reset 0
                self.jmlh_kursi = 0

        input_jmlh_kur.bind("<KeyRelease>", lambda event: update_jmlh_kursi()) #setiap key yang dtekan di keyboard buat masukin angka update self.jmlh_kursi di bind ke entry


        Film = Label(self.film, text="CineBOX\t\t\t\t\t\t\t\t", font=("Perpetua", 40), relief=FLAT, bg="#5E0101",
                     fg="#BE965A")
        Film.grid(row=0, column=0, columnspan=3, sticky="w", pady=10)

        # Frame2 wadah film
        Frame2 = LabelFrame(self.film, text=" Film", font=("Perpetua", 25), relief=FLAT, bg="#5E0101", fg="#BE965A")
        Frame2.grid(row=2, column=0, columnspan=15, sticky="n", pady=10)

        # Movies
        Movie = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\Spiderman.png")
        Movie = Movie.resize((150,335), Image.LANCZOS)
        self.movie1 = ImageTk.PhotoImage(Movie)

        MovieS = Label(Frame2, image=self.movie1,bg="#BE965A")
        MovieS.grid(row=4,column=1,sticky="we",padx=60)
        
        judul = Label(Frame2,text="Spider-Man: Across the Spider-Verse",font=("Times New Roman",10),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=1,sticky="n",pady=10,padx=10)

        #2
        Movie = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\Laland.png")
        Movie = Movie.resize((150,335), Image.LANCZOS)
        self.movie2 = ImageTk.PhotoImage(Movie)

        MovieS = Label(Frame2, image=self.movie2,bg="#BE965A")
        MovieS.grid(row=4,column=2,sticky="we",padx=50)

        judul = Label(Frame2,text="La La Land",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=2,sticky="n",pady=10,padx=10)

        #3
        Movie = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\bomb.png")
        Movie = Movie.resize((150,335), Image.LANCZOS)
        self.movie3 = ImageTk.PhotoImage(Movie)

        MovieS = Label(Frame2, image=self.movie3,bg="#BE965A")
        MovieS.grid(row=4,column=3,sticky="we",padx=50)

        judul = Label(Frame2,text="Oppenheimer",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=3,sticky="n",pady=10,padx=10)

        #4
        Movie = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\whisper of the heart .png")
        Movie = Movie.resize((150,335), Image.LANCZOS)
        self.movie4 = ImageTk.PhotoImage(Movie)

        MovieS = Label(Frame2, image=self.movie4,bg="#BE965A")
        MovieS.grid(row=4,column=4,sticky="we",padx=50)

        judul = Label(Frame2,text="Whisper of the Heart",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=4,sticky="n",pady=10,padx=5)
        
        #5
        Movie = Image.open("D:\B. Tugas Kuliah\Prinsip Pemrograman\Project_UAs\Avengers.png")
        Movie = Movie.resize((150,335), Image.LANCZOS)
        self.movie5 = ImageTk.PhotoImage(Movie)

        MovieS = Label(Frame2, image=self.movie5,bg="#BE965A")
        MovieS.grid(row=4,column=5,sticky="we",padx=50)

        judul = Label(Frame2,text="Avengers: Endgame",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=5,sticky="n",pady=10,padx=5)

        #6
        Movie = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\Literally me.png")
        Movie = Movie.resize((150,335), Image.LANCZOS)
        self.movie6 = ImageTk.PhotoImage(Movie)

        MovieS = Label(Frame2, image=self.movie6,bg="#BE965A")
        MovieS.grid(row=4,column=6,sticky="we",padx=60)

        judul = Label(Frame2,text="American Psycho",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=6,sticky="n",pady=10,padx=5)

        Frame3 = LabelFrame(self.film,text="Pilihan Kursi", font=("Perpetua",25),relief=FLAT,bg="#5E0101",fg="snow1")
        Frame3.grid(row=7, column=0, columnspan=1, pady= 10,padx=5)


        kursi = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]  # list lima
        for idx, kursi_t in enumerate(kursi):  # idx pengganti index cuma buat cek modul 7
            var = StringVar(value="")
            self.pilih_kursi.append(var)
            self
            checkbutton = Checkbutton(Frame3, text=kursi_t, variable=var, onvalue=kursi_t, offvalue="",
                                      command=lambda: self.okefilm(pilih_film)) #tidak ada kursi_terpilih supaya pencet cek
            checkbutton.grid(row=7 + idx // 3, column=1 + idx % 3, padx=2, pady=1)  # operator 4
    
            
class snack:
    def __init__(self, Parent,nt):  # Parent = window utama
        self.snack = Parent
        self.akses_nota = nt
        
        
        # buat halaman baru isi snack
    def snack1(self,film_terpilih,kursi_terpilih):
        for i in self.snack.winfo_children():
            i.destroy()
       

        self.list_snack(film_terpilih,kursi_terpilih)  # nampilin halaman penting

    # def Konfirmasi_ke_nota(self,film_terpilih,kursi_terpilih,harga_kursi_rp):
    def Konfirmasi_ke_nota(self,film_terpilih,kursi_terpilih):
        self.akses_nota.nota1(film_terpilih,kursi_terpilih)


    def list_snack(self,film_terpilih,kursi_terpilih):  # fungsi isinya halaman snack

        Film = Label(self.snack, text="CineBOX\t\t\t\t\t\t\t\t", font=("Perpetua", 40), relief=FLAT, bg="#5E0101",
                     fg="#BE965A")
        Film.grid(row=0, column=0, columnspan=3, sticky="w", pady=10)

      
        # Frame2
        Frame4 = LabelFrame(self.snack, text=" Snack", font=("Perpetua", 25), relief=FLAT, bg="#5E0101", fg="#BE965A")
        Frame4.grid(row=2, column=0, columnspan=15, sticky="n", pady=10)

        
        # snack
        
        
        Snack = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\kentang.png")
        Snack = Snack.resize((150,155), Image.LANCZOS)
        self.snack_1 = ImageTk.PhotoImage(Snack)

        SnackS = Label(Frame4, image=self.snack_1,bg="#BE965A")
        SnackS.grid(row=4,column=1,sticky="we",padx=60)
        
        judul = Label(Frame4,text="French Fries\nRp.20.000",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=1,sticky="n",pady=10,padx=10)

        #2
        Snack = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\hotdog.png")
        Snack = Snack.resize((150,155), Image.LANCZOS)
        self.snack_2 = ImageTk.PhotoImage(Snack)

        SnackS = Label(Frame4, image=self.snack_2,bg="#BE965A")
        SnackS.grid(row=4,column=2,sticky="we",padx=50)

        judul = Label(Frame4,text="Hotdog\nRp.25.000",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=2,sticky="n",pady=10,padx=10)

        #3
        Snack = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\pop.png")
        Snack = Snack.resize((150,155), Image.LANCZOS)
        self.snack_3 = ImageTk.PhotoImage(Snack)
        
        SnackS = Label(Frame4, image=self.snack_3,bg="#BE965A")
        SnackS.grid(row=4,column=3,sticky="we",padx=50)

        judul = Label(Frame4,text="Popcorn\nRp.20.000",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=3,sticky="n",pady=10,padx=10)

        #4
        Snack = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\buerger.png")
        Snack = Snack.resize((150,155), Image.LANCZOS)
        self.snack_4 = ImageTk.PhotoImage(Snack)
        
        SnackS = Label(Frame4, image=self.snack_4,bg="#BE965A")
        SnackS.grid(row=4,column=4,sticky="we",padx=50)

        judul = Label(Frame4,text="Burger\nRp.30.000",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=4,sticky="n",pady=10,padx=10)
        
        #5
        Snack = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\soda.png")
        Snack = Snack.resize((150,155), Image.LANCZOS)
        self.snack_5 = ImageTk.PhotoImage(Snack)
        
        SnackS = Label(Frame4, image=self.snack_5,bg="#BE965A")
        SnackS.grid(row=4,column=5,sticky="we",padx=50)

        judul = Label(Frame4,text="Soda\nRp.15.0000",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=5,sticky="n",pady=10,padx=10)

        #6
        Snack = Image.open("D:\\B. Tugas Kuliah\\Prinsip Pemrograman\\Project_UAs\\water.png")
        Snack = Snack.resize((150,155), Image.LANCZOS)
        self.snack_6 = ImageTk.PhotoImage(Snack)
        
        SnackS = Label(Frame4, image=self.snack_6,bg="#BE965A")
        SnackS.grid(row=4,column=6,sticky="we",padx=50)

        judul = Label(Frame4,text="Air Mineral\nRp.10.0000",font=("Times New Roman",12),relief=FLAT,fg="snow1",bg="#5E0101")
        judul.grid(row=5,column=6,sticky="n",pady=10,padx=10)
        #Tombol konfirmasi snack geser
        knfrm_flm = Button(self.snack, text="Konfirmasi", command=lambda: self.Konfirmasi_ke_nota(film_terpilih,kursi_terpilih))#############################
        knfrm_flm.grid(row=7, column=0, padx=10, pady=10,columnspan=3) #tombol konfirmasi snack

        Frame5 = LabelFrame(self.snack, text="Masukan Snack", font=("Perpetua", 25), relief=FLAT, bg="#5E0101", fg="#BE965A")
        Frame5.grid(row=7, column=0, pady=50 ,sticky="w",padx=30)

        fr_fries = Label(Frame5, text="French Fries", font=("Times New Roman", 15),bg="#5E0101", fg="#BE965A")
        fr_fries.grid(row=0, column=0, padx=1, pady=5, sticky="w")
        input_fr_fries = Entry(Frame5, width=5, borderwidth=5, relief=GROOVE)
        input_fr_fries.grid(row=0, column=1, padx=10, pady=10)
        input_fr_fries.insert(0, 0) 

        htdg = Label(Frame5, text="Hotdog", font=("Times New Roman", 15),bg="#5E0101", fg="#BE965A")
        htdg.grid(row=1, column=0, padx=1, pady=5, sticky="w")
        input_htdg = Entry(Frame5, width=5, borderwidth=5, relief=GROOVE)
        input_htdg.grid(row=1, column=1, padx=10, pady=10)
        input_htdg.insert(0, 0) 

        pop = Label(Frame5, text="Popcorn", font=("Times New Roman", 15),bg="#5E0101", fg="#BE965A")
        pop.grid(row=2, column=0, padx=1, pady=5, sticky="w")
        input_pop = Entry(Frame5, width=5, borderwidth=5, relief=GROOVE)
        input_pop.grid(row=2, column=1, padx=10, pady=10)
        input_pop.insert(0, 0) 

        
        brgr = Label(Frame5, text="Burger", font=("Times New Roman", 15),bg="#5E0101", fg="#BE965A")
        brgr.grid(row=0, column=2, padx=1, pady=5, sticky="w")

        input_brgr = Entry(Frame5, width=5, borderwidth=5, relief=GROOVE)
        input_brgr.grid(row=0, column=3, padx=10, pady=10)
        input_brgr.insert(0, 0) 

        soda = Label(Frame5, text="Soda", font=("Times New Roman", 15),bg="#5E0101", fg="#BE965A")
        soda.grid(row=1, column=2, padx=1, pady=5, sticky="w")

        input_soda = Entry(Frame5, width=5, borderwidth=5, relief=GROOVE)
        input_soda.grid(row=1, column=3, padx=10, pady=10)
        input_soda.insert(0, 0) 

        air = Label(Frame5, text="Air Mineral", font=("Times New Roman", 15),bg="#5E0101", fg="#BE965A")
        air.grid(row=2, column=2, padx=1, pady=5, sticky="w")
        
        input_air = Entry(Frame5, width=5, borderwidth=5, relief=GROOVE)
        input_air.grid(row=2, column=3, padx=10, pady=10)
        input_air.insert(0, 0) 

        Total = Label(Frame5, text="Total", font=("Times New Roman", 15),bg="#5E0101", fg="#BE965A")
        Total.grid(row=5, column=0, padx=1, pady=10, sticky="w")

        Rp = Label(Frame5, text="Rp", font=("Times New Roman", 15),bg="#5E0101", fg="#BE965A")
        Rp.grid(row=6, column=0, padx=1, pady=10, sticky="w")
         
        

        self.Total_snck = Entry(Frame5, width=10, borderwidth=5, relief=GROOVE)
        self.Total_snck.grid(row=6, column=0, padx=1, pady=0,columnspan=2)
        self.Total_snck.insert(0, 0) #nampilin harga total

       

        
         

        cek_harga_snack = Button(Frame5, text="Cek", command=lambda: self.total_harga_snack(input_fr_fries,input_htdg,input_pop,input_brgr,input_air,input_soda,self.Total_snck), bg="snow1", fg="black",relief=RAISED)
        cek_harga_snack.grid(row=7, column=0, padx=1, pady=10,sticky="n",columnspan=4) #tombol cek haega snack

        del_harga_snack = Button(Frame5, text="Del", command=lambda: self.hapus_harga_snack(input_fr_fries,input_htdg,input_pop,input_brgr,input_air,input_soda,self.Total_snck), bg="snow1", fg="black",relief=RAISED)
        del_harga_snack.grid(row=7, column=1, padx=1, pady=10,sticky="n",columnspan=4) #tombol hapus snack harga dan jumlah



    def total_harga_snack(self,input_fr_fries,input_htdg,input_pop,input_brgr,input_air,input_soda,Total_snck):#fungsinya cek harga
        harga_fr_fries = int(input_fr_fries.get())*20000
        harga_htdg = int(input_htdg.get())*25000
        harga_pop = int(input_pop.get())*20000
        harga_brgr = int(input_brgr.get())*30000
        harga_soda = int(input_soda.get())*15000
        harga_air = int(input_air.get())*10000

        self.Total_snack = harga_fr_fries + harga_htdg + harga_pop +harga_brgr + harga_soda + harga_air

        total_formatted = "{:,.0f}".format(self.Total_snack)
        Total_snck.delete(0, END)
        Total_snck.insert(0, total_formatted)

        self.simpan_total_snack_value()


        

    def hapus_harga_snack(self,input_fr_fries,input_htdg,input_pop,input_brgr,input_air,input_soda,Total_snck):#fungsinya hapus
        hapus_fr_fries = int(input_fr_fries.get()) * 0
        hapus_htdg = int(input_htdg.get()) * 0
        hapus_pop = int(input_pop.get()) * 0
        hapus_brgr = int(input_brgr.get()) *0
        hapus_soda = int(input_soda.get())*0
        hapus_air = int(input_air.get())*0

        hapus_formatted_fr = "{:,.0f}".format(hapus_fr_fries)
        input_fr_fries.delete(0, END)
        input_fr_fries.insert(0, hapus_formatted_fr)

        hapus_formatted_htdg = "{:,.0f}".format(hapus_htdg)
        input_htdg.delete(0, END)
        input_htdg.insert(0, hapus_formatted_htdg)

        hapus_formatted_pop = "{:,.0f}".format(hapus_pop)
        input_pop.delete(0, END)
        input_pop.insert(0, hapus_formatted_pop)

        hapus_formatted_brgr = "{:,.0f}".format(hapus_brgr)
        input_brgr.delete(0, END)
        input_brgr.insert(0, hapus_formatted_brgr)

        hapus_formatted_soda = "{:,.0f}".format(hapus_soda)
        input_soda.delete(0, END)
        input_soda.insert(0, hapus_formatted_soda)

        hapus_formatted_air = "{:,.0f}".format(hapus_air)
        input_air.delete(0, END)
        input_air.insert(0, hapus_formatted_air)

        self.Total_snack = hapus_fr_fries + hapus_htdg + hapus_pop + hapus_brgr + hapus_soda + hapus_air

        hapus_formatted = "{:,.0f}".format(self.Total_snack)
        Total_snck.delete(0, END)
        Total_snck.insert(0, hapus_formatted)

        self.simpan_total_snack_value()

  

      

      

class nota:
    # def __init__(self,Parent,harga_kursi_rp,snack_total_value):
    def __init__(self,Parent):
        self.nota = Parent
        
    def nota1(self,film_terpilih,kursi_terpilih):
        for i in self.nota.winfo_children():
            i.destroy()
       
        self.nota_bayar(film_terpilih,kursi_terpilih)  # nampilin halaman penting

    def nota_bayar(self,film_terpilih,kursi_terpilih):  # fungsi isinya halaman snack

        Film = Label(self.nota, text="CineBOX\t\t\t\t\t\t\t\t", font=("Perpetua", 40), relief=FLAT, bg="#5E0101",
                     fg="#BE965A")
        Film.grid(row=0, column=0, columnspan=4, sticky="w", pady=10)

        Frame8 = LabelFrame(self.nota,text="Pembayaran",font=("Perpetua",25),relief=FLAT,bg="#5E0101",fg="#BE965A")
        Frame8.grid(row=2, column=0, columnspan=4, sticky="n", pady=10)

        Frame9 = LabelFrame(Frame8,text="",font=("Perpetua",25),relief=FLAT,bg="azure4",fg="#BE965A")
        Frame9.grid(row=3, column=0, columnspan=4, sticky="n")
        
        nama_film = Label(Frame9, text="Nama Film", font=("Times New Roman", 15),bg="azure4", fg="black")
        nama_film.grid(row=0, column=0, padx=1, pady=5, sticky="w")

        input_nama_film = Entry(Frame9, width=20, borderwidth=5, relief=GROOVE)
        input_nama_film.grid(row=0, column=1, padx=10, pady=10)
        input_nama_film.insert(0, film_terpilih) 

        tmptddk = Label(Frame9, text="Kursi", font=("Times New Roman", 15),bg="azure4", fg="black")
        tmptddk.grid(row=1, column=0, padx=1, pady=5, sticky="w")

        input_tmptdkk = Entry(Frame9, width=20, borderwidth=5, relief=GROOVE)
        input_tmptdkk.grid(row=1, column=1, padx=10, pady=10)
        input_tmptdkk.insert(0, kursi_terpilih) 

        harga_total = Label(Frame9, text="Harga Total", font=("Times New Roman", 15),bg="azure4", fg="black")
        harga_total.grid(row=2, column=0, padx=1, pady=5, sticky="w")

        input_harga_total = Entry(Frame9, width=20, borderwidth=5, relief=GROOVE)
        input_harga_total.grid(row=2, column=1, padx=10, pady=10)
        input_harga_total.insert(0, kursi_terpilih) 


        
def main():
    nt = nota(win)
    snck = snack(win,nt)
    mn = menu(win, snck)
    Log = Login(win, mn)
    Log.Hal1()

    win.mainloop()


if __name__ == "__main__":
    main()
