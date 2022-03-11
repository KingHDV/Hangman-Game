import pygame
import os

pygame.init()

# setup display
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

#load images
images = []
for i in range(7):
  image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(image)

#game variables
hangman_status = 0

#colors
WHITE = (255,255,255)

FPS = 60 # max Frames per Second
clock = pygame.time.Clock()

#setup game loop
run = True

while run:
  clock.tick(FPS)

  #update and refresh the display + draw current hangman status
  win.fill(WHITE)
  win.blit(images[hangman_status],(150,100)) # draw image, get the correct image + set the position
  pygame.display.update() #tell the game to update with the color
  
  for event in pygame.event.get(): #any event that has happend, will be stored in here
    if event.type == pygame.QUIT: # if red X Button clicked
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      print(pos)

pygame.quit()