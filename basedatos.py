import csv
import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from inferencia import *

archivo_usuarios = "C:\\Users\\vanea\\OneDrive - Universidad Nacional de Colombia\\Vanessa\\IA\MatchAI (4)\\Base_de_datos.csv"
archivo_preferencias = "C:\\Users\\vanea\\OneDrive - Universidad Nacional de Colombia\\Vanessa\\IA\\MatchAI (4)\\Preferencias.csv"

def obtener_ultimo_id():
    try:
        with open(archivo_usuarios, mode="r") as file:
            reader = csv.reader(file)
            data = list(reader)
            if len(data) > 1 and len(data[1]) > 0:
                valid_data = [row for row in data[1:] if len(row) >= 1 and row[0].isdigit()]
                if valid_data:
                    ultimo_id = max(int(row[0]) for row in valid_data)
                else:
                    ultimo_id = 0
            else:
                ultimo_id = 0
        return ultimo_id
    except FileNotFoundError:
        return 0
def verificarpref(uid):
    with open(archivo_preferencias, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Salta la primera fila de encabezado
        usuarios = [row for row in reader]
        for i in range(len(usuarios)):
            if int(usuarios[i][0]) == int(uid):
                return True


def registrar_preferencias(id_usuario, genero, estado_civil, orientacion_sexual):
    with open(archivo_preferencias, mode="a") as file:
        file.write(f"{id_usuario},{genero},{estado_civil},{orientacion_sexual}\n")
    messagebox.showinfo("Registro de Preferencias Románticas", "Tus preferencias románticas han sido registradas exitosamente. ¡Que comience la búsqueda del amor!")



def registrar_usuario(root_registrar):
    usuario = simpledialog.askstring("Registro de Amor", "Ingresa un nombre de usuario romántico:")
    contraseña = simpledialog.askstring("Registro de Amor", "Escribe una contraseña secreta del corazón:")
    edad = simpledialog.askstring("Registro de Amor", "Edad (joven/adulto joven/adulto mayor):")
    contextura = simpledialog.askstring("Registro de Amor", "Descripción física (delgado/promedio/robusto):")
    genero = simpledialog.askstring("Registro de Amor", "Género (femenino/masculino):")
    estatura = simpledialog.askstring("Registro de Amor", "Estatura (baja/promedio/alta):")
    estado_civil = simpledialog.askstring("Registro de Amor", "Estado civil (soltero/casado/divorciado/viudo):")
    orientacion_sexual = simpledialog.askstring("Registro de Amor", "Orientación sexual (heterosexual/homosexual/bisexual):")
    nivel_academico = simpledialog.askstring("Registro de Amor", "Nivel académico (educación superior/basica secundaria/basica primaria/no presenta):")

    with open(archivo_usuarios, mode="a") as file:
        ultimo_id = obtener_ultimo_id() + 1
        file.write(f"{ultimo_id},{usuario},{contraseña},{edad},{contextura},{genero},{orientacion_sexual},{estatura},{estado_civil},{nivel_academico}\n")
    messagebox.showinfo("Registro de Amor Exitoso", "¡Registro exitoso! Ahora puedes empezar a escribir tu historia de amor.")
    root_registrar.destroy()

    iniciar_sesion()

def iniciar_sesion():
    root_iniciar = tk.Tk()
    root_iniciar.geometry("400x250")
    root_iniciar.title("Iniciar Sesión Romántica")

    style = ttk.Style()
    style.configure("TLabel", padding=5)
    style.configure("TButton", padding=5)
    style.configure("TEntry", padding=5)

    frame = ttk.Frame(root_iniciar)
    frame.grid(column=0, row=0, padx=20, pady=10, sticky=(tk.W, tk.E))

    iniciar_sesion_button = ttk.Button(frame, text="Iniciar Sesión", command=lambda: iniciar_sesion_accion(root_iniciar))
    iniciar_sesion_button.grid(column=0, row=0, columnspan=2)

    registrar_button = ttk.Button(frame, text="Registrarse", command=lambda: registrar_usuario(root_iniciar))
    registrar_button.grid(column=0, row=1, columnspan=2)

    root_iniciar.mainloop()

def iniciar_sesion_accion(root_iniciar):
    root_iniciar.destroy()  # Cerrar la ventana de inicio
    root_iniciar = tk.Tk()
    root_iniciar.geometry("400x250")
    root_iniciar.title("Iniciar Sesión Romántica")

    style = ttk.Style()
    style.configure("TLabel", padding=5)
    style.configure("TButton", padding=5)
    style.configure("TEntry", padding=5)

    frame = ttk.Frame(root_iniciar)
    frame.grid(column=0, row=0, padx=20, pady=10, sticky=(tk.W, tk.E))

    label_usuario = ttk.Label(frame, text="Nombre de Usuario:")
    label_usuario.grid(column=0, row=0)

    label_contraseña = ttk.Label(frame, text="Contraseña:")
    label_contraseña.grid(column=0, row=1)

    entry_usuario = ttk.Entry(frame)
    entry_usuario.grid(column=1, row=0)

    entry_contraseña = ttk.Entry(frame, show="*")
    entry_contraseña.grid(column=1, row=1)

    iniciar_sesion_button = ttk.Button(frame, text="Iniciar Sesión", command=lambda: verificar_credenciales(root_iniciar, entry_usuario.get(), entry_contraseña.get()))
    iniciar_sesion_button.grid(column=0, row=2, columnspan=2)

    root_iniciar.mainloop()

def verificar_credenciales(root_iniciar, usuario, contraseña):
    global user_id

    with open(archivo_usuarios, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la primera fila de encabezado
        for row in reader:
            if row[1] == usuario and row[2] == contraseña:
                messagebox.showinfo("Inicio de Sesión Exitoso", "¡Bienvenido de nuevo!")
                root_iniciar.destroy()
                user_id = row[0]
                if verificarpref(row[0]):
                    break
                orientacion_sexual = simpledialog.askstring("Registro de Amor", "Orientación sexual (heterosexual/homosexual/bisexual):")
                estado_civil = simpledialog.askstring("Registro de Amor", "Estado civil (soltero/casado/divorciado/viudo):")
                return registrar_preferencias(row[0],row[5],orientacion_sexual,estado_civil)

iniciar_sesion()
main(user_id)

