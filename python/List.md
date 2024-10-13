- List(memory structure) is collection of elements saparated by comma and of similar or different data types
- List sized dynamically,no fixed size and is mutable after its creation
- It stores elements in sequence and we can update, remove or add new elements to existing list
- To store names of 100 strudents, we can use list and no need to declaring 100 varibles.
- Elements in list are ordered and the index starts with 0 and duplicates are allowed
- Not all funtions of list return object, the just perform the operation on same object
```
# list of integers
a = [1,2,3,4,5,10]
# list of strings
b = ['hello','bolo','chalo']
# extract elemnets using index
print(a[1])

# list of integers
from audioop import reverse

num = [1,2,3,4,-5,6,7,-10]
#print(num)
#list of strings
st = ['hello','how','are','you']
#print(st)
#list of mixed types
l_mix = [1,2,-3,'mine',10]
#print(l_mix)
#find length
print(len(num))
print(len(st))
#find max and min
print(min(num))
print(max(st))

#list slicing using index
#syntax for index slicing starts with zero and ends with length [<index>,<len>]
#syntax for index extended slicing includes step  [<index>,<len>,<step>]
print(st[1])
print(num[1:7])
score = [1,2,3,4,-19,-25,12,42,10,-19]
print(score[1:7:2])
#sorting list, need to sort first and then print
score.sort()
print(score)
num1 = sorted(score)
print(num1)
#use reverse
score.reverse()
print(score)

#sorting on mixed list is not allowed
#l_mix.sort()
#print(l_mix)

#add element at the end
score.append(80)
print(score)

#add element at specific index
score.insert(5,900)
print(score)

#add multiple elements
score.extend([999,758,666])
print(score)

#update or replace a value
score[5]=800
print(score)
score[0:4]=[654,677,1222]
print(score)

#remove the element
#list.remove(<element>)
score.remove(1222)
print(score)

#pop to remove the last element and returns the element that was removed.
print(score.pop())
print(score)

#Use pop to remove perticular element
score.pop(5)
print(score)

#find number of element occurrance
print(score.count(-19))

#clear the list
score.clear()
print(score)
```
