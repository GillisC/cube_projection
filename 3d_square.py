import pygame
from vector3 import Vector3
import numpy as np
import math

pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

COLOR = (180, 180, 180)


def project_2d(matrix: np.matrix):
    xy_projection = np.matrix(
        ([1, 0, 0],
        [0, 1, 0],
        [0, 0, 0])
    )
    return matrix.dot(xy_projection)

def create_points() -> list[Vector3]:
    p0 = Vector3(-100, -100, -100)
    p1 = Vector3(100, -100, -100)
    p2 = Vector3(100, 100, -100)
    p3 = Vector3(-100, 100, -100)

    p4 = Vector3(-100, -100, 100)
    p5 = Vector3(100, -100, 100)
    p6 = Vector3(100, 100, 100)
    p7 = Vector3(-100, 100, 100)
    return [p0, p1, p2, p3, p4, p5, p6, p7]

def draw_points(points: list[Vector3], color: (int)):
    for point in points:
        pygame.draw.circle(screen, color, (point.x+WIDTH/2, point.y+HEIGHT/2), 8)

def draw_cube(points: list[Vector3], color: (int)):
    x_offset = WIDTH/2
    y_offset = HEIGHT/2

    for i in range(0, 4):
        start = points[i]
        if i == 3:
            end = points[0]
        else:
            end = points[i+1]
        pygame.draw.line(screen, color, (start.x+x_offset, start.y+y_offset), (end.x+x_offset, end.y+y_offset), 4)

    for i in range(4, 8):
        start = points[i]
        if i == 7:
            end = points[4]
        else:
            end = points[i+1]
        pygame.draw.line(screen, color, (start.x+x_offset, start.y+y_offset), (end.x+x_offset, end.y+y_offset), 4)
    
    for i in range(0,4):
        start = points[i]
        end = points[i+4]
        pygame.draw.line(screen, color, (start.x+x_offset, start.y+y_offset), (end.x+x_offset, end.y+y_offset), 4)

def advance_color(r, g, b) -> ():
    r += 0.3
    r %= 255
    g += 0.2
    g %= 255
    b += 0.1
    b %= 255
    return r, g, b

def main():
    points = create_points()
    running = True
    r, g, b = 180, 180, 180
    color = (r, g, b)
    while running:
        clock.tick(FPS)
        screen.fill((31, 31, 31))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for index, point in enumerate(points):
                points[index] = point.rotate(0.01, 0.03, 0.02)

        
        draw_points(points, color)  
        draw_cube(points, color)

        r, g, b = advance_color(r, g, b)
        color = (r, g, b)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
