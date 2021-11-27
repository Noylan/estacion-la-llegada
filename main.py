# Importando modulos que sirven para importar tkinter, la fehca y limpiar la consola.
import os, tkinter, datetime
from tkinter import *
from tkinter import ttk
from datetime import *

# Comando para limpiar la consola. 
os.system ("cls")

# Variable para la logica de ventanas.
cerrado = True

# <------------------------------------------------------------ MENUS SECUNDARIOS Y FUNCIONES ----------------------------------------------------------->
def usuario():
    global cerrado

    def cerrar():
        global cerrado
        ventana_usuario.destroy()
        cerrado = True

    def guardar_usuario():
        #Creo el vector clientes.
        clientes = []

        #nombre = input('Ingrese un nombre: ')
        nombre = caja_nombre.get()

        #apellido = input('Ingrese un apellido: ')
        apellido = caja_apellido.get()

        #dni = input('Ingrese un D.N.I (sin puntos): ')
        dni = caja_dni.get()

        localidad = caja_localidad.get()

        telefono = str(caja_telefono.get())

        correo = caja_correo.get()

        direccion = caja_direccion.get()

        codigo_postal = str(caja_codigo_postal.get())

        #Al final de cada usuario lo guardo en el vector.
        clientes.append(nombre + ',' + apellido + ',' + dni + ',' + localidad + ',' + telefono + ',' + correo + ',' + direccion + ',' + codigo_postal)

        #Borramos los datos ya guardados del formulario.
        caja_nombre.delete(0,"end")
        caja_apellido.delete(0,"end")
        caja_dni.delete(0,"end")
        caja_localidad.delete(0,"end")
        caja_telefono.delete(0,"end")
        caja_correo.delete(0,"end")
        caja_direccion.delete(0,"end")
        caja_codigo_postal.delete(0,"end")
        
        #Selecionamos la primera entrada para mayor facilidad.
        caja_nombre.focus()

        try:
            archivo = open('./archivos/clientes.txt', 'x', encoding='utf-8') #Creo el archivo cliente.txt
        except FileExistsError:
            archivo = open('./archivos/clientes.txt', 'a', encoding='utf-8') #Agrego al archivo ya creado nuevos datos
        
        #Recorro el vector clientes por posicion.
        for a in range(len(clientes)):
            archivo.write(clientes[a])
            archivo.write('\n')

    if cerrado:
        ventana_usuario = tkinter.Tk()
        ventana_usuario.title('Guardar Usuario')
        ventana_usuario.geometry('790x450')

        etiqueta = tkinter.Label(ventana_usuario, text = 'Guardar usuario')
        etiqueta.grid(row = 0, column = 1)

        etiqueta_nombre = tkinter.Label(ventana_usuario, text ='Nombre:').grid(row = 1, column = 0, padx= 2)
        caja_nombre = tkinter.Entry(ventana_usuario, width=50)
        caja_nombre.grid(row = 1, column = 1, padx= 5, pady = 5)

        etiqueta_apellido= tkinter.Label(ventana_usuario, text ='Apellido:').grid(row = 1, column = 2, padx= 2)
        caja_apellido = tkinter.Entry(ventana_usuario, width=50)
        caja_apellido.grid(row = 1, column = 3, padx= 5, pady = 5)

        etiqueta_dni = tkinter.Label(ventana_usuario, text ='D.N.I:').grid(row = 2, column = 0, padx= 2)
        caja_dni = tkinter.Entry(ventana_usuario, width=50)
        caja_dni.grid(row = 2, column = 1, padx= 5, pady = 5)

        etiqueta_localidad = tkinter.Label(ventana_usuario, text ='Localidad: ').grid(row = 2, column = 2, padx= 2)
        caja_localidad = tkinter.Entry(ventana_usuario, width=50)
        caja_localidad.grid(row = 2, column = 3, padx= 5, pady = 5)


        etiqueta_telefono = tkinter.Label(ventana_usuario, text ='Telefono: ').grid(row = 3, column = 0, padx= 2 )
        caja_telefono = tkinter.Entry(ventana_usuario, width= 50)
        caja_telefono.grid(row = 3, column = 1, padx= 5, pady = 5)
        
        
        etiqueta_correo = tkinter.Label(ventana_usuario, text ='Correo: ').grid(row = 3, column = 2, padx= 2)
        caja_correo = tkinter.Entry(ventana_usuario, width=50)
        caja_correo.grid(row = 3, column = 3, padx= 5, pady = 5)


        etiqueta_direccion = tkinter.Label(ventana_usuario, text ='Direccion: ').grid(row = 4, column = 0, padx= 2)
        caja_direccion = tkinter.Entry(ventana_usuario, width = 50)
        caja_direccion.grid(row = 4, column = 1, padx= 2)
        
        
        etiqueta_codigo_postal = tkinter.Label(ventana_usuario, text ='Codigo postal: ').grid(row = 4, column = 2, padx= 2)
        caja_codigo_postal = tkinter.Entry(ventana_usuario, width=50)
        caja_codigo_postal.grid(row = 4, column = 3, padx= 5, pady = 5)

        boton_usuario = tkinter.Button(ventana_usuario, text = 'Guardar', command = guardar_usuario,  width=25)
        boton_usuario.grid(row = 5, column = 1, padx = 10, pady = 10)

        cerrado = False
        ventana_usuario.protocol("WM_DELETE_WINDOW", cerrar)

