import pygame

class game:

	dis = None
	aliens = []
	gameOver = False
	bullets = []

	def __init__(self, width, height): 

		pygame.init()
		self.width = width
		self.height = height
		FPS = 30
		dis = pygame.display.set_mode(width,height)
		self.clock = pygame.display.set_mode((width, height))
		done = False
	

	while not gameOver:
#
#
		pygame.display.update()
		for event in pygame.event.get():
		if event.type == pygame.K_A:
			player.move.x+=10
		else if event.type == pygame.K_D:
			player.x-=10
		else if event.type == pygame.K_SPACE:
			self.bullets.append(bullet(self,player.x,player.y))
		
		pygame.display.flip()
		self.clock.tick(FPS)
		self.display.fill((0,0,0)) #black bkgrnd
		for aliens in self.aliens:
			alien.draw()
			aliens.checkCollision(self)
			if(alien.y>height):
				self.gameOver = True
		for bullet in self.bullets:
			bullet.draw():
		if not self.lost: player.draw():

class  aliens:
	
	def __init__(self, game, x, y)
		self.x=x
		self.y=y
		self.size = 30

	def draw(self):
		pygame.draw.rect(self.game.display,(81,43,88),
			pygame.Rect(self.x,self.y,self.size,self.size))
		self.y+=0.05
	def checkCollision(self,game):
		for bullet in game.bullets:
			if(bullet.x <self.x + self.size
				and rocket.x > self.x
				and rocket.y < self.y
		and rocket.y > self.y-self.size):
				game.bullets.remove(bullet)
				game.aliens.remove(self)
			
