import tkinter as tk
import sqlite3
from tkinter import ttk

# Crear la ventana principal
root = tk.Tk()
root.title("Base de datos de productos")

# Crear la base de datos o conectar si ya existe
conn = sqlite3.connect("TablaNutricional.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT,
        supermercado TEXT,
        valor_energetico INTEGER,
        grasas INTEGER,
        saturadas INTEGER,
        carbohidratos INTEGER,
        azucares INTEGER,
        fibra INTEGER,
        proteinas INTEGER,
        sal INTEGER
    )
''')
conn.commit()

# Función para mostrar el formulario de agregar producto
def mostrar_formulario_agregar():
    ventana_agregar = tk.Toplevel(root)
    ventana_agregar.title("Agregar producto")

    tk.Label(ventana_agregar, text="ID:").grid(row=0, column=0)
    id_entry = tk.Entry(ventana_agregar)
    id_entry.grid(row=0, column=1)
    id_entry.insert(0, obtener_siguiente_id())

    tk.Label(ventana_agregar, text="Nombre del producto:").grid(row=1, column=0)
    nombre_entry = tk.Entry(ventana_agregar)
    nombre_entry.grid(row=1, column=1)

    tk.Label(ventana_agregar, text="Supermercado:").grid(row=2, column=0)
    supermercado_entry = tk.Entry(ventana_agregar)
    supermercado_entry.grid(row=2, column=1)

    tk.Label(ventana_agregar, text="Valor Energético:").grid(row=3, column=0)
    valor_energetico_entry = tk.Entry(ventana_agregar)
    valor_energetico_entry.grid(row=3, column=1)

    tk.Label(ventana_agregar, text="Grasas:").grid(row=4, column=0)
    grasas_entry = tk.Entry(ventana_agregar)
    grasas_entry.grid(row=4, column=1)

    tk.Label(ventana_agregar, text="De las cuales saturadas:").grid(row=5, column=0)
    saturadas_entry = tk.Entry(ventana_agregar)
    saturadas_entry.grid(row=5, column=1)

    tk.Label(ventana_agregar, text="Hidratos de carbono:").grid(row=6, column=0)
    carbohidratos_entry = tk.Entry(ventana_agregar)
    carbohidratos_entry.grid(row=6, column=1)

    tk.Label(ventana_agregar, text="De los cuales azúcares:").grid(row=7, column=0)
    azucares_entry = tk.Entry(ventana_agregar)
    azucares_entry.grid(row=7, column=1)

    tk.Label(ventana_agregar, text="Fibra Alimentaria:").grid(row=8, column=0)
    fibra_entry = tk.Entry(ventana_agregar)
    fibra_entry.grid(row=8, column=1)

    tk.Label(ventana_agregar, text="Proteínas:").grid(row=9, column=0)
    proteinas_entry = tk.Entry(ventana_agregar)
    proteinas_entry.grid(row=9, column=1)

    tk.Label(ventana_agregar, text="Sal:").grid(row=10, column=0)
    sal_entry = tk.Entry(ventana_agregar)
    sal_entry.grid(row=10, column=1)

    def guardar_producto():
        id_producto = id_entry.get()
        nombre = nombre_entry.get()
        supermercado = supermercado_entry.get()
        valor_energetico = valor_energetico_entry.get()
        grasas = grasas_entry.get()
        saturadas = saturadas_entry.get()
        carbohidratos = carbohidratos_entry.get()
        azucares = azucares_entry.get()
        fibra = fibra_entry.get()
        proteinas = proteinas_entry.get()
        sal = sal_entry.get()

        cursor.execute('''
            INSERT INTO productos (id, nombre, supermercado, valor_energetico, grasas, saturadas, carbohidratos, azucares, fibra, proteinas, sal)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_producto, nombre, supermercado, valor_energetico, grasas, saturadas, carbohidratos, azucares, fibra, proteinas, sal))
        conn.commit()

        ventana_agregar.destroy()

    guardar_button = tk.Button(ventana_agregar, text="Guardar", command=guardar_producto)
    guardar_button.grid(row=11, columnspan=2, pady=10)


