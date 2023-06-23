import pygame
import time

pygame.init()
windows_surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Collider game")

# colors
black = (0, 0, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
white = (255, 255, 255)
# Keys
K_right_pressed = False
K_left_pressed = False
K_up_pressed = False
K_down_pressed = False
# Positions initiales
rect_pos = (20, 50)
# Def textes:
loose_font = pygame.font.SysFont("arial", 30)
loose_text = loose_font.render("Game Over ! ", True, white)

winner_font = pygame.font.SysFont("Arial", 30)
winner_text = winner_font.render("You won! Congratulations ! ", True, white)


# Def rectangles
Rect1 = pygame.Rect(20, 50, 60, 60)
Obstacle1 = pygame.Rect(400, 50, 60, 60)
Obstacle2 = pygame.Rect(100, 369, 60, 60)
Obstacle3 = pygame.Rect(300, 460, 60, 60)
Obstacle4 = pygame.Rect(200, 140, 60, 60)
Obstacle5 = pygame.Rect(300, 280, 60, 60)
flag = pygame.Rect(550, 10, 30, 550)

pygame.draw.rect(windows_surface, magenta, Rect1)
pygame.draw.rect(windows_surface, cyan, Obstacle1)
pygame.draw.rect(windows_surface, white, flag)
pygame.draw.rect(windows_surface, cyan, Obstacle2)
pygame.draw.rect(windows_surface, cyan, Obstacle3)
pygame.draw.rect(windows_surface, cyan, Obstacle4)
pygame.draw.rect(windows_surface, cyan, Obstacle5)
pygame.display.flip()

loading = True


def draw_rect():
    pygame.draw.rect(windows_surface, magenta, Rect1)
    pygame.draw.rect(windows_surface, cyan, Obstacle1)
    pygame.draw.rect(windows_surface, white, flag)
    pygame.draw.rect(windows_surface, cyan, Obstacle2)
    pygame.draw.rect(windows_surface, cyan, Obstacle3)
    pygame.draw.rect(windows_surface, cyan, Obstacle4)
    pygame.draw.rect(windows_surface, cyan, Obstacle5)
    pygame.display.flip()


while loading:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loading = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                K_right_pressed = True
                while K_right_pressed:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key != pygame.K_RIGHT:
                                K_right_pressed = False
                    draw_rect()
                    time.sleep(.10)
                    windows_surface.fill(black)
                    Rect1.x += 5
            if event.key == pygame.K_LEFT:
                K_left_pressed = True
                while K_left_pressed:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key != pygame.K_LEFT:
                                K_left_pressed = False
                    draw_rect()
                    time.sleep(.10)
                    windows_surface.fill(black)
                    Rect1.x -= 5

            if event.key == pygame.K_UP:
                K_up_pressed = True
                while K_up_pressed:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key != pygame.K_UP:
                                K_up_pressed = False
                    draw_rect()
                    time.sleep(.10)
                    windows_surface.fill(black)
                    Rect1.y -= 5
            if event.key == pygame.K_DOWN:
                K_down_pressed = True
                while K_down_pressed:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key != pygame.K_DOWN:
                                K_down_pressed = False
                    draw_rect()
                    time.sleep(.10)
                    windows_surface.fill(black)
                    Rect1.y += 5

    if Rect1.colliderect(Obstacle1) is True or Rect1.colliderect(Obstacle2) is True or \
            Rect1.colliderect(Obstacle3) is True or Rect1.colliderect(Obstacle4) is True or\
            Rect1.colliderect(Obstacle5) is True:
        windows_surface.fill(black)
        windows_surface.blit(loose_text, [200, 200])
        pygame.display.flip()
    elif Rect1.colliderect(flag) is True:
        windows_surface.fill(black)
        windows_surface.blit(winner_text, [200, 200])
        pygame.display.flip()

