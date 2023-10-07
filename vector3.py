import math
import numpy as np
import pygame

pygame.init()

WIDTH = 600
HEIGHT = 600
FPS = 60
WHITE = (180, 180, 180)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

class Vector3():

    def __init__(self, x, y, z) -> None:
        self.row: list[float] = [x, y, z]
        self.x: float = self.row[0]
        self.y: float = self.row[1]
        self.z: float = self.row[2]

    """Computes the dot product a Vector3 and a 3x3 matrix"""
    def dot_product(self, matrix: list):
        a = np.matrix(self.row)
        b = np.matrix(matrix) 
        result = a.dot(b)
        return Vector3(result.tolist()[0][0], result.tolist()[0][1], result.tolist()[0][2])

    
    def rotate_x(self, angle: int):
        rotation_x = [
            [1,               0,                0],
            [0, math.cos(angle), -math.sin(angle)],
            [0, math.sin(angle),  math.cos(angle)]]
        
        result = self.dot_product(rotation_x)
        return result 


    def rotate_y(self, angle: int):
        rotation_y = [
            [ math.cos(angle), 0, math.sin(angle)],
            [               0, 1,               0],
            [-math.sin(angle), 0, math.cos(angle)]]
        result = self.dot_product(rotation_y)
        return result

    def rotate_z(self, angle: int):
        rotation_z = [
            [math.cos(angle), -math.sin(angle), 0],
            [math.sin(angle),  math.cos(angle), 0],
            [              0,                0, 1]]
        result = self.dot_product(rotation_z)
        return result
    
    """Rotates the Vector3 around the x, y and z axi"""
    def rotate(self, x_angle: int, y_angle: int, z_angle: int) -> None:
        v = self.rotate_x(x_angle)
        v = v.rotate_y(y_angle)
        v = v.rotate_z(z_angle)
        return v
    
    """Projects the Vector3 onto the xy-plane"""
    def project_2d(self) -> None:
        projection_matrix = [
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, 0]]
        result = self.dot_product(projection_matrix)
        return result

    """String representation for Vector3"""
    def __str__(self) -> str:
        return f"x: {self.x}, y: {self.y}, z: {self.z}"

"""Used for testing"""
def test() -> None:
    v = Vector3(1, 0, 0)

    test_matrix = [
        [3, 1, 4],
        [7, 8, 3], 
        [6, 3, 5]
    ]

if __name__ == "__main__":
    test()