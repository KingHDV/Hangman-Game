import pygame
import math
import os

pygame.init()

# setup display
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman Game")

# button variables
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) /2)
starty = 400
A = 65

for i in range(26):
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
  y = starty + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x, y, chr(A + i), True])

# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
  
#load images
images = []
for i in range(7):
  image = pygame.image.load("hangman" + str(i) + ".png")
  images.append(image)

#game variables
hangman_status = 0

#colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#setup game loop
FPS = 60 # max Frames per Second
clock = pygame.time.Clock()
run = True

def draw():
  # update and refresh the display + draw current hangman status
  win.fill(WHITE)

  # draw buttons
  for letter in letters:
    x, y, ltr, visible = letter # split up the variables from the letters []
    if visible: #let the button disappear if it has been klicked
      pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
      text = LETTER_FONT.render(ltr, 1, BLACK)
      win.blit(text, (x - text.get_width()/2, y - text.get_height()/2)) # go back in width and height to draw the letters in the middle of the buttons
  
  win.blit(images[hangman_status],(150,100)) # draw image, get the correct image + set the position
  pygame.display.update() # tell the game to update with the color

while run:
  clock.tick(FPS)

  draw()
  
  for event in pygame.event.get(): #any event that has happend, will be stored in here
    if event.type == pygame.QUIT: # if red X Button clicked
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
      #check if the mouse hits a button
      m_x, m_y = pygame.mouse.get_pos()
      for letter in letters:
        x, y, ltr, visible = letter
        if visible:
          dis = math.sqrt((x - m_x)**2 + (y - m_y)**2) # determine the distance between two points
          if dis < RADIUS:
            letter[3] = False
      

pygame.quit()