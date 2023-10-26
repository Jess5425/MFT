import json
import tkinter as tk
from tkinter import messagebox

global cont
cont = 0

# Crear o abrir el archivo 'usuarios.json' con un diccionario vacío
try:
    with open('usuarios.json', 'r') as archivo:
        usuarios = json.load(archivo)
except FileNotFoundError:
    usuarios = {}

def registrar():
    username = entry_username.get()
    password = entry_password.get()

    if username in usuarios:
        messagebox.showerror("Registro", "Usuario ya existente. Por favor elija otro.")
    else:
        usuarios[username] = password
        with open('usuarios.json', 'w') as archivo:
            json.dump(usuarios, archivo)
        entry_username.delete(0, 'end')
        entry_password.delete(0, 'end')
        messagebox.showinfo("Registro", "Usuario registrado con éxito.")
        ventana_registro = tk.Toplevel()
        ventana_registro.geometry("568x650")
        ventana_registro.resizable(False, False)

        # canvas
        canvas = tk.Canvas(ventana_registro, width=568, height=650, bg="#D5D2FF")
        canvas.place(x=0, y=0)

def iniciar_sesion():
    global cont
    username = entry_username.get()
    password = entry_password.get()

    if username in usuarios and usuarios[username] == password and cont == 1:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión de jugador 2 exitoso.")
        cont += 1
    elif username in usuarios and usuarios[username] == password and cont == 0:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión de jugador 1 exitoso.")
        cont += 1
    elif username in usuarios and usuarios[username] == password and cont >= 2:
        messagebox.showinfo("Inicio de Sesión", "No se pudo iniciar sesión ya que ya está el limite de usuarios ingresados.")
    else:
        messagebox.showerror("Inicio de Sesión", "Nombre de usuario o contraseña incorrectos.")
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')

ventanaP = tk.Tk()
ventanaP.title("Registro e Inicio de Sesión")
ventanaP.geometry("987x629")
ventanaP.resizable(False, False)


label_username = tk.Label(ventanaP, text="Nombre de Usuario:")
label_username.place(relx=0.425, rely=0.45)
entry_username = tk.Entry(ventanaP)
entry_username.place(relx=0.42, rely=0.5)

label_password = tk.Label(ventanaP, text="Contraseña:")
label_password.place(relx=0.425, rely=0.55)
entry_password = tk.Entry(ventanaP, show="*")
entry_password.place(relx=0.425, rely=0.6)


btn_iniciar_sesion = tk.Button(ventanaP, text="Iniciar Sesión", command=iniciar_sesion).place(relx=0.445, rely=0.65)
btn_registrar = tk.Button(ventanaP, text="Registrar", command=registrar).place(relx=0.452, rely=0.7)


def infojugador():
    global ventana_info, nombreju
    ventanaP.withdraw()
    ventana_info = tk.Toplevel()
    ventana_info.geometry("568x650")
    ventana_info.resizable(False, False)

#canvas
    canvas = tk.Canvas(ventana_info, width=568, height=650, bg="#D5D2FF")
    canvas.place(x=0, y=0)



#btn_inicio_sesion = tk.Button(ventanaP, text="boton que se usa dps", width=15, height=2, command= infojugador).place(relx=0.425, rely=0.8)
btnjugar = tk.Button(ventanaP, text="JUGAR", width=10, height=2).place(relx=0.44, rely=0.9)
btnmp = tk.Button(ventanaP, text="MEJORES PUNTUACIONES", width=20, height=2).place(relx=0.403, rely=0.78)
btninfo = tk.Button(ventanaP, text="ACERCA DE", width=12, height=2).place(relx=0.83, rely=0.05)
fuera = tk.Button(ventanaP, text="CERRAR", width=12, height=2, command=lambda: [ventanaP.destroy()]).place(relx=0.057, rely=0.05)

ventanaP.mainloop()


