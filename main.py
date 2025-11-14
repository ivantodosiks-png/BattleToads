import pygame
import sys

# Инициализация Pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mini Battletoads")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Игрок
player_size = 50
player_x, player_y = WIDTH//2, HEIGHT//2
player_speed = 5

# Главный цикл игры
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Очистка экрана
    screen.fill(WHITE)

    # Рисуем игрока
    pygame.draw.rect(screen, GREEN, (player_x, player_y, player_size, player_size))

    # Обновление экрана
    pygame.display.flip()

pygame.quit()
sys.exit()
