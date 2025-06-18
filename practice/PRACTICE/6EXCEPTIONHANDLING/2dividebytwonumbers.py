
# Program 2 : Exception Handling 

# This program provides the number divison by using exception handling

print("Program to divide two numbers with exception handling")

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    
    result = num1 / num2  # This might raise ZeroDivisionError
    print(f"Result = {result}")

except ValueError:
    print("Invalid input. Please enter only numbers.")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except Exception as e:
    print(f"Unexpected error occurred: {e}")

finally:
    print("Execution completed. Thank you!")
