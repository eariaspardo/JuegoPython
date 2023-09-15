import pygame
import sys
from Rescate import start_rescatar_astronauta
from EliminarNave import start_eliminar_nave

# Inicializar Pygame
pygame.init()

# Configuración de la pantalla
width, height = 800, 600
PANTALLA = pygame.display.set_mode((width, height))
pygame.display.set_caption("Menú Interactivo en Pygame")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Fuente
font = pygame.font.Font(None, 36)

PANTALLA.fill(NEGRO)

# Opciones del menú
menu_options = ["Jugar Eliminar Naves", "Jugar Rescatar Astronautas", "Salir"]

# Función para mostrar el menú
def show_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i in range(len(menu_options)):
                    text = font.render(menu_options[i], True, BLANCO)
                    text_rect = text.get_rect(center=(width // 2, height // 2 - len(menu_options) * text.get_height() // 2 + i * 50))
                    if text_rect.collidepoint(mouse_pos):
                        if i == 0:
                            start_rescatar_astronauta()
                        elif i == 1:
                            start_eliminar_nave()
                        elif i == 2:  # Salir
                            pygame.quit()
                            sys.exit()

        PANTALLA.fill(NEGRO)

        # Dibuja las opciones del menú
        for i in range(len(menu_options)):
            text = font.render(menu_options[i], True, (255, 255, 255))
            y_position = height // 2 - len(menu_options) * text.get_height() // 2 + i * 50
            PANTALLA.blit(text, (width // 2 - text.get_width() // 2, y_position))

        pygame.display.update()

# Bucle principal del menú
show_menu()