# Función para obtener el siguiente ID disponible
def obtener_siguiente_id():
    cursor.execute("SELECT MAX(id) FROM productos")
    ultimo_id = cursor.fetchone()[0]
    if ultimo_id is None:
        return 1
    else:
        return ultimo_id + 1

# Función para obtener la lista de nombres de productos únicos
def obtener_nombres_productos():
    cursor.execute("SELECT DISTINCT nombre FROM productos")
    nombres = cursor.fetchall()
    return [nombre[0] for nombre in nombres]

# Función para obtener la lista de supermercados únicos
def obtener_supermercados():
    cursor.execute("SELECT DISTINCT supermercado FROM productos")
    supermercados = cursor.fetchall()
    return [supermercado[0] for supermercado in supermercados]

def mostrar_formulario_consultar():
    ventana_consultar = tk.Toplevel(root)
    ventana_consultar.title("Consultar producto")

    # Crear etiquetas y campos desplegables para los valores de búsqueda
    tk.Label(ventana_consultar, text="Buscar por Nombre:").pack(pady=5)
    nombre_combobox = ttk.Combobox(ventana_consultar, values=obtener_nombres_productos())
    nombre_combobox.pack()

    tk.Label(ventana_consultar, text="Buscar por Supermercado:").pack(pady=5)
    supermercado_combobox = ttk.Combobox(ventana_consultar, values=obtener_supermercados())
    supermercado_combobox.pack()

    def consultar_producto():
        nombre_producto = nombre_combobox.get()
        supermercado = supermercado_combobox.get()

        if not nombre_producto and not supermercado:
            return  # No se seleccionaron campos para buscar

        sql_query = 'SELECT * FROM productos WHERE 1=1'  # Inicia la consulta

        if nombre_producto:
            sql_query += f" AND nombre LIKE '{nombre_producto}%'"

        if supermercado:
            sql_query += f" AND supermercado LIKE '{supermercado}%'"

        cursor.execute(sql_query)
        productos = cursor.fetchall()
        
        if productos:
            ventana_detalle = tk.Toplevel(ventana_consultar)
            ventana_detalle.title("Resultados de la búsqueda")

            etiquetas = ["ID", "Nombre", "Supermercado", "Valor Energético", "Grasas", "de las cuales saturadas", "Hidratos de Carbono",
                        "de los cuales azúcares", "Fibra", "Proteínas", "Sal"]
            
            tabla = ttk.Treeview(ventana_detalle, columns=etiquetas, show="headings")

            for etiqueta in etiquetas:
                tabla.heading(etiqueta, text=etiqueta, anchor="center")  # Centra el texto de la cabecera
                tabla.column(etiqueta, width=120, anchor="center")  # Ajusta el ancho y centra los valores

            tabla.pack()

            for producto in productos:
                tabla.insert("", "end", values=producto)

    consultar_button = tk.Button(ventana_consultar, text="Consultar", command=consultar_producto)
    consultar_button.pack(pady=10)

    

# Función para abrir el formulario de crear plato
def mostrar_formulario_crear_plato():
    ventana_crear_plato = tk.Toplevel(root)
    ventana_crear_plato.title("Crear plato")

# Crear el botón para agregar producto
boton_agregar = tk.Button(root, text="Agregar producto", command=mostrar_formulario_agregar)
boton_agregar.pack(pady=20)

# Crear el botón para consultar producto
boton_consultar = tk.Button(root, text="Consultar producto", command=mostrar_formulario_consultar)
boton_consultar.pack(pady=20)

# Crear el botón para crear plato
boton_crear_plato = tk.Button(root, text="Crear plato", command=mostrar_formulario_crear_plato)
boton_crear_plato.pack(pady=20)

# Iniciar la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al cerrar la ventana
conn.close()