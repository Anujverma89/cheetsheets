# PYTHON 

### Basics 
```py
#python is interpreted langugage
#python is both interpreted and compiled language. 
#Regular python is also called as cpython and cpython is an interpreter and also a compiler.
#python files are compiled into bytecode when they are imported are executed i.e modules are compiled and stored as .pyc file
#Python code can be both compiled and interpreted but wheather it is compiled or interpreted depends on the interpreter.
#It is both scripting and general purpose programming language.
#Scripting language differ from Programming language in its operating sense
#Python interpretor can be an executable or a set of libraries linked with eachother depending upon how you use it.
#python programme is nothing but a text file.
#python execution (python programes --> interpreter(Bytecode --> PVM))
#Byte code is platform independent whereas machine code is platform dependent, in python it is saved as .pyc in same directory where your souce code exists.
#It is simply for speed optimization  and speed startup time, if python has no write access in your machine it simply generates the byte code in memeory and discards when programme execution exits.
#Byte code is fast enough to run than source code and slower than machine code(0,1). 
#.pyc (byte code) can be shipped as you want.
#PVM is a run time engine of a python.
#PVM is loop which iterates through byte code.
#Since python generates byte code it is faster then traditional interpreted language.
#In compiled language once the programe is compiled we don't require language support to run the system but in python we need python interpretor while running the programme
#implemenation of python cpython , jpython, ironpython, cython.
#psycho jit compiler
#Shedskin c++ translator 
#frozen binaries (py2exe, pyinstaller, freeze)
#The speed of forzen binaries are same as the source byte code becuase they are not executable but they are bundled together with byte code and the pvm.
#Frozen binaries are not same as output of true compiler since they are bytecode + PVM packed together.
#In cython , jpython or ironpython the code is compiled down to the language dependent byte code or binary code then it is executed by the correcponding or interpreter.
#Compiled code doesnot required interpreter to execute the programme.
#Cython is a implementation in which python can access the c apis and libraries then can be completely compiled into the bytecode.
#While importing it runs all the content in the file with differ 


#Running python programme :
"""
1)Interactive prompt
2)python programme file (text file) 
3)Linux based file execution method(Unix executables scripts) 
    create a file with executable previleges : chmod +x filename
    #! python path : /home/anuj/anaconda3/bin/python
    python commands 
    runs : ./filename

4)Clicking on file icon
5)exec(open("FIlename.py).read()) function to load the file
6)importing a module also runs the code the way they are imported
7)Forzen binaries 
8)Embeded calls from one to another file.
9)python IDLE (INtegerated , development and learnning environment)

Note : its always a good idea to run python file using command line approach
    python filename.py

"""



"""
Scripting language is Interpreted.
Used for automation , manuplation of existing entities, Testing etc.

General purpose programming languages are more compiled.
They are used for development.


Python codes can be compiled directly into c binary code using interpreter for incresing efficiency.
As well as it is interpreted in nature also. 

python can be used for both development and scripting roles 
"""

"""
For python programmes componenets written in python and c are same so c can be used for which requires efficeincy and then it can be compiled
else can be interpreted with python.

python programme can also be saved in .txt file formaat because python files are nothing but a text files

"""
import pandas as pd
import redirectinputoutput

print("HEy")
print(pd)

print(dir(redirectinputoutput)) #this prints other 

"""
Python interpreter 

1)Python source code is compiled to byte code with extension .pyc
2)Then Byte code is interpreted by Python Virtual Machine (PVM) runs byte code line by line.
PVC is a runtime engine of python.
Note : PYC is only generated only for imports and not for TOP level files or programes and interactive shell.
It is saved in ram and destroyed after code is finished running.

byte code instruction & CPU instruction

its speed is between traditional interpreted and traditional compiled langugage
there is no compilation phase in python there is direct execution phase and all linking and loading is done in same phase

Cpython c & c++
Jpython --java framework
Ironpython -- .net framework

There are the version that can be run on top of other technologies as c & java with python code.

Psyco jit compiler : Compiles the byte code into machine code and replaces the byte code with that part of machine code. Bascially does with the datatypes used in Language.
shedskin c++ translator : Translates python into C++ langugage and then it is compiled by C++ compiler 


shipping executables of python can be done thorugh forzen binaries.
py2exe for windows : pvm + bytecode = forzen binary(.exe file)
pyinstaller for linux : 


cython and cpython are different 
jython and jpython are same 

"""

#PYthon programs are combination of object, modules, statements and expression.
#big picture : programmes ->(Decomposed)->Modules->(Decomposed)->Statements ->(Decomposed)->Expressoins(create and operate on)->Object 
"""
BIG PICTURE : 
Programme 
    Modules 
        Statements
            Expressoins
                Objects 
"""

#PYthon is completely object object oriented 
#Every thing in python is object even built in data types.
#Modules, numbers, strings every thing is object in python
#contant means literal in python and doesn't means const like in c and cpp
#Language provides syntax : we use syntax to create expression : Those expression generates object : which is also called as literal
#Syntax : RULE TO DEFINE A EXPRESSION AND STATEMENT


#note : 
"""
    In Python variables are only created when they are assigned values else they are not created
"""

a=None
b = 14
# variables can be assigned new literals 
b = 12


#dynamic type interlude 
#in python type is not associated with variable but is associated with literal and values assigned to it 
#Variables always link to objects and never to other variables, but larger objects may link to other objects (for instance, a list object has links to the objects it contains).

#object is a piece of allocated memory and variable is a pointer to that memeory 
#each time you generate a new value in a python a oject is created and varialbe is pointed to that 
#when reference is removed the grabage is collected i.e. occupied mememory is removed
#sometimes caching is done and value is not changed but reutilized 


#objects have 
    #type designator 
    #refernce counter : garbage collection is based on reference counter
        #when the objects pointer is reduced to zero i's space is automatically collected by the interpreter and saved in free space pool i.e reference counter is zero
    #there is also a cyclic refrencing in pyhthon we will see later
    #when variables are used in an expression they are replaced by the objects and operations are perfomed on operations 
    #shared reference also exits in python :
        #multiple variable refrencing to the same object is called shared refrencing 
    
#there may be someobjects which make inplace changes rather than making a completely new object
#if objects are mutable and and multiple variable are refrencing to the same object then change in a object will relfect in all the reference variables


#is and ==
#is checks for the same object 
#== checks for the same value



#pypi.org for different packages and libraries related to python pypi = (python package index) 




## Compilation and error generation
# In compiled language error are generated and reported at once 
# in interpreted language errors are generated and reported line by line and one line at a time at runtime.
# in compiled lanuage errors are reported once while compiling or converting it into the byte code like in java.

"""
Compilation steps in c language 
preprocessing
lexical analysis
syntactic analysis
semantic analysis
linking
The fact that error messages are generated by different stages of the compiler, 

compilation and interpretition step in python and java
    1)Preprocessingand linking are avoided in python and java.


stages in pythonc compilation 
2) scanning
1) parsing

we can compile python code using : 
python3 -m compileall 


"""


"""
Built in data types : 
    Number
    String
    List 
    Tuples
    Dict 
    sets
    bool
"""


"""
exec() funcstion executes the string code in python 
eval() function exuectes the expression in python 

"""
```


