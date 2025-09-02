* If statements
```
syntax
if [ condition ] ; then command; fi

#!/bin/bash
count=100
if [ $count -eq 100 ]
then
  echo Count is 100
else
  echo Count is not 100
fi

or

if [ $count -eq 100 ]; then echo Count is 100; else echo count is not 100; fi
```

* Check if file exists
```
syntax 
use -e to check if file exists, it returns true when there is file.
#!/bin/bash
clear
if [ -e /home/chakra.txt ]; then echo file exists; else echo file does not exists; fi
```

* case statement
```
#!/bin/bash

NOW=$(date +"%a")
case $NOW in
        Mon)
                echo "Full backup";;
        Tue|Wed|Thu|Fri)
                echo "Partial backup";;
        Sat|Sun)
                echo "No backup";;
        *) ;;
esac
```
```

#!/bin/bash

This is the shebang. It tells the system to run this script with the Bash shell.

NOW=$(date +"%a")

date +"%a" returns the current day of the week in short form (e.g., Mon, Tue, Wed).

The result is stored in the variable NOW.

Example:

date +"%a"
# Output: Mon


case $NOW in ... esac

This is a case statement in Bash, similar to a switch-case in other languages.

It checks the value of $NOW and runs the matching block.

Cases defined:

Mon) → prints "Full backup"

Tue|Wed|Thu|Fri) → matches any of these days → prints "Partial backup"

Sat|Sun) → weekend → prints "No backup"

*) → default (catch-all) → does nothing here

;; -> Marks the end of each case block.

If today is Monday:

Full backup

If today is Thursday:

Partial backup


If today is Sunday:

No backup
```

