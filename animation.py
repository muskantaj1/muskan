import pygame
import random
pygame.init()

black = [0,0,0]
white = [255, 255, 255]

myDisplay = pygame.display.set_mode((720,1022))
pygame.display.set_caption("Snow Animation")
a=2

snow_list = []
for i in range(100):
    x = random.randrange(0,1190)
    y = random.randrange(0,590)
    snow_list.append([x, y])

clock = pygame.time.Clock()
done = False
background_position = [0,0]
background_image = pygame.image.load("Desktop/2.png").convert()


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    myDisplay.blit(background_image, background_position)
    for i in range(len(snow_list)):
        pygame.draw.circle(myDisplay, white, snow_list[i], 8)
        snow_list[i][1] += 1
 
        
        if snow_list[i][1] > 590:
            y = random.randrange(-500, -200)
            snow_list[i][1] = y
            x = random.randrange(0, 1190)
            snow_list[i][0] = x
    
    if a==2:
        b=str(a)
        background_image = pygame.image.load("Desktop/"+ b+".png").convert()
    if a==100:
        b=str(a)
        background_image = pygame.image.load("Desktop/"+ b+".png").convert()
    if a==200:
        b=str(a)
        background_image = pygame.image.load("Desktop/"+ b+".png").convert()
    if a==200:
        a=2
    pygame.display.flip()
    clock.tick(20)
    a=a+1

pygame.quit()
