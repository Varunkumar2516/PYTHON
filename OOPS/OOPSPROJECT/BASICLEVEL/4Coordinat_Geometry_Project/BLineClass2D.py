## ===================================================
#        DAY 14 - 2D coordinate Geometry :Line Class
#                    Menu driven Practice
#         Creation using class magicfunctions
# ===================================================

#Importing the previous point class 
from APointClass2D import Point
import math

class Line:

    #constructor __init__()
    def __init__(self,point1,point2):
      self.p1=point1
      self.p2=point2

    def lineslope(self):
       linescope=self.p1.slope(self.p2) 
       return linescope

    def linemid(self):
       mid_point=self.p1.midpoint(self.p2)
       return mid_point
    
    def y_intercept(self):
       m=self.lineslope()
       c= (self.p1.ordinate)- m* (self.p1.abscissa)
       return c
    
    def __str__(self):
       #  y=mx+c  (m=slope and c is y intercept)
       #  c=y-mx then use any point and find c
       m=self.p1.slope(self.p2)
    #  c= (       y        )- m*(        x         ) 
       c= (self.p1.ordinate)- m* (self.p1.abscissa)
       return f"y={m:.2f}x+{c:.2f}" 
    
    def check_point(self,point):
       m=self.lineslope()
       c=self.y_intercept()
       if m is None:
           return point.abscissa == self.p1.abscissa  # vertical line case
       if point.ordinate == m * point.abscissa +c:
          print("Point Is On the Line ")
          return True
       else:
          return False
    
    def Distance_point_line(self,point):
       m=self.lineslope()
       c=self.y_intercept()
       if m is None:
          return (point.abscissa-self.pq.abscissa)
       if self.check_point(point):
           return 0
       else:
            distance=(abs(m*point.abscissa -point.ordinate +c))/math.sqrt(1+m**2)
            return round(distance,2)
    

def main():
   print("=== 2D Line Geometry Menu Program ===\n")

  # Get two points from user
   str1=input("Enter coordinates of first point (x1 y1): ")
   x1, y1 = map(int,str1.strip().split(",") if ',' in str1 else str1.strip().split(" "))
   str2=input("Enter coordinates of first point (x1 y1): ")
   x2, y2 = map(int,str2.strip().split(",") if ',' in str2 else str2.strip().split(" "))

   p1 = Point(x1, y1)
   p2 = Point(x2, y2)

   line = Line(p1, p2)

   while True:
     print("\nChoose Operation:")
     print("1. Print Line Equation")
     print("2. Get Slope")
     print("3. Get Midpoint")
     print("4. Get Y-Intercept")
     print("5. Check if a Point Lies on Line")
     print("6. Distance from Point to Line")
     print("0. Exit")

     choice = input("Enter choice: ")

     if choice == '1':
         print("Line Equation:", line)
     elif choice == '2':
         print("Slope:", round(line.lineslope(),2))
     elif choice == '3':
         print("Midpoint:", line.linemid())
     elif choice == '4':
         print("Y-intercept:", round(line.y_intercept(),2))
     elif choice == '5':
         str1=input("Enter coordinates of first point (x1 y1): ")
         x, y = map(int,str1.strip().split(",") if ',' in str1 else str1.strip().split(" "))
         test_point = Point(x, y)
         if line.check_point(test_point):
             print("Point lies on the line.")
         else:
             print("Point does NOT lie on the line.")
     elif choice == '6':
         str1=input("Enter coordinates of first point (x1 y1): ")
         x, y = map(int,str1.strip().split(",") if ',' in str1 else str1.strip().split(" "))
         test_point = Point(x, y)
         distance = line.Distance_point_line(test_point)
         print(f"Distance from point to line: {distance} Units")
     elif choice == '0':
         print("Goodbye!")
         break
     else:
         print("Invalid option. Try again.")


#when we use it as Module And Import it in another file
#__name__ becomes "That script name"
#so the main() function not runs only the class (Point) can be used in that file
if __name__=="__main__":
   main()
