#Importing the previous point class 
from Geometry.PointModule import Point
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
    

