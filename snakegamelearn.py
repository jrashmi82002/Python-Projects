import pygame
import random

#for starting
pygame.init()

scr_x = 500
scr_y = 500

#colours
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)

#game window
pyw = pygame.display.set_mode((scr_x,scr_y))

font = pygame.font.SysFont(None, 25)
#for introducing clock in game
fps = 30
c = pygame.time.Clock()
slst = []

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    pyw.blit(screen_text, [x,y])
    
def plot_snake(pyw, color, slst, sizes):
	for x,y in slst:
		pygame.draw.rect(pyw, color,[x, y, sizes, sizes])

def gameloop():
	#game variables
	game_exit = False
	game_over = False
	sx = 45
	sy = 56
	velo = 2
	vx = 1
	vy = 0
	sizes = 10
	score = 0
	slen = 1
	foodx = random.randint(50, 450)
	foody = random.randint(0, 150)
	sizef = 10
	while  not game_exit:
		if game_over:
			pyw.fill(white)
			text_screen("Game Over!", green, 50, 50)
			for events in pygame.event.get():
				if event.type == pygame.QUIT:
					exit_game = True
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_s:
						gameloop()
		else:	
			#main game loop
			for event in pygame.event.get():
				if event.type == pygame.KEYDOWN:      #handling keys
					if event.key == pygame.K_e:
						game_exit = True
					if event.key == pygame.K_u:
						sy-= 10
						vy=-velo
						vx=0
					if event.key == pygame.K_d:
						sy+=10
						vy=velo
						vx=0
					if event.key == pygame.K_r:
						sx+=10
						vx=velo
						vy=0
					if event.key == pygame.K_l:
						sx-=10
						vx=-velo
						vy=0
					
			pyw.fill(black)
			pygame.draw.rect(pyw, green,[foodx, foody, sizef, sizef])     #drawing in pygame
			
			sx+=vx
			sy+=vy
			if abs(sx-foodx)<6 and abs(sy-foody)<6:
				score+=5
				slen += 5
				foodx = random.randint(50, 450)
				foody = random.randint(50, 450)
			H =[]
			H.append(sx)
			H.append(sy)
			slst.append(H)
			
			if len(slst)>slen:
				del slst[0]
			text_screen(f"score: {score}",  white, 5, 5)
			plot_snake(pyw, red, slst, sizes )
			if sx<0 or sx>scr_x or sy<0 or sy>scr_y:
				game_over = True
			if H in slst[:-1]:
				game_over = True
				
		c.tick(fps)	
		pygame.display.update()

	# To quit the game
	pygame.quit()
	quit()
gameloop()