### Input and output Redirection 
```py
print("This is anuj's code")
x=None
input(x)
print(x)
#input and output can be redirect to a file rather then a normal console input and output
#output python filename.py > outputfile
#input python filename.py < inputfile
#this is taken from c itself. C also has this inbuilt feature.
```


### Data types 
```py
import sys


print(sys.argv)
for p in sys.argv[1:]:
    print(p)


# printing the argvalue that is given to execute the programme as an input
# line.rstrip is used for proper cleanup and other tasks


# everything in a python is object 
# lets decompose 
"""
    Programmes : Multiple modules together
        Modules : multiple statements (Namespace)
            Statements : multiple expressoins
                expressions : combination of values, variabes and operations

    literals : Consants 

    __something__ = magic method or an attribute.
    use dir()
    use help)()  for documentation


"""
#these are core datatypes 
number = 14
str = "This is string"
list = [1,2,4,[124]] #list and tuouples are same but tupes are immutable so invented
dict = {"a":"b"}
tupe=(1,3,5,5)
sets = {1,2,4,5} #unordered collection os something
files = open("new.txt",'a+')
bool = False
no = None

string = "THis is new string"
string = "a" + string[2:]
print(string)

def func():
    print(1)

# print(dir(func.__str__))
print(help(func.__str__))
```

