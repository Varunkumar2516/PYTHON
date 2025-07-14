# TriangleClass.py

from PointModule import Point
import math

class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

        if self.is_collinear():
            raise ValueError("The points are collinear; cannot form a triangle.")

    def is_collinear(self):
        # Area formula will be 0 for collinear points
        area = self.area()
        return area == 0

    def side_lengths(self):
        a = self.p2.distance(self.p3)
        b = self.p1.distance(self.p3)
        c = self.p1.distance(self.p2)
        return a, b, c

    def perimeter(self):
        a, b, c = self.side_lengths()
        return a + b + c

    def area(self):
        x1, y1 = self.p1.abscissa, self.p1.ordinate
        x2, y2 = self.p2.abscissa, self.p2.ordinate
        x3, y3 = self.p3.abscissa, self.p3.ordinate

        return abs((x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2)

    def centroid(self):
        x = (self.p1.abscissa + self.p2.abscissa + self.p3.abscissa) / 3
        y = (self.p1.ordinate + self.p2.ordinate + self.p3.ordinate) / 3
        return Point(x, y)

    def __str__(self):
        return f"Triangle with vertices: {self.p1}, {self.p2}, {self.p3}"

    def type_by_sides(self):
        a, b, c = self.side_lengths()
        if round(a, 5) == round(b, 5) == round(c, 5):
            return "Equilateral"
        elif round(a, 5) == round(b, 5) or round(b, 5) == round(c, 5) or round(a, 5) == round(c, 5):
            return "Isosceles"
        else:
            return "Scalene"

    def type_by_angles(self):
        a, b, c = self.side_lengths()
        sides = sorted([a, b, c])
        # Use Pythagorean Theorem
        if round(sides[2] ** 2, 5) == round(sides[0] ** 2 + sides[1] ** 2, 5):
            return "Right-Angled"
        elif round(sides[2] ** 2, 5) < round(sides[0] ** 2 + sides[1] ** 2, 5):
            return "Acute-Angled"
        else:
            return "Obtuse-Angled"



