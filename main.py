import pygame

pygame.init()

window = pygame.display.set_mode((800,500))
fps = pygame.time.Clock()

fon_image = pygame.image.load("background.png")
fon_image = pygame.transform.scale(fon_image,(800,500))

sprite1 = pygame.image.load("sprite1.png")
sprite1 = pygame.transform.scale(sprite1,(50,50))
x1, y1= 50,50


while True:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()


    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        x1 += 5
    if keys[pygame.K_a]:
        x1 -= 5
    if keys[pygame.K_DOWN]:
        y1 += 3
    if keys[pygame.K_UP]:
        y1 -= 3


    window.blit(fon_image, [0, 0])
    window.blit(sprite1, [x1, y1])
    pygame.display.flip()
    fps.tick(60)