* Create script to delete files as specified.
* Create files with older timestamp.
* Find and delete files older than 90 days.
* Find and rename old files.

```
find /path -mtime +10 -exec ls {} \;
{} - Is an empty string means ls what is returned.
find /root/mon/prometheus-3.5.0.linux-amd64.old -mtime +2 -exec mv {} {}.old \;
```
