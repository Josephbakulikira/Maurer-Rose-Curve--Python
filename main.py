import pygame
from algorithm import Rose

WIDTH, HEIGHT = 500, 500
SCREEN = (WIDTH, HEIGHT)

pygame.display.set_caption("Maurer Rose Curve")
win = pygame.display.set_mode(SCREEN)

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#set background
win.fill(WHITE)

def Draw(d, num, size):

	curve = Rose(d, num, size, WIDTH, HEIGHT, BLACK, win)
	curve.Maurer()
	curve.Rhodonea()
Draw(71, 6, 200)


pygame.display.flip()

run = True

while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()	
			run = False

		pygame.display.update()

