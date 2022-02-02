import pygame

pygame.init()

surface= pygame.display.set_mode((1920,1080)
surface.fill(())
pygame.display.update()

running = True

while running:
  for event in pyga,e.event.get():
    if event.type == KEYDOWN:
      if event.type == K_ESCAPE:
        running = False
    elif event.type == QUIT:
      running = False
  
