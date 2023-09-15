import pygame
import random

# Inicializar Pygame
pygame.init()

def start_eliminar_nave():

    # Configuración de la pantalla
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Juego de Disparar Naves")

    # Colores
    white = (255, 255, 255)

    # Fuente
    font = pygame.font.Font(None, 36)

    # Cargar la imagen de fondo
    background_image = pygame.image.load("images/espacio.jpg")
    background_image = pygame.transform.scale(background_image, (width, height))


    # Clase para la nave del jugador
    class PlayerShip(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("images/nave-p.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.center = (width // 2, height - 50)
            self.speed = 5

        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.speed
            if keys[pygame.K_RIGHT] and self.rect.right < width:
                self.rect.x += self.speed

    # Clase para las naves enemigas
    class EnemyShip(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.image = pygame.image.load("images/nave.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
            self.rect = self.image.get_rect()
            self.rect.x = random.randint(0, width - self.rect.width)
            self.rect.y = random.randint(10, height - 200)
            self.speed = random.randint(2, 4)

        def update(self):
            self.rect.x += self.speed
            if self.rect.left > width:
                self.rect.x = 0
                self.rect.y = random.randint(20, height - 200)
                self.speed = random.randint(2, 4)

    # Clase para los disparos
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super().__init__()
            self.image = pygame.image.load("images/bullet.png")
            self.image = pygame.transform.scale(self.image, (20, 40))
            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.speed = 8

        def update(self):
            self.rect.y -= self.speed
            if self.rect.bottom < 0:
                self.kill()

    # Grupos de sprites
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    player = PlayerShip()
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Disparar un proyectil cuando se presiona la barra espaciadora
                    bullet = Bullet(player.rect.centerx, player.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)

        # Crear nuevas naves enemigas aleatoriamente
        if len(enemies) < 5:
            enemy = EnemyShip()
            all_sprites.add(enemy)
            enemies.add(enemy)

        # Verificar si los disparos impactan a las naves enemigas
        hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for hit in hits:
            score += 1

        # Actualizar todos los sprites
        all_sprites.update()

        # Dibujar la pantalla
        #screen.fill(white)
        # Dibuja el fondo
        screen.blit(background_image, (0, 0))
        all_sprites.draw(screen)

        # Mostrar la puntuación
        font = pygame.font.Font(None, 36)
        text = font.render(f"Eliminados: {score}", True, (255, 255, 255))
        screen.blit(text, (10, 10))

        pygame.display.update()

        # Controlar la velocidad del juego
        clock.tick(60)

    # Salir del juego
    pygame.quit()

if __name__ == "__main__":
    start_eliminar_nave()
