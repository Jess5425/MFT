import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import shutil
import os

global cont, username, password
cont = 0

# Crear o abrir el archivo 'usuarios.json' con un diccionario vacío
try:
    with open('usuarios.json', 'r') as archivo:
        usuarios = json.load(archivo)
except FileNotFoundError:
    usuarios = {}

def registrar():
    global username, password
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

        #messagebox.showinfo("Registro", "Usuario registrado con éxito.")
        ventanaP.withdraw()
        ventana_registro = tk.Toplevel() #ventana que nos va a ayudar a recopilar mas datos como foto, correo, cancion
        ventana_registro.geometry("500x350")
        ventana_registro.resizable(False, False)

        #Canva donde se van a poner los labels
        canvas = tk.Canvas(ventana_registro, width=500, height=400, bg="#D5D2FF")
        canvas.place(x=0, y=0)

        #label y lugar en donde se va a subir la imagen
        canvas.create_text(250, 80, text="Sube una imagen para que sea tu foto de perfil",
                         fill="black", font=("Small fonts", 14))

        canvas.create_text(250, 200, text="Sube una cancion",
                           fill="black", font=("Small fonts", 14))
        def seleccionar_imagen():
            ruta_imagen = filedialog.askopenfilename()
            if ruta_imagen:
                # Ruta donde se guarda la imagen seleccionada
                destino = "C://Users//gonza//PycharmProjects//MFT//Imagenes usuario"
                shutil.copy(ruta_imagen, destino)
                nuevo_nombre = username + ".png"

                # Obtiene el directorio de destino (puedes personalizar esto)
                directorio_destino = "C:/Users/gonza/PycharmProjects/MFT/Imagenes usuario/"

                # Combina el directorio de destino y el nuevo nombre para obtener la ruta completa
                nueva_ruta = os.path.join(directorio_destino, nuevo_nombre)

                # Mueve el archivo de la ruta original a la nueva ruta con el nuevo nombre
                shutil.copy(ruta_imagen, nueva_ruta)

        btn_seleccionar_imagen = tk.Button(canvas, text="Seleccionar Imagen", command=seleccionar_imagen)
        btn_seleccionar_imagen.place(relx=0.37, rely=0.34)

        def seleccionar_cancion():
            ruta_cancion = filedialog.askopenfilename(filetypes=[("Archivos de audio", "*.mp3")])

            if ruta_cancion:
                nuevo_nombre_cancion = username + ".mp3"  # Cambiar el nombre de la canción

                directorio_destino2 = "C:/Users/gonza/PycharmProjects/MFT/Imagenes usuario/"
                nueva_rutac = os.path.join(directorio_destino2, nuevo_nombre_cancion)
                shutil.copy(ruta_cancion, nueva_rutac)

        btn_seleccionar_cancion = tk.Button(canvas, text="Seleccionar cancion", command=seleccionar_cancion)
        btn_seleccionar_cancion.place(relx=0.37, rely=0.6)
        btregresar2 = tk.Button(canvas, text="Inicio", width=6, height=2,
                             command=lambda: [ventana_registro.destroy(), ventanaP.deiconify()]).place(x=40, y=10)



def iniciar_sesion():
    global cont
    username = entry_username.get()
    password = entry_password.get()

    if username in usuarios and usuarios[username] == password and cont == 1:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión de jugador 2 exitoso.")
        cont += 1
        nombre_jugador2 = tk.Label(ventanaP, text=username)
        nombre_jugador2.place(relx=0.8, rely=0.3)
    elif username in usuarios and usuarios[username] == password and cont == 0:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión de jugador 1 exitoso.")
        cont += 1
        nombre_jugador1 = tk.Label(ventanaP, text=username)
        nombre_jugador1.place(relx=0.2, rely=0.3)
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

#btn_inicio_sesion = tk.Button(ventanaP, text="boton que se usa dps", width=15, height=2, command= infojugador).place(relx=0.425, rely=0.8)
btnjugar = tk.Button(ventanaP, text="JUGAR", width=10, height=2).place(relx=0.44, rely=0.9)
btnmp = tk.Button(ventanaP, text="MEJORES PUNTUACIONES", width=20, height=2).place(relx=0.403, rely=0.78)
btninfo = tk.Button(ventanaP, text="ACERCA DE", width=12, height=2).place(relx=0.83, rely=0.05)
fuera = tk.Button(ventanaP, text="CERRAR", width=12, height=2, command=lambda: [ventanaP.destroy()]).place(relx=0.057, rely=0.05)

ventanaP.mainloop()


