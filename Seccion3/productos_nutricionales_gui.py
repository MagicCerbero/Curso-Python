import sqlite3

# Conectar a la base de datos (creará un archivo si no existe)
conn = sqlite3.connect('productos.db')
cursor = conn.cursor()

# Crear tabla de productos si no existe
cursor.execute('''
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        calorias REAL,
        proteinas REAL,
        grasas REAL,
        carbohidratos REAL
    )
''')

# Función para insertar un nuevo producto
def insertar_producto(nombre, calorias, proteinas, grasas, carbohidratos):
    cursor.execute('''
        INSERT INTO productos (nombre, calorias, proteinas, grasas, carbohidratos)
        VALUES (?, ?, ?, ?, ?)
    ''', (nombre, calorias, proteinas, grasas, carbohidratos))
    conn.commit()

# Ejemplos de inserción de productos
insertar_producto('Manzana', 52, 0.26, 0.17, 14)
insertar_producto('Yogur', 59, 3.47, 3.25, 3.56)
insertar_producto('Pollo', 165, 31, 3.6, 0)

# Consulta para obtener todos los productos
def obtener_productos():
    cursor.execute('SELECT * FROM productos')
    return cursor.fetchall()

# Imprimir todos los productos en la base de datos
productos = obtener_productos()
for producto in productos:
    print(producto)

# Cerrar la conexión a la base de datos al finalizar
conn.close()
