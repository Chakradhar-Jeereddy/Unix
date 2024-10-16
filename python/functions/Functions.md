# Functions in Python
- Funtion is a block of code which does a specific task when it is called.
- Function types 1) builtin and 2) user defined.
- Arugment is actual value that we pass to the funtion
- Parameter holds the value passed to the argument
- Number of arguments should match number of parameters
```
Syntax  -
def function_name(parameters):
  funtion body
  return expresion <optional>
- Call function
function_name()

- With Parameters
def function_name(param1,param2,...)
    a = param1+param2...
    print(a)
```
```
- Examples: Write function to accept two arguments and print
def addition(a,b):
    print(a+b)

addition(1,2) => prints 3
addition(4)  => missing one required positional argument

def great(name):
    print(f"hi {name}")
great('chakra')
great('Nihal')  => prints Hi nihal

```


