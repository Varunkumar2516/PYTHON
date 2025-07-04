#1 with readline () code
line_count=0

with open("append.txt",'r') as F:
    while True:
        data=F.readline()
        if data!="":
            print(data,end='')
        else:
            break
        line_count+=1

print("Total Lines: ",line_count)



# 2 with For i in F 
line_count=0

with open("append.txt",'r') as F:
    for i in F:
        line_count+=1
        print(i,end='')

print("Total Lines: ",line_count)