### DICT
```py
dict = {}
dict["name"]="anuj"
dict["age"] = 22
dict["city"] = "kolhapur"



# iterating dictonery
for d in dict.keys():
    print(dict[d])
```

### FIle
```py
file = open("newfile.txt","a+")
file.write("THis is new created file\n")
file.close()

print(dir(file))
```

### List 
```py
l = [1,2,5]
l.append(0) #add items at end i.e exapand the list
l.pop(0) #delete item by index
l.remove(2) #deltes item by value
l.insert(99,11) #Inserts value at aribitrary (position, value)
print(l)

#list comprehensions are also one of the important tasks in python
lis = [1,2,5,6,7,8,8]

# filters out the even numbers from above lis and creates a new list 
newl = [x for x in lis if x%2==0]
print(newl)


# list slicing with
od = [1,2,4,5,5,6,7,8,8,10,12,14,16]
# 1st is start index included
# second is end index excluded file = open("newfile.txt","a+")
file.write("THis is new created file\n")
file.close()

print(dir(file))

# last is the skin if positive skips left to right
# if negative started from right to left
# list[i:j:k]
sli = od[::-1]
print(sli)


# new operators ellipsis 
li = [...]
dic ={...}

print(li,dic)

#operator presedence 
#first with higher precidence
#if same precidence order they move from left to right
#only comparision and exponent moves from right to left 
#you can override precidence rule using parenthesis 
#python automatically converts the objects to the higher and comples types like int to float. only applied to numeric type

```

### Numbers 
```py
#numbers in python are objects 
"""
        types of nos 
            deciaml = 10
            hex = 0X1234
            binary = 0b101001
            octal = 0o1234214 
"""

#other number types 
#Integers and floating-point numbers
#sets 
#fractions / #Rational fraction numbers
#Unlimited integer precision 
#Fixed-precision decimal numbers = fixed precision floating numbebers /Decimala
#Complex no 

#you will have to import modules to work with this kind of data types.
#in python floating point numbers are implemented as c double 
#Some of the operators like assignment operators and comparison operators do not have any associativity order in python, 

import math
import decimal as decimal
import fractions as frac

#in python two there were int and long in python3 only long but as a int
dec = 10 #in python 3.0 integer is always a large int of greater precision and its called as int not long
float1 = 2.5 #double like in c 
hexa = 0x124124
octal = 0o1243124
binary = 0b101010
print(bin(dec)) #converts the value interger to binary 
print(hex(dec)) #converts into hex
print(oct(binary)) #converts into ocatl number system
print(dec,hexa,octal,binary)

#converts string to int 
strin = "124124"
conv = int(strin,dec)
print(type(conv))
print(int(strin,dec))


#complex no 
comp = 12 +15j



#working with floats 
print(float1.as_integer_ratio()) #represents the integer as a fraction part 


#operators 
#normal division 
#normal division always returns the float value
a = 6/2

#floor division
#floor dvision always returns the integer value if the operands are integer else returns float
b=5//2.0

print(type(b), type(a))
print(a,b)
    

# repr and str both of them produces string
n=str(42/2)
print(type(n))


# other operators in python 
#math.floor()
#math.trunc()

print(math.floor(45.0/7.0))
print(math.trunc(45.0/7.0))


#decimals points 
# decimal are used for precision and human readable format
print(0.1+0.4+0.11)
print(decimal.Decimal('0.1')+decimal.Decimal('.4')+decimal.Decimal('.11'))



# fractions 
#working with fractions using fractoins
print(frac.Fraction(.25))
```


