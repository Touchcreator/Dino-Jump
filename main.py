#Player Sprites by Arks
#https://arks.itch.io/dino-characters
#Arks' Twitter: @ScissorMarks
#yes

import pygame

#constant vars
screenSize = (700,500)
white = (255,255,255)
cyan = (117, 235, 225)
logo = pygame.image.load("./assets/images/tard/tard_00.png")

#init
pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Dino Jump")
pygame.display.set_icon(logo)

#player
playerImage = pygame.image.load("./assets/images/tard/tard_00.png")

#platforms
platform = pygame.Rect(100,300,400,50)

#game loop
running = True
while running:

  #get input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #update

  #draw
  #bg
  screen.fill(cyan)
  #plats
  pygame.draw.rect(screen,(),platform)
  #player
  screen.blit(playerImage,(300,0))
  #screen
  pygame.display.flip()

#quit
pygame.quit()