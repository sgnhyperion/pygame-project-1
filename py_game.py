import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

pos = pygame.Rect(400,400,50,50)

while running:
    screen.fill("white")   
    # pygame.display.flip()    
    pygame.draw.rect(screen, "red", pos)
    
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
        pos.move_ip(-2,0)
    elif key[pygame.K_d] == True:
        pos.move_ip(2,0)
    elif key[pygame.K_w] == True:
        pos.move_ip(0,-2)
    elif key[pygame.K_s] == True:
        pos.move_ip(0,2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    pygame.display.update()
pygame.quit()