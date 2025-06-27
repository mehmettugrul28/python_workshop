import pygame
import time
import random

# Pygame'i başlat
pygame.init()

# Renk tanımları (R, G, B)
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)  

# Oyun ekranı boyutları
display_width = 600
display_height = 400

# Ekran oluşturma
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Yılan Oyunu')

# Oyun saat ayarı
clock = pygame.time.Clock()

# Yılanın boyutu
snake_block = 10
snake_speed = 5

# Fontlar
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Skor hesaplama
def score_display(score):
    value = score_font.render("Skor: " + str(score), True, yellow)
    game_display.blit(value, [0, 0])

# Yılanın kendisini çizme fonksiyonu
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(game_display, green, [block[0], block[1], snake_block, snake_block])

# Mesaj yazdırma fonksiyonu
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    game_display.blit(mesg, [display_width / 6, display_height / 3])

# Oyun döngüsü
def game_loop():
    game_over = False
    game_close = False

    # Başlangıç pozisyonu
    x = display_width / 2
    y = display_height / 2

    x_change = 0
    y_change = 0

    # Yılanın vücut parçaları
    snake_list = []
    length_of_snake = 1

    # Yem pozisyonu
    food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            game_display.fill(blue)
            message("Oyunu kaybettin! Tekrar oynamak için C'ye, çıkmak için Q'ya bas", red)
            score_display(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0

        # Sınır kontrolü
        if x >= display_width or x < 0 or y >= display_height or y < 0:
            game_close = True
        x += x_change
        y += y_change
        game_display.fill(blue)

        # Yemi çiz
        pygame.draw.rect(game_display, red, [food_x, food_y, snake_block, snake_block])

        # Yılanın başı
        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        # Yılan kendine çarpıyor mu kontrolü
        for block in snake_list[:-1]:
            if block == snake_head:
                game_close = True

        # Yılanı çiz
        draw_snake(snake_block, snake_list)
        score_display(length_of_snake - 1)

        pygame.display.update()

        # Yılan yemi yedi mi kontrolü
        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, display_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, display_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Oyunu başlat
game_loop()
