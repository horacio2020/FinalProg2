from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from conexion import *
from conexion import DataBase
import time
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4


ventanaPrincipal=Tk()
ventanaPrincipal.title("CELU-STORE 1.0v")
ventanaPrincipal.geometry("600x500")

db=DataBase()

modelo=StringVar()
descripcion=StringVar()
marca=StringVar()
precio=StringVar()
modificar=False

def seleccionar(event):
    
    Id=tablaproductos.selection()[0]
    if int(Id)>0:
        marca.set(tablaproductos.item(Id,"values")[1])
        modelo.set(tablaproductos.item(Id,"values")[2])
        descripcion.set(tablaproductos.item(Id,"values")[3])
        precio.set(tablaproductos.item(Id,"values")[4])

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
tablaproductos=ttk.Treeview(marco, selectmode=NONE)
tablaproductos.grid(column=0, row=3, columnspan=4)  #column span averiguar que hace
tablaproductos["columns"]=("Id","MARCA","MODELO","DESCRIPCION","PRECIO")
tablaproductos.column("#0", width=0, stretch=NO) #averiguasr que hace
tablaproductos.column("Id", width=50, anchor=CENTER) #averiguasr que hace
tablaproductos.column("MARCA", width=100, anchor=CENTER) #averiguasr que hace
tablaproductos.column("MODELO", width=100, anchor=CENTER) #averiguasr que hace
tablaproductos.column("DESCRIPCION", width=100, anchor=CENTER) #averiguasr que hace
tablaproductos.column("PRECIO", width=50, anchor=CENTER) #averiguasr que hace
#tablaproductos.column("IVA", width=50, anchor=CENTER) #averiguasr que hace
tablaproductos.bind("<<TreeviewSelect>>", seleccionar)

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

btnActualizar=Button(marco, text= "SELECCIONAR", command=lambda:actualizar()) #averiguar lambda
btnActualizar.grid(column=1,row=4)

btnVender=Button(marco, text= "FACTURAR", command=lambda:imprimir_ticket()) #averiguar lambda
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
            txtMensaje.config(text="REGISTRO AGREGADO CORECTAMENTE", fg="green")
            llenar_tabla()
            limpiar()
        else:
            txtMensaje.config(text="CAMPOS VACIOS", fg="red")
    else:
            modificarFalse()
                

def validar():
    return len(marca.get()) and len(modelo.get()) and len(descripcion.get()) and  len(precio.get())
    


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
            Id=tablaproductos.selection
            val=(marca.get(),descripcion.get(),modelo.get(),precio.get())
            sql="update celustore set marca=%s,modelo=%s,descripcion=%s,precio=%s where Id="+Id
            db.cursor.execute(sql,val)
            db.connection.commit()
            txtMensaje.config(text="REGISTRO ACTUALIZADO", fg="green")
            llenar_tabla()
            limpiar()
        else:
            txtMensaje.config(text="CAMPOS VACIOS", fg="red")
    else:
            modificarTrue()
            messagebox.showinfo("Ticket Impreso", "Ticket de venta generado correctamente")
            
            
def imprimir_ticket():
    selected_item = tablaproductos.selection()
    if selected_item:
        item_data = tablaproductos.item(selected_item)['values']
        with open('ticket.txt', 'w') as file:
            file.write(f"marca: {item_data[1]}\n")
            file.write(f"modelo: {item_data[2]}\n")
            file.write(f"descripción: {item_data[3]}\n")
            file.write(f"precio: ${item_data[4]}\n")
        with open('ticket.txt', 'r') as file:
            print(file.read())



llenar_tabla()
ventanaPrincipal.mainloop()