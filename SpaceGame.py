import pygame
import math
import random
import os
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("Space game")

width = screen.get_width()
height = screen.get_height()
fps = pygame.time.Clock()
counter = 0
centre = (width/2,height/2)
show_axes = True
sysfont = pygame.font.get_default_font()
font = pygame.font.SysFont(None, 24)

#Gravitational constant
g = 0.0001
#Body object

class Body:
    mass = 0.5
    def __init__(self, type, position, color, velocity):
        self.type = type
        self.position = position
        self.color = color
        self.velocity = velocity

class Ship:
    mass = 0.5
    velocity = (1.0, 1.0)
    fuel = 200.0
    hp = 100.0
    def __init__(self, type, position, color):
        self.type = type
        self.position = position
        self.color = color

#Ship
ship = Ship("ship", (50.0, 50.0), (255, 255, 255))

#Planets
a = Body("planet", (centre[0]/2, centre[1]), (random.randint(1,254), random.randint(1,254), random.randint(1,254)), (0.2,-0.2))
b = Body("planet", (centre[0], centre[1]/1.5), (random.randint(1,254), random.randint(1,254), random.randint(1,254)), (0.2,-0.2))
planets = {a,b}

print('Ship details:')
print('pos: ', ship.position)
print('velocity: ', ship.velocity)

def unit_vector(vector):
    magnitude = math.sqrt(vector[0]*vector[0]+vector[1]*vector[1])
    return vector[0]/magnitude, vector[1]/magnitude

def from_centre(x,y):
    return (centre[0]-x,centre[1]-y)

def ship_polygon(pos, vel):
    x = unit_vector(vel)
    normal = unit_vector((math.pow(x[0],-1)*-1, math.pow(x[1],-1)*-1))
    return (pos[0]+x[0]*20, pos[1]+x[1]*20.0),  (pos[0]+((-0.5*x[0])+normal[0])*20.0, pos[1]+((-0.5*x[1])+normal[1])*20.0), (pos[0]-((-0.5*x[0])-normal[0])*20.0, pos[1]-((-0.5*x[1])-normal[1])*20.0)

def render():
    screen.fill((0, 0, 0))

    #Draw planets
    pygame.draw.circle(screen, (255, 110, 0), centre, 65)
    for planet in planets:
        pygame.draw.circle(screen, planet.color, planet.position, 20)
    #Draw ship
    polygon = ship_polygon(ship.position, ship.velocity)
    pygame.draw.polygon(screen, ship.color, polygon, 0)

    #Fuel
    #Draw text
    img = font.render('FUEL', True, (255, 0, 0))
    screen.blit(img, (centre[0]*0.02,centre[1]*1.8))
    pygame.draw.rect(screen, (255, 255, 0), pygame.Rect(centre[0]*0.1, centre[1]*1.8, ship.fuel//2, 24))
    #Health
    #Draw text
    img = font.render('HEALTH', True, (0, 255, 0))
    screen.blit(img, (centre[0]*0.02,centre[1]*1.6))
    pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(centre[0]*0.1, centre[1]*1.6, ship.hp, 24))

#Is the mouse pressed down?
mouseDown = False

while True:
    counter += 1
    #Input
    for event in pygame.event.get():
        #Keyboard
        if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_q]:
            pygame.quit()
        if pygame.key.get_pressed()[pygame.K_a] and ship.fuel > 0:
            ship.velocity = (ship.velocity[0]-0.2, ship.velocity[1])
            ship.fuel -= 0.1
        if pygame.key.get_pressed()[pygame.K_w] and ship.fuel > 0:
            ship.velocity = (ship.velocity[0], ship.velocity[1]-0.2)
            ship.fuel -= 0.1
        if pygame.key.get_pressed()[pygame.K_d] and ship.fuel > 0:
            ship.velocity = (ship.velocity[0]+0.2, ship.velocity[1])
            ship.fuel -= 0.1
        if pygame.key.get_pressed()[pygame.K_s] and ship.fuel > 0:
            ship.velocity = (ship.velocity[0], ship.velocity[1]+0.2)
            ship.fuel -= 0.1
        #Mouse
        if event.type == pygame.MOUSEBUTTONUP:
            mouseDown = False
        if (event.type == pygame.MOUSEBUTTONDOWN and ship.fuel > 0) or mouseDown and ship.fuel > 0:
            print("\nMouse Down\n")
            if not mouseDown:
                mouseDown = True
            mousePos = pygame.mouse.get_pos()
            vector = ship.position[0]-mousePos[0], ship.position[1]-mousePos[1]
            x = unit_vector(vector)
            ship.velocity = ship.velocity[0]-x[0]*0.2, ship.velocity[1]-x[1]*0.2
            ship.fuel -= 0.1
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