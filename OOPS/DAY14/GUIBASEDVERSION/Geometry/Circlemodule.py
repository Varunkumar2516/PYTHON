
from Geometry.LineModule import Point,Line
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
    """Plots the circle, its center, and both equations using matplotlib."""
    def plot(self):

     fig, ax = plt.subplots()

     # Plot circle
     circle_patch = plt.Circle(
        (self.Center.abscissa, self.Center.ordinate),
        self.radius,
        color='blue',
        fill=False,
        linewidth=2,
        label='Circle'
     )
     ax.add_patch(circle_patch)

     # Plot center point
     ax.plot(self.Center.abscissa, self.Center.ordinate, 'ro', label='Center')

     # Annotate center
     ax.text(
        self.Center.abscissa + 0.2,
        self.Center.ordinate + 0.2,
        f"Center ({self.Center.abscissa}, {self.Center.ordinate})",
        fontsize=10,
        color='red'
     )

     # Add equations
     ax.text(
        0.05,
        0.1,
        f"Standard: {self.String_equation()}",
        transform=ax.transAxes,
        fontsize=10,
        color='green',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')
     )

     ax.text(
        0.05,
        0.90,
        f"General: {self.General_Equation()}",
        transform=ax.transAxes,
        fontsize=10,
        color='purple',
        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')
     )

     # Plot settings
     ax.set_aspect('equal')
     ax.set_xlim(self.Center.abscissa - self.radius - 3, self.Center.abscissa + self.radius + 3)
     ax.set_ylim(self.Center.ordinate - self.radius - 3, self.Center.ordinate + self.radius + 3)
     plt.grid(True)
     plt.title("Circle Visualization with Center and Equations")
     plt.xlabel("x-axis")
     plt.ylabel("y-axis")
     plt.legend()
     plt.show()

     


    


