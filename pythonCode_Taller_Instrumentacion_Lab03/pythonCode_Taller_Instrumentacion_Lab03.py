import mysql.connector

def crear_tabla_prueba(cursor):
    # Crear una tabla
    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT)''')

    # Insertar datos
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ('Garret', 32))

    # Mostrar tabla en consola
    cursor.execute("SELECT * FROM usuarios")
    datos = cursor.fetchall()
    for fila in datos:
        print(fila)

def crear_tablaYdatos_lab3(cursor, autor, fecha, numcanal, unidades, vectordatos):
    # Crear una tabla
    cursor.execute('''CREATE TABLE IF NOT EXISTS datos_lab3 (autor VARCHAR(255), fecha VARCHAR(255), numeroCanal INT, unidadesFisicas INT, vectorDatos INT)''')

    print('Agregando nuevos datos a la base')
    # Insertar datos
    cursor.execute("INSERT INTO datos_lab3 (autor, fecha, numeroCanal, unidadesFisicas, vectorDatos) VALUES (%s, %s, %s, %s, %s)", (autor, fecha, numcanal, unidades, vectordatos))
    
    # Mostrar tabla en consola
    cursor.execute("SELECT * FROM datos_lab3")
    datos = cursor.fetchall()
    for fila in datos:
        print(fila)

#####################
###               ###
###     Main      ###
###               ###
#####################

# Establecer la conexión
conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="ti1234",
    database="ti_g2"
)
cursor = conn.cursor()


#crear_tabla_prueba(cursor)
crear_tablaYdatos_lab3(cursor, 'Cristian', '3/10/2023', 1, 5, 1)

# Guardar cambios y cerrar la conexión
conn.commit()
conn.close()

print('Base de datos actualizada')




