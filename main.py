import json
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import shutil
import os
import pygame, sys
from pygame.locals import *
import math
from PIL import Image, ImageTk

global cont, username, password, player1, player2
cont = 0

#se inicia la libreria de pygame
pygame.init()

# Tamaño del mundo de juego
filas = 10
columnas = 10

# Inicialización de la matriz con celdas vacías (0)
mundo = [[0] * columnas for _ in range(filas)]

#VENTANA PRINCIPAL
ventanaP = tk.Tk()
ventanaP.title("Registro e Inicio de Sesión")
ventanaP.geometry("987x629")
ventanaP.resizable(False, False)

imgfondo = ImageTk.PhotoImage(Image.open("aguila.png"))
fondo = tk.Label(ventanaP, image= imgfondo)
fondo.pack(side="bottom", fill="both")

#labels de username y password
label_username = tk.Label(ventanaP, text="Nombre de Usuario:")
label_username.place(relx=0.425, rely=0.45)
entry_username = tk.Entry(ventanaP)
entry_username.place(relx=0.42, rely=0.5)

label_password = tk.Label(ventanaP, text="Contraseña:")
label_password.place(relx=0.425, rely=0.55)
entry_password = tk.Entry(ventanaP, show="*")
entry_password.place(relx=0.425, rely=0.6)


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
                             command=lambda: [ventana_registro.destroy(), ventanaP.deiconify(),messagebox.showinfo("Registro", "Usuario registrado con éxito.") ]).place(x=40, y=10)

#funcion que ayuda a iniciar la sesión
def iniciar_sesion():
    global cont, player1, player2
    username = entry_username.get()
    password = entry_password.get()

    if username in usuarios and usuarios[username] == password and cont == 1:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión de jugador 2 exitoso.")
        cont += 1
        player2 = username
        nombre_jugador2 = tk.Label(ventanaP, text=username)
        nombre_jugador2.place(relx=0.8, rely=0.3)
    elif username in usuarios and usuarios[username] == password and cont == 0:
        messagebox.showinfo("Inicio de Sesión", "Inicio de sesión de jugador 1 exitoso.")
        cont += 1
        player1 = username
        nombre_jugador1 = tk.Label(ventanaP, text=username)
        nombre_jugador1.place(relx=0.2, rely=0.3)
    elif username in usuarios and usuarios[username] == password and cont >= 2:
        messagebox.showinfo("Inicio de Sesión", "No se pudo iniciar sesión ya que ya está el limite de usuarios ingresados.")
    else:
        messagebox.showerror("Inicio de Sesión", "Nombre de usuario o contraseña incorrectos.")
    entry_username.delete(0, 'end')
    entry_password.delete(0, 'end')

#Ventana que va a dar a elegir el rol del jugador
def definir_rol():
    global cont, player1, player2, ventana_definir_rol
    if cont == 2:
        ventanaP.withdraw()
        ventana_definir_rol = tk.Toplevel()
        ventana_definir_rol.geometry("600x500")
        ventana_definir_rol.resizable(False, False)

        canvas_rol = tk.Canvas(ventana_definir_rol, width=600, height=650, bg="#D5D2FF")
        canvas_rol.place(x=0, y=0)

        canvas_rol.create_text(200, 100, text="¿Cual jugador sera el defensor?", fill="black", font=("Arial", 16))
        def defensor_pl1():
            juego()

        def defensor_pl2():
            juego()

        btn_jugador1 = tk.Button(canvas_rol, text=player1, width=15, height=15, command=defensor_pl1).place(relx=0.25, rely=0.34)
        btn_jugador2 = tk.Button(canvas_rol, text=player2, width=15, height=15, command=defensor_pl2).place(relx=0.5, rely=0.34)

    else:
        messagebox.showerror("Problema con inicio de sesión", "Se ocupa que dos usuarios esten registrados.")

