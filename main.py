import json
import tkinter as tk
from tkinter import messagebox

# Crear o abrir el archivo 'usuarios.json' con un diccionario vacío
try:
    with open('usuarios.json', 'r') as archivo:
        usuarios = json.load(archivo)
except FileNotFoundError:
    usuarios = {}

def registrar():
    username = entry_username.get()
    password = entry_password.get()
    usuarios[username] = password

    with open('usuarios.json', 'w') as archivo:
        json.dump(usuarios, archivo)
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')
    messagebox.showinfo("Registro", "Usuario registrado con éxito.")

def iniciar_sesion():
    username = entry_username.get()
    password = entry_password.get()

    if username in usuarios and usuarios[username] == password:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión exitoso.")
    else:
        messagebox.showerror("Inicio de Sesión", "Nombre de usuario o contraseña incorrectos.")
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')

root = tk.Tk()
root.title("Registro e Inicio de Sesión")

label_username = tk.Label(root, text="Nombre de Usuario:")
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()

label_password = tk.Label(root, text="Contraseña:")
label_password.pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

btn_registrar = tk.Button(root, text="Registrar", command=registrar)
btn_registrar.pack()

btn_iniciar_sesion = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion)
btn_iniciar_sesion.pack()

root.mainloop()

