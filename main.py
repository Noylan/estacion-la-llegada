'''
Grupo:  “Aerofin Technology".
Gallardo Ezequiel 					ezegalla11@gmail.com
Cordoba Marco					    marco.cba2@gmail.com
Mosello Christopher                 chrismoselloo@gmail.com
'''

# Importando modulos que sirven para importar tkinter, la fecha y limpiar la consola.
import os, tkinter, datetime
from tkinter import *
from tkinter import ttk
from datetime import *

# Comando para limpiar la consola. 
os.system ("cls")

# Variable para la logica de ventanas.
cerrado = True

# <----------------------------------------------------- MENUS SECUNDARIOS Y FUNCIONES ------------------------------------------------------------------>
def login():
    usuario = nombre_usuario.get()
    contraseña = contraseña_usuario.get()

    if usuario and contraseña == 'admin':
        menu_principal()
    else:
        label_incorrecto =  tkinter.Label(ventana, text = 'USUARIO O CONTRASEÑA INCORRECTO', width = 50)
        label_incorrecto.grid(row = 6, column = 1, padx = 10, pady = 10)

def menu_principal():
    ventana.destroy()
    ventana_menu_principal = tkinter.Tk()
    ventana_menu_principal.title('ABM')
    ventana_menu_principal.geometry('465x200')

    titulo = tkinter.Label(ventana_menu_principal, text = 'SISTEMA ESTACION LA LLEGADA: ', width = 50)

    boton_usuario = tkinter.Button(ventana_menu_principal, text = 'Gestionar Clientes', command = usuario, width = 60)
    boton_usuario.grid(row = 1, column = 2, padx = 20, pady = 10)

    boton_producto = tkinter.Button(ventana_menu_principal, text = 'Gestionar Productos', command = productos, width = 60)
    boton_producto.grid(row = 2, column = 2, padx = 10, pady = 10)

    boton_venta = tkinter.Button(ventana_menu_principal, text = 'Gestionar Ventas', command = ventas, width = 60)
    boton_venta.grid(row = 3, column = 2, padx = 10, pady = 10)
         
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

    def buscar_usuario():
        archivo = open('./archivos/clientes.txt', 'rt', encoding='utf-8') #Abro el archivo cliente.txt
        todos_los_clientes = archivo.readlines()
        dni = caja_dni.get()
        clientes = []
        for i in todos_los_clientes:
            tpm = i.split(',')
            clientes.append(tpm)

        def limpiar():
            boton_usuario = tkinter.Button(ventana_usuario, text = 'Guardar', command = guardar_usuario,  width=25)
            boton_usuario.grid(row = 5, column = 1, padx = 10, pady = 10)

            caja_nombre.delete(0,"end")
            caja_apellido.delete(0,"end")
            caja_localidad.delete(0,"end")
            caja_telefono.delete(0,"end")
            caja_correo.delete(0,"end")
            caja_direccion.delete(0,"end")
            caja_codigo_postal.delete(0,"end")
            caja_dni.configure(state = NORMAL)
            caja_dni.delete(0,"end")
            caja_dni.delete(0,"end")
            caja_nombre.focus()
            
            boton_limpiar.grid_forget()

        for i in clientes:
            if i[2] == dni:
                caja_nombre.insert(0, i[0])
                caja_apellido.insert(0, i[1])
                caja_localidad.insert(0, i[3])
                caja_telefono.insert(0, i[4])
                caja_correo.insert(0, i[5])
                caja_direccion.insert(0, i[6])
                caja_codigo_postal.insert(0, i[7])
                caja_dni.configure(state = DISABLED)
                boton_usuario.grid_forget()
                boton_limpiar = tkinter.Button(ventana_usuario, text = 'Limpiar', command = limpiar,  width=25)
                boton_limpiar.grid(row = 6, column = 1, padx = 10, pady = 10)
        
    def editar_usuario():
        dni = caja_dni.get()
   
    if cerrado:
        ventana_usuario = tkinter.Tk()
        ventana_usuario.title('Gestionar Clientes')
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

        boton_buscar = tkinter.Button(ventana_usuario, text = 'Buscar', command = buscar_usuario,  width=25)
        boton_buscar.grid(row = 6, column = 1, padx = 10, pady = 10)


        cerrado = False
        ventana_usuario.protocol("WM_DELETE_WINDOW", cerrar)

