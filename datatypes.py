#Data types 
# 1. None
When variable is not assigned with any value then it is considered as NONE

# 2. Numeric
int 1,2,3,4,5
float  1.2,1.0,3.1
complex x=6+9j
bool 

a=5.6
b=int(a)
b=float(b)
c=complex(a,b)
bool=a<b
>>> int(True)
1
>>> int(False)
0

# 3. List
lst=[1,2,4,5,7,1,0]
type(lst)

# 4. Tuple
tup=(1,2,4,5,7,1,0)

# 5. Set
s={1,2,4,5,7,1,0}

# 6. String
str='ABCDEFGHI'

# 7. Range
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,10,2))
[2, 4, 6, 8]


# 8. Dictionary
# all the keys should be unique
>>> d={'sumeet':'oneplus','joe':'iPhone','john':'samsung'}
>>> d
{'sumeet': 'oneplus', 'joe': 'iPhone', 'john': 'samsung'}
>>> d.keys()
dict_keys(['sumeet', 'joe', 'john'])
>>> d.values()
dict_values(['oneplus', 'iPhone', 'samsung'])
>>> d['sumeet']
'oneplus'
>>> d.get('joe')
'iPhone'