### Sets 
```py
# sets are immutable in python 
# regular mathematical operations can be called upon sets 
#empty set = set()
#empty dict = {}
#sets are collection os unique and immutable elements
import sys

empty = set()
seta = {1,3,4,5}
setb = {1,5,9,10}
print(seta | setb) #unions
print(seta & setb) #intersection
print(seta -setb) #substartion

#set comprehension can also be called 
setc = {x for x in seta if x==1}
print(setc)
print(type(setc))


# types cecking
print(type(setc) == set)
print(isinstance(setc,set))
print(type(setc) == type(set()))
print(empty)

# iterating sets

for x in seta:
    print(x)

setq = {1,2,4,5,5}
setc = setq #here pointing to the same object
setc = {x for x in setq} #creaing a copy of object i.e different object 
print(hex(id(setc)), hex(id(setq)))

# pointing to the same object here we are checking for caching mechanism and reuse 
a =13
a = 13
b= 13
v= None
print(a is b)
print(sys.getrefcount(v))
```

### String
```py
# sets are immutable in python 
# regular mathematical operations can be called upon sets 
#empty set = set()
#empty dict = {}
#sets are collection os unique and immutable elements
import sys

empty = set()
seta = {1,3,4,5}
setb = {1,5,9,10}
print(seta | setb) #unions
print(seta & setb) #intersection
print(seta -setb) #substartion

#set comprehension can also be called 
setc = {x for x in seta if x==1}
print(setc)
print(type(setc))


# types cecking
print(type(setc) == set)
print(isinstance(setc,set))
print(type(setc) == type(set()))
print(empty)

# iterating sets

for x in seta:
    print(x)

setq = {1,2,4,5,5}
setc = setq #here pointing to the same object
setc = {x for x in setq} #creaing a copy of object i.e different object 
print(hex(id(setc)), hex(id(setq)))

# pointing to the same object here we are checking for caching mechanism and reuse 
a =13
a = 13
b= 13
v= None
print(a is b)
print(sys.getrefcount(v))
```

### Control structure  
### Looping structure

