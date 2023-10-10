import pygame, sys
import pyodbc
import bcrypt
from pygame.locals import *
pygame.init()

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BRIGHT_GREEN = (0, 255, 0)

# Datos del servidor SQL
server = "LAPTOP-SUA8H24U\SQLEXPRESS"
database = "BDTest"
usuario = "sa"
password = "12345"

# Cadena de conexión a la base de datos
conn_str = 'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + usuario + ';PWD=' + password

# Conexión a la base de datos SQL Server
try:
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

except Exception as e:
    print("Ocurrió un Error al conectar con la base de datos:", e)
    sys.exit(1)

# Crear la ventana
WINDOW_SIZE = (800, 500)
window = pygame.display.set_mode(WINDOW_SIZE)

# Función para dibujar un botón
def draw_button(color, x, y, width, height, text):
    pygame.draw.rect(window, color, (x, y, width, height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=(x + width / 2, y + height / 2))
    window.blit(text_surface, text_rect)

# Función para manejar el evento de clic del botón
def button_click(event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos  # Obtiene la posición del mouse
        if login_button.collidepoint(mouse_pos):
            login_window()  # Abre la ventana de inicio de sesión
        elif register_button.collidepoint(mouse_pos):
            register_window()  # Abre la ventana de registro

# Función para abrir la ventana de inicio de sesión
def login_window():
    login_window = pygame.display.set_mode((400, 200))
    pygame.display.set_caption('Ventana de inicio de sesión')

# Función para abrir la ventana de registro
def register_window():
    register_window = pygame.display.set_mode((400, 200))
    pygame.display.set_caption('Ventana de registro')

    username_input_rect = pygame.Rect(150, 50, 200, 30)
    password_input_rect = pygame.Rect(150, 100, 200, 30)
    register_button_rect = pygame.Rect(150, 150, 100, 40)

    username_text = ""
    password_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if register_button_rect.collidepoint(mouse_pos):
                    # Registrar al usuario en la base de datos
                    hashed_password = bcrypt.hashpw(password_text.encode('utf-8'), bcrypt.gensalt())
                    insert_user(username_text, hashed_password)
                    print("Usuario registrado con éxito")
                    return  # Regresar a la ventana anterior

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    # Registrar al usuario en la base de datos
                    hashed_password = bcrypt.hashpw(password_text.encode('utf-8'), bcrypt.gensalt())
                    insert_user(username_text, hashed_password)
                    print("Usuario registrado con éxito")
                    return  # Regresar a la ventana anterior
                elif event.key == pygame.K_BACKSPACE:
                    username_text = username_text[:-1]
                    password_text = password_text[:-1]
                else:
                    username_text += event.unicode
                    password_text += event.unicode

        window.fill(WHITE)
        draw_button(GREEN, *register_button_rect, "Registrarse")
        pygame.draw.rect(window, (0, 0, 0), username_input_rect, 2)
        pygame.draw.rect(window, (0, 0, 0), password_input_rect, 2)

        font = pygame.font.Font(None, 36)
        username_surface = font.render(username_text, True, (0, 0, 0))
        password_surface = font.render('*' * len(password_text), True, (0, 0, 0))

        window.blit(username_surface, (username_input_rect.x + 5, username_input_rect.y + 5))
        window.blit(password_surface, (password_input_rect.x + 5, password_input_rect.y + 5))

        pygame.display.flip()


# Función para insertar un usuario en la base de datos
def insert_user(username, hashed_password):
    cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, hashed_password))
    conn.commit()

# Crear rectángulos para los botones
login_button = pygame.Rect(50, 50, 150, 50)
register_button = pygame.Rect(50, 150, 150, 50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        button_click(event)

    window.fill(WHITE)
    draw_button(GREEN, *login_button, "Iniciar Sesión")
    draw_button(BRIGHT_GREEN, *register_button, "Registrarse")
    pygame.display.flip()


def principal_window():
    principal_window = pygame.display.set_mode((800, 700))
    pygame.display.set_caption('Ventana Principal del juego')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    window.fill(WHITE)
    draw_button(BRIGHT_GREEN, *register_button_rect, "Acerca de")
    pygame.draw.rect(window, (0, 255, 0), username_input_rect, 2)
    pygame.draw.rect(window, (0, 255, 0), password_input_rect, 2)

    draw_button(BRIGHT_GREEN, *register_button_rect, "Configuración")
    pygame.draw.rect(window, (0, 255, 0), username_input_rect, 2)
    pygame.draw.rect(window, (0, 255, 0), password_input_rect, 2)

    draw_button(BRIGHT_GREEN, *register_button_rect, "Ayuda")
    pygame.draw.rect(window, (0, 255, 0), username_input_rect, 2)
    pygame.draw.rect(window, (0, 255, 0), password_input_rect, 2)


