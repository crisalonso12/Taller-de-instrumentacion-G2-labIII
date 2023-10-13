import mysql.connector
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt
import datetime


# Variables globales para almacenar los valores de tiempo, data1 y data2
tiempo_actual = []
data1_actual = []
data2_actual = []


## ======================================================================================================================================================================================

def agregar_base_de_datos():
    # Crear una tabla
    cursor.execute('''CREATE TABLE IF NOT EXISTS datos (Nombre_Usuario VARCHAR(255), Fecha DATE, Canal INT, Unidades_Fisicas VARCHAR(255), Vector_Datos DOUBLE)''')
    
    # Obtener el valor del nombre de usuario desde la variable
    nombre_del_usuario = nombre_usuario.get()
    print(f"Nombre del usuario: {nombre_del_usuario}")

    # Extraer la fecha 
    fecha_actual = datetime.date.today()
    
    # Obtener datos    
    for data in data1_actual:

        print(data)
        
        # Insertar datos
        cursor.execute("INSERT INTO datos (Nombre_Usuario, Fecha, Canal, Unidades_Fisicas, Vector_Datos) VALUES (%s, %s, %s, %s, %s)", (nombre_del_usuario, fecha_actual, 1, 'Voltios(V)', data))
        print("Datos del canal 1 agregados")
        
    for data in data2_actual:

        print(data)
        
        # Insertar datos
        cursor.execute("INSERT INTO datos (Nombre_Usuario, Fecha, Canal, Unidades_Fisicas, Vector_Datos) VALUES (%s, %s, %s, %s, %s)", (nombre_del_usuario, fecha_actual, 2, 'Voltios(V)', data))
        print("Datos del canal 2 agregados")

    # Guardar cambios
    conn.commit()

## ======================================================================================================================================================================================


# Función para generar datos en tiempo real para las dos entradas (simulación de voltaje)
def generar_datos():
    min_voltage = 0.0  # Valor mínimo de voltaje
    max_voltage = 5.0  # Valor máximo de voltaje (ajusta según tus necesidades)
    tiempo = np.linspace(0, 25, 100)  # Rango de tiempo de 0 a 25 segundos
    data1 = np.random.uniform(min_voltage, max_voltage, 100)  # Datos para la entrada 1
    data2 = np.random.uniform(min_voltage, max_voltage, 100)  # Datos para la entrada 2
    return tiempo, data1, data2

# Función para actualizar la gráfica
def actualizar_grafica():
    
    global tiempo_actual, data1_actual, data2_actual
    #tiempo_actual.clear() 
    #data1_actual.clear()
    #data2_actual.clear()
    
    tiempo, data1, data2 = generar_datos()
    tiempo_actual = tiempo
    data1_actual = data1
    data2_actual = data2  

    ax.clear()
    ax.plot(tiempo, data1, label='Entrada 1')
    ax.plot(tiempo, data2, label='Entrada 2')
    ax.set_xlabel('Tiempo (s)')  # Etiqueta del eje X actualizada a "Tiempo (s)"
    ax.set_ylabel('Voltaje (V)')  # Etiqueta del eje Y actualizada a "Voltaje (V)"
    ax.set_title(f'Datos de Voltaje en Tiempo Real de dos Entradas para {nombre_usuario.get()}')
    ax.set_xlim(0, 25)  # Establecer límites del eje X
    ax.legend()
    canvas.draw()
    root.after(1000, actualizar_grafica)  # Actualiza cada segundo (ajusta según tus necesidades)

# Función para manejar el cambio de estado de los radiobuttons
def cambiar_estado(canal, valor):
    if canal == 1:
        print(f'Canal 1: {valor}')
    elif canal == 2:
        print(f'Canal 2: {valor}')
    
# Crear la ventana principal
root = tk.Tk()
root.title("Interfaz de Datos en Tiempo Real para dos Entradas en el mismo Gráfico")

# Crear una figura de Matplotlib
fig = Figure(figsize=(8, 6), dpi=100)
ax = fig.add_subplot(1, 1, 1)

# Crear un lienzo para mostrar la gráfica en la ventana
canvas = FigureCanvasTkAgg(fig, master=root)
canvas_widget = canvas.get_tk_widget()
canvas_widget.grid(row=0, column=0, rowspan=12, columnspan=12)  # Ubicar el gráfico en la esquina superior izquierda

# Crear un cuadro de entrada de texto para el nombre del usuario
nombre_usuario = tk.StringVar()  # Variable para almacenar el nombre del usuario
nombre_usuario_entry = ttk.Entry(root, textvariable=nombre_usuario)
nombre_usuario_label = ttk.Label(root, text="Nombre del Usuario:")
nombre_usuario_label.grid(row=13, column=9, padx=10, pady=5, sticky="w")
nombre_usuario_entry.grid(row=13, column=10, padx=10, pady=5, sticky="w")

