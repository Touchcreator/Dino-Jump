#Player Sprites by Arks
#https://arks.itch.io/dino-characters
#Arks' Twitter: @ScissorMarks
#yes

import pygame

#constant vars
screenSize = (700,500)
white = (255,255,255)
cyan = (117, 235, 225)
green = (5, 255, 72)
WIDTH = 700
HEIGHT = 500
logo = pygame.image.load("./assets/images/tard/tard_00.png")

#init
pygame.init()
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Dino Jump")
pygame.display.set_icon(logo)

#player
playerImage = pygame.image.load("./assets/images/tard/tard_00.png")
playerX = 300
playerY = 100

#platforms
platforms = [
  pygame.Rect(100,300,400,50),
  pygame.Rect(100,250,50,50),
  pygame.Rect(450,250,50,50)
]

#game loop
running = True
while running:

  #quit check
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  #player input
      keys = pygame.key.get_pressed()
      if keys[pygame.K_a]:
        playerX -= 2
      if keys[pygame.K_d]:
        playerX += 2

  #draw
  #bg
  screen.fill(cyan)
  #plats
  for p in platforms:
    pygame.draw.rect(screen,(green),p)
  #player
  screen.blit(playerImage,(playerX,playerY))
  #screen
  pygame.display.flip()

#quit
pygame.quit()