def productos():
    global cerrado

    def cerrar():
        global cerrado
        ventana_producto.destroy()
        cerrado = True
    
    def guardar_producto():
        #Creo un vector producto
        productos = []

        codigo = str(numero_venta.get())
        tipo = tipo_producto.get()
        nombre = nombre_producto.get()
        precio = str(precio_producto.get())

        productos.append(codigo + ',' + tipo + ',' + nombre + ',' + precio)

        #Borramos los datos ya guardados del formulario.
        numero_venta.delete(0,"end")
        tipo_producto.delete(0,"end")
        nombre_producto.delete(0,"end")
        precio_producto.delete(0,"end")

        numero_venta.focus()

        try:
            archivo_productos = open('./archivos/productos.txt', 'x', encoding='utf-8') #Creo el archivo productos.txt
        except FileExistsError:
            archivo_productos = open('./archivos/productos.txt', 'a', encoding='utf-8') #Agrego al archivo ya creado nuevos datos

        for i in range(len(productos)):
            archivo_productos.write(productos[i])
            archivo_productos.write('\n')

    if cerrado:
        ventana_producto = tkinter.Tk()
        ventana_producto.title('Guardar Producto')

        ventana_producto.geometry('370x400')
        
        etiqueta = tkinter.Label(ventana_producto, text = 'Guardar Producto')
        etiqueta.grid(row = 0, column = 0, padx= 30, pady = 5)

        numero_venta_label = tkinter.Label(ventana_producto, text = 'Codigo De Producto').grid(row = 1, column = 0, padx= 30, pady = 5)

        numero_venta = tkinter.Entry(ventana_producto, width=50)
        numero_venta.grid(row = 2, column = 0)

        label_tipo_producto = tkinter.Label(ventana_producto, text = 'Seleccionar Tipo De Producto: ').grid(row = 3, column = 0, padx= 30, pady = 5)

        tipo_producto = ttk.Combobox (ventana_producto, state = "readonly", width= 47)
        tipo_producto.grid(row = 4, column = 0, padx= 30, pady = 5)
        tipo_producto['values'] = ['Lubricante', 'Combustible']
        
        label_producto = tkinter.Label(ventana_producto, text = 'Nombre Producto: ').grid(row = 5, column = 0, padx= 30, pady = 5)

        # producto = ttk.Combobox (ventana_producto, state = "readonly", width= 47)
        # producto.grid(row = 6, column = 0, padx= 30, pady = 5)
        # producto['values'] = ['Test', 'Hola']

        nombre_producto = tkinter.Entry(ventana_producto, width=50)
        nombre_producto.grid(row = 6, column = 0, padx= 30, pady = 5)

        label_precio = tkinter.Label(ventana_producto, text = 'Precio $ : ').grid(row = 7, column = 0, padx= 30, pady = 5)

        precio_producto = tkinter.Entry(ventana_producto, width = 50)
        precio_producto.grid(row = 8, column = 0, padx= 30, pady = 5)

        
        boton_producto = tkinter.Button(ventana_producto, text = 'Guardar Producto', command = guardar_producto,  width=25)
        boton_producto.grid(row = 9, column = 0, padx = 5, pady = 5)


        cerrado = False
        ventana_producto.protocol("WM_DELETE_WINDOW", cerrar)

