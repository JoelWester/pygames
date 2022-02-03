import pygame
import math
import os
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Space game")

width = screen.get_width()
height = screen.get_height()
fps = pygame.time.Clock()
counter = 0
centre = (width//2,height//2)
show_axes = False

#Gravitational constant
g = 0.0002
#Ship object

class Ship:
    position =(50.0, 50.0)
    mass = 0.5
    velocity = (0.0, 0.0)

print('Ship details:')
print('pos: ', Ship.position)
print('mass: ', Ship.mass)
print('velocity: ', Ship.velocity)

def from_centre(x,y):
    return (centre[0]-x,centre[1]-y)

def render():
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 110, 0), centre, 65)
    pygame.draw.circle(screen, (91, 226, 87), Ship.position, 20)


while True:
    counter += 1
    #Keyboard Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            pygame.quit()
        if pygame.key.get_pressed()[pygame.K_a]:
            Ship.velocity = (Ship.velocity[0]-0.2, Ship.velocity[1])
        if pygame.key.get_pressed()[pygame.K_w]:
            Ship.velocity = (Ship.velocity[0], Ship.velocity[1]-0.2)
        if pygame.key.get_pressed()[pygame.K_d]:
            Ship.velocity = (Ship.velocity[0]+0.2, Ship.velocity[1])
        if pygame.key.get_pressed()[pygame.K_s]:
            Ship.velocity = (Ship.velocity[0], Ship.velocity[1]+0.2)
    #Ship updates
    distance = from_centre(Ship.position[0], Ship.position[1])
    print('distance: ', distance)
    gravity = (g*distance[0], g*distance[1])
    print('gravity: ', gravity)
    Ship.velocity = (Ship.velocity[0] + gravity[0], Ship.velocity[1] + gravity[1])
    Ship.position = (Ship.position[0] + Ship.velocity[0], Ship.position[1] + Ship.velocity[1])
    render()
    pygame.display.update()
    fps.tick(60)