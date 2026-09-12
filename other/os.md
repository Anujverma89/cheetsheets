# Operating System

>`Free and open Source` - FOSS  (Linux)
>`Propratory` - Windows, mac, unix 

`Shell` - Both CLI and Langugage.
`Pipes |` - To combine Multiple cmds and create complex workflow for OS.


### Three UNIX like system :
```
i) That uses source code from bell labs i.e BSD
ii) Branded and Trademarked unix system like HP-UX, IBM-AIX
iii) Functional UNIX like systems 

```

> LINUX Doesn't used the source code of UNIX.   
> UNIX IS NOT OPEN SOURCE.  
> LINUX IS MODULAR OS LIKE OS i.e you can use one component in contrast with other.


### Linux family systems :
```
Red Hat family system(RED HAT ENTERPRISE LINUX) --> fedora --> (Centos,oracle linux)   
Suse family system (openSUSE)  
Debian Family System  

```


### Parts of OS 
```
CONSOLE
i) Desktop Environment
ii) Window manager
iii) X Window -- Tool kit and protocol to built GUI.

CONSOLE :
i) Shell
ii) Kernel
iii) Hardware 

```

`Shell scripting is also a part of programing`


```
Architectures :
i) ARM-64
ii) x86-64
iii) ARM(Advanced Risk Machine)
iv) x86(Cisc)
v)

NOTE : Machine code of x86 won't run on ARM-64 because they support different instruction set.

```

>C headres files are included in usr/include   
>java libraries are places in usr/lib/jvm


### Ubuntu folder architecture : 
* /bin : Contains system level binary files that can be executed by running that command on terminal for all users
* /etc : hold configuation files like hostnames, networks etc
        : NOTE : Configuration realted all files are stored in /etc 
* /home : stores different user's data

* /root : Home directory for root user contains files related to root user
* /usr : used to store user related data
* /var : In Linux, /var is a standard directory that stores variable data, meaning files that change size or content during the system's operation
* /sbin : Binary executables for root user 
* /lib.usr-is-merged : A folder which says all the the system binaries and user binaries are merged together.
* /libexec : binary executables that are not intented to be executed standalone and are used by other for some functionality.
* /local : For packages and other stuff that are not part of standard system.
* /src : A repository used to store source code that are part of core system and are built on system.
* /share : Containsa the data and resources which can be shared accross multiple platform independent of hardware.
* /lib : Contains essential shared libraries and modules needed to run command. Shared libraries are code that multiple programs can use without needing to make separate copy.
* /media : Media folder is used to store media like images, videos, songs 
* /cdrom : mount point for CD/DVD
* /mnt : A folder where the temporary filesystems mount like pen drive or other stuff

* /sys : In Linux, /sys is a virtual file system (also known as sysfs) that provides access to information about the kernel, devices, and their drivers. 
* /run : This folder contains the information about the current runtime or the current boot. IT's a virutal filesystem
* /proc : List of all the processes running in a system it is runtime directory or a virtual file system 
* /dev  : Virtual files system in Linux, /dev is a virtual filesystem that provides access to hardware devices and other kernel resources
* tmp : In Linux, /tmp is a directory used as a temporary storage location for files that programs and the operating system use during their operation
* /opt : is used to install additional softwares that are not part of core operating system
