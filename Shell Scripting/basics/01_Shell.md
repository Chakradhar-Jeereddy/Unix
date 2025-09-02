* Kernel: Interface between hardware and software. Stored inside operating system, always running and takes command from SHELL.
* Kernel talks to hardware (CPU,Memoery and HD). SHELL + Kernel = Operating System.

* SHELL: Command line interface between users and kernel/OS.
  ```
echo $0
Available  shells "cat /etc/shells"
Your Shell? /etc/passwd
```

* Shell scripting: Put all shell commands in a file and run it.
* Types of shells
  * Gnome - graphical interface.
  * KDE - graphical interface.
  * Command line shells
   1. sh: born shell
   2. bash: born again shell
   3. csh & tcsh
   4. ksh
   5. ksh: korn shell(developed by david korn), compatible with sh and bash. Most of the time this shell is used in solaris.

* Starting a shell
  * Simply type the shell type
  * Type exit to go back to previous shell.

* Absolute path and relative path
  -> /u01/opt/scripts/delete.sh  # aboslute path
  -> cd /u01/opt/scripts  ./delete.sh  # relative path
  -> "." we inform OS we are running script from current directory.



   
  
