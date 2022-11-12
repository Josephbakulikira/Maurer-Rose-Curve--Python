import pygame
from algorithm import Rose

WIDTH, HEIGHT = 500, 500
SCREEN = (WIDTH, HEIGHT)

pygame.display.set_caption("Maurer Rose Curve")
win = pygame.display.set_mode(SCREEN)
clock = pygame.time.Clock()
fps = 30

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#set background
win.fill(WHITE)

# def Draw(d, num, size):
# Draw(71, 6, 200)

curve = Rose(71, 6, 200, WIDTH, HEIGHT, BLACK, win)



pygame.display.flip()

run = True

while run:
	clock.tick(fps)
	frame_rate = int(clock.get_fps())
	pygame.display.set_caption(f"Maurer Rose : FPS -> {frame_rate}")

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				run = False	

	curve.Maurer()
	curve.Rhodonea()
	
	pygame.display.update()
pygame.quit()	

