# ==========================================
# 📌 Iteration Using For Loop
# ==========================================

fruits = ["apple", "banana", "cherry"]

print("\n1.For Loop Without range")
for i in fruits:
    print(i,end=" ")

# Output:
# apple banana cherry



# ==========================================
# 📌 Iteration Using For Loop with Range and Length function
# ==========================================
print("\n2.For Loop With range")
for i in range(len(fruits)):
    print(fruits[i])

# Output:
# apple
# banana
# cherry



# ==========================================
# 📌 Iteration Using While Loop
# ==========================================
print("\n3.While Loop ")
i = 0
while i < len(fruits):
    print(fruits[i])
    i += 1

# Output:
# apple
# banana
# cherry



# ==========================================
# 📌 Iteration Using for Loop With Shorthand
# ==========================================
print("\n4.for Loop short hand iteration ")

[print(i) for i in fruits]

# OUPTUT
# apple
# banana
# cherry