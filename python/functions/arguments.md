# Types of argument
- Default
- Positional
- Keyword
- Aribitrory/ variable length
- A P, A K
```
- Default argument example
- Default arguments should be provided after non default arguments
- def greet(dept="css",name,sub) is not allowed
def greet(name,subject,dept="CS"):
  print(f"hi {name}")
  print(f"Do you teach {subject}?")
  print(f"Are you from {dept} department?")
greet("Jenny","Python")
hi Jenny
Do you teach Python?
Are you from CS department?


greet("Jenny","Python","ME")  => Overrides the default value of the parameter
hi Jenny
Do you teach Python?
Are you from ME department?
```
```
- Positional argument example

def greet(name,dept):
    print(f"Hi {name}")
    print(f"Are you from {dept} deparment?")

greet(name="Jenny",dept="CSS")
greet(dept='ME',name="jenny")
greet("jenny",dept='CSS')
great(name="jenny","css") => SyntaxError: positional argument follows keyword argument(it should position first and then keyword)


Hi Jenny
Are you from CSS deparment?
Hi jenny
Are you from ME deparment?
Hi jenny
Are you from CSS deparment?
```
```
## Aribitrory/ variable length
- When we dont know how many arguments we should pass use * (the single * is used for positional arguements)
- It will take the arguments as tuple.
```
def add(a,b)
  c=a+b
  print(f"sum is {c}")
add(5,7,9)   => Error:Required two positional arguments and provided three

def add(*a):
    print(a)  => this will print a tuple (5,7,9)
add(5,7,9)

def add(*numbers):
    c = 0
    for i in numbers:
        c += i
    print(f"sum is {c}")

add(1,1,1,1,1,1,1,1,1,)
```





