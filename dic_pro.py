Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> d={1:"hi","py"=30}
SyntaxError: invalid syntax
>>> d={1:"hi","py":30}
>>> d[1]
'hi'
>>> d[py]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    d[py]
NameError: name 'py' is not defined
>>> d["py"]
30
>>> d[30]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d[30]
KeyError: 30
>>> 
