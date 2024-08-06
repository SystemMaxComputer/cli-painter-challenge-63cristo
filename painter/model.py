# TODO: Add code here
import math
import matplotlib.pyplot as plt


class Point:
    def __int__(self, x: float, y: float):
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
        return f"Circle with center at {self.center.x, self.center.y} and radius r: {self.radius}"
