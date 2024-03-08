import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import*
from tkinter.messagebox import showinfo
import ast
from tkVideoPlayer import TkinterVideo
from tkVideoPlayer import TkinterVideo
import pygame
pygame.init()
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import font

from tkinter import scrolledtext


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)
        self.title('Reacciona')
        self.geometry("1000x600")
        self.resizable(False, False)
        
        paginas = tk.Frame(self)
        paginas.pack(side="top", fill="both", expand=True)
        paginas.grid_rowconfigure(0, weight=1)
        paginas.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        for Paginas in (App, Registro, Login, Ordenar):
            frame = Paginas(paginas, self)
            self.frames[Paginas] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_Ventana(App)
            
        
            
    def show_Ventana(self, paginas):
        ventana = self.frames[paginas]
        ventana.tkraise()
            
class Registro(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Registro.png")
        self.w = self.image1.width()
        self.h = self.image1.height()


        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        
        
                
        self.username = StringVar()
        self.contraseña = StringVar()
        self.email = StringVar()
        self.confirm = StringVar()
        
        
        
        self.entrada_username= tk.Entry(self, textvariable=self.username, width=29,bd=0,font=("League Spartan",13)).place(x=50,y=185)
        
        
        self.entrada_contraseña = tk.Entry(self, textvariable=self.contraseña, width=25,bd=0,  font=("League Spartan",15),show="*").place(x=45,y=335)
        
        self.entrada_email= tk.Entry(self, textvariable=self.email, width=29,bd=0, font=("League Spartan",13)).place(x=50,y=263)
        self.confirm_entrada = tk.Entry(self, textvariable=self.confirm, width=25,bd=0,  font=("League Spartan",15),show="*").place(x=45,y=422)

        self.label = tk.Label(self, text = "Already have an account?", fg = "black", bg = "white", font = ('Microsoft YaHei UI Light', 11)).place(x=70, y=520)
    
        self.button2 = tk.Button(self,text="Sign in", cursor="hand2", bg = "white", border = 0,  fg = "#28847F", font=("League Spartan underline",11), command = (lambda: self.cambiar_Pagina(controller))).place(x=264,y=520)

        self.button = tk.Button(self,text="Create new Account", bg = "#E16B52", width = 45, pady = 7,  relief = "flat", border = 0, font = ("League Spartan",12), command = (lambda: self.save())).place(x=20,y=465)
           
            
    def save(self):
        self.name = self.username.get()
        self.contra = self.contraseña.get()
        self.em = self.email.get()
        conn = sqlite3.connect("Reacciona1.db")
        with conn:
            cur=conn.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Info(username, contraseña, email)")
            cur.execute("INSERT INTO Info(username, email, contraseña) VALUES(?,?,?)", (self.name, self.contra, self.em))
            conn.commit()
            


    def cambiar_Pagina(self, controller):
        controller.show_Ventana(Login)
        self.button2.config()


class Login(tk.Frame):


    def __init__(self, parent, controller):
    
    

        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Login.png")
        self.w = self.image1.width()
        self.h = self.image1.height()


        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        self.username = StringVar()
        self.contraseña = StringVar()
        
        self.entrada_username= tk.Entry(self, textvariable=self.username, width=29,bd=0,font=("League Spartan",13)).place(x=70,y=270)
        
        self.entrada_contraseña = tk.Entry(self, textvariable=self.contraseña, width=29,bd=0,font=("League Spartan",15),show="*").place(x=70,y=400)

        self.label = tk.Label(self, text = "Don´t have an account yet?", fg = "black", bg = "white", font = ('Microsoft YaHei UI Light', 11)).place(x=70, y=520)
        self.button2 = tk.Button(self,text="Sign up", cursor="hand2", bg = "white", border = 0, fg = "#28847F", font=("League Spartan underline",11), command = (lambda: self.cambiar_Pagina(controller))).place(x=266,y=521)
        
        self.button = tk.Button(self,text="Ingresar", bg = "#E16B52", width = 39,pady = 10,  relief = "flat", border = 0, font = ("League Spartan",12), command = (lambda: self.login(controller))) .place(x=50,y=450)
        
    def login(self, controller):
       
        conn = sqlite3.connect("Mentally.db")
        c = conn.cursor()
        
        self.name = self.username.get()
        self.contra = self.contraseña.get()
        
        c.execute('SELECT * FROM Info WHERE username = ? AND contraseña = ?', (self.name, self.contra))

        if c.fetchall():
            controller.show_Ventana(App)
            self.button2.config()

        c.close()

        
            
    def cambiar_Pagina(self, controller):
        controller.show_Ventana(Registro)
        self.button2.config()
        
    
        
class App(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Página.png")
        self.w = self.image1.width()
        self.h = self.image1.height()
        
        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        self.league_spartan_font = font.Font(family="Roboto", size=12, weight = "bold")
    
        
        self.button = Button(self,text="ORDENA YA", bg = "#FFCE4A", fg = "black", width = 25, pady = 7,  relief = "flat", border = 0, font = self.league_spartan_font, command = (lambda: self.ordenar(controller))).place(x=160,y=360)
        self.button2 = tk.Button(self,text="Inicio", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=264,y=30)
        self.button2 = tk.Button(self,text="Conocenos", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=330,y=30)
        self.button2 = tk.Button(self,text="Promociones", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=440,y=30)
        self.button2 = tk.Button(self,text="Llamar mesero", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=560,y=30)
        self.button2 = tk.Button(self,text="🛒", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",16, "bold")).place(x=850,y=23)
        self.button2 = tk.Button(self,text="👤", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",16, "bold")).place(x=950,y=23)
        self.button2 = tk.Button(self,text="★", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",14, "bold")).place(x=900,y=24)

    def ordenar(self, controller):
        controller.show_Ventana(Ordenar)
        self.button2.config()
        
class Ordenar(tk.Frame):
     def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg = "white" )
        self.image1 = tk.PhotoImage(file="Menu1.png")
        self.w = self.image1.width()
        self.h = self.image1.height()
        
        self.panel1 = tk.Label(self, image=self.image1)
        self.panel1.pack(side='top', fill='both', expand='yes')

        self.panel1.image = self.image1
        
        self.foto33 = PhotoImage(file = "Entradas.png")
        self.button3333 = tk.Button(self,  image = self.foto33, borderwidth=0, highlightthickness=0)
        self.button3333.place(x=20, y=380)
        
        self.foto1 = PhotoImage(file = "Taco.png")
        self.button1 = tk.Button(self,  image = self.foto1, borderwidth=0, highlightthickness=0)
        self.button1.place(x=260, y=380)
        
        self.foto2 = PhotoImage(file = "Flan (1).png")
        self.button2 = tk.Button(self,  image = self.foto2, borderwidth=0, highlightthickness=0)
        self.button2.place(x=480, y=380)
            
        self.foto22 = PhotoImage(file = "Bebidas.png")
        self.button22 = tk.Button(self,  image = self.foto22, borderwidth=0, highlightthickness=0)
        self.button22.place(x=730, y=380)
        
        self.button2 = tk.Button(self,text="Entradas", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",12, "bold")).place(x=110,y=560)
        self.button2 = tk.Button(self,text="Platos Fuertes", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",12, "bold")).place(x=320,y=560)
        self.button2 = tk.Button(self,text="Postres", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",12, "bold")).place(x=560,y=560)
        self.button2 = tk.Button(self,text="Bebidas", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",12, "bold")).place(x=810,y=560)

        self.button2 = Label(self,text="Inicio", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=264,y=12)
        self.button2 = Label(self,text="Conocenos", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=330,y=12)
        self.button2 = Label(self,text="Promociones", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=440,y=12)
        self.button2 = Label(self,text="Llamar mesero", cursor="hand2", bg = "white", border = 0,  fg = "grey", font=("League Spartan underline",12, "bold")).place(x=560,y=12)
                
        self.button2 = tk.Button(self,text="🛒", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",16, "bold")).place(x=850,y=5)
        self.button2 = tk.Button(self,text="👤", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",16, "bold")).place(x=950,y=5)
        self.button2 = tk.Button(self,text="★", cursor="hand2", bg = "white", border = 0,  fg = "black", font=("League Spartan underline",14, "bold")).place(x=900,y=8)


if __name__ == '__main__':
    app = Main()
    app.mainloop()
        
        
        
        
        



