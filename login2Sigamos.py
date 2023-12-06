from tkinter import *
from tkinter import ttk
from tkinter import messagebox, Image
import tkinter as tk

import sqlite3





#COLORES FONDO
fondo_entrar="#FF1616" #rojo
fondo_salir="#004AAD" #azul
fondo_correcto="#8C52FF"
fondo_incorrecto="#1DE6E6"
fondo_entrada="#D9D9D9"



ventanaLogin= tk.Tk()
ventanaLogin.title("Celu-Store")
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
    

    else:
        messagebox.showwarning("Cuidado", "Datos Incorrectos")
        #incorrecta()
        
        
        
#-----------------------

def abrirventana2():
    ventanaLogin.withdraw()
    win=tk.Toplevel()
    win.geometry("500x500+500+50")
    win.configure(background="sky blue")
    win.title("ventana 2")
    e3=tk.Label(win, text="Celu-Store", bg="navajo white", fg="white")
    e3.pack(padx=5,pady=5,ipadx=5,ipady=5, fill=tk.X)
    
    entrada3=tk.Entry(abrirventana2, textvar=usuario, width=15, relief="flat", bg=fondo_entrada)
    entrada3.place(x=320, y=300)
    
    ventanaPrincipal=Tk()
ventanaPrincipal.title("CELU-STORE 1.0v")
ventanaPrincipal.geometry("600x500")

db=DataBase()

modelo=StringVar()
descripcion=StringVar()
marca=StringVar()
precio=StringVar()
modificar=False

marco= LabelFrame(ventanaPrincipal, text="Sistema de Ventas de Celualres")
marco.place(x=60,y=60,width=500, height=400)

#labels y entry

lblmarcaCelular=Label(marco, text="MARCA").grid(column=0,row=0, padx=5, pady=5)
txtmarcaCelular=ttk.Combobox(marco, values=["Motorola","Samsung","Nokia","TCL","Xiaomi","LG","Huawei","ZTE","Apple"], textvariable=marca)
txtmarcaCelular.current(0) #deja seleccionado por defecto el primer elemento
txtmarcaCelular.grid(column=1,row=0)

lblmodeloCelular=Label(marco, text="MODELO").grid(column=0,row=1, padx=5, pady=5)
txtmodeloCelular=Entry(marco, textvariable=modelo)
txtmodeloCelular.grid(column=1,row=1)

lbldescripcionCElular=Label(marco, text="DESCRIPCION").grid(column=2,row=0, padx=5, pady=5)
txtdescripcionCelular=Entry(marco, textvariable=descripcion)
txtdescripcionCelular.grid(column=3,row=0)

lblprecioCelular=Label(marco, text="PRECIO").grid(column=2,row=1, padx=5, pady=5)
txtprecioCelular=Entry(marco, textvariable=precio)
txtprecioCelular.grid(column=3,row=1)

txtMensaje=Label(marco, text="☆::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::☆", fg="green")
txtMensaje.grid(column=0, row=2, columnspan=4)

# tabla treview
tablaproductos=ttk.Treeview(marco)
tablaproductos.grid(column=0, row=3, columnspan=4)  #column span averiguar que hace
tablaproductos["columns"]=("Id","MARCA","MODELO","DESCRIPCION","PRECIO")
tablaproductos.column("#0", width=0, stretch=NO) #averiguasr que hace
tablaproductos.column("Id", width=50, anchor=CENTER) #averiguasr que hace
tablaproductos.column("MARCA", width=100, anchor=CENTER) #averiguasr que hace
tablaproductos.column("MODELO", width=100, anchor=CENTER) #averiguasr que hace
tablaproductos.column("DESCRIPCION", width=100, anchor=CENTER) #averiguasr que hace
tablaproductos.column("PRECIO", width=50, anchor=CENTER) #averiguasr que hace
#tablaproductos.column("IVA", width=50, anchor=CENTER) #averiguasr que hace

#encabezados de la tabla

tablaproductos.heading("#0", text="")
tablaproductos.heading("Id", text="Id", anchor= CENTER)
tablaproductos.heading("MARCA", text="MARCA", anchor= CENTER)
tablaproductos.heading("MODELO", text="MODELO", anchor= CENTER)
tablaproductos.heading("DESCRIPCION", text="DESCRIPCION", anchor= CENTER)
tablaproductos.heading("PRECIO", text="PRECIO", anchor= CENTER)

#botones de accion

btnAgregar=Button(marco, text= "AGREGAR", command=lambda:agregar()) #averiguar lambda
btnAgregar.grid(column=0,row=4)

