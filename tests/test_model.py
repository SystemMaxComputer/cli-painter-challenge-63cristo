import pytest

from painter.model import Circle, Point, Rectangle, Triangle


@pytest.fixture
def point_1():
    return Point(3, 4)


@pytest.fixture
def point_2():
    return Point(1, 2)


@pytest.fixture
def point_3():
    return Point(3, 4)


@pytest.fixture
def circle():
    return Circle(Point(3, 4), 5)


@pytest.fixture
def triangle():
    return Triangle(Point(0, 0), Point(3, 4), Point(8, 2))


@pytest.fixture
def rectangle():
    return Rectangle(Point(1, 2), Point(5, 8))


# Point tests
def test_point_initializes_with_x_and_y(point_1):
    assert point_1.x == 3
    assert point_1.y == 4


# Circle tests
def test_circle_initializes_with_center_and_radius(circle):
    assert circle.center.x == 3
    assert circle.center.y == 4
    assert circle.radius == 5


def test_circle_area(circle):
    assert circle.area() == pytest.approx(78.53981633974483)


def test_circle_str(circle):
    assert str(circle) == "Circle with center at (3, 4) and radius 5"


def test_circle_draw(circle):
    circle.draw()
    # This test is not very useful, but it's hard to test the draw method in a meaningful way
    

# Triangle tests
def test_triangle_initializes_with_three_points(triangle):
    assert triangle.point_1.x == 0
    assert triangle.point_1.y == 0
    assert triangle.point_2.x == 3
    assert triangle.point_2.y == 4
    assert triangle.point_3.x == 8
    assert triangle.point_3.y == 2
    

def test_triangle_area(triangle):
    assert triangle.area() == pytest.approx(13)


def test_triangle_str(triangle):
    assert str(triangle) == "Triangle with vertices at (0, 0), (3, 4), and (8, 2)"


def test_triangle_draw(triangle):
    triangle.draw()
    # This test is not very useful, but it's hard to test the draw method in a meaningful way


# Rectangle tests
def test_rectangle_initializes_with_two_points(rectangle):
    assert rectangle.point_1.x == 1
    assert rectangle.point_1.y == 2
    assert rectangle.point_2.x == 5
    assert rectangle.point_2.y == 8


def test_rectangle_area(rectangle):
    assert rectangle.area() == 24


def test_rectangle_str(rectangle):
    assert str(rectangle) == "Rectangle with vertices at (1, 2) and (5, 8)"
    

def test_rectangle_draw(rectangle):
    rectangle.draw()
    # This test is not very useful, but it's hard to test the draw method in a meaningful way