def ventas():
    global cerrado
    def cerrar():
        global cerrado
        ventana_venta.destroy()
        cerrado = True

    def guardar_venta():
        #Creo un vector para ventas
        ventas = []

        fecha_final = fecha.get()
        nombre_producto = nombre_venta.get()
        precio = str(caja_precio.get())

        ventas.append(fecha_final + ',' + nombre_producto + ',' + precio)

        nombre_venta.delete(0,"end")
        caja_precio.delete(0,"end")

        nombre_venta.focus()
        try:
            archivo_ventas = open('./archivos/ventas.txt', 'x', encoding='utf-8') #Creo el archivo ventas.txt
        except FileExistsError:
            archivo_ventas = open('./archivos/ventas.txt', 'a', encoding='utf-8') #Agrego al archivo ya creado nuevos datos

        for i in range(len(ventas)):
            archivo_ventas.write(ventas[i])
            archivo_ventas.write('\n') 
       
    if cerrado:
            
        ventana_venta = tkinter.Tk()
        ventana_venta.title('Guardar Venta')
        ventana_venta.geometry('500x400')

        etiqueta_2 = tkinter.Label(ventana_venta, text = 'Guardar venta')
        etiqueta_2.grid(row = 0, column = 1)

        label_fecha = tkinter.Label(ventana_venta, text = 'Fecha: ')
        label_fecha.grid(row = 1, column = 0, padx= 5, pady = 5)

        fecha = tkinter.Entry(ventana_venta, width=50)
        fecha.grid(row = 1, column = 1, padx = 5, pady = 5)
        fecha.insert(0, datetime.today().strftime('%d-%m-%Y'))

        label_nombre_venta = tkinter.Label(ventana_venta, text = 'Nombre del producto: ')
        label_nombre_venta.grid(row = 2, column = 0)

        nombre_venta = tkinter.Entry(ventana_venta, width=50)
        nombre_venta.grid(row = 2, column = 1, padx= 5, pady = 5)

        label_precio = tkinter.Label(ventana_venta, text = 'Precio $: ').grid(row = 3, column = 0, padx= 5, pady = 5)
        caja_precio = tkinter.Entry(ventana_venta, width = 50)
        caja_precio.grid(row = 3, column = 1, padx = 5, pady = 5)

        boton_venta = tkinter.Button(ventana_venta, text = 'Guardar', command = guardar_venta,  width=25)
        boton_venta.grid(row = 4, column = 1, padx = 5, pady = 5)

        cerrado = False
        ventana_venta.protocol("WM_DELETE_WINDOW", cerrar)

# <------------------------------------------------------------ MENU PRINCIPAL -------------------------------------------------------------------------->
ventana = tkinter.Tk()
ventana.title('ABM')
ventana.geometry('380x400')

titulo = tkinter.Label(ventana, text = 'SISTEMA ESTACION LA LLEGADA:', width = 50)

boton_usuario = tkinter.Button(ventana, text = 'Guardar Usuario', command = usuario, width = 50)
boton_usuario.grid(row = 1, column = 2, padx = 10, pady = 10)

boton_producto = tkinter.Button(ventana, text = 'Guardar Producto', command = productos, width = 50)
boton_producto.grid(row = 2, column = 2, padx = 10, pady = 10)

boton_venta = tkinter.Button(ventana, text = 'Guardar Venta', command = ventas, width = 50)
boton_venta.grid(row = 3, column = 2, padx = 10, pady = 10)

ventana.mainloop()

# EDITAR, ELIMINAR DE USUARIO Y PRODUCTOS.
# ACTUALIZAR STOCK.
# BUSCAR POR DNI, CODIGO PRODUCTO.
# COMPROBACION DE CARACTERES Y CAMPOS VACIOS.
# TICKET Y DESCUENTO.