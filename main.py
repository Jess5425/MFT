import pygame
import sys
import pyodbc
from pygame.locals import *

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
        mouse_pos = pygame.mouse.get_pos()  # Obtiene la posición del mouse
        if login_button_rect.collidepoint(mouse_pos):
            login_window()  # Abre la ventana de inicio de sesión
        elif register_button_rect.collidepoint(mouse_pos):
            register_window()  # Abre la ventana de registro


def main_menu_window():
    main_menu_window = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Eagle Defender')  # Cambiamos el título

    # Centro de la pantalla
    center_x = 400

    # Título
    font_title = pygame.font.Font(None, 48)
    title_text = font_title.render("Eagle Defender", True, GREEN)
    title_rect = title_text.get_rect(center=(center_x, 50))

    # Botones
    button_width = 200
    button_height = 50
    button_spacing = 100

    config_button_rect = pygame.Rect(center_x - button_width / 2, 150, button_width, button_height)
    about_button_rect = pygame.Rect(center_x - button_width / 2, 150 + button_spacing, button_width, button_height)
    role_switch_rect = pygame.Rect(center_x - button_width / 2, 150 + button_spacing * 2, button_width, button_height)
    start_game_button_rect = pygame.Rect(center_x - button_width / 2, 150 + button_spacing * 3, button_width,
                                         button_height)

    role_options = ["Atacante", "Defensor"]
    current_role = 0  # Índice del rol actual

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        mouse_pos = pygame.mouse.get_pos()

        if config_button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Lógica para abrir la configuración
                print("Configuración")
        elif about_button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Lógica para abrir la pantalla "Acerca de"
                print("Acerca de")
        elif role_switch_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Cambiar el rol del juego (alternar entre las opciones)
                current_role = (current_role + 1) % len(role_options)
                print("Rol actual:", role_options[current_role])
        elif start_game_button_rect.collidepoint(mouse_pos):
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Lógica para iniciar el juego con el rol seleccionado
                print("Iniciar juego con el rol:", role_options[current_role])

        window.fill(WHITE)

        # Dibujar el título "Eagle Defender" centrado en la parte superior
        window.blit(title_text, title_rect)

        draw_button(GREEN, *config_button_rect, "Configuración")
        draw_button(GREEN, *about_button_rect, "Acerca de")
        draw_button(GREEN, *role_switch_rect, "Cambiar Rol: " + role_options[current_role])
        draw_button(BRIGHT_GREEN, *start_game_button_rect, "Iniciar Juego")

        pygame.display.flip()


# Función para abrir la ventana de inicio de sesión
# Función para abrir la ventana de inicio de sesión
def login_window():
    login_window = pygame.display.set_mode((400, 200))
    pygame.display.set_caption('Ventana de inicio de sesión')

    username_input_rect = pygame.Rect(150, 50, 200, 30)
    password_input_rect = pygame.Rect(150, 100, 200, 30)
    login_button_rect = pygame.Rect(150, 150, 100, 40)

    username_text = ""
    password_text = ""
    input_active = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if login_button_rect.collidepoint(mouse_pos):
                    # Verificar las credenciales del usuario en la base de datos
                    if verify_credentials(username_text, password_text):
                        print("Inicio de sesión exitoso")
                        main_menu_window()
                        return  # Regresar a la ventana anterior
                elif username_input_rect.collidepoint(mouse_pos):
                    input_active = "username"
                elif password_input_rect.collidepoint(mouse_pos):
                    input_active = "password"
                else:
                    input_active = None

            elif event.type == pygame.KEYDOWN:
                if input_active == "username":
                    if event.key == pygame.K_RETURN:
                        input_active = "password"
                    elif event.key == pygame.K_BACKSPACE:
                        username_text = username_text[:-1]
                    else:
                        username_text += event.unicode
                elif input_active == "password":
                    if event.key == pygame.K_RETURN:
                        # Verificar las credenciales del usuario en la base de datos
                        if verify_credentials(username_text, password_text):
                            print("Inicio de sesión exitoso")
                            return  # Regresar a la ventana anterior
                    elif event.key == pygame.K_BACKSPACE:
                        password_text = password_text[:-1]
                    else:
                        password_text += event.unicode

        window.fill(WHITE)
        draw_button(GREEN, *login_button_rect, "Iniciar Sesión")
        pygame.draw.rect(window, (0, 0, 0), username_input_rect, 2)
        pygame.draw.rect(window, (0, 0, 0), password_input_rect, 2)

        font = pygame.font.Font(None, 36)
        username_surface = font.render(username_text, True, (0, 0, 0))
        password_surface = font.render('*' * len(password_text), True, (0, 0, 0))

        window.blit(username_surface, (username_input_rect.x + 5, username_input_rect.y + 5))
        window.blit(password_surface, (password_input_rect.x + 5, password_input_rect.y + 5))

        pygame.display.flip()


# Función para verificar las credenciales del usuario en la base de datos
def verify_credentials(username, password):
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
    row = cursor.fetchone()
    return row is not None

# Función para abrir la ventana de registro
def register_window():
    register_window = pygame.display.set_mode((400, 200))
    pygame.display.set_caption('Ventana de registro')

    username_input_rect = pygame.Rect(150, 50, 200, 30)
    password_input_rect = pygame.Rect(150, 100, 200, 30)
    register_button_rect = pygame.Rect(150, 150, 100, 40)

    username_text = ""
    password_text = ""
    input_active = None

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if register_button_rect.collidepoint(mouse_pos):
                    # Registrar al usuario en la base de datos
                    insert_user(username_text, password_text)
                    print("Usuario registrado con éxito")
                    return  # Regresar a la ventana anterior
                elif username_input_rect.collidepoint(mouse_pos):
                    input_active = "username"
                elif password_input_rect.collidepoint(mouse_pos):
                    input_active = "password"
                else:
                    input_active = None

            elif event.type == pygame.KEYDOWN:
                if input_active == "username":
                    if event.key == pygame.K_RETURN:
                        input_active = "password"
                    elif event.key == pygame.K_BACKSPACE:
                        username_text = username_text[:-1]
                    else:
                        username_text += event.unicode
                elif input_active == "password":
                    if event.key == pygame.K_RETURN:
                        # Registrar al usuario en la base de datos
                        insert_user(username_text, password_text)
                        print("Usuario registrado con éxito")
                        return  # Regresar a la ventana anterior
                    elif event.key == pygame.K_BACKSPACE:
                        password_text = password_text[:-1]
                    else:
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
# Función para insertar un usuario en la base de datos
def insert_user(username, password):
    try:
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("Usuario registrado con éxito")
    except pyodbc.Error as e:
        conn.rollback()
        print("Error al insertar usuario en la base de datos:", e)


# Crear rectángulos para los botones
login_button_rect = pygame.Rect(325, 200, 150, 50)
register_button_rect = pygame.Rect(325, 300, 150, 50)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        button_click(event)

    window.fill(WHITE)
    draw_button(GREEN, *login_button_rect, "Iniciar Sesión")
    draw_button(BRIGHT_GREEN, *register_button_rect, "Registrarse")
    pygame.display.flip()