#tuple is almost same as list but it is immutable we cannot change the value inside tuple

>>> tup=(1,2,3,4,5,4,3,6,7,2,1,2)
>>> tup.count(2)
3
>>> tup.index(4)
3




#set uses concept of hash
# insets indexing is not supported
>>> s={12,32,41,64,12,99,34}
>>> s
{32, 64, 34, 99, 41, 12}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> 