def juego():
    ventana_definir_rol.withdraw()
    tamano = (1300,800)
    blanco = (255, 255, 255)
    #ventana para el juego
    ventana_juego = pygame.display.set_mode(tamano)
    pygame.display.set_caption("Eagle Defender")
    ventana_juego.fill(blanco)
    #fondo para el juego
    fondo_pantallajuego = pygame.image.load("Imagenes/fondo_juego.jpg")
    fondo_pantallajuego = pygame.transform.scale(fondo_pantallajuego, (1300, 800))
    ventana_juego.blit(fondo_pantallajuego, (0, 0))

    #imagenes de los bloques
    bloquea = pygame.image.load("Imagenes/Acero.jpg")
    bloque_acero = pygame.transform.scale(bloquea, (40, 40))

    bloquec = pygame.image.load("Imagenes/Concreto.jpg")
    bloque_concreto = pygame.transform.scale(bloquec, (40, 40))

    bloquem = pygame.image.load("Imagenes/Madera.jpg")
    bloque_madera = pygame.transform.scale(bloquem, (40, 40))

    #Clase que ayuda a poner los bloques como un boton y tenerlos en la pantalla
    class Image_button:
        def __init__(self, x, y, image, key):
            self.x = x
            self.y = y
            self.image = image
            self.rect = image.get_rect(topleft=(x, y))
            self.key = key
            self.clicked = False
            self.visible = True

        # Function to draw the buttons created
        def draw(self, screen):
            if self.visible:
                screen.blit(self.image, (self.x, self.y))  # Draw it in the screen

        # Check if the key is pressed or not
        def check_keypress(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN and self.visible:
                if self.rect.collidepoint(event.pos):
                    self.clicked = True
                else:
                    self.clicked = False
            elif event.type == pygame.MOUSEBUTTONUP and self.visible:
                self.clicked = False
            elif event.type == pygame.KEYDOWN and event.key == self.key and not self.clicked and self.visible:
                self.clicked = True
                print(f"Tecla {pygame.key.name(self.key)}")  # Print to check if pressed
            elif event.type == pygame.KEYUP:
                self.clicked = False
            else:
                self.clicked = False

        # Set new position
        def set_position(self, x, y):
            self.rect.x = x
            self.rect.y = y

        # Hide the button in the screen
        def hide(self):
            self.visible = False

        # Show the button in the screen
        def show(self):
            self.visible = True

    #instancias de la clase button, se utiliza para los tres tipos de bloque
    bmadera = Image_button(70, 320, bloque_madera, K_a)
    bmadera.draw(ventana_juego)
    bmadera.show()

    bacero = Image_button(70, 400, bloque_acero, K_s)
    bacero.draw(ventana_juego)
    bacero.show()

    bconcreto = Image_button(70, 480, bloque_concreto, K_d)
    bconcreto.draw(ventana_juego)
    bconcreto.show()

    #clase que ayuda a colocar los bloques en la pantalla de juego
    class Movement(pygame.sprite.Sprite):
        def __init__(self, image, initial_position, ini_angle, is_eagle, health):
            super().__init__()
            self.image = image
            self.rect = self.image.get_rect()
            self.rect.topleft = initial_position
            self.rotation = ini_angle
            self.is_moving = False
            self.is_rotating = False
            self.offset_x = 0
            self.offset_y = 0
            self.initial_angle = 0
            self.is_eagle = is_eagle
            self.is_colliding = False
            self.health = health

        def handle_move(self, event):
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.rect.collidepoint(event.pos):
                        self.is_moving = True
                        self.offset_x = self.rect.x - event.pos[0]
                        self.offset_y = self.rect.y - event.pos[1]
                elif event.button == 3:
                    if self.rect.collidepoint(event.pos):
                        self.is_rotating = True
                        self.initial_angle = self.rotation - math.atan2(event.pos[1] - self.rect.centery,
                                                                        event.pos[0] - self.rect.centerx)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1 or event.button == 3:
                    self.is_moving = False
                    self.is_rotating = False

        def update(self, others):
            if self.is_moving:
                new_x = pygame.mouse.get_pos()[0] + self.offset_x
                new_y = pygame.mouse.get_pos()[1] + self.offset_y
                if not any(self.rect.colliderect(other) for other in others):
                    if self.is_eagle == "y":
                        if self.rect.x > 675 and self.rect.y > 100:
                            if 1230 > new_x > 675:
                                self.rect.x = new_x
                            if 585 > new_y > 100:
                                self.rect.y = new_y
                    else:
                        if self.rect.x > 665 and self.rect.y > 70:
                            if 1290 > new_x > 675:
                                self.rect.x = new_x
                            if 630 > new_y > 80:
                                self.rect.y = new_y

                for other in others:
                    if self.is_eagle == "y":
                        if self.rect.colliderect(other):
                            if other.rect.right - 30 < new_x > other.rect.left:
                                self.rect.y = new_y
                                self.rect.x = new_x
                            if other.rect.right - 180 > new_x < other.rect.left - 100:
                                self.rect.y = new_y
                                self.rect.x = new_x
                            if other.rect.bottom + 20 < new_y > other.rect.top:
                                self.rect.y = new_y
                                self.rect.x = new_x
                            if other.rect.bottom - 100 > new_y < other.rect.top - 100:
                                self.rect.y = new_y
                                self.rect.x = new_x
                    else:
                        if self.rect.colliderect(other):
                            if other.rect.right < new_x > other.rect.left:
                                self.rect.y = new_y
                                self.rect.x = new_x
                            if other.rect.right - 70 > new_x < other.rect.left - 70:
                                self.rect.y = new_y
                                self.rect.x = new_x
                            if other.rect.bottom < new_y > other.rect.top:
                                self.rect.y = new_y
                                self.rect.x = new_x
                            if other.rect.bottom - 70 > new_y < other.rect.top - 70:
                                self.rect.y = new_y
                                self.rect.x = new_x

            if self.is_rotating:
                new_angle = math.atan2(pygame.mouse.get_pos()[1] - self.rect.centery,
                                       pygame.mouse.get_pos()[0] - self.rect.centerx)
                self.rotation = math.degrees(new_angle + self.initial_angle)
                self.rotation %= 360

        def draw(self, screen):
            if self.health > 0:
                rotated_image = pygame.transform.rotate(self.image, -self.rotation)
                rotated_rect = rotated_image.get_rect(center=self.image.get_rect(topleft=self.rect.topleft).center)
                screen.blit(rotated_image, rotated_rect.topleft)
            else:
                self.rect.topleft = (-1000, -1000)
                self.kill()
                del self

        def getPosition(self):
            return [str(self.offset_x), str(self.offset_y), str(self.health)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            bmadera.check_keypress(event)
            if bmadera.clicked:
                print("bloque madera")
                madera = Movement(bloque_madera, (500,500), 0, "n", 34)
                madera.handle_move(event)
                madera.draw(ventana_juego)

            bacero.check_keypress(event)
            if bacero.clicked:
                print("bloque de acero")
                acero = Movement(bloque_acero, (400, 400), 0, "n", 34)
                acero.handle_move(event)
                acero.draw(ventana_juego)

            bconcreto.check_keypress(event)
            if bconcreto.clicked:
                print("bloque de concreto")
                concreto = Movement(bloque_concreto, (300, 300), 0, "n", 34)
                concreto.handle_move(event)
                concreto.draw(ventana_juego)
        pygame.display.update()




def mejores_puntuaciones():
    ventanaP.withdraw()
    ventana_mejoresp = tk.Toplevel()
    ventana_mejoresp.geometry("568x650")
    ventana_mejoresp.resizable(False, False)

    btregresar2 = tk.Button(ventana_mejoresp, text="Inicio", width=6, height=2,
                         command=lambda: [ventana_mejoresp.destroy(), ventanaP.deiconify()]).place(x=40, y=20)

#botones de la ventana principal
btn_iniciar_sesion = tk.Button(ventanaP, text="Iniciar Sesión", command=iniciar_sesion).place(relx=0.445, rely=0.65)
btn_registrar = tk.Button(ventanaP, text="Registrar", command=registrar).place(relx=0.452, rely=0.7)
btnjugar = tk.Button(ventanaP, text="JUGAR", width=10, height=2, command=definir_rol).place(relx=0.44, rely=0.9)
btnmp = tk.Button(ventanaP, text="MEJORES PUNTUACIONES", width=20, height=2, command=mejores_puntuaciones).place(relx=0.403, rely=0.78)
btninfo = tk.Button(ventanaP, text="ACERCA DE", width=12, height=2).place(relx=0.83, rely=0.05)
fuera = tk.Button(ventanaP, text="CERRAR", width=12, height=2, command=lambda: [ventanaP.destroy()]).place(relx=0.057, rely=0.05)

ventanaP.mainloop()


