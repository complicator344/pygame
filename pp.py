import sys, pygame
pygame.init()
size = width, height = 600, 800
speed = [2, 2]
black = 0, 0, 0
screen = pygame.display.set_mode(size)
ball = pygame.image.load("pat.bmp")
ballrect = ball.get_rect()
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
            speed[10] = -speed[10]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[5] = -speed[5]

        screen.fill(black)
        screen.blit(ball, ballrect)
        pygame.display.flip()








