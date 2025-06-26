# TriangleClass.py

from APointClass2D import Point
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



def main():
    print("\n===== Coordinate Geometry - Triangle Menu =====\n")
    try:
        print("Enter coordinates for the 3 triangle vertices:")
        x1, y1 = map(float, input("Enter x1 y1: ").split())
        x2, y2 = map(float, input("Enter x2 y2: ").split())
        x3, y3 = map(float, input("Enter x3 y3: ").split())

        p1 = Point(x1, y1)
        p2 = Point(x2, y2)
        p3 = Point(x3, y3)

        triangle = Triangle(p1, p2, p3)
    except ValueError as e:
        print("Error:", e)
        return

    while True:
        print("\n===== MENU =====")
        print("1. Show Triangle Vertices")
        print("2. Get Side Lengths")
        print("3. Get Perimeter")
        print("4. Get Area")
        print("5. Get Centroid")
        print("6. Type by Sides")
        print("7. Type by Angles")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print(triangle)

        elif choice == '2':
            a, b, c = triangle.side_lengths()
            print(f"Side lengths:\nAB = {a:.2f}, BC = {b:.2f}, AC = {c:.2f}")

        elif choice == '3':
            print("Perimeter:", round(triangle.perimeter(), 2))

        elif choice == '4':
            print("Area:", round(triangle.area(), 2))

        elif choice == '5':
            centroid = triangle.centroid()
            print(f"Centroid: ({centroid.abscissa}, {centroid.ordinate})")

        elif choice == '6':
            print("Triangle is:", triangle.type_by_sides())

        elif choice == '7':
            print("Triangle is:", triangle.type_by_angles())

        elif choice == '8':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
