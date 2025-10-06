import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Two Rectangles Game")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

rect1 = pygame.Rect(100, 100, 100, 60)
rect2 = pygame.Rect(500, 300, 120, 80)

speed = 5
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        rect1.y -= 10
    if keys[pygame.K_s]:
        rect1.y += 10
    if keys[pygame.K_a]:
        rect1.x -= 10
    if keys[pygame.K_d]:
        rect1.x += 10

    rect1.x = max(0, min(rect1.x, WIDTH - rect1.width))
    rect1.y = max(0, min(rect1.y, HEIGHT - rect1.height))

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, rect1)
    pygame.draw.rect(screen, BLUE, rect2)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()