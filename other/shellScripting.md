# Bash Shell Scripting
### Bourne Again Shell

### There are different types of shell 
* Bourne shell (sh) 
* Bash shell (Bourne Again shell)
* Korn shell (ksh)
* C shell (csh & tcsh)
* Z shell (zsh) used in unix 

#### Bash : Bash is an command line interpreter or shell for GNU operating system. 
#### Shell : In general shell is a interpreter and a language that is used to talk with operating system.


#### Posix : Family of open system standards based on unix.

### Commands : 
* cat /etc/shells : gives output of all shells supported by os 
* whereis bash : location where bash is located 

#### Shell file extension ends with .sh eg: filename.sh
* index.sh


#### Permissions on a file 
* Read -r
* Write -w
* Executre -x 

#### When you create a file first using touch it has write and read permission we have to change it to executre by running command 
* chmod +x filename.sh


##### if else 
```sh
    if [ $1 == "arg" ]
    then
        echo $1
    fi
```

##### arrary
```sh
    echo enter array 
    read -a arr
    echo  ${arr[0]} ${arr[1]}
```
#### command line arguments
```sh
    #passing arguments 
    #arguments in script are saved in number like 1 2 3 
    echo $0 $1 $2 $3
    # this variables holds all the arguments passed except name
    echo "$@"
    # this variables holds no of arguments 
    echo $#
    # all the arguments as string
    echo $*
```

#### System variables
```sh
    # system defined variable $BASH are all upper case
    echo $BASH
    echo $HOME
    echo $PWD
    echo $BASH_VERSION

```


#### User defined variables 
```sh
    # user defined variable 

    name=Anuj
    echo My Name is $name

    #taking input

    echo Enter your name
    read anothername
    echo Another name is $anothername


    # multiple inputs 
    echo Enter multiple name:
    read name1 name2 name3
    echo $name1 , $name2 , $name3


    # reading input and output in same line with password 

    read -p "Enter username : " u_name
    read -sp "Enter password : " pass
    echo 
    echo $u_name $pass


    # in the above line we have the command we have flag 
    # -p to read in same prompt 
    # -sp to read in silent or secure prompt

```

#### Comaprision 
```sh
    [ "$a" = "$b" ]   # True if strings are equal.
    [ "$a" != "$b" ]  # True if strings are not equal.
    [ -z "$a" ]       # True if string is empty.
    [ -n "$a" ]       # True if string is not empty.

    [ "$a" -eq "$b" ]   # True if integers are equal.
    [ "$a" -ne "$b" ]   # True if integers are not equal.
    [ "$a" -lt "$b" ]   # True if a is less than b.
    [ "$a" -le "$b" ]   # True if a is less than or equal to b.
    [ "$a" -gt "$b" ]   # True if a is greater than b.
    [ "$a" -ge "$b" ]   # True if a is greater than or equal to b.


    [ -e "$file" ]     # True if file exists.
    [ -f "$file" ]     # True if file is a regular file.
    [ -d "$directory" ] # True if directory exists.
    [ -r "$file" ]     # True if file is readable.
    [ -w "$file" ]     # True if file is writable.
    [ -x "$file" ]     # True if file is executable.

    [ "$a" -a "$b" ]   # AND: True if both conditions are true.
    [ "$a" -o "$b" ]   # OR: True if either condition is true.

```

# Note 
* When we write a script file .sh we have to use shebang or hashbang as the first command to tell which interpreter to use else it will use default one.
* There should be no blank space while declaring variable `eg. name=right` is correct `name = wrong`
* single equal works for equality `a=b evaluates to True`