# Crear Radiobuttons adicionales antes de los Radiobuttons principales para Canal 1
opciones_previas_canal1 = ["IN 1", "IN 2"]
var_previas_canal1 = tk.StringVar()
var_previas_canal1.set(opciones_previas_canal1[0])  # Establecer la opción predeterminada
for i, opcion in enumerate(opciones_previas_canal1):
    radio_button = ttk.Radiobutton(root, text=opcion, variable=var_previas_canal1, value=opcion, command=lambda i=i: cambiar_estado(1, opciones_previas_canal1[i]))
    radio_button.grid(row=i + 1, column=12, padx=(10, 10), sticky="w")  # Usar padx para establecer el espacio a la izquierda

# Crear Radiobuttons para Canal 1
canal1_label = ttk.Label(root, text="Canal 1")
canal1_label.grid(row=0, column=12, padx=(40, 10), columnspan=2)  # Usar padx para establecer el espacio entre las columnas
canal1_radio_buttons = []
opciones_canal1 = ["Atenuación 1", "Atenuación 2", "Seguidor", "Ganancia 1", "Ganancia 2", "Ganancia 3"]
var_canal1 = tk.StringVar()
var_canal1.set(opciones_canal1[0])  # Establecer la opción predeterminada
for i, opcion in enumerate(opciones_canal1):
    radio_button = ttk.Radiobutton(root, text=opcion, variable=var_canal1, value=opcion, command=lambda i=i: cambiar_estado(1, opciones_canal1[i]))
    radio_button.grid(row=i + 1, column=13, padx=(40, 10), sticky="w")  # Usar padx para establecer el espacio a la izquierda
    canal1_radio_buttons.append(radio_button)

# Crear Radiobuttons adicionales antes de los Radiobuttons principales para Canal 2
opciones_previas_canal2 = ["IN 1", "IN 2"]
var_previas_canal2 = tk.StringVar()
var_previas_canal2.set(opciones_previas_canal2[0])  # Establecer la opción predeterminada
for i, opcion in enumerate(opciones_previas_canal2):
    radio_button = ttk.Radiobutton(root, text=opcion, variable=var_previas_canal2, value=opcion, command=lambda i=i: cambiar_estado(2, opciones_previas_canal2[i]))
    radio_button.grid(row=i + 1, column=16, padx=(40, 10), sticky="w")  # Usar padx para establecer el espacio a la izquierda
    
# Crear Radiobuttons para Canal 2
canal2_label = ttk.Label(root, text="Canal 2")
canal2_label.grid(row=0, column=15, padx=(40, 5), columnspan=2)  # Usar padx para establecer el espacio entre las columnas
canal2_radio_buttons = []
opciones_canal2 = ["Atenuación 1", "Atenuación 2", "Seguidor", "Ganancia 1", "Ganancia 2", "Ganancia 3"]
var_canal2 = tk.StringVar()
var_canal2.set(opciones_canal2[0])  # Establecer la opción predeterminada
for i, opcion in enumerate(opciones_canal2):
    radio_button = ttk.Radiobutton(root, text=opcion, variable=var_canal2, value=opcion, command=lambda i=i: cambiar_estado(2, opciones_canal2[i]))
    radio_button.grid(row=i + 1, column=17, padx=(40, 5), sticky="w")  # Usar padx para establecer el espacio a la izquierda
    canal2_radio_buttons.append(radio_button)
    


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

# Título del botón "Agregar"
titulo_base_de_datos = ttk.Label(root, text="Base de Datos")
titulo_base_de_datos.grid(row=13, column=6, pady=5)

# Botón para agregar la base de datos
agregar_btn = ttk.Button(root, text="Agregar datos", style="Agregar.TButton", command=agregar_base_de_datos)
agregar_btn.grid(row=13, column=7, pady=10, padx=1, sticky="w")  # Alineado a la izquierda y espacio en el lado izquierdo

# Crear un estilo personalizado para los botones
style = ttk.Style()
style.configure("Inicio.TButton", foreground="black", background="red")
style.configure("Agregar.TButton", foreground="black", background="green")

# Botón para iniciar la visualización de datos en tiempo real
iniciar_btn = ttk.Button(root, text="Inicio", style="Inicio.TButton", command=actualizar_grafica)
iniciar_btn.grid(row=13, column=0, columnspan=6, pady=10, padx=10)  # Alineado a la izquierda y espacio en el lado izquierdo

# Ejecutar la aplicación
root.after(1000, actualizar_grafica)  # Comienza la actualización de la gráfica
root.mainloop()

# Cerrar la conexión con la base de datos
conn.close()






