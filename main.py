#Player Sprites by Arks
#https://arks.itch.io/dino-characters
#Arks' Twitter: @ScissorMarks

import pygame

#constant vars
screenSize = (700,500)
white = (255,255,255)
logo = pygame.image.load("./assets/images/tard/tard_00.png")

#init
pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Dino Jump")
pygame.display.set_icon(logo)

#game loop
running = True
while running:

  #get input
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #update

  #draw
  screen.fill(white)
  pygame.display.flip()

#quit
pygame.quit()