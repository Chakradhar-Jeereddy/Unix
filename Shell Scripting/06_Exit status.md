0 = OK or successful
1 = Minor problem
2 = Serious trouble
3-255 = Everything else

```
ls -l
echo $?
pwd
echo $?
pwdd
echo $?

#!/bin/bash
echo hello
echo $?

Return exist status if file exists
#!/bin/bash
ls -l /home/iafzal/check
if [ $? -eg 0 ]
then
echo file exist
else
echo File does not exist
fi
```