def productos():
    global cerrado

    def cerrar():
        global cerrado
        ventana_producto.destroy()
        cerrado = True

    def obtener_codigo_producto():
        #Se lee el archivo.
        archivo_productos_2 = open('./archivos/productos.txt', 'r', encoding='utf-8') #Creo el archivo productos.txt
        todos_los_productos = archivo_productos_2.readlines()

        codigo_producto = len(todos_los_productos)
        numero_codigo_producto.insert(0, codigo_producto)
        numero_codigo_producto.configure(state = DISABLED)

    def guardar_producto():
        #Creo un vector producto
        productos = []

        codigo = numero_codigo_producto.get()
        codigo_nuevo = int(codigo) + 1
        tipo = tipo_producto.get()
        nombre = nombre_producto.get()
        precio = str(precio_producto.get())
        stock = str(cantidad_producto.get())

        productos.append(codigo + ',' + tipo + ',' + nombre + ',' + precio + ',' + stock)

        #Borramos los datos ya guardados del formulario.
        numero_codigo_producto.configure(state = NORMAL)
        numero_codigo_producto.delete(0,"end")
        numero_codigo_producto.insert(0, codigo_nuevo)
        numero_codigo_producto.configure(state = DISABLED)

        tipo_producto.set('')
        nombre_producto.delete(0,"end")
        precio_producto.delete(0,"end")

        numero_codigo_producto.focus()

        try:
            archivo_productos = open('./archivos/productos.txt', 'x', encoding='utf-8') #Creo el archivo productos.txt
        except FileExistsError:
            archivo_productos = open('./archivos/productos.txt', 'a', encoding='utf-8') #Agrego al archivo ya creado nuevos datos

        for i in range(len(productos)):
            archivo_productos.write(productos[i])
            archivo_productos.write('\n')

    def buscar_producto():
        archivo = open('./archivos/productos.txt', 'rt', encoding='utf-8') #Abro el archivo cliente.txt
        todos_los_clientes = archivo.readlines()
        codigo = numero_codigo_producto_2.get()
        productos = []
        for i in todos_los_clientes:
            tpm = i.split(',')
            productos.append(tpm)
        
        def limpiar():
            numero_codigo_producto.configure(state = NORMAL)
            numero_codigo_producto.delete(0,"end")
            obtener_codigo_producto()

            tipo_producto['values'] = ['Lubricante', 'Combustible']
            nombre_producto.delete(0,"end")
            precio_producto.delete(0,"end")
            cantidad_producto.delete(0,"end")

            boton_producto = tkinter.Button(ventana_producto, text = 'Guardar Producto', command = guardar_producto,  width=25)
            boton_producto.grid(row = 11, column = 0, padx = 5, pady = 5)

            boton_producto_buscar = tkinter.Button(ventana_producto, text = 'Buscar Producto', command = buscar_producto,  width=25)
            boton_producto_buscar.grid(row = 10, column = 1, padx = 5, pady = 5)

            numero_codigo_producto_2 = tkinter.Entry(ventana_producto, width=50)
            numero_codigo_producto_2.grid(row = 11, column = 1)
            tipo_producto.focus()

            boton_limpiar.grid_forget()

        for i in productos:
            if i[0] == codigo:
                boton_producto.grid_forget()
                boton_producto_buscar.grid_forget()
                numero_codigo_producto_2.grid_forget()

                numero_codigo_producto.configure(state = NORMAL)
                numero_codigo_producto.delete(0,"end")
                numero_codigo_producto.insert(0, codigo)
                numero_codigo_producto.configure(state = DISABLED)

                tipo_producto['values'] = i[1]
                tipo_producto.current(0)

                nombre_producto.insert(0, i[2])
                precio_producto.insert(0, i[3])
                cantidad_producto.insert(0, i[4])
                boton_limpiar = tkinter.Button(ventana_producto, text = 'Limpiar', command = limpiar,  width=25)
                boton_limpiar.grid(row = 10, column = 1, padx = 10, pady = 10)

    if cerrado:
        ventana_producto = tkinter.Tk()
        ventana_producto.title('Gestionar Productos')

        ventana_producto.geometry('680x400')
        
        etiqueta = tkinter.Label(ventana_producto, text = 'Guardar Producto')
        etiqueta.grid(row = 0, column = 0, padx= 30, pady = 5)

        numero_codigo_producto_label = tkinter.Label(ventana_producto, text = 'Codigo De Producto').grid(row = 1, column = 0, padx= 30, pady = 5)

        numero_codigo_producto = tkinter.Entry(ventana_producto, width=50)
        numero_codigo_producto.grid(row = 2, column = 0)

        label_tipo_producto = tkinter.Label(ventana_producto, text = 'Seleccionar Tipo De Producto: ').grid(row = 3, column = 0, padx= 30, pady = 5)

        tipo_producto = ttk.Combobox (ventana_producto, state = "readonly", width= 47)
        tipo_producto.grid(row = 4, column = 0, padx= 30, pady = 5)
        tipo_producto['values'] = ['Lubricante', 'Combustible']
        
        label_producto = tkinter.Label(ventana_producto, text = 'Nombre Producto: ').grid(row = 5, column = 0, padx= 30, pady = 5)

        nombre_producto = tkinter.Entry(ventana_producto, width=50)
        nombre_producto.grid(row = 6, column = 0, padx= 30, pady = 5)

        label_precio = tkinter.Label(ventana_producto, text = 'Precio $ : ').grid(row = 7, column = 0, padx= 30, pady = 5)

        precio_producto = tkinter.Entry(ventana_producto, width = 50)
        precio_producto.grid(row = 8, column = 0, padx= 30, pady = 5)

        label_cantidad = tkinter.Label(ventana_producto, text = 'Cantidad : ').grid(row = 9, column = 0, padx= 30, pady = 5)

        cantidad_producto = tkinter.Entry(ventana_producto, width = 50)
        cantidad_producto.grid(row = 10, column = 0, padx= 30, pady = 5)
        
        boton_producto = tkinter.Button(ventana_producto, text = 'Guardar Producto', command = guardar_producto,  width=25)
        boton_producto.grid(row = 11, column = 0, padx = 5, pady = 5)

        boton_producto_buscar = tkinter.Button(ventana_producto, text = 'Buscar Producto', command = buscar_producto,  width=25)
        boton_producto_buscar.grid(row = 10, column = 1, padx = 5, pady = 5)

        numero_codigo_producto_2 = tkinter.Entry(ventana_producto, width=50)
        numero_codigo_producto_2.grid(row = 11, column = 1)

        cerrado = False
        ventana_producto.protocol("WM_DELETE_WINDOW", cerrar)
        # Llamo a la fucion para obtener el codigo de la producto.
        obtener_codigo_producto()

