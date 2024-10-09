Variables are memory buckets to hold infomraion to reuse.
```
name = input("what is your name?")
print(name)
length = len(name)
print(length)
```

#variable naming rules
#A-Z, a-Z, 0-9, _
#name cannot start with number
#should have a meaning full name
#can use camel case

```
age_ = 10
age- = 10 -> #cannot use -
1age = 20  -> # cannot start with numeric
myAge=20
var a = 'hello' # cannot declare datatype
Roll_no = 40
"age" = 60  #cannot use double quotes for variable
```

#Excersice
#Use input function to pass weight in kilograms with type int
#height in meters in float type
#calculare BMI = weight/height**2

weight = int(input("Enter you weight: "))
height = float(input("Enter you height: "))
BMI = weight/height**2)
print(BMI)
print(type(BMI))
print(int(BMI))



