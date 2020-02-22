from math import sin 
from math import cos 
from math import radians
import pygame

class Rose:
	def __init__(self,d, num, size, width, height, color, screen):
		self.num = num
		self.d = d
		self.size = size
		self.width = width
		self.height = height
		self.color = color
		self.screen = screen

	def Rhodonea(self):
		points = []
		for a in range (0, 361):

			# the equations
			r = self.size * sin(radians(self.num * a))

			x = r * cos(radians(a))
			y = r * sin(radians(a))

			list.append(points, (self.width / 2 + x, self.height/2 + y))

		pygame.draw.lines(self.screen, self.color, False, points,1)

	def Maurer(self):
		    points =[] 
		    for a in range(0, 361): 
		        # The equation of a maurer rose 
		        k = a * self.d 
		        r = self.size * sin(radians(self.num * k)) 
		  
		        # Converting to cartesian co-ordinates 
		        x = r * cos(radians(k)) 
		        y = r * sin(radians(k)) 
		  
		        list.append(points, (self.width / 2 + x, self.height / 2 + y)) 
		  
		    # Draws a set of line segments connected by set of vertices points 
		    # Also don't close the path and draw it black and set the width to 5 
		    pygame.draw.lines(self.screen, self.color, False, points, 1) 
