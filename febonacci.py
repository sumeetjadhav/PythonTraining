def fib(n):
    a=0
    b=1
    if (n<1):
        print("Enter range equal to 1 or higher") 
    elif(n==1):
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            print(c)


fib(5)

# # simple method
# a, b = 0, 1
# for i in range(0, 10):
#     print (a)
#     a, b = b, a + b

# # method 3

# def fib1(num):
#   a,b = 0, 1
#   for i in range(0, num):
#     yield "{} : {}".format(i + 1,a)
#     a, b = b, a + b

# for item in fib1(7):
#   print (item)



# # Method 4 - recursive
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))

# nterms = 0

# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))