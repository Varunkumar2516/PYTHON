# zgeometry_test
#including ALL the Modules And Then Test them

# Test script for all Geometry Classes: Point, Line, Circle, Triangle

from PointModule import Point
from LineModule import Line
from Circlemodule import Circle
from TriangleModule import Triangle

def main():
    print("\n====== GEOMETRY MODULE TESTING ======\n")

    # -------- Point Class Test --------
    print("[POINT TEST]")
    p1 = Point(2, 3)
    p2 = Point(4, 7)
    p3 = Point(0, 0)

    print("Point 1:", p1)
    print("Point 2:", p2)

    print("1. Distance:", round(p1.distance(p2), 2))
    print("2. Midpoint:", p1.midpoint(p2))
    print("3. Slope:", p1.slope(p2))
    print("\n")

    # -------- Line Class Test --------
    print("[LINE TEST]")
    line = Line(p1, p2)
    test_pt = Point(3, 5)

    print("4. Line Equation:", line)
    print("5. Slope:", line.lineslope())
    print("6. Midpoint:", line.linemid())
    print("7. Y-Intercept:", line.y_intercept())
    print("8. Is point", test_pt, "on line?", line.check_point(test_pt))
    print("9. Distance from point to line:", round(line.Distance_point_line(test_pt), 2))
    print("\n")

    # -------- Circle Class Test --------
    print("[CIRCLE TEST]")
    center = Point(3, 5)
    radius = 4
    circle = Circle(center, radius)
    out_point = Point(9, 5)

    print("10. Circle Equation:", circle.String_equation())
    print("11. General Equation:", circle.General_Equation())
    print("12. At Origin?:", circle.CheckAtOrigin())
    print("13. Circumference:", round(circle.Circumference(), 2))
    print("14. Area:", round(circle.Area(), 2))
    print("15. Point", test_pt, "in circle?", circle.contains_point(test_pt))
    print("16. Point", out_point, "in circle?", circle.contains_point(out_point))
    print("\n")

    # -------- Triangle Class Test --------
    print("[TRIANGLE TEST]")
    t1 = Point(0, 0)
    t2 = Point(4, 0)
    t3 = Point(0, 3)

    
    triangle = Triangle(t1, t2, t3)
    print("17. Triangle:", triangle)
    a, b, c = triangle.side_lengths()
    print("18. Side Lengths: AB =", round(a, 2), ", BC =", round(b, 2), ", AC =", round(c, 2))
    print("19. Perimeter:", round(triangle.perimeter(), 2))
    print("20. Area:", triangle.area())
    print("21. Centroid:", triangle.centroid())
    print("22. Type by sides:", triangle.type_by_sides())
    print("23. Type by angles:", triangle.type_by_angles())

    print("\n====== END OF TEST ======")

if __name__ == "__main__":
    main()
