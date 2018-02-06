Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a={4,0,3,6,2}
>>> print(a)
{0, 2, 3, 4, 6}
>>> a={black,white,red,yellow}
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    a={black,white,red,yellow}
NameError: name 'black' is not defined
>>> a={"black,white,red,yellow"}
>>> print(a)
{'black,white,red,yellow'}
>>> 
