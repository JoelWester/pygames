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
    mass = 0.5
    velocity = (0.0, 0.0)
    def __init__(self, type, position):
        self.type = type
        self.position = position

#Ship
ship = Body("ship", (50.0, 50.0))

#Planets
a = Body("planet", (centre[0]//2, centre[1]//2))
planets = {a}

print('Ship details:')
print('pos: ', ship.position)
print('velocity: ', ship.velocity)

def from_centre(x,y):
    return (centre[0]-x,centre[1]-y)

def render():
    screen.fill((0, 0, 0))

    pygame.draw.circle(screen, (255, 110, 0), centre, 65)
    for planet in planets:
        pygame.draw.circle(screen, (91, 226, 87), planet.position, 20)
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
    #Ship updates
    distance = from_centre(ship.position[0], ship.position[1])
    print('distance: ', distance)
    gravity = (g*distance[0], g*distance[1])
    print('gravity: ', gravity)
    ship.velocity = (ship.velocity[0] + gravity[0], ship.velocity[1] + gravity[1])
    ship.position = (ship.position[0] + ship.velocity[0], ship.position[1] + ship.velocity[1])
    #Planet updates
    for planet in planets:
        distance = from_centre(planet.position[0], planet.position[1])
        gravity = (g*distance[0], g*distance[1])
        planet.velocity = (planet.velocity[0] + gravity[0], planet.velocity[1] + gravity[1])
        planet.position = (planet.position[0] + planet.velocity[0], planet.position[1] + planet.velocity[1])
    render()
    pygame.display.update()
    fps.tick(60)