### Modules 
```py
#Module is also an object in python. It's a package of names which self contains names and avoids name clashes
#All the names defined in a module becomes and attribute of an module when it is imported
#Module can be a python programe file or a extension coded in c and java or cpp or any other language


# Uses 
# code reusability 
# namespace partition
    # Names defined in different modules are names in that file scope which doesnot conflicts with other.
    # 
# 



# importing and working 
# when first time module is loaded in any module. Interpreter execute every piece of code of a module(creates object) and places it in sys.module
# Now in susequest import the module is imported from sys.module without reloading the module
# lets demonstrate it


#Programe : 
    # Top level file or script file --> Launch the application
    # Module files : contains the component required by top level files

import sys


for a in sys.modules:
    print(a)
print(" -------------------------------- ")
import modulea
print("---------------------------------")
for a in sys.modules:
    print(a)

print("_____________________________Loading Finished___________________________________")
#now since the modules is already present in sys.module this below import will not work .
import modulea
# here we are appending the path in sys.path from where it will search for module
# since there is no path and .py extension we have to use this to run
# here we are appending the root directory path to the sys.module or module search path 
sys.path.append("/home/anuj/Desktop/DSA/python")
import external
# from datahiding import *
import datahiding
import importlib
# import compiledgcc see this later

print(sys.path)

#here we can print all the namescopes of the python
print(modulea.__dict__.keys())
print(dir(modulea))


# print(three)
# print(two)
print(datahiding._not)
# this is way to relaod a file in python
importlib.reload(external)
print(external.changeed)
external.changeed = 110
print(external.changeed)



#absolute imports 
print(sys.path)
from functions.basic import *
#this is an absolute path because the parent directory is python which is in sys.path module
# Absoulte path are the full path from the root directory to the module
from mod.modulea import chela
print(chela)

print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
# we can work with commandline argument using sys.argv argv = argument value it a list of values provided while running a code
print(sys.argv)
# from ..mod import f2
# newfunc()
#it is always recommended to use the absolute import in large project or code .


# relative import i.e. navigate from current path
# location of the file with respect to current file
# relative import doesnot works on main script 
# . single dot means current package , .. means parents package and ... means above that
# they only work in proper package 
# when you run main script it is not considered as a part of package and hence realtive import doesnot work with main script
# from .  import modulea
# print(modulea.nowayback)
from mod import f1




# here each dot represents the directory 

# Note
# import filename here filename name becomes a variable in sys.module and gives interpreter the knowledge what to import
# standard library is the collection of modules provided by python language for different task.
# in c when we import modules it just simple copies the code of a module and places it in a source file.
# but in python when we import module 
    #1) First it is searched 
    #2) Second it is compiled into the byte code i.e pyc which is sotred in pycache of a python and in a sys module
    #3) It creates a python object which are defined in python file i.e the byte code is executed line by line

# there is a module search path
# programme can be shipped both as module and top level file and we can use __name__ attribute of a module to work around
# interprter trys to bypass the compile process as far as possible to speed up programme
# if the timestamp of byte code is older than that of source code it is compiled else the compilation process is avoided.
# compilation is generally done for python modules.
# def statement defines the function object for later use.



# Module search path : it is defined of these four parts 
    # 1) home directory : where your top level i.e. main script resides
    # 2) PYTHONPATH directories : user defined and platform specific name of directories 
    # 3) standard library modules : where all standard modules of libraries resides 
    # 4) .pth (a file with .pth extension listing all the directories which will be used for import)
            #all the paths added here will be listen in python path appending from last.
            # you just create .pth file and store it in site-packages to extend the search path 
            # this is only required when you are importing the file which is not present in home directory

# sys.path is the attribute that holds the different modules of the programme
    #sys.path holds all the paths that python will search for the module.
    # we can always append it
    # sys.path merges the home directory by default i.e the directory which contains the entory point of the programe
    # merges the PYTHONPATH
    # merges the content of .pth file
    # PYTHONPATH and .pth files are more presided way of chaning moduel search path


# we can also import the compiled modules written in c just by typing its name.
# module.attr fetches all the attributes present in the module

# python intentionally omits the extension becuase it gives previlige to import anything that is named with modulename not just python file
# it can be c byte code or java byte code or anything else
# if two modules are named same python will pick the first module which is found while searching from left to right so name them distinctly
# Python also supports the notion of .pyo optimized byte code files, created and run with the -O Python command-line flag;
# while using import python automatically imports the content of the zip file without extracting it
# python import statement can support files like .py, .pyc., c extensions, java extensions, zip file, .net extensions
# the modules written in othe rlanguage are called extensions
# when we import module with file name it imports a filename and also and that filename servers as an variable.


# from . import statement ;
# imports the specifc part of module and writes in the main file scope.
# since now attribute is availble in the current namespace it can be used without module name
# from . import something creates a copy of the attribute in the current file.
# wheres the import moudle statment cretes object and they remain in it's own file scope no copy is made.
# first from works same as import just extra work it does it it adds the copy to the current importing file.
#global scope is limited to file they are defined in.


# encapsulation : private, public, default, protected
# polymorphism : method overloading, overriding
# abstration : abstract classes and modules
# inheritance : inheriting classes


# qualification means a file name with an object name.
# when we use qualification it directly searches the object for a given attribute
# Qualification is really an expression that returns the value assigned to an attribute name associated with an object.
#A variable’s meaning is always determined by the locations of assignments in your source code, and attributes are always requested of an object explicitly.



# PACKAGES : 
    # Directory of python codes is called packages.
    # there should be an __init__.py present in the package to make python treat dictionary as a python package
    # you can define __all__ in init.py to help import list of package using command 
    # from package import *
    # each package listen in import path must contain __init__.py file


# Scopes and Namespaces are different:
    # scopes is a region where certain indentifier's are visible 
    # Namespace is a container to which certain variable belongs to 


# import creates an object of a module and provides a link to another module importing it 
    #changing attributes using import will affect the real attributes of the file.
# from create a copy of an object in importing file but doesn't provide link to the object 
    #changing attributes using from won't affect the real attributes of the file.
    # there is no link between the module object and the attrubute copied in imported file

# reload doesnot work with from statement becuase of copy it makes 
# we can access the attributes of an module object using qualification or indexing the dictonary of all attributes of module object
# attr is an attribute that yeild the string at runtime.
# sys.module contains all the loaded modules.
# metaprogrammes are the programmes that manages the other programme.
# every module has attribute __name__ that allows to check if file runs as a module or a script
# we can also work with command line argument in python. using argv
# behind the scene *argv is a arbitrary argument that can hold as many no of arguments 

#import filename
#from filename import attribute
#In general terms a file is a object and had many objects associated with it which we can fetch using dot operator.
#import gets module while, from gets copy of file's name.
#modules are the way to avoid name space collisions, same name in two different modules won't create a problem.
# if we import using from we will have to import every attribute required and that can be overwritten we define a variable with same name.
#but using simple import won't cause the same because we will have to use dot operator to access or assign variable which won't collide
#reload doesnot runs other imported module in a module.


from . import f2
import sys

f2.name = "Tum Chutiya ho balak"

f2.func(5)

from . import modulea
print(modulea.nowayback)

#when we import any module it runs all the content in the file with differing any.

print(f2.name)
print(dir(f2))

#ex is similar to copy pasting the code in the same region where exec() is opened.
exec(open("ex.py").read())
print(sys.path)


# note if this file will be included in some other modules this will be f1 
# if it is run independently it is __main__
print(__name__)

#sys is a builtin python module that contains parameter specific to system which is used by python interpreter 
#sys.path is a variable that contains a list of directories where python searches for modules 
#First python searches for imported modules in built in modules then the directories listed by sys.path
#PYTHONPATH can be set.

```

