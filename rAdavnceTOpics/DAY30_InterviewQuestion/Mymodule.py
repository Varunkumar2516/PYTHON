class SquareClass:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
    

def main():
    
    #checkCode
    print("Checking code")
    a=SquareClass(5)
    print(a.area())

"""This line ensures that certain code only
 runs when the file is executed directly, 
 not when it is imported as a module in another script.
"""
if __name__=="__main__":
    main()

print("__name__ of Mymodule",__name__)
