## ===================================================
#        DAY 14 - 2D coordinate Geometry :Point Class
#                    Menu driven Practice
#         Creation using class magicfunctions
# ===================================================
import math
class Point:

    #Constructor using __init__():
    def __init__(self,x,y):
        self.abscissa=x
        self.ordinate=y

    #To print the cordinates
    def __str__(self):
     return f"{self.abscissa,self.ordinate}"
    
    # For Distance Between the Two Points

    def distance(self,other):
        mydist=math.sqrt((self.abscissa-other.abscissa)**2 + (self.ordinate-other.ordinate)**2)
        return mydist
    
    def slope(self,other):
       if self.abscissa==other.abscissa:
          return None
       slope=(other.ordinate-self.ordinate)/(other.abscissa-self.abscissa)
       return slope
    
    def midpoint(self,other):
       midx=(other.abscissa+self.abscissa)/2
       midy=(other.ordinate+self.ordinate)/2
       return Point(midx,midy)
    
    def __eq__(self,other):
       return self.abscissa==other.abscissa and self.ordinate==other.ordinate
    
    def __repr__(self):
        """Developer-friendly string representation."""
        return f"Point({self.abscissa}, {self.ordinate})"
    
    def distzero(self):
       distfromzero=math.sqrt(self.abscissa**2 +self.ordinate**2)
       return distfromzero
    
