def numberofones(n):
    count = 0
    while n:
        if (n & 1) == 1:
            count += 1
        n = n >> 1  # Properly indented: inside while loop
    return count

num = int(input("Enter the number: "))
count = numberofones(num)
print(count)
