

def count(lst):
    ev=0
    od=0
    for i in lst:
        if i%2==0:
            ev+=1
        else:
            od+=1
    return ev,od
        
            


lst=[22,4,2,121,5,9,43,6,7,8]

even, odd = count(lst)
print("Even : {} and Odd : {}".format(even,odd))