def ventas():
    global cerrado
    def cerrar():
        global cerrado
        ventana_venta.destroy()
        cerrado = True

    def obtener_nombre_productos(e):
        nombre_venta.set('')
        #Se lee el archivo.
        archivo_ventas = open('./archivos/productos.txt', 'r', encoding='utf-8') #Creo el archivo productos.txt
        todos_los_productos = archivo_ventas.readlines()

        productos = []
        lubricante = []
        combustible = []

        for i in todos_los_productos:
            tpm = i.split(',')
            productos.append(tpm)

        for i in productos:
            categoria = i[1]
            if categoria == 'Lubricante':
                lubricante.append(i[2])
            elif categoria == 'Combustible':
                combustible.append(i[2])
        
        # if len(lubricante) == 0:
        #     productos.append('No existe ningun producto')
        #     lubricante.append('No existe ningun producto')
        #     boton_venta.configure(state = DISABLED)

        categoria_selecionada = categoria_venta.get()
        if categoria_selecionada == 'Lubricante':
            nombre_venta['values'] = lubricante
        elif categoria_selecionada == 'Combustible':
            nombre_venta['values'] = combustible

    def guardar_venta():
        #Creo un vector para ventas
        ventas = []

        fecha_final = fecha.get()
        categoria = categoria_venta.get()
        nombre_producto = nombre_venta.get()
        precio = str(caja_precio.get())

        ventas.append(fecha_final + ',' + categoria + ',' + nombre_producto + ',' + precio)

        categoria_venta.set('')
        nombre_venta.set('')
        caja_precio.delete(0,"end")

        categoria_venta.focus()
        
        try:
            archivo_ventas = open('./archivos/ventas.txt', 'x', encoding='utf-8') #Creo el archivo ventas.txt
        except FileExistsError:
            archivo_ventas = open('./archivos/ventas.txt', 'a', encoding='utf-8') #Agrego al archivo ya creado nuevos datos

        for i in range(len(ventas)):
            archivo_ventas.write(ventas[i])
            archivo_ventas.write('\n') 
       
    if cerrado:
            
        ventana_venta = tkinter.Tk()
        ventana_venta.title('Guardar Ventas')
        ventana_venta.geometry('500x350')

        etiqueta_2 = tkinter.Label(ventana_venta, text = 'Guardar venta')
        etiqueta_2.grid(row = 0, column = 1)

        label_fecha = tkinter.Label(ventana_venta, text = 'Fecha: ')
        label_fecha.grid(row = 1, column = 0, padx= 5, pady = 5)

        fecha = tkinter.Entry(ventana_venta, width=50)
        fecha.grid(row = 1, column = 1, padx = 5, pady = 5)
        fecha.insert(0, datetime.today().strftime('%d-%m-%Y'))
        fecha.configure(state = DISABLED)

        label_categoria_venta = tkinter.Label(ventana_venta, text = 'Categoria del producto: ')
        label_categoria_venta.grid(row = 2, column = 0)

        categoria_venta = ttk.Combobox (ventana_venta, state = "readonly", width= 47)
        categoria_venta.grid(row = 2, column = 1, padx= 5, pady = 5)
        categoria_venta['values'] = ['Lubricante', 'Combustible']
        categoria_venta.bind("<<ComboboxSelected>>", obtener_nombre_productos)
        
        label_nombre_venta = tkinter.Label(ventana_venta, text = 'Nombre del producto: ')
        label_nombre_venta.grid(row = 3, column = 0)

        nombre_venta = ttk.Combobox (ventana_venta, state = "readonly", width= 47)
        nombre_venta.grid(row = 3, column = 1, padx= 5, pady = 5)

        label_precio = tkinter.Label(ventana_venta, text = 'Precio $: ').grid(row = 4, column = 0, padx= 5, pady = 5)
        caja_precio = tkinter.Entry(ventana_venta, width = 50)
        caja_precio.grid(row = 4, column = 1, padx = 5, pady = 5)

        boton_venta = tkinter.Button(ventana_venta, text = 'Guardar', command = guardar_venta,  width=25)
        boton_venta.grid(row = 5, column = 1, padx = 5, pady = 5)

        cerrado = False
        ventana_venta.protocol("WM_DELETE_WINDOW", cerrar)

# <------------------------------------------------------------ MENU PRINCIPAL -------------------------------------------------------------------------->
ventana = tkinter.Tk()
ventana.title('ABM')
ventana.geometry('380x400')

titulo = tkinter.Label(ventana, text = 'SISTEMA ESTACION LA LLEGADA: ', width = 50)
titulo.grid(row = 0, column = 1, padx = 10, pady = 10)

label_usuario = tkinter.Label(ventana, text = 'Usuario: ', width = 50)
label_usuario.grid(row = 1, column = 1, padx = 10, pady = 10)

nombre_usuario = tkinter.Entry(ventana, width=50)
nombre_usuario.grid(row = 2, column = 1, padx = 10, pady = 10)

label_contraseña =  tkinter.Label(ventana, text = 'Contraseña: ', width = 50)
label_contraseña.grid(row = 3, column = 1, padx = 10, pady = 10)

contraseña_usuario = tkinter.Entry(ventana, show="*" , width=50)
contraseña_usuario.grid(row = 4, column = 1, padx = 10, pady = 10)

boton_ingresar = tkinter.Button(ventana, text = 'Ingresar', command = login, width = 45)
boton_ingresar.grid(row = 5, column = 1, padx = 10, pady = 10)


ventana.mainloop()