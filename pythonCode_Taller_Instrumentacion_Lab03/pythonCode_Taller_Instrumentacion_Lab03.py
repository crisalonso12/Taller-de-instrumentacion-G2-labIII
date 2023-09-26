import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="ti1234",
    database="ti_g2"
)

cursor = conn.cursor()

# Crear una tabla
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(255), edad INT)''')

# Insertar datos
cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)", ('Alice', 30))

# Realizar una consulta
cursor.execute("SELECT * FROM usuarios")
datos = cursor.fetchall()
for fila in datos:
    print(fila)

conn.commit()
conn.close()


print('Base de datos creada')







