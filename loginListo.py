from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from PIL import Image
from NUEVOcRUD import *















#COLORES FONDO
fondo_entrar="#FF1616" #rojo
fondo_salir="#004AAD" #azul
fondo_correcto="#8C52FF"
fondo_incorrecto="#1DE6E6"
fondo_entrada="#D9D9D9"


ventanaLogin= tk.Tk()
ventanaLogin.title("Celu-Store 1.0v")
ventanaLogin.geometry("500x500+500+50")
ventanaLogin.resizable(0,0)
fondo= tk.PhotoImage(file='src/entrar.png')
fondo1=tk.Label(ventanaLogin, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)



usuario=tk.StringVar()
password=tk.StringVar()

#ENTRADAS
entrada=tk.Entry(ventanaLogin, textvar=usuario, width=15, relief="flat", bg=fondo_entrada)
entrada.place(x=320, y=300)

entrada2=tk.Entry(ventanaLogin, textvar=password, show="#", width=15, relief="flat", bg=fondo_entrada)
entrada2.place(x=320, y=335)


def login():
    
    nombre=usuario.get()
    contraseña=password.get()

    if nombre == "hora" and contraseña == "1234":
        abrirventana2()
        ventanaLogin.withdraw()
    

    else:
        messagebox.showwarning("Cuidado", "Pasword Incorrecto")
        #incorrecta()
    

def abrirventana2():
    ventanaLogin.withdraw()
    win()



win=tk.Toplevel()
win.geometry("800x670")
win.configure(background="dark turquoise")
win.resizable(0,0)
win.title("Celu-Store 1.0v")
e3=tk.Label(win, text="SISTEMA DE FACTURACION", bg="pink", fg="white")
e3.pack(padx=5,pady=5,ipadx=5,ipady=5, fill=tk.X)
    
marco =LabelFrame(win, text="Informacion del producto",font=("Comic Sans", 10,"bold"),pady=5)
marco.config(bd=2)
marco.pack()
    
boton2=tk.Button(win, text="SALIR",command=win.destroy)
boton2.pack(side=tk.TOP)
    
    

    
    
    


#--------------------------

def correcta():
    
    ventanaLogin.withdraw()#oculta ventana sin destruirla
    window=tk.Toplevel()
    window.title("BIENVENIDOS")
    window.geometry("500x500+500+50")
    window.resizable(0,0)
    fondo= tk.PhotoImage(file='crud.png')
    fondo1=tk.Label(ventanaLogin, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)
    NUEVO

    window.mainloop()



def salir():
    ventanaLogin.destroy()

#BOTONES
boton1 =tk.Button(ventanaLogin, text="ENTRAR",command=login, cursor="hand2", bg =fondo_entrar, width=12, relief="flat")# relief BOTON DISIMULA BORDE, SIN RELIEVE
boton1.place(x=320, y=370)

boton2 =tk.Button(ventanaLogin, text="SALIR",command=salir, cursor="hand2", bg =fondo_salir, width=12, relief="flat")
boton2.place(x=320, y=405)



ventanaLogin.mainloop()

                

