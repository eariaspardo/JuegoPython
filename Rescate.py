import pygame
import random

# Inicializar Pygame
pygame.init()


def start_rescatar_astronauta():

    # Configuración de la pantalla
    width, height = 550, 700
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Juego con Sprites en Pygame")

    # Cargar la imagen de fondo
    background_image = pygame.image.load("images/espacio.jpg")
    background_image = pygame.transform.scale(background_image, (width, height))

    # Clase para el personaje
    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("images/nave-p.png")
            self.image = pygame.transform.scale(self.image, (50, 50))  # Escalar a 50x50 píxeles
            self.rect = self.image.get_rect()
            self.rect.center = (width // 2, height - 50)
            self.speed = 4

        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < width:
                self.rect.x += self.speed

    # Clase para la moneda
    class Astronauta(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("images/astronauta.png")
            self.image = pygame.transform.scale(self.image, (30, 30))  # Escalar a 50x50 píxeles
            self.rect = self.image.get_rect()
            self.rect.center = (random.randint(20, width - 20), 0)  # Iniciar monedas en la parte superior

        def update(self):
            # Mover la moneda hacia abajo
            self.rect.y += 3
            # Si la moneda sale de la pantalla, eliminarla
            if self.rect.top > height:
                self.kill()

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    astronautas = pygame.sprite.Group()
    player = Player()
    all_sprites.add(player)

    # Puntuación
    score = 0

    # Reloj para controlar la velocidad del juego
    clock = pygame.time.Clock()

    # Bucle principal del juego
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Crear nuevas monedas aleatoriamente
        if len(astronautas) < 2:
            astronauta = Astronauta()
            astronautas.add(astronauta)
            all_sprites.add(astronauta)

        # Verificar si el jugador recoge monedas
        hits = pygame.sprite.spritecollide(player, astronautas, True)
        for hit in hits:
            score += 1

        # Actualizar todos los sprites
        all_sprites.update()

        # Dibuja el fondo
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)

        # Mostrar la puntuación
        font = pygame.font.Font(None, 36)
        text = font.render(f"Salvados: {score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.update()

        # Controlar la velocidad del juego
        clock.tick(60)

    # Salir del juego
    pygame.quit()

# Ejecutar el juego si se llama directamente este script
if __name__ == "__main__":
    start_rescatar_astronauta()
