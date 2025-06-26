# mygeometry_test
#including both the Modules And Then Test them

from APointClass2D import Point
from BLineClass2D import Line

def main():
    print("=== Testing Point and Line Classes ===\n")

    # Create 2 Points
    #Point Test
    p1 = Point(2, 3)
    p2 = Point(4, 7)

    print("Point 1:", p1)
    print("Point 2:", p2)

    
    print("\n[1] Distance between p1 and p2:", p1.distance(p2))

   
    print("[2] Midpoint between p1 and p2:", p1.midpoint(p2))

 
    print("[3] Slope between p1 and p2:", p1.slope(p2))

    # Now test Line class
    line = Line(p1, p2)

    print("\n[4] Line created from p1 and p2:")
    print("Line Equation:", line)

    print("[5] Line slope:", line.lineslope())
    print("[6] Line midpoint:", line.linemid())
    print("[7] Y-intercept of line:", line.y_intercept())

    # Create a test point
    test_point = Point(3, 5)

    print("\n[8] Check if test point", test_point, "lies on line:")
    print("On line?" , line.check_point(test_point))

    print("[9] Distance of point", test_point, "from line:")
    print("Distance:", line.Distance_point_line(test_point))

if __name__ == "__main__":
    main()


#OUTPUT
"""
=== Testing Point and Line Classes ===

Point 1: (2, 3)
Point 2: (4, 7)

[1] Distance between p1 and p2: 4.47
[2] Midpoint between p1 and p2: (3.0, 5.0)
[3] Slope between p1 and p2: 2.0

[4] Line created from p1 and p2:
Line Equation: y = 2.00x + -1.00
[5] Line slope: 2.0
[6] Line midpoint: (3.0, 5.0)
[7] Y-intercept of line: -1.0

[8] Check if test point (3, 5) lies on line:
On line? True
[9] Distance of point (3, 5) from line:
Distance: 0.0
"""