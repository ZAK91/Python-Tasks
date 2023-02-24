Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
x = TRUE
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    x = TRUE
NameError: name 'TRUE' is not defined. Did you mean: 'True'?
x = True
 y = 14
 
SyntaxError: unexpected indent
y = 14
z = 14.8
type(z)
<class 'float'>
s = "Hi"
x= 5
type(x)
<class 'int'>
float(x)
5.0
type(x)
<class 'int'>
print("yes we can convert the int to string by using int() function ")
yes we can convert the int to string by using int() function 
z = [1,2,3,4,5]
type of (z)
SyntaxError: invalid syntax
>>> 
>>> type(z)
<class 'list'>
>>> x= 5
>>> tuble(z)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuble(z)
NameError: name 'tuble' is not defined. Did you mean: 'tuple'?
>>> tuple(z)
(1, 2, 3, 4, 5)
>>> a = (10,11,12,13,14,15)
>>> type(a)
<class 'tuple'>
>>> a={1,2,3,4,5}
>>> type(a)
<class 'set'>
>>> a={1:zakria , 2 : ahmad , 3: mohammad , 4 : yahya , 5 : jebrel}
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a={1:zakria , 2 : ahmad , 3: mohammad , 4 : yahya , 5 : jebrel}
NameError: name 'zakria' is not defined
>>> a={1 : zakria , 2 : ahmad , 3: mohammad , 4 : yahya , 5 : jebrel}
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    a={1 : zakria , 2 : ahmad , 3: mohammad , 4 : yahya , 5 : jebrel}
NameError: name 'zakria' is not defined
>>> a={1: 'zakria' , 2 : 'ahmad' , 3: 'mohammad' , 4 : 'yahya' , 5 : 'jebrel'}
>>> type(a)
<class 'dict'>
>>> print('yes, we can use the semicolon in python but when we need it , not in every single statment)
...       
SyntaxError: incomplete input
>>> print('yes, we can use the semicolon in python but when we need it , not in every single statment')
...       
yes, we can use the semicolon in python but when we need it , not in every single statment
