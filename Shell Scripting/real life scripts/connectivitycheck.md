* Check remote server connectivity(ping)
```
#!/bin/bash

ping -c1 8.8.8.0 &> /dev/null
        if [ $? -eq 0 ]; then echo IP is reachable; else echo IP is not reachable; fi
```
* Define variables
```
#!/bin/bash

host=8.8.8.8
ping -c1 $host &> /dev/null
if [ $? -eq 0 ]; then echo IP is reachable; else echo IP is not reachable; fi
```

* Multiple hosts
```
#!/bin/bash

list=/root/list
for i in $(cat $list); do ping -c1 $i &> /dev/null; if [ $? -eq 0 ]; then echo IP is reachable; else echo IP is not reachable; fi; done
```
