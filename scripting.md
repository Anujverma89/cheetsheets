#! /usr/bin/bash
# the above line is sha-bang or hashbang used to tell the location of the bash (interpreter) 
# use whereis bash to know location of bash
# only # is used to write comment

echo "this is echo(print) command to print on screen" #comment goes here

# there are two type of variables 
#  System written in upper case
#  User defined written in lower case


# system defined variable $BASH
echo $BASH
echo $HOME
echo $PWD
echo $BASH_VERSION

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



# array variable 
# array outof bound doesnot givess error
echo enter array 
read -a arr
echo  ${arr[0]} ${arr[1]}

# default variable is $REPLY

read 
echo This is REPLAY variable value $REPLY


#passing arguments 
#arguments in script are saved in number like 1 2 3 

echo $0 $1 $2 $3

# this variables holds all the arguments passed except name
echo "$@"

# this variables holds no of arguments 
echo $#

# all the arguments as string
echo $*



# ifelse scripting is here 

if [ $1=="arg1" ]
then
	echo "YES $1"
else
	echo NO
fi




