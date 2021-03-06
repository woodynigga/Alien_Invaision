import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

	# Class, for 1 ufo.
	def __init__(self, ai_settings, screen):
		super(Alien, self).__init__()
		self.screen = screen
		self.ai_settings = ai_settings

		self.image = pygame.image.load('images/ufo.bmp')
		self.rect = self.image.get_rect()

		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		self.x = float(self.rect.x)

	def check_edges(self):

		# Return True, if UFO on left side.
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True


	def update(self):

		# Move UFO to the right.
		self.x += (self.ai_settings.alien_speed_factor *
			self.ai_settings.fleet_direction)
		self.rect.x = self.x

	def blitme(self):

		# Input UFO in current position.
		self.screen.blit(self.image, self.rect)