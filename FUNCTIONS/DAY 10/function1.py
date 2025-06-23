print("\n1. Simple Function with Parameters")
def add(a, b):
    return a + b
print(add(2, 3))  # Output: 5


print("\n2. Function with Default Value")
def greet(name="Guest"):
    return f"Hello {name}"
print(greet())            # Output: Hello Guest
print(greet("Aman"))      # Output: Hello Aman


print("\n3. Function with *args (Multiple Values)")
def multiply_all(*nums):
    result = 1
    for n in nums:
        result *= n
    return result

list=[4,5,6,6]
print(multiply_all(2, 3, 4))  # Output: 24


print("\n4. Function with **kwargs (Multiple Keyword Values)")
def user_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

        
user_info(name="Aman", age=25, country="India")
# Output:
# name = Aman
# age = 25
# country = India


print("\n5. Function Without Return (Print only)")
def greet_user(name):
    print(f"Hello, {name}!")
greet_user("Alok")  # Output: Hello, Alok!
