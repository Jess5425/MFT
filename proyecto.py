import threading
import time
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
#from natsort import natsorted
#from pygame import mixer
#import random

#-----------------------VENTANA PRINCIPAL-----------------------
ventanaP = Tk()
ventanaP.title("Eagle Defender")
ventanaP.geometry("987x629")
ventanaP.resizable(False, False)
#fondo
imgfondo = ImageTk.PhotoImage(Image.open("fondito.png"))
fondo = Label(ventanaP, image= imgfondo)
fondo.pack(side="bottom", fill="both", expand=YES)
ventanaP.mainloop()