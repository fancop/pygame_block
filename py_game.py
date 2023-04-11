import pygame
import sys

pygame.init()

# экран
screen_width = 800  # ширина экрана в пикселях
screen_hight = 600  # высота экрана в пикселях
screen = pygame.display.set_mode((screen_width, screen_hight))    # экран
pygame.display.set_caption("моя игра")

# игрок
player_width = 100
player_hight = 100
player_x = screen_width // 2 - player_width // 2
player_y = screen_hight // 2 - player_width //2
player_color = (255, 255, 000)  # RGB
player = pygame.Rect((player_x, player_y, player_width, player_hight))  # x, y, ширина, высота

while True: # главный цикл

    # событие
    for event in pygame.event.get():  # собираем событие
        if event.type == pygame.QUIT:  # обработка события
            pygame.quit()  # выгрузили мудули pygame из памяти
            sys.exit()  # закрыли программу
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # нажатая клавиша
                pygame.quit()
                sys.exit()

    keys = pygame.key.get_pressed()  # собираем нажатые клавиши
    if keys[pygame.K_w]:  # обрабатываем нажатые клавиши
        player.y -= 1
    if keys[pygame.K_s]:
        player.y += 1
    if keys[pygame.K_a]:
        player.x -= 1
    if keys[pygame.K_d]:
        player.x += 1

    

    # отрисовка
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, player_color, player)  # рисуем игрока
    pygame.display.flip()  #обновляем экран 