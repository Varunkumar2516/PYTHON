###############################
#Challenge for Today
"""Write a program that takes two lists and provide
Common elements, Unique elements, in each Total unique elements combined,"""



#Two lists
A=[1 , 2 , 3 , 6 , 7 , 9 ]
B=[2 , 3 , 4 , 1 , 2 ]
print("List A",A,"\nList B",B)
#Create Two sets from them
Set1=set(A)
Set2=set(B)

print("Common Elements in Both lists :",Set1|Set2)
print("Elements In Only A(Unique Elements In A)",Set1-Set2)
print("Elements In Only B(Unique Elements In B)",Set2-Set1)
print("Elements In Either set,Not In Both(Combined Unique Elements)",Set1^Set2)

#OUTPUT
# List A [1, 2, 3, 6, 7, 9] 
# List B [2, 3, 4, 1, 2]    
# Common Elements in Both lists : {1, 2, 3, 4, 6, 7, 9}
# Elements In Only A(Unique Elements In A) {9, 6, 7}
# Elements In Only B(Unique Elements In B) {4}
# Elements In Either set,Not In Both(Combined Unique Elements) {4, 6, 7, 9}