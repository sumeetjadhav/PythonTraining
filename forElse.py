# print only one number divisible by 5

nums=[12,15,18,21,25]

for i in nums:
    if i%5==0:
        print(i)
        break






numbers=[12,11,18,21,22]

for i in nums:
    if i%5==0:
        print(i)
        break
    # else:  #it will print not found 5 times
    #     print('not found')
else:
    print('not found') # this will print not found only one time