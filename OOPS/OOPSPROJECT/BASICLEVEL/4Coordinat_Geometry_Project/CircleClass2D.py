## ===================================================
#        DAY 14 - 2D coordinate Geometry :Circle Class
#                    Menu driven Practice
#         Creation using class magicfunctions
# ===================================================
from BLineClass2D import Point,Line
#using matplotlib for plotting the circle
import matplotlib.pyplot as plt
class Circle:

    def __init__ (self,Center,R):
        self.Center=Center
        self.radius=R
        self.Atcenter=False
        self.Equation=''
        self.general=''


        #Different cases for x-h and y-k signs
        if self.Center.abscissa==0 and self.Center.ordinate==0:
            self.Atcenter=True
            self.Equation=f"x^2 + y^2 ={self.radius **2}" 
            self.general=self.Equation
        else:
             h=self.Center.abscissa
             k=self.Center.ordinate
             if self.Center.abscissa<0 and self.Center.ordinate<0:
                
                 h*=-1
                 k*=-1
                 self.Equation=f"(x+{h})^2 + (y+{k})^2={self.radius**2}"
                 self.general=f" (x^2 + y^2) + {2*h}x + {2*k}y + {(self.Center.abscissa)**2 + (self.Center.ordinate)**2 - (self.radius)**2} = 0"
             elif h<0:
                 h*=-1
                 self.Equation=f"(x+{h})^2 + (y-{k})^2={self.radius**2}"
                 self.general=f" (x^2 + y^2) + {2*h}x - {2*k}y + {(self.Center.abscissa)**2 + (self.Center.ordinate)**2 - (self.radius)**2} = 0"
             elif k<0:
                 k*=-1
                 self.Equation=f"(x-{h})^2 + (y+{k})^2={self.radius**2}"
                 self.general=f" (x^2 + y^2) - {2*h}x + {2*k}y + {(self.Center.abscissa)**2 + (self.Center.ordinate)**2 - (self.radius)**2} = 0"
             else:
                 self.Equation=f"(x-{h})^2 + (y-{k})^2={self.radius**2}"
                 self.general=f" x^2 + y^2 - {2*h}x - {2*k}y + {(self.Center.abscissa)**2 + (self.Center.ordinate)**2 - (self.radius)**2} = 0"
       
    
    def __str__(self):
        return self.Equation
    
    def String_equation(self):
        return self.Equation
     
    # def String_equation_general(self):
    def General_Equation(self):
        return self.general
    
    def CheckAtOrigin(self):
        return self.Atcenter
    
    def Circumference(self):
        return 2*3.14*self.radius
    
    def Area(self):
        return 3.14*(self.radius)**2
    
    def Diameter(self):
        return self.radius ** 2
    
    def __eq__(self,other):
       return self.radius==other.radius and self.Center == other.Center
    
    def contains_point(self,point):

        distance=self.Center.distance(point)
        if distance==self.radius:
            return "point LIes On Circle"
        elif distance<self.radius:
            return 'Point is Inside The circle'
        else:
            return 'Point is Outside The Circle'
    
    def position_relation(self,other_circle):
        d=self.Center.distance(other_circle.Center)
        r1=self.radius
        r2=other_circle.radius

        if d==0 and r1==r2:
            return "Circles are identical"
        elif d==abs(r1-r2):
            return "Circles Touch Intenally"
        elif d==r1+r2:
            return "Circles Touch Externally"
        elif abs(r1-r2)< d <r1+r2:
            return "Circles Intersect"
        else:
            return 'Circles are Separate Do not interract'
        

    def __contains__(self,point):
        """Allows use of `in` keyword to check if a point lies within or on the circle."""
        return self.Center.distance(point) < self.radius
    
    def plot(self):
      """Plots the circle using matplotlib."""
      fig, ax = plt.subplots()
      circle = plt.Circle((self.Center.abscissa, self.Center.ordinate), self.radius, color='blue', fill=False)
      ax.add_patch(circle)
      ax.set_aspect('equal', adjustable='datalim')
      ax.plot()  
      plt.grid(True)
      plt.title("Circle Visualization")
      plt.show()

    



def main():
    print("====== 2D Geometry: Circle Class Menu ======")
    str1=input("Enter the Point (x,y) by (,) separated values :")
    x,y=map(int,str1.strip().split(",") if ',' in str1 else str1.strip().split(""))
    r = float(input("Enter radius of the circle: "))

    center = Point(x, y)
    circle = Circle(center, r)

    while True:
        print("\n======== MENU =========")
        print("1. Print Circle Equation")
        print("2. Print General Equation")
        print("3. Check if Circle is at Origin")
        print("4. Get Circumference")
        print("5. Get Area")
        print("6. Check if Point lies on / inside / outside the Circle")
        print("7. Check Position Relation with another Circle")
        print("8. Plot Circle (matplotlib)")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("Standard Equation:", circle.String_equation())

        elif choice == '2':
            print("General Form:", circle.General_Equation())

        elif choice == '3':
            print("Is the circle at origin?", circle.CheckAtOrigin())

        elif choice == '4':
            print("Circumference:", round(circle.Circumference(), 2))

        elif choice == '5':
            print("Area:", round(circle.Area(), 2))

        elif choice == '6':
            x = float(input("Enter x-coordinate of point: "))
            y = float(input("Enter y-coordinate of point: "))
            p = Point(x, y)
            print(circle.contains_point(p))

        elif choice == '7':
            print("Enter another circle to compare:")
            x2 = float(input("Enter x-coordinate of 2nd center: "))
            y2 = float(input("Enter y-coordinate of 2nd center: "))
            r2 = float(input("Enter radius of 2nd circle: "))
            other = Circle(Point(x2, y2), r2)
            print("Relation:", circle.position_relation(other))

        elif choice == '8':
            try:
                circle.plot()  # Ensure this method is inside the class or pass `circle` to external `plot(circle)`
            except Exception as e:
                print("Plotting failed:", e)

        elif choice == '9':
            print("Thanks for using the Circle Geometry Program!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
