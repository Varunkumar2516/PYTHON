L=[1,2,3]

#Built in Scope FUnction
print(max(L))

#here i create my own Global scope Function
def max():
    print("My max version")

# this uses the global scope version of function
# according to the rule L->E->G_>B
# global COmes before the built in scope
print(max(L))