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
    
def wait():
   input("\nPress Enter To Continue :")
def main():
    print("\n 2D Coordinate Geometry Menu")
    str1=input("Enter cordinates of (x1,y1)= :")
    a,b=map(int,str1.strip().split(",") if ',' in str1 else str1.strip().split() )
    P1=Point(a,b)
    str2=input("Enter cordinates of (x2,y2)= :")
    c,d=map(int,str2.strip().split(",") if ',' in str2 else str2.strip().split() )
    P2=Point(c,d)
    while True:
     print("1. Show both points")
     print("2. Distance between points")
     print("3. Midpoint")
     print("4. Slope")
     print("5. Are the points equal?")
     print("6. Distance From Origin to Point")
     print("7. Exit")
     user=input("Enter the Input")
     if user=='1':
        print("\n\tFirst Point    :(x,y)",P1)
        print("\tSecond  Point  :(x,y)",P2)
        wait()
     elif user=='2':
        dist=P1.distance(P2)
        print("\n\tDistance Between Two Points :",round(dist,2)," Units")
        wait()
     elif user=='3':
        midpoint=P1.midpoint(P2)
        print("\n\tMid-Point Between Two Points :",midpoint)
        wait()
     elif user=='4':
        slope=P1.slope(P2)
        print("\n\tSlope Of Two points ",round(slope,2)," Units")
        wait()
     elif user=='5':
        print("\n\tIs Both Points Are Equal?  :",P1==P2)
        wait()
     elif user=='6':
        distzero1=P1.distzero()
        distzero2=P2.distzero()
        #round(variable,points) =>>  #round(variable,2)
        #round is used to give the numeric results from 1.2234132 => 1.22 only 
        print("\n\tDistance From Zero To First Point ",round(distzero1,2)," Units")
        print("\tDistance From Zero To Second Point ",round(distzero2,2)," Units")
        wait()
     elif user=='7':
        print("Thank You")
        break
     else:
        print("Invalid Option! Try Again")

#when we use it as Module And Import it in another file
#__name__ becomes "That script name"
#so the main() function not runs only the class (Point) can be used in that file
if __name__=="__main__":
   main()
      
    