### Functions
```py
def function():
    print("this is main function")


# def glob():
#     nonlocal  b; b =15
#     return x

def newfunc():
    print("this") 
    #this function returns None

#here we are asigining new name to the function
lf = newfunc
lf.val = 14



# function with multiple arguments 
# arbitrary arguments 
def multiargs(a,*kwargs):
    print(a, kwargs)
# here all defines all the attributes that can be copied to another module using from 
# the attributes aprt from those listen in __all__ wont be copied into the module importing from
# it's not applicable to import since in import we use filename to access attribbutes
# here _not will not be copied by other module copying it 
# all of the below are not accessible by other module using from 
__all__=["one","two"]
_not = 15
one = 15
two = 20

three = 1000

#function with keyand value pair

def keyvaluee(b, **argu):
    print(argu)


multiargs(2,4,5,6,6,131)


b = ()
print(b)
# we can pass to **kwargs using **kwargs
keyvaluee(912,name="Verma")
keyvaluee(14,**{"Name":"ANuj"})











# print(x)
# check if the file is being imported as a module as being run independently 
if __name__ == "__main__":
    function()
    # i = glob()
    # print(i)
    l=lf()
    print(l)
    print(newfunc.val)
#functions are also called subroutines & procedures 
#function in python are differnet than python in compiled language like c and cpp
"""c function defination type 
return type functionname(parameter){
    //function defination
}
"""


"""
functions in python 
    def is ececutable 
    functino doesnot exists untile def runs 
    def are automatically executed when modules are imported 
    def creates a function object and assigns it a name given at runtime 
    function name is a reference to function object 
    lamda function also creates a function object and returns an object as result
    yeilds sends result object back to the caller it remembers the state of the function where it left off.
    In python argument are passed to function by assignment
    function without return call returns None

    def executes at runtime and creates object at runTime
    code inside the def is executed when it is called later.
    functions can be assgined attributes in python
    functions are object in python

    two parts of function 
        defination 
        def functionname(x):
            return this


        calls 
            functionname(14)
        
        here 14 is assigend to x since it value is passed by assignment

        * works for both intger and string(sequence)

    
        Polymorphism : 
            It is a type dependent behaviour 
            Different bevahiour by same entity on different objects 
            Meaning of operator is defined by the object it is being called upon

            Difference between Python and statically typed languages like C++ and Java: in Python, your code is not supposed to care about
            specific data types. 
            If it does, it will be limited to working on just the types you antici-pated when you wrote it
            Meaning of the operator is defined when it is called on specific object

"""


"""
Scopes and namespace 
    Namespace is basically a scope 
    every vairable has a name and it belong to certain namespace which has its own defined scope.
    All the variables(names) declared inside a function reside in a function namespace that is in the scope of the function.
    In python : 
        Scopes are three types : 
            1) Global scope 
                They are attribute to the module object outsite the world but are simple varible inside a file
            2) Non Local :
                Functions inside a enclosing function 
            3) Local
            This is called lexical scoping. Their scope is defined where they are declared. 

            Python uses The LEGB Rule for name resolution
            note that any type of assignment within a function classifies a name as local. Unless its assigned it is never treated as local
            Conversely, in-place changes to objects do not classify names as locals; only actual name assignments do.
    
    Built in scope 
    The built-in scope is implemented as a standard library module named builtins, but that name itself is not placed in the built-in scope, so you have to import it in order to inspect it.
"""

"""
Global and NonLocals 
    Module itself is a namespace for that particular file
    They are namespace declerations not type declerations
    Cross files changes are possible in python but they must be minimized 

"""


# NOTEE
# When we run python in repl or in intreactive prompt every thing gets stored in module named __main__ which is limited for that speicifc session.
# Local variables hide global variable 
# def is just a executable that generates the function object and assign a name to it which can further be called.



def func1():
    global x
    x = 19
    print(x)

func1()

# here x was not present but x is created when we call it as a global 
print(x)

def enc():
    def enclosed():
        return 4
    return enclosed

# this is factory function 



"""
    There are different ways to access the global varible s
    1) Using global name 
    2) Importing moduls 
    3) Using sys.module 


    When we declare global it just searches in global namespace
    Else first it starts from localScope, Enclosing , then global & builtins 

    Nested function are possible in python that is using def 


    Factory functions or closure functinos are the functinos which remember the state that is enclosing data and variables 

    Nonlocal refers to the namespace of enclosing fucntion
"""

def nesting():
    x = 14
    def nested():
        print("printing internal",x)
        return 14
    return nested

outer = nesting()
invaue = outer()
print("pringint external",invaue)


# non local function 

def nonLocal():
    r = 54
    def impl():
        nonlocal r
        r = 100
    impl()
    return r

val = nonLocal()
print(val)

#the above mechanism is also called as factory function 
# they are used to remember the state 

```
### Lambda
```py
lam = lambda x, y,z : x+y+z

def fuc(lam):
    return lam*2

#lambda argument, argument, : statement

print(fuc(lam(2,3,5)))
print(lam(3,4,5))
#defines anonymus functions without name
#used to pass function as an argument to the function 
# lambda's body is single statement not a block of statment 
# lamda is an expression not an statement
```



