* First script
```
vi chakra

#!/bin/bash
#Author: Chakra
#Date Created: 08/20/2020
#Description: This script will output "Hello World" on the screen.
#Date modified: 08/20/2020
echo  #this creates empty lines
echo "Hello World"
echo
chmod a+x chakra.sh
./chakra
```

* Second script
```
vi script1

#!/bin/bash
#Author: chakra
#Date: 09/1/2025
#Purpose: Display the output of the commands
echo
echo "This script will run some basic commands"
echo
pwd
echo
ls
echo
whoami
echo
date
echo
cal
echo
touch a b c
echo "End of Script"
```

* Defining variables
```
syntax
variable=value
$variable
for command variable=`value`
echo $variable
p=pwd
l=ls
wi=whoami
d=date
```

* input and output
* Use read command to read the input
```
echo what is you name?
read b
echo
echo hello $b
echo
```
  
