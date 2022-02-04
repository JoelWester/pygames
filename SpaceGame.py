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
g = 0.0001
#Body object

class Body:
    position =(50.0, 50.0)
    mass = 0.5
    velocity = (0.0, 0.0)
    def __init__(self, type):
        self.type = type

ship = Body("Ship")

print('Body details:')
print('pos: ', ship.position)
print('mass: ', ship.mass)
print('velocity: ', ship.velocity)

def from_centre(x,y):
    return (centre[0]-x,centre[1]-y)

def render():
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 110, 0), centre, 65)
    pygame.draw.circle(screen, (91, 226, 87), ship.position, 20)


while True:
    counter += 1
    #Keyboard Input
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            pygame.quit()
        if pygame.key.get_pressed()[pygame.K_a]:
            ship.velocity = (ship.velocity[0]-0.2, ship.velocity[1])
        if pygame.key.get_pressed()[pygame.K_w]:
            ship.velocity = (ship.velocity[0], ship.velocity[1]-0.2)
        if pygame.key.get_pressed()[pygame.K_d]:
            ship.velocity = (ship.velocity[0]+0.2, ship.velocity[1])
        if pygame.key.get_pressed()[pygame.K_s]:
            ship.velocity = (ship.velocity[0], ship.velocity[1]+0.2)
    #Body updates
    distance = from_centre(ship.position[0], ship.position[1])
    print('distance: ', distance)
    gravity = (g*distance[0], g*distance[1])
    print('gravity: ', gravity)
    ship.velocity = (ship.velocity[0] + gravity[0], ship.velocity[1] + gravity[1])
    ship.position = (ship.position[0] + ship.velocity[0], ship.position[1] + ship.velocity[1])
    render()
    pygame.display.update()
    fps.tick(60)