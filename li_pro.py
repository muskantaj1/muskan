Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> [2,4,6,7]
[2, 4, 6, 7]
>>> {2,6,4,[6,9,8],2]
SyntaxError: invalid syntax
>>> [2,6,4,[6,9,8],2]
[2, 6, 4, [6, 9, 8], 2]
>>> a=[1,2,3]
>>> b=a+[4,5,6]
>>> print(b)
[1, 2, 3, 4, 5, 6]
>>> ["google",1,2,3]
['google', 1, 2, 3]
>>> a=[3,6,4,8,]
>>> a[0]
3
>>> a[4]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a[4]
IndexError: list index out of range
>>> a[3,6,7,[4,5,6],8]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    a[3,6,7,[4,5,6],8]
TypeError: list indices must be integers or slices, not tuple
>>> a=[3,6,7,[4,5,6],8]
>>> a[0][1]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    a[0][1]
TypeError: 'int' object is not subscriptable
>>> 
