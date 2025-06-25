#using the FRaction Module Here by imporing it.....


from Fraction_Module import Fraction


f1 = Fraction(1, 2)
f2 = Fraction(3, 4)
print("\n1. Print")
print("f1 =", f1)                       # 1/2
print("f2 =", f2)                       # 3/4


print("\n2. ADD :")
print("f1 + f2 =", f1 + f2)             # 5/4

print("\n3. Substract :")
print("f1 - f2 =", f1 - f2)             # -1/4

print("\n4. Multiply :")
print("f1 * f2 =", f1 * f2)             # 3/8

print("\n5. DIVIDE :")
print("f1 / f2 =", f1 / f2)             # 2/3

print("6. Compare :")
print("Are f1 and f2 equal?", f1 == f2) # False

print("\n7. Less Than :")
print("Is f1 < f2 ?", f1 < f2)     # True

print("\n8. Greater than : ")
print("Is f1 > f2 ?", f1 > f2)     # False

print("\n9. Less Than Equal to :")
print("Is f1 <= f2 ?", f1 <= f2)   # True


print("\n10. Greater Than Equal To: ")
print("Is f1 >= f2 ?", f1 >= f2)   # False


print("\n 11. Developer Printing :")
print("Number 1",repr(f1))
print("Number 2",repr(f2))



# Testing reduction
print("\n12. Checking the Reductions ::")
f3 = Fraction(4, 8)
print("Reduced 4/8 =", f3)              # 1/2


    
