# range(start,stop,step_interval)
- Start from zero by default
- stop is mandatory parameter
- step is optional and default interval is 1

```
  for i in range(2,6,3):
    print(i)
a = range(6)
print(a[4], end=' ')
```
```
# print numbers from 1 to 10
#fizzbuzz program
#if number divisible by 3,5 print fizz, buzz
#if number divisible by 3 and 5 print fizzbuzz

for n in range(1,101):
    if n%3==0 and n%5==0:
        print('fizzbuzz')
    elif n%3==0:
        print('buzz')
    elif n%6==0:
        print('fuzz')
    else:
        print(n)
```
