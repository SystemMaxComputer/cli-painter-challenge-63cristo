# TODO: Add code here
import math
import pickle

import matplotlib.pyplot as plt


class Point:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y


class Circle:
    def __init__(self, center: Point, radius: float):
        self.center: Point = center
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

    def draw(self):
        circle = plt.Circle((self.center.x, self.center.y), self.radius, color="r")
        plt.gca().add_patch(circle)
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str:
        return (f"Circle with center at {self.center.x, self.center.y} and radius "
                f"{self.radius}")


class Triangle:
    def __init__(self, point_1: Point, point_2: Point, point_3: Point):
        self.point_1: Point = point_1
        self.point_2: Point = point_2
        self.point_3: Point = point_3

    def area(self) -> float:
        area = abs(1/2 * (self.point_1.x * self.point_2.y + self.point_2.x * self.point_3.y +
                          self.point_3.x * self.point_1.y - self.point_2.x * self.point_1.y -
                          self.point_3.x * self.point_2.y - self.point_1.x * self.point_3.y))
        return area

    def draw(self):
        x = [self.point_1.x, self.point_2.x, self.point_3.x, self.point_1.x]
        y = [self.point_1.y, self.point_2.y, self.point_3.y, self.point_1.y]
        plt.fill(x, y, color='b')
        plt.axis("scaled")
        plt.show()

    def __str__(self) -> str:
        return f"Triangle with vertices at ({self.point_1.x, self.point_1.y}), ({self.point_2.x, self.point_2.y}), \
               and ({self.point_3.x, self.point_3.y})"


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

    def __str__(self) -> str:
        return (f"Rectangle with opposite vertices at ({self.point_1.x, self.point_1.y}) and "
                f"({self.point_2.x, self.point_2.y})")


class Painter:
    FILE = ".painter"

    def __init__(self) -> None:
        self.shapes: list = []
        self._load()

    def _load(self) -> None:
        try:
            with open(Painter.FILE, "rb") as f:
                self.shapes = pickle.load(f)
        except (EOFError, FileNotFoundError):
            self.shapes = []

    def _save(self) -> None:
        with open(Painter.FILE, "wb") as f:
            pickle.dump(self.shapes, f)

    def add_shape(self, shape) -> None:
        self.shapes.append(shape)
        self._save()

    def total_area(self) -> float:
        return sum(shape.area() for shape in self.shapes)

    def clear(self) -> None:
        self.shapes = []
        self._save()
