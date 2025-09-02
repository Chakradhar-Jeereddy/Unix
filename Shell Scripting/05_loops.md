## For loop scripts
* The loop keeps running until the specified number of variables.
* eg: variable = 10 then run the script 10 times or
* variable = green, blue, red -> run the script for 3 times
```
Syntax -
#!/bin/bash
for i in 1 2 3 4 5
do
echo "Welcome $i times"
done


#!/bin/bash

for i in eat run jump play
do
echo "Welcome $i times"
done
```

* While loop
```
#!/bin/bash

count=0
num=10
while [ $count -lt 10 ]
do
   echo
   echo $num seconds left to stop this process $1
   echo
   sleep 1

num='expr $num -1`
count='expr $count+1'
done
echo
echo $1 process is stoppped!!!
echo
```
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             
                                                                             b              
