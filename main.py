import pygame

pygame.init()
# create screen
screen = pygame.display.set_mode((800, 600))

# caption
pygame.display.set_caption("Space")
# icon = pygame.image.load("")
# pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("space.jpg")
playerX = 70
playerY = 80
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 150, 0))
    playerX += 0.2
    playerY -= 0.2
    print(playerX)
    player(playerX, playerY)
    pygame.display.update()
