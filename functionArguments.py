def person(name,age): # formal arguments
    print("Name ", name)
    print("age ", age)

def person2(name,age=18): # default arguments
    print("Name ", name)
    print("age ", age)

person("Sumeet",30) #  actual arguments

person(age=25,name="SJ") # keyword arguments

person2("Sumeet") # call to default arguments

#variable length arguments
# use it when number of arguments are not fixed
# here *b will be tuple
# we can use only *b in that case c =0 will be assignment
def sum(a, *b):
    c=a
    for i in b:
        c +=i
    
    print(c)

sum(5,6,3,6)

# keyword variable length arguments
# use ** when you want to pass multiple arguments with keywords
def personDet(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

personDet('Sumeet',age=30,city='Irving',mob=9876543210)