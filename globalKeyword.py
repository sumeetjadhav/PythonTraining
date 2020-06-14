# scope
a=10
print(id(a))
    

def something():
    # global a   # you can declare variable as global
    a=15
    x=globals()['a']
    print(id(x))

    print("in func ",a)
    globals()['a']=20 #using this we access global variables

something()
print("outside ", a)