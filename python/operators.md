#Operators
- Arithmetic
- Comparison
- Logical
- Bitwise
- Assignment
- Identity
- Membership

```
Arithmetic

+, - , *, /, %, power => "**"

print(4/2) = 2.0     # alwaya gives in float
print(4//2) = 2      #// is floor divisionand always retrun integer
print(2**3)  8
print(4**2) 16      

Operator precedence 
(),
**,
*,/,//,%
+,-

----> always move let to right
print(5+2*3-1+10/5)           =====> 12
print(5+2*(3-1)+10/5)         =====> 11
```

#Assignment operators

```
a = 5
a is memory location

a = a+2 or a += 2
short hand operators +=,-+,*=,/=,//=,%=.**=
a = a/2
a /= 2
a = a+2
a,b,c = 5,6,7

```
#Comparition operators
```
<>
<=
>=
==
!=
a=5
print(a<5) => false
print(a==5) => true
```

#Logical operators
```
and
or 
not

print(a>4 and b<0)
print(a>4 or b<0)

and - 
f f => f
t f => f
f t => f
t t => t

or - 
t t => t
f t => t
t f => t
f f => f

a = false
print(not(a)) = > true
```

# Identity operator
```
is 
is not

It compares both objects are same or not
memory address is same or not

example 
a =5 
b =5
print( a is b)

memory location is allocated to a=5
for b same memory location is resused a =5 = b

how to test?
check the memory address
print(id(b))
print(id(a))

another example
a = 5
b = '5'
print (a is b)
```

#Membershio operators

```
in
not in 

Check if a char present in a string, list, sequence and so on.

str = 'chakra'
print('a' in str)
print('A' in str)

l = [1,2,4,5,10]
print(10 in l)
```


  







