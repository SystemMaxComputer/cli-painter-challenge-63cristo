# TODO: Add code here
import math
import matplotlib.pyplot as plt
import pickle


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def area(self) -> float:
        area = math.pi * (self.radius ** 2)
        return area

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return (f"Circle with center at {self.center.x, self.center.y} and radius r: "
                f"{self.radius}")


class Triangle:
    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_1: Point = point_1
        self.point_2: Point = point_2
        self.point_3: Point = point_3

    def area(self) -> float:
        area = 1/2 * (self.point_1.x * self.point_2.y + self.point_2.x * self.point_3.y +
                      self.point_3.x * self.point_1.y - self.point_2.x * self.point_1.y -
                      self.point_3.x * self.point_2.y - self.point_1.x * self.point_3.y)
        return area

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return (f"Triangle with vertices at {self.point_1.x, self.point_1.y}, "
                f"{self.point_2.x, self.point_2.y} and {self.point_3.x, self.point_3.y}")


class Rectangle:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1: Point = point_1
        self.point_2: Point = point_2

    def area(self) -> float:
        # Calculate base and height
        base = abs(self.point_2.x - self.point_1.x)
        height = abs(self.point_2.y - self.point_1.y)

        # Calculate the área
        area = base * height
        return area

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_2.x, self.point_1.x, self.point_1.x]
        y = [self.point_1.y, self.point_1.y, self.point_2.y, self.point_2.y, self.point_1.y]
        plt.fill(x, y, color='g')
        plt.axis("scaled")
        plt.show()

    def __str__(self):
        return (f"Rectangle with opposite vertices at {self.point_1.x, self.point_1.y} and "
                f"{self.point_2.x, self.point_2.y}")
