# container where you can put you value
# it will assign datatype as you assign the value
x=2
print(x+3)
y=3
print(x+y)



# underscore (_) represents value of previous operation
x+5
print(_+y)



>>> name='Youtube'
>>> name
'Youtube'
>>> name + ' rocks"
SyntaxError: EOL while scanning string literal
>>> name + ' rocks'
'Youtube rocks'
>>> name[0]
'Y'
>>> name[6]
'e'

#it goes backwords in the string
>>> name[-1]
'e'
>>> name[-7]
'Y'

# substring it will exclude last character
>>> name[1:4]
'out'

>>> name[:4]
'Yout'

>>> 'my ' +name[3:]
'my tube'

# strings in Python is immutable it means we cannot change the value of string

>>> name[0]='M'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    name[0]='M'
TypeError: 'str' object does not support item assignment


#find length
>>> len(name)
7
