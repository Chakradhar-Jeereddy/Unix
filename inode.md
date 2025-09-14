## Inode
It holds the metadata of a file and directory.

```
$stat dnf.librepo.log
  File: dnf.librepo.log
  Size: 13200           Blocks: 32         IO Block: 4096   regular file
Device: fd05h/64773d    Inode: 133         Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2024-02-22 19:37:21.023729196 +0000
Modify: 2025-09-14 08:31:52.021798503 +0000
Change: 2025-09-14 08:31:52.021798503 +0000
 Birth: 2024-02-22 19:37:21.023729196 +0000
```

- It contains information of file
- File type, permissions, owner, size, create/update timestamp, data pointer location.

## Softlink/symlink
- Its a shortcut to actual file
- Symlink will have different inode as its different file.
- Inodes are different for symlink and actual file.
- deleting actual file will not delete symlink, but it will break the file.

## Hardlink:
- When you copy same will at different location with different name.
- It points to same inode and point to same data.
- Data is only removed when all copies are removed (called hard link)

## Softlink
 ln -s dnf.log /home/ec2-user/dnf.log

stat dnf.log
  File: dnf.log
  Size: 34044           Blocks: 72         IO Block: 4096   regular file
Device: fd05h/64773d    Inode: 132         Links: 1
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2024-02-22 19:37:21.023729196 +0000
Modify: 2025-09-14 08:31:52.211798675 +0000
Change: 2025-09-14 08:31:52.211798675 +0000
 Birth: 2024-02-22 19:37:21.023729196 +0000


stat /home/ec2-user/dnf.log
  File: /home/ec2-user/dnf.log -> dnf.log
  Size: 7               Blocks: 0          IO Block: 4096   symbolic link
Device: fd02h/64770d    Inode: 524420      Links: 1
Access: (0777/lrwxrwxrwx)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2025-09-14 08:57:43.594342647 +0000
Modify: 2025-09-14 08:57:43.594342647 +0000
Change: 2025-09-14 08:57:43.594342647 +0000
 Birth: 2025-09-14 08:57:43.594342647 +0000



## Hardlink
[ root@ip-172-31-23-1 /var/log ]# ln dnf.log dnf1.log

52.90.222.151 | 172.31.23.1 | t3.micro | null
[ root@ip-172-31-23-1 /var/log ]# stat dnf.log
  File: dnf.log
  Size: 34044           Blocks: 72         IO Block: 4096   regular file
Device: fd05h/64773d    Inode: 132         Links: 2
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2025-09-14 08:58:52.216433898 +0000
Modify: 2025-09-14 08:31:52.211798675 +0000
Change: 2025-09-14 09:05:51.458925247 +0000
 Birth: 2024-02-22 19:37:21.023729196 +0000

52.90.222.151 | 172.31.23.1 | t3.micro | null
[ root@ip-172-31-23-1 /var/log ]# stat dnf1.log
  File: dnf1.log
  Size: 34044           Blocks: 72         IO Block: 4096   regular file
Device: fd05h/64773d    Inode: 132         Links: 2
Access: (0644/-rw-r--r--)  Uid: (    0/    root)   Gid: (    0/    root)
Access: 2025-09-14 08:58:52.216433898 +0000
Modify: 2025-09-14 08:31:52.211798675 +0000
Change: 2025-09-14 09:05:51.458925247 +0000
 Birth: 2024-02-22 19:37:21.023729196 +0000

52.90.222.151 | 172.31.23.1 | t3.micro | null
[ root@ip-172-31-23-1 /var/log ]#






- 