### OOPS Basic 
```py
    class human:
    #constructor#import filename
#from filename import attribute
#In general terms a file is a object and had many objects associated with it which we can fetch using dot operator.
#import gets module while, from gets copy of file's name.
#modules are the way to avoid name space collisions, same name in two different modules won't create a problem.
# if we import using from we will have to import every attribute required and that can be overwritten we define a variable with same name.
#but using simple import won't cause the same because we will have to use dot operator to access or assign variable which won't collide
#reload doesnot runs other imported module in a module.
    #self is like this where it points to object of itself.
    def __init__(self,name,age,degree):
        self.name= name
        self.age=age
        self.degree = degree
    
    def printHuman(self):
        print(self.__str__)


# this is the example of inheritance okay babay 
class engineer(human):
    def __init__(self,name, age, degree, post):
        self.post= post

    def printEngieer(self):
        print(self.name, self.age, self.degree, self.post)


# classes contains attribute and behaviour
# attribute == properties 
# behaviour == methods
# __init__ = constructor , self it this(i.e current instace of a class)


h1 = human("Anuj",22, "B-Tech")
print(h1.printHuman)

e1 = engineer("Kumar", 24, "B.E", "SDE1")
e1.printEngieer()

# attributes is data of an object. 
# behaviour is a method of an object.



# Main concepts : 
    # inheritance
    # polymorphism 
    # encapsulation 
    # abstraction

```

### Inheritance
### Polymorphism 
### Encapsulation 
### Abstraction 


### Data hiding
```py

# here all defines all the attributes that can be copied to another module using from 
# the attributes aprt from those listen in __all__ wont be copied into the module importing from
# it's not applicable to import since in import we use filename to access attribbutes
# here _not will not be copied by other module copying it 
# all of the below are not accessible by other module using from 
__all__=["one","two"]
_not = 15
one = 15
two = 20

three = 1000
```