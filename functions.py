def greet():
    print("Hello")
    print("Sumeet")

greet()

def add(a,b):
    sum=a+b
    return sum

def add_sub(a,b):
    sum=a+b
    sub=a-b
    return sum,sub


result=add(10,4)
print(result)
result1,result2=add_sub(10,4)
print(result1, result2)


# when we call a funtion with a value 
# a=10
# update(a)


# we don't use pass by value or pass by reference in Python
# so when we pass variable it will point to same ID in the memory but when we change the value of it, 
#  then it will switch to new ID
# but when we pass list to function and change value at a particular position it will not change the id of that list  
def update(x):
    print(id(x))
    x=8
    print(id(x))
    print("x ",x)

a=10
print(id(a))
update(a)
print("a ",)