btnELiminar=Button(marco, text= "ELIMINAR", command=lambda:eliminar()) #averiguar lambda
btnELiminar.grid(column=0,row=5)

btnActualizar=Button(marco, text= "ACTUALIZAR", command=lambda:actualizar()) #averiguar lambda
btnActualizar.grid(column=1,row=4)

btnVender=Button(marco, text= "FACTURAR", command=lambda:facturar()) #averiguar lambda
btnVender.grid(column=3,row=4)







#funciones (el treview se borra fila x fila, hay  q recorrer, 
# primero averiguo la cantidad de filas y despues la recorro)

def modificarFalse():
    global modificar
    modificar=False
    tablaproductos.config(selectmode=NONE)
    btnAgregar.config(text="Guardar")
    btnActualizar.config(text="Seleccionar")
    btnELiminar.config(state=DISABLED)
def modificarTrue():
    global modificar
    modificar=TRUE
    tablaproductos.config(selectmode=BROWSE)
    btnAgregar.config(text="Nuevo")
    btnActualizar.config(text="Modificar")
    btnELiminar.config(state=NORMAL)    
def agregar():
    if modificar==FALSE:
        if validar():
            val=(marca.get(),descripcion.get(),modelo.get(),precio.get())
            sql="insert into celustore (marca,modelo,descripcion,precio) values (%s,%s,%s,%s)"
            db.cursor.execute(sql,val)
            db.connection.commit()
            txtMensaje.config(text="REGISTRO AGREGADO CORECCTAMENTE", fg="green")
            llenar_tabla()
            limpiar()
        else:
            txtMensaje.config(text="CAMPOS VACIOS", fg="red")
    else:
            modificarFalse()
                

def validar():
    return len(marca.get()) and  len(modelo.get()) and len(descripcion.get()) and  len(precio.get())
    


def limpiar():
    marca.set("")
    modelo.set("")
    descripcion.set("")
    precio.set("")

def vaciar_tabla():
    filas=tablaproductos.get_children()  #averiguo cuantas filas tiene devuelve todas las filas
    for fila in filas:   # esto es na tupla
        tablaproductos.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    sql="select * from celustore"
    db.cursor.execute(sql)
    filas=db.cursor.fetchall() #averiguar que es
    
    for fila in filas:
        Id=fila[0]
        tablaproductos.insert("", END,Id, text= Id, values=fila)
            

def eliminar():
    Id=tablaproductos.selection()[0]
    if int(Id)>0:
        sql="delete from celustore where Id="+Id
        db.cursor.execute(sql)
        db.connection.commit() # que hace se debe confirmar o comitear
        tablaproductos.delete(Id)
        txtMensaje.config(text="REGISTRO ELIMINADO CORRECTAMENTE", fg="green")
    else:
        txtMensaje.config(text="SELECCIONE UN REGISTRO PARA ELIMINAR", fg="red")
        

def actualizar():
    if modificar==TRUE:
        if validar():
            val=(marca.get(),descripcion.get(),modelo.get(),precio.get())
            sql="update celustore set marca=%s,modelo=%s,descripcion=%s,precio=%s"
            db.cursor.execute(sql,val)
            db.connection.commit()
            txtMensaje.config(text="REGISTRO ACTUALIZADO", fg="green")
            llenar_tabla()
            limpiar()
        else:
            txtMensaje.config(text="CAMPOS VACIOS", fg="red")
    else:
            modificarTrue()




llenar_tabla()
ventanaPrincipal.mainloop()
    
    
    
    
#-----------------------






"""
    boton2=tk.Button(win, text="facturar",command=win.destroy)
    boton2.pack(side=tk.TOP)
    """

#--------------------------
"""

def correcta():
    
    ventanaLogin.withdraw()#oculta ventana sin destruirla
    window=tk.Toplevel()
    window.title("BIENVENIDOS")
    window.geometry("500x500+500+50")
    window.resizable(0,0)
    fondo= tk.PhotoImage(file='crud.png')
    fondo1=tk.Label(ventanaLogin, image=fondo).place(x=0, y=0, relwidth=1, relheight=1)


    window.mainloop()

"""

def salir():
    ventanaLogin.destroy()

#BOTONES
boton1 =tk.Button(ventanaLogin, text="ENTRAR",command=login, cursor="hand2", bg =fondo_entrar, width=12, relief="flat")# relief BOTON DISIMULA BORDE, SIN RELIEVE
boton1.place(x=320, y=370)

boton2 =tk.Button(ventanaLogin, text="SALIR",command=salir, cursor="hand2", bg =fondo_salir, width=12, relief="flat")
boton2.place(x=320, y=405)




ventanaLogin.mainloop()
                

