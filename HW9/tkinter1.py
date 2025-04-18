import pygame
import sys

# مقداردهی اولیه
pygame.init()
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("انیمیشن گالری شبانه")

# بارگذاری تصاویر
girl_img = pygame.image.load("girl.png")
shop_img = pygame.image.load("shop.png")

# تغییر اندازه تصاویر
girl_img = pygame.transform.scale(girl_img, (100, 150))
shop_img = pygame.transform.scale(shop_img, (250, 250))

# موقعیت اولیه دختر
girl_x = -100
girl_y = height - 170

# موقعیت مغازه
shop_x = 500
shop_y = height - 250

# فونت متن
font = pygame.font.SysFont("arial", 32)

clock = pygame.time.Clock()
show_text = False

running = True
while running:
    screen.fill((10, 10, 40))  # پس‌زمینه شب

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # حرکت دختر
    if girl_x < shop_x - 80:
        girl_x += 2
    else:
        show_text = True

    # نمایش تصاویر
    screen.blit(shop_img, (shop_x, shop_y))
    screen.blit(girl_img, (girl_x, girl_y))

    # نمایش متن وقتی دختر رسید
    if show_text:
        text = font.render("به گالری شبانه خوش اومدی!", True, (255, 200, 200))
        screen.blit(text, (width // 2 - text.get_width() // 2, 50))

    pygame.display.update()
    clock.tick(60)

pygame.quit()
sys.exit()
