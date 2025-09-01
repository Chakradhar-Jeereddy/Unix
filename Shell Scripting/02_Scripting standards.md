* Scripting naming convention.
   * Script name should match its purpose.
   * Use .shell type extension when using multiple shells. Example (helloworld.bash)
   * All scripts to be executed should have proper executable file permissions. => rwxr-xr-x (chmod a+x script-name)
      - a means everyone.
   * In linux by default you will not have executable permissions.
 
  * Script format
     1. Define shell (#!/bin/bash)
     2. Define comments (# comments)
     3. Define variables (eg name=Imran)
     4. Commands (echo, cp,grep,etc)
     5. Statements (if, while, for etc.)
  ```
  Format like this

#!/bin/bash
#Purpose: Testing script format
#Date: 08/20/2024
#Modification: 09/1/2025
#Inspect the script

a='my name is chakea'
echo $a
date
df -h
        if { $a -eq file }
        then echo $a
        else
        echo "hello"
        fi
```




