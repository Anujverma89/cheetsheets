# C Language 

```c
    /*Categories of lanaguge*/
    /*
        Procedural 
        Structural 
        Functional 
        Object Oreinted
        Declerative Lanuguage 
    */
```
### Getting strarted 
```c
#include <stdio.h>


int main(){
    int var = 14;
    const int VALUE = 15; // memory location whouse value cannot be changed
    return 0;
}


// getting started : 
// four ascpects of any language : 
/**
 * 1) How it stores data ?
 * 2) How it operates upon the data ?
 * 3) How it accomplishes input and output ?
 * 4) How it control's exection ?
 */

/**History 
 * Developed at AT & T labs 1972 by dennis ritche
 * 
 * 
 * WHY C : 
 * It a base for understanding the concetps of language.
 * Speed it offers
 * To write device drivers for operating system
 * Hardware intractions
 */

/**What is character ? what is character set ?
 * Character can by anything alphabet,symbol or digit used to reprsenet information
 * Set of characters is called character set.
 */

/**Types of data : 
 * 1) Image
 * 2) Strings 
 * 3) Videos 
 * 3) Voice 
 */

/**Variable, constants and keywords 
 * Varaible : A name given to memory locatoin. Value at memory location can be changed hence it is called Variable.
 * variable name can only start with _ or aplhabet it can only contain underscore in between.
 * constant is the name of the memory location whose value cannot be changed.
 * Constant : Meanings it doesn't change. the value that is sotred at memory locatoin is called constant
 *  types : 
 *  Primary constants : Integer, real, character 1, 1.2, 'A
 *  Secondary constants : Array, string, pointer, strucutre , enum ,union
 *  length of variable is 1-31 generally 
 * Keywrods : keywords are some specil reserved words which have some predefined meaning in the language. there are 32 in c.
 * Allowing to redefine values to the keywords are allowed by some compilers
 * 
 * C is called free-form lanauge becuase it doenot defined the position at which statement is to be written. 
 * we can change the name of the main function by going inside the library files
 */


/**Types of instructions 
 * 1) Type declaration instruction 
 * 2) Arithematic instruction 
 * 3) Control Instruction 
 * 
 */

// (variable, constants , keyword) make expressions
// expression make statements;
// statemetns make programme
```


>Intro   
    #Developed by Dannis Ritche 1972 in bell laboratories.  
    #Languages before C were cobol, algol, PL/L, Fortran etc  
    #Language has for role   
>>      Storing Data  
>>      Operating On Data
>>      Input & Output
>>      Sequence of Execution

> Alphabets + Digits + Special Symbols = keywords, contant and variables


### Constant, variable, keywords :
```c
    /*Constants are never changed*/
    /* Variables may or maynot change*/
    /* keywords are reserved words of a laguage that cannot be used to define constant or variable
        It's meaning are already defined in the compiler
        They are also called reserved words 
        there are only 32 keywords
        specific vendor compiler can come with other than 32 keywords but they start with double underscores __
    */
    // Variable and constants are named memory location 
    //Memory is matrix of rows and columns called cells and they can be named


    //Constants  int and float convention is always used as capital letter A
    const int A = 14; //consant integer (signed integer)
    const int B = -1; //negative constant integer (signed integer)
    const float C = 1.5; //floating or real constant
    const float EX = 13.2e4; //this is called exponent declaration :
    //exp declaration is divided into two parts manitssa = 13.2, 4=exponent
    //before e is called mantissa and after e is called exponent
    //In c we cannot use  comma or underscores while declaring integers and float like in java(int a = 123_123_123)
    //defautl sign is always postive for float and int

    //constant char : 
    const a = '1'; //must be in single inverted command and comma should point to the left 

    //types : 
        //primary : int, float, char, 
        //secondary : array, enum, struct, union 


    //variables 
    //type of variable depends on the type of constant it can hold
    //int variable can only hold int constant like int a = 3; right int b = 1.2 wrong
    //variable name length between 1 - 31 character is ideal 
    int a = 14; //correct
    int b = 12.4 //incorrect 
    int b = 15; //variable entity 

```
### Programme 
```c
    //instructions are individual statements 
    //programm is combined of several statement
    //statement terminator == ;
    //c is free-form language i.e doesnot defines position of statements 
    //comment should say what is does rather than how it does.
    //some vendors proivde IDE along with compiler like TURBO C++
    //gcc is just a compiler and can be used with different IDES or editors 


    int main(int argc ,char *args[]){
        int d;
        scanf("%d",&d);
        printf("%d",d); //output
        //scanf() & printf() are the builtin functions for 
        //& is used to refer the address of the variable 
        //while giving inputs we must separete input using line, space or tab
    }

```

### Types of instructions 
```c
    //types of instruction 
    //type declartion instruction -- Declare the type of variable
    //arithematic instruction
    //control instruction
```
### Operand & Operator 
```c
    //operand are constant or variables on which operators are applied
    //first right side is operated and then the value is assigned to the left
    //int to float == promotion
    //float to int == demotion
```

### Type conversion 
```c
    //Conversion of types from one type to another:
    //types : 
        //a. Implicit (Done by the compiler) or automatic type conversion
        //b. Explicit (Done by the user)

        //Promote & Demote
        
    //implict conversion :
        //it is always promoted to save the output of the data
        //data type is upggraded to the variable having larger value

```
![conversion](https://www.scaler.com/topics/images/implicit-type-conversion-in-c-image1.webp)
![rank](https://scaler.com/topics/images/implicit-type-conversion-in-c-image3.webp)



### Pointers and Double pointers

```c
    /* Mid level lanaguage close to Hardware*/
    // reference variable &
    // single pointer  & double pointer value and reference 
    int main(){

    int a = 15;
    int *b = &a;
    int **c = &b;
    printf("%p\n",&a); //address
    printf("%p\n",b); //value 
    printf("%p\n",c); //prints value
    printf("%p\n",&b); //prints address
    printf("%p\n",&c); //address
    printf("%d\n",*b); //pointer - reference value
    printf("%d",**c); //pointer - pointer - reference value
    return 0;
}
```


### premitive data types 
```
```


### operators

```c
    //arithematic operator >> +,-,%,/,*
    
    //#include <math.h>
    //exponent == math.pow()

    //artithematic operators can only be applied to int, float and char
    // % operator cannot be performed on real no 
    // using % module gives the sign of the reminder with the sign of numerator 
    //assignment operators >> =
    //arithematic operation performance mode 
    //when arithematic operations are performed ascii operations are perfomed on ascii values not on operatos 
    //integer mode i.e variables are only integer
    //real number mode i.e variables and constants are real no 
    //mixed mode : variables and constants can be of any type type casting is must to get the desired result 
    //when differnet types of values are present first values are promoted or demoted and then operations are performed

    /*
        Priority & Associativity
        OperatorsDescription
        1   multiplication, division, modular division
        2   +-addition, subtraction
        3rd =assignment

        Associativity 
        left to right 
        right to left
    */


    int a = 14;
    int b = 16;
    int sum = a+b; //integer mode
    a = 14.5;
    b = 16.5;
    sum = a+b; //real no mode
    a = 15;
    sum = (int)a+b; //mixed mode
```


### Non-premitive data types : 

```c
    //structure 
    struct human{
        char n[];
        int age;
    }

    //union
```



<!-- major concepts
Basic Syntax and Structure:

Functions: Blocks of code that perform a specific task, defined using the syntax return_type function_name(parameters) { body }.
Main Function: The entry point of a C program, defined as int main() { ... }.

Data Types and Variables:
Basic Data Types: int, float, double, char, etc.
Derived Data Types: Arrays, pointers, structures, and unions.
Variables: Containers for storing data values, declared with a specific type.


Operators:
Arithmetic Operators: +, -, *, /, %.
Relational Operators: ==, !=, >, <, >=, <=.
Logical Operators: &&, ||, !.
Bitwise Operators: &, |, ^, ~, <<, >>.
Assignment Operators: =, +=, -=, *=, /=, %=.


Control Flow:
Conditional Statements: if, else if, else, switch.
Loops: for, while, do-while.
Jump Statements: break, continue, goto, return.


Functions:
Function Declaration: Declaring a function prototype before defining it.
Function Definition: Actual implementation of the function.
Function Call: Invoking the function to execute.


Pointers:
Pointer Variables: Variables that store memory addresses.
Pointer Arithmetic: Operations on pointers like incrementing, decrementing, and difference.
Pointer to Pointer: A pointer holding the address of another pointer.
Function Pointers: Pointers to functions for dynamic function calls.


Arrays:
Single-Dimensional Arrays: A list of variables of the same type.
Multi-Dimensional Arrays: Arrays of arrays, like matrices.


Strings:
Character Arrays: Arrays of characters, terminated with a null character \0.
String Functions: Functions like strcpy, strlen, strcmp, strcat.


Structures and Unions:
Structures: User-defined data types that group different data types.
Unions: Similar to structures, but with shared memory for all members.


Memory Management:
Dynamic Memory Allocation: Using malloc, calloc, realloc, and free for managing memory at runtime.


File I/O:
File Operations: Using fopen, fclose, fread, fwrite, fprintf, fscanf, fseek, etc.
File Pointers: Pointers to file streams for file operations.


Preprocessor Directives:
Macros: Using #define for defining constants and macro functions.
File Inclusion: Using #include for including header files.
Conditional Compilation: Using #ifdef, #ifndef, #endif, #else, #elif.


Libraries:
Standard Libraries: stdio.h, stdlib.h, math.h, string.h, etc.


Typecasting:
Converting one data type to another using explicit casting (e.g., (int)someFloat).


Error Handling:
Using errno and related functions for error detection and handling.

-->

### Types of Instruction 
* Type Declaration Instruction 
* Arithmatic instruction 
* control instructions


### Basics 
```c
    #include <stdio.h>



    int main(){


        int a = 15;
        int *b = &a;
        int **c = &b;
        printf("%p\n",&a); //address
        printf("%p\n",b); //value 
        printf("%p\n",c); //prints value
        printf("%p\n",&b); //prints address
        printf("%p\n",&c); //address
        printf("%d\n",*b); //pointer - reference value
        printf("%d",**c); //pointer - pointer - reference value
        return 0;


    }

```


### Data types 
```c
    #include <stdio.h>
#include <stdbool.h>

static int ii = 35; //global static available within file

int main(){
    /**
     * Data types 
     * int 4 byte
     * char 1 byte
     * float 4 byte %f
     * bool 1 byte
     * double 8 byte %lf
     * short 2 byte %d
     * long double 16 byte %Lfs
     */
    register float r =13;
    {  
        static int ii = 15; //its static but not available to all
        printf("%d\n", ii);
    }

    printf("%d\n",ii); //static is not avaible 

    int a = 2147483649; //results in negative value 
    short ab = 15;
    float b = 15.4;
    char aa = 'a';
    bool bo = false;
    long l = 1231232l; //used when liternal is not big enought to fit long value
    unsigned singe = -15; 
    long double d = 123124.124;
    printf("%d\n",singe);
    printf("%d\n",a);
    printf("%ld, %ld , %ld, %ld , %ld, %ld %ld ", sizeof(a), sizeof(b), sizeof(aa), sizeof(bo), sizeof(l), sizeof(ab), sizeof(d));
    // unsigned  ch = 128 ;
    // printf( "\n%d %c", ch, ch );
}
/*
Note 
    Boolean are not built-in datatypes include <stdbool.h>
*/

    // 1 1 1 1 1 1 1 1 -> Byte unisgned  all used to store values = 255
    // 0 1 1 1 1 1 1 1 -> singed + 127 max value 
    // 0 0 0 0 0 0 0 0 -> signed + 0 min value 0 - 127 (range)

    // 1 1 1 1 1 1 1 1 -> signed - largest
    // 0 0 0 0 0 0 0 0 -> 1s compilment 
    //               1 
    // 0 0 0 0 0 0 0 1 -> 2s compliment largest = -1

    // 1 0 0 0 0 0 0 0 -> signed - smallest 
    // 0 1 1 1 1 1 1 1 -> 1s compliment
    //               1 - > add
    // 1 0 0 0 0 0 0 0 - > 2s complimnet = -128 range = -128 -2^(n-1) to (2^(n-1)-1)


    //there are three primary tyeps in c i.e 
    // char
    // int
    // float 


    // when we compile code using 16 bit cimpiler it can run on 16bit processor and above same is with 32bit, 64bit etc
    // declaring unsigned increases the range fo pointer since it won't be used to store the negative value.
    // by default int float and char are signed 
    // char is also signed when you enter value that exceds 127 it starts assigining it from -128 so 128 maps to -128, 256 maps to 0 and 257 maps to 1
    // You can declare it as unsigned to remove this default behaviour  
    // compiler we use to compile also makes sure code will run on which microprocesssor like 16bit trubo compiles for 8086 microprocessor
    // Negative numbers are always stored as two's compliment
    // when we try to store value grater than 127 it tries to allocate 9 bits but since only 8 bit can be taken it takes right 8 bit and since MSB is used for sign representation that behaviour is seen
    // in general if we exceed range in positive side we will end up in negative side and vice versa and is true for all the signed datatypes
```


### Storage classes 
```c

    // Storage classes : Defines where the variable will be stored
    // where varibles are stored 
    // Every variable has a storge class even if we don't specify the default is auto
    // there are 4 
    /*
    Automatic 
        Key word : auto
        scope : block where it is defined
        initial value = garbage
        space : Memory
        auto int a ;
        life : till block of code is running
        when not used any below classes
    External
        keyword : extern
        life : until programme exection comes to end
        initial value = 0
        space : memory 
        scope : Entire programmen (GLobal)
        use when variable is to be needed by all the file to avoid it passing as function call
    Register
        Key word : register
        scope : block where it is defined
        initial value = garbage
        space : CPU Register (If registers are full it is treated as auto)
        life : till block exits 
        Used when the variable is to be used very frequently 
    static 
        key word : static
        scope : whereever it is defined
        intial value = 0
        space : Memory
        life : value persists between different function calls till programme end but not accssible by all 
        The main goal of static is not to make it gloabal but to make it persitent.
        static initializtion executes only once not more than once.
        static can 
    // 1 1 1 1 1 1 1 1 -> Byte unisgned  all used to store values = 255
    // 0 1 1 1 1 1 1 1 -> singed + 127 max value 
    // 0 0 0 0 0 0 0 0 -> signed + 0 min value 0 - 127 (range)

    // 1 1 1 1 1 1 1 1 -> signed - largest
    // 0 0 0 0 0 0 0 0 -> 1s compilment 
    //               1 
    // 0 0 0 0 0 0 0 1 -> 2s compliment largest = -1

    // 1 0 0 0 0 0 0 0 -> signed - smallest 
    // 0 1 1 1 1 1 1 1 -> 1s compliment
    //               1 - > add
    // 1 0 0 0 0 0 0 0 - > 2s complimnet = -128 range = -128 -2^(n-1) to (2^(n-1)-1)


    //there are three primary tyeps in c i.e 
    // char
    // int
    // float 


    // when we compile code using 16 bit cimpiler it can run on 16bit processor and above same is with 32bit, 64bit etc
    // declaring unsigned increases the range fo pointer since it won't be used to store the negative value.
    // by default int float and char are signed 
    // char is also signed when you enter value that exceds 127 it starts assigining it from -128 so 128 maps to -128, 256 maps to 0 and 257 maps to 1
    // You can declare it as unsigned to remove this default behaviour  
    // compiler we use to compile also makes sure code will run on which microprocesssor like 16bit trubo compiles for 8086 microprocessor
    // Negative numbers are always stored as two's compliment
    // when we try to store value grater than 127 it tries to allocate 9 bits but since only 8 bit can be taken it takes right 8 bit and since MSB is used for sign representation that behaviour is seen
    // in general if we exceed range in positive side we will end up in negative side and vice versa and is true for all the signed datatypes


    // Storage classes : Defines where the variable will be stored
    // where varibles are stored 
    // Every variable has a storge class even if we don't specify the default is auto
    // there are 4 
    /*be declared out of function and this will be available to all the code in the file
        Use when we want value to persist 
*/


```

### Decision 
```c
    #include <stdio.h>



int main(){
   
    // but if can run without else
    if(1){
        printf("OKAy\n");
    }
     // else cannot run without if 
    else{
        printf("THis is okay\n");
    }

    // pit fall
    // the printf() always gets executed since if(4==5); is treated as different statement and
    // printf() is different the null statement is executed after the if() condition is true
    if(4==5);
        printf("this is okay\n");


    // conditional operator or ternary operator  :
    // here it can return value or execute the expression 
    int b = 14;
    int c;
    //Assignment statements used with conditional operators must be enclosed within a pair of parenthesis.
    b==15?(c=14):(c=15);
    int d = 1;
    // this is an unary operator operates only on one operator
    if(!d){
        printf("NO B");
    }

    return 0;
}


// decision is basically what to execute and when to execute.

/**
 * Types of decision instruction 
 * if, else,  else-if
 * switch
 * Conditional operators : AND, OR , NOT
 *  
 */


// if is always followed by condition and condition results true or false by executing relational operators or conditional operators 
// Decision and condtion works hands on hands 

// Note:
// In c non-zero values are considered to be true and zero values are considered to be false.


// if , else
/*
* if (if) statement is evaluadted to true then then the immediate next statement is executed becuase the scope of the if is immediate next statement
* Hence we create the block of statement if we need more than one statement to be executed if (if) is satisfied. this is called grouping of statements.
* The block of code followed by if and condition is called if block and similar for else block 
* If block can run without else block but else block cannot run without if block
* More concepts : 
    Nested if, else if and else , else-if ladder
*/

// else if 
/**
 * It is used to check for multiple conditions 
 */


// conditional operators or logical operators 

/**
 * &&, ||, !
 * They are also called bitwise operators 
 * &&, || allow to combine two or more conditions 
 * && executes to true if all of them are true 
 * || executes to true if even one of them is true
 * && and || are binary operators, whereas, ! is a unary operator.
 */


/**
 * 
 * Conditional or ternay operator
 * expression 1 ? expression 2 : expression 3
    What this expression says is: “if expression 1 is true (that is, if its
    value is non-zero), then the value returned will be expression 2,
    otherwise the value returned will be expression 3”. Let us
    understand this with the help of a few examples:
    Conditional operators can be nested as well.
    Assignment statements used with conditional operators must be enclosed within a pair of parenthesis.
 */
```


### Bitwise operators 
```c
    #include <stdio.h>

int main(){
    // showbits(14);
    int a= -1;
    int b = 5;
    a = a >> 1; //rightshift
    // here blanks are always filled by zero which are created by shifiting
    //Note that if the operand is a multiple of 2 then shifting the operand one bit to right is same as dividing it by 2 and ignoring the remainder.
    // here sign is preserved and extended
    a = a << 4; //
    // leftshift is similar to rightshift just the digits are shifted to the right
    int c = a & b;
    // this is different than the && 
    // it operates on bit by bit
    int d = a | c;
    int k = ~a; //1's compliment
    int j = a ^ b; //xor operator 

    printf("%d %d %d %d %d %d ", a , b, c,d, k, j);

    return 0;
}

// programmes are byte oriented but hardware are bit oriented.
/** No we will look bit by bit into byte
 * Bit wise operators : 
 * ~ NOR(1's compliment) negation 
 * & AND
 * | OR
 * ^ XOR
 * << left shift
 * >> right shift 
 * 
 * 
 * MSB|7|6|5|4|3|2|1|0|LSB
 * |64|32|16|8|4|2|1| = sum = 255
 *  Bitwise operator can only be appliend on int and char but not on float and doubles 
 */


```


### Arrays 
```c
#include <stdio.h>

//here pointer caputers the address passed to the function
void printValue(int *pointer){
    printf("%p\n", pointer); // prints the address of the element passed in function
    printf("%d\n",*pointer); //prints value at pointer
    doublestar(&pointer);
}

void printVaalue(int a){
    printf("%d\n",a);
}

void doublestar(int **ptr){
    printf("value by address of %d\n",**ptr);
}
// passing pointer to the function
void ptrfunction(int *value){
    printf("%p\n",value);
}

void arrayFunction(int value[]){
    printf("%p\n",value);
}

int main(){

    void mot(a);

    unsigned int arr[10]={1,3,4,6,5,6,7,8,9,10}; //declaring int varaible int -> type & arr = name & [size] no of elements 
    // they are initialized with all zero 

    int d2[3][2]={{1,2},{2,3},{3,4}}; //two dimensional matrix
    int d3[3][3]={1,2,3}; //this is also correct only while we declare and initialize values at same time 
    // here in d3[][3] second subscript tells the compiler the length of the one dimensional array 
    // While incrementing the first subscript it is not incremented by the size of data type but incremented by the size into the dimension of 1d array
    //eg : 
    //in d3 while incrementing *(d3+2) here d3 is an 1D array


    printf("%ld", sizeof(arr));

    int a;
    scanf("%d",&a);
    scanf("%d", &arr[9]);
    printf("%d\n",arr[4]);
    printf("%d\n", arr[20]);
    printValue(&arr[10]); // pass by reference i.e. passing the address.
    printVaalue(arr[10]); //pass by value
    int *arpte = &arr[0];
    for(int i = 1; i <= 10; i++){
        printf("%p\n",++arpte);
    }
    ptrfunction(arr); // when we do like this the address of the first element of an array is passed to the function
    arrayFunction(arr);
    printf("%p\n", arr+4); // the foruth address will be pointed when we do this arr is actually a ptr
    printf("%d",*arr);
    printf("%d",arr[9]); // interally is done as arr+9 i.r arr is incremented by 9 
    return 0;   
}


/**
 * Array in c is the collection of smilar elements stored in contegious memeory location.
 * Is a set of smilar data elements.
 * An array is a collective name given to a group of ‘similar quantities’.
 * Arrays and pointer work hand in hand.
 * Array of string is called string. and array of floats or int is generally an array
 * In c first we have to declare then define and use. or declare & define at same time and use
 * We access the elements of an array using subscript i.e arr_name[postition] arr[4] (accesses the third element)
 * scanf() // takes the forment of variable and address where it is to be stored
 * it is also known as subscripted variable.
 * storage class of array is be default auto we can chagne 
 * when storgae class is extern or static it will initialized with 0
 * array always reserves the contigious memeory location
 * passing array to functin i) Call by value ii) Call be reference 
 * when pointer is incremented it always points to the next address of same type;
 * pointer can be incremented or decremented to point to the next or previous memory locations 
 * 281
 * Array can be passed to function both as array and as pointer.
 * Array when passed to function address of first element is passed to the function
 * when we access array without indexing its first element's address will be accessed;
 * (a) Array elements are always stored in contiguous memory locations.
 * (b) A pointer when incremented always points to an immediately next location of its type.
 * when you use index number to access the array element index number gets added to starting position of the array i.e arr;
 * if you want to access 8th element we do arr[8] which internally becomes (arr+8);
 * We also know that on mentioning the name of the array we get its base address
 * In two dimensional array it is not stored as row and column in memeory instead it is stored sequntially.
 * memory doesn’t contain rows and columns.In memory whether it is a one-dimensional or a two-dimensional array the array elements are stored in one continuous chain.
 * it can treat parts of arrays as array i.e each row is an array
 * We can also create an array of pointers
 * The array variable acts as a pointer to the zeroth element of the array. In a 1-D array, zeroth element is a single value, whereas, in a 2-D array this element is a 1-D array.
*/

```


### 2D array and ND array
```c
#include <stdio.h>


int main(){

    int d[3][2]={
        {3,105},{5,100},{9,200}
    };


    int d3[2][3][3]={
        {
            {3,4,5},
            {6,7,8},
            {9,10,11}
        },
        {
            {12,13,14},
            {15,16,17},
            {18,19,20}
        }
    };
    int (*dn)[3][3]=d3;
    int (*ptr)[2] = d; // here now if we increment the ptr it increases not by size of int but by (size of int * no of element in dimension)  is 4*2 = 8 bytes
    printf("%p\n",ptr);
    // printf("%d\n",(*ptr)[0]);
    // printf("%d\n",(*ptr)[1]);
    printf("%p\n",++ptr);
    printf("%p\n",++ptr);

    // 3d trial works here
    // here since dn is the pointer that holds 3d array so when we increment dn it gets incremented by the size of ((row*column)*size of int)
    printf("%p\n",dn);
    printf("%p\n",++dn);
    printf("%p\n",++dn);
    return 0;
}
```


### Argument in Main function 
```c
#include <stdio.h>

int main(int argc, char *argv[]){
    if(argc == 1){
        printf("%s\n",argv[0]);
        printf("Enter arguments \n");
    }else{
        for(int i=0; i < argc; i++){
            printf("%s\n",argv[i]);
            argv[i][2] = 'h';
            printf("%s\n",argv[i]);
        }
    }

    // char ch;
    // while((ch=fgetc(stdin)) != EOF){
    //     putc ( ch, stdout ) ;
    // }
    // this programe ends when we press ctrl+z becuase that is often called the end of the file

    // for(unsigned  i = 0 ; i <= 255; i++){
    //     printf ( "\n%d %c", i, i ) ;
    // }s

    FILE *fp;
    fp = fopen("filenmae.txt","r");
    // fputc('c',fp);

    /// yet to read
    // if(ferror(fp)){
    //     perror("TRIAL");
    // }

    return 0;
}
// first argument is always the cmd to run file i.e ./a.out
// argv[] holds string 
// the arguments that we pass are called command line arguments 
// we can use ferror() function to detect error while working with file opertations returns non-zero value in case of error
// perror() prints the error if error had orrcured 
// standard I/O  by OS
// stdin = keyboard
// stdout = VDU
// stderr = VDU

// we can use getc(stdin) to take input from keyboard rther from file
// there can be standard priting and auxilar devices as well but depends on system stdprn stdaux


// IO Redirection 
// we can redirect IO from standard IO devices to any other IO devices 
// redirection operator 
// a.out > oputput.txt
// a.out < input.txt
// inputoutput together a.out<input.txt>output.txt
// we can also send to printer a.out<input.txt>prn
// never try to use samefile for input and output becuase output file is erased before output is written
// there is another os operator | pipe this can be used to feed the output of one file into other a input
// this approach is called fipelining

```


### File in c 
```c

#include <stdio.h>

struct employee{
    int sal;
    int id;
    char name[100];
};


int main(){
//FILE is a strucutre that contains the pionter 
    FILE *fp;
    // here first file is searched from disk 
    // then it's contenet is loaded into buffer memory
    // sets the character pointer to the first element of the buffer
    // How to print the EOF of the file
    fp=fopen("newfile.txt","rw");
    if(fp == NULL){
        printf("FILE cannot be opened\n");
    }else{
        while (1)
        {
            //fgetc() reads the content of the buffer character by character and increases the pointer by 1 to point to next 
            char ch = fgetc(fp);
            // fopen() returns null if file cannot be opened
            // EOF is actually substitue whose ascii value is 26 
            // sometimes 28 is also used  that is file seperator 
            if(ch == EOF){
                printf("\n%d\n",ch);
                break;
            }else
                printf("%c",ch);
        }
    }
    
    // things done while closing
    // the character from buffer gets copied into the file stored in disk
    // at the end of the file ascii value 26 will be written 
    // buffer will be deleted from the memory

    fclose(fp);

    /**MODES
     * here t is text mode and b is binary mode t is by default so we can omit t i.e. only r can be given
     * r or rt : only read
     * w or wt: write to file (content of file is overwritten)
     * a  or at = append model (pointer points to the last element in the buffer)
     * r+ : pointer points to the first element in the buffer 
     * w+ : pointer points to the first element in the buffer
     * a+ : pointer points to the first element in the buffe
    */

    // fgetc(storeingarray, string length, stream source);
    // fputc(destination object)
    // \r carriage return moves the cursor to the begining of the line without moving to the new line
    //a newline character is converted into the carriage return-linefeed combination before being written to the disk.
    // when writing string file using fputc it also write  carriage return in front of \n hence 



    // we use fscanf() and fprintf() to organize dissimilar data into the file
    // example is demonostrated here 
    // fflush() is used to clear the buffer it takes the argument which buffer to clear 
    FILE *epf;
    epf = fopen("employe.txt","at+");

    struct employee emp;    

    if(epf == NULL){
        printf("File cannot be opened\n");
    }else{
        int flag = 1;
        while (flag)
        {
            scanf("%d %d %s",&emp.id, &emp.sal,emp.name);
            // here fsacnf also be used same as scanf() but first argument is the fiel pointer;
            fprintf(epf,"Employee Id : %d\n\t Name : %s\n\t Salary : %d\n", emp.id, emp.name, emp.sal);
            flag=0;
        }
        
    }



    // Binary mode 
    // fwrite() and fread() are used to work in binary mode.
    // fwrite ( address of source, sizeof ( source ), no_of_instance_of_source_to_be_written, filePointer ) ;
    //fread( destination address, sizeof ( source ), no_of_instance_of_source_to_be_read, filePointer ) ;
    //any database management application in C must make use of fread( ) and fwrite( )
    // frewind() places the pointer to the begining of the file 
    // fseek() places the file to the place where we want to point

    //clrscr() clears the content of the screen 
    // gotoxy places the cursor to the xy position of the , SEEK_CUR, SEEK_END, SEEK_SET
    // ftell() current position of the pointer
    
    return 0;
}






/**How binary files are differnet than text file 
 * Handeling of new lines
 *   //a newline character is converted into the carriage return-linefeed combination before being written to the disk in text mode
 *  // however this is not true in binary mode
 * Representation of end of file
 *  // there is no EOF in binary file wheres there is EOF In text file
 * //he binary mode files keep track of the end of file from the number of characters present in the directory entry of the file.
 * // the file written using binary mode should always be read using the binary mode becuase they are not compatible.
 * Storage of numbers
 * // Nummbers or any other elements are always stored in the form of string in database or files.
 * // Each character require 1 byte of a memory if it is opened in text mode so if there is a float 12.4561231 it will take 10 bytes but using flaot it will only use only 4 bytes.
 * // so to work with this we use fread() and fwrite() to work with numerical data. this helps us to read and write data in binary format
 */











/* FILE IO 
* It is important to store data somewhere becuase if it is just available in ram it will be lost.
* Data can be stored in FILE or in Database 
* Here we will be talking about database.

    popular file operations: 
        1) Creating new
        2) opeaning
        3) reading
        4) Writing
        5) moving to part of file
        6) Closing

* FILE is a strucutre where the contents like size, mode, next pointer etc is mentioned.
* While creating non-binary files the ascii value of the elements is stored in file not the actual value.

* Buffer is temporary space in a memory that reserved and used for some IO task to perform IO efficiently. 
* It is also used to match up with speed of different IO systems
* reading and writing from and to a IO device is generally done through buffer not directly from cpu to IO device.
* 
*/

// Database is a software
// DBMS is used to control Databases; 
// File is an object 
// Both files and databases are stored on disk but how they are managed differs
// All the data stored in a disk is in binary form. how can we access them differes from os to os 


// NOTE : 
// 1) Reading and writing can be done only at the postion where file pointer is placed.
// 2) so if we want to read or write at some place to have to move our file pointer there.
// fseek(fp, offest, postion_of_start_of_offset) Helps us to move the pointer 
// SEEK_END = begining of the file 
// SEEK_END = offset starts from the end
// SEEK_CUR = offset starts from the current position 
// ftell(fp) tells the postion of the pointer 
// There is always a buffer involved in IO operations becuase there is no direct operations perfomed on IO devices.
// we can always use differnet methods to both read and write files in different modes.

//fprintf() for formatted output and fscanf() for formatted input
//getc() and putc() gets() putc() for input and output of character in text mode 
// fread() fwrite()













// revistied : 

// get character
/* 
fgetc(fp) readers character from file

fputc(ch, fp) // puts character to the file  
unformatted 
*/



// get line 
/* 
fgets(destination, length, fp) 
    reutrns null when read is complete

fputs(string, filepointer) introduces \r\n with in exit file 
unformatted
*/

// with record of multiple type 
/**Formatted 
 * fprintf(fp, "format string", data)
 * 
 * fscanf(fp, "format string", address_variable)
 * 
 * fflush() to flush io buffer
 * 
 * all of the above are used to work with text mode 
 */


// Binary mode 
/**
 * fread(address_of_destination,sizeof(destination),no_of_instance, fp)
 * 
 * fwrite(address_of_source, sizeof(source),no_of_instance, fp);
 * 
 * rewind(fp) moves the filepointer to the begining of the file
 * 
 * fseek(fp, offest, postion_of_start_of_offset)
 * 
 * ftell(fp) -> tells the position of the pointer 
 */




// LOW LEVEL IO
// in low level I/O functions data can only be written using IO function and buffer full of bytes
// Low level io functions are faster and efficient 
// at the end everything is written in database or files in the form of 1 or 0;
// opening the file requires 
//open(name, mode) to open file in low level returns -1 if not opened 
//read(source_file, target_buffer, Max_size_of_reading_Data) returns no of bytes read;
//write(desination, buffer, no_of_bytes_to_write_from_buffer)

```


### Function 
```c
#include <stdio.h>

void print(int a){
    printf("%d\n",a);
}

dosome(a,b,c){
    //Kernighan and Ritchie (or just K & R) method. to pass the value to the function also called formal argument
    // int a,b,c;
    printf("%d %d %d\n", a,b,c);
    printf("%c %c %c\n",a,b,c);
    return a+b+c;
}

int another(int a, int b, int c){
    // this method is called ANSI method
    return a+b+c;
}

lets(){
    printf("letssdfgs\n");
    printf("%d\n",6+5);
    printf("%d\n",4+5);
    printf("%d\n",4+5);
}

// here we are not returning anything but still works because it returns anything it likes.
int valueret(){
    int idea = 14;
}

// purpose to return nothing
void voidreturn(){
    printf("Pringting void function\n");
}

int recur(int n){
    if(n==1){
        return 1;
    }else{
        return n*recur(n-1);
    }
}

// pointers starts here 
// here ptr means it will refer to a memory location or point to a memroy location 
int *ptr;  // pointer is simply a variable that holds a address rather than a actual value i.e ptr will hold a address containing a int 
int value = 14;
*ptr = &value;
int **ptrr; //double pointer points to the variable that holds the address of other pointer 
**ptrr = &ptr;
//pointer points to a value


int main(){

    // declaring function inside the main function 

    int insidemain(int);

    print(13);
    print(12);
    print(11);
    int a=dosome('a','b','c');
    printf("%d",a); //print 294
    printf("%c",a); //print &
    int b  = another('a','b','b'); //here value is being type caseted into int by default
    printf("%d\n",b);
    int le = lets();
    printf("%d\n",le);
    voidreturn();
    insidemain(100);
    printf("%d\n",*(&value)); // value at address &value
    printf("%p\n",ptr);
    printf("%p\n",&value);
    printf("%p\n",&ptr);
    printf("%p\n",ptrr);
    printf("%p\n",*ptrr); //value at address here ptrr points to ptr (i.e value at address pointed by *ptrr) = ptrr -> ptr (&value)
    printf("%d\n",**ptrr); // ptrr -> ptr(&value) -> ptr -> &value value at adress &value 
    printf("%d\n",*ptr);

    // function without return value 
    int noret = valueret();
    printf("Value of someNon return is %d\n",noret);
    int rec = recur(5);
    printf("%d is the recurssion value ", rec);
}       

int insidemain(int a){
    printf("Being defined here outside %d\n",a);
}

/*
* Functions and pointer
* Function is a block of statement that is specified to perform some specific task
* When function calls another function that calling function is suspended for sometime and control passes to the called function after
* Called functions runs out of instruction to run the control is passed to the calling function 
* Every c programme contains atleast one function i.e main 
* Declaration void func();  
* Defination func(){};
* Calling   func();
* when main function runs out the statements the programme ends
* Function cannot be defined in another function 
* Types : Library , user-defined, library functions come by default with compilers
* Return servers two purposes first : returns value to calling and second pass control back to calling function
* If return is not present it still works fine
* If return type is not specified still it works 
* If apramter type is not specified it works 
* Function always returns something inorder to avoid to not return anything we must specify it as void
* No return type or the type of paramenter is defined its default value is always int as in function lets.
* Before using the library function we have to import respective file in the programme to use it.
* the default value that functions returns in c is int.
* function can be decalred in main as well but since it will not be available to other we declare it outside the function in global scope.
* call by value & call be reference 
* & is a address of operator 
* * is called as value at operator or indirection operator
* Pointer is a reference variable that points to address of another variable.
* we can overcome the limitation of the return(only one) by using call be reference since here we can manuplate the external varibles 
*/

// int i = 3 ; 
// reserve a space in memory to store int
// name memory location with i 
// store the value of 3 in that locaiton

// function call stack contains :
// local variables 
// arguments 
// return address 

// data strucutre is a way of organizing the data
// recursion uses call stack to store call 
// when function gets called it retuns something to the calling function and that can be used for further processing.
// when main is called everything is pushed into stack in order in which it appers.
// main pushes the parameters and clears it this is called as CDecl Calling Convention
// there is yet another convetion where the called functin itself removes the paramter. and in default manner the parameters are pushed into stack from right to left manner
// we can always create our own function and add to library using header file or adding to the standard library module.
// can always create a header file and use it 


// NOTE : 
// if we declare a function return type but we don't return a value function returns something but it's value is unintended
// Weather programe will run or not it completely depends upon the nature of the compiler and its optimization.
```


### Preporcessors :
```c
    #define MORE 14
    // define, #include #if #elif macro undef pragma
//(a) Macro expansion
//(b) File inclusion
//(c) conditional directives
//(d) miscellaneous directives #undef & #pragma

// file inclusion
// it is used to include the content of the external file in the source code.
// when file is included the source code of the file get's copied in the current file.
// the file must be present to include 
// why to use this preprocessor 
// 1)this helps to divide large code into modules 
// 2)this helps to store the proptotypes of function and macro defination in file. this file is generally created with .h extension
// because they are added to the had of the file
// file can be included in two ways 
// include search path is a path where compiler searches for file to be included in the file
#include "included.c"
#include <stdbool.h>
#include <stdio.h>



// macro expanssions 
#define IDEA 14
#define STR "THIS IS NICE\n"
#define IDEA2 15
#define CLEARSCREEN "\x1B[2J" // this command clears the screen in computer
#define FOUND printf("THis is the example of expression declaration using macro\n")
#define ADULT (a>18) // macro is used for defining logics
#define AND && // can be used to replace operators  
const int a = 14;
// macros with arguments 
// this doesnot gets called but it's value gets replaced while preprocessing
#define WORDS(x) (x+1)
// macro expansion should always be enclosed parenthesis

// multiline macro
#define MULTILINE(x) for(int i = 0; i<x; i++){\
                        printf("%c",196);\
}
// here #define is macro defination idea is macro template and 14 is macro expansion

// lets check function defination if it works 
// function is actually explate and expansion is replaced 
#define FUNCTION(x) int func(){\
return 5;\
}



// conditional preprocessings
//ifdef
//uses
//1) When we wan't that certain part of code should only work . Since there must already be a comment and there is no nested comment in c
//2) to make source code portable
#define OKAY 0
#define VALUE 14



// miscellaneous directives
// here is OKAY is undefined and #ifdef condition will not work 
#undef OKAY

// #pragma is used to turn on off the certain feature 
// you can read for more information
void fun1( ) ;
void fun2( ) ;
#pragma startup fun1
#pragma exit fun2

void fun1( )
{
printf ( "\nInside fun1" ) ;
}
void fun2( )
{
printf ( "\nInside fun2" ) ;
}

int main(){
    printf("this is anuj\n");
    FOUND;
    int a =19;
    printf("%s",STR);
    if(ADULT){
        printf("adult\n");
    }else{
        printf("minor\n");
    }
    int d = IDEA + IDEA2;
    printf("%d",d);
    int b = WORDS(5);
    printf("%d",b);
    // printf(CLEARSCREEN);
    // MULTILINE(6);
    // the code below works fine  though it shows an error
    FUNCTION(10)
    int lls = func();
    printf("%d",lls);


    // conditional preprocessing
    // OKAY is defined then the code will be replaced else it won't be replaced in preprocessing step
    #ifdef OKAY
    printf("Running if def code\n");
    #endif
    // this code won't be replaced since there is no NOTOKAY macro
    #ifdef NOTOKAY
    printf("Running if def code\n");
    #endif

    #ifndef NOTOKAY
    printf("WOrking since NOTOKAY macro is not present");
    #endif

    // portable for differnet machines
    //ifndef
    #ifdef INTEL
    printf("Code for intel\n");
    #else
    printf("code for motorola pc\n");
    #endif


    // #if #elif #endif #else
    #if VALUE == 14
        printf("Valueis okay\n");
    #elif VALUE >= 14
        printf("VALUE IS LARGE\n");
    #else 
        printf("Nothing is printed");
    #endif
    

    return 0;
}






/**
 * Steps 
 * Preprocessing
 * Compiling
 * Linking
 */

// preprocessors are also called as directive
// they can be defined any where in the programe but generally they are defined at the start of the programme 
// IN preprocessing step every macro template is replaced by macro expansion before it is passed to the compiler



//why to use macros : 
// to implement dry principle 
// To increase readability of the code 

// You may ask variable can also do same things then why macros , there are three reasons
// 1) Macros are constant and there is no chance for it to get altered in any situation
// 2) Macros are better to read
// 3) Compilers are good with constants for generating the code 


/**
 * Why use define over const 
 * const :
 *  1) Used to create a variable or function that cannot be modifed ore alter later
 *  2) User memeory 
 *  3) can be used to declare const pointer 
 *  4) constant reamains as it is in preprocessing step while the macros are replaced with its expansion
 * Define: 
 *  1) Declare constants which are replaced by preprocessing step
 *  2) Uses no memeory 
 *  3) can be used to shorten the code 
 *  4) cannot be used to create constant poitner
 *  5) they can be used to replace the statement
 *  6) Everything defined using macro just get's replaced in preprocessing step
 *  7) If function is defined using macros it get's replaced with macros expansion but it is not called 
 *  8) Macros with arguments act like function although they are never called.
 *  9) Nested macros are not allowed
 *  10) Consumes memory in rom but not in ram
 *  if we compare const and define in terms of primitve data type difference is quite negligible.
 *  But for define a keyword 
 * 
 *  Note : 
 * macros make the program run faster but increase the program size, whereas functions make the program smaller and compact.
 * 
 * 
 * 
 *  To see the extended code or preprocessed code after preprocessing use command 
 *  cpp filename.c filetostore.i
 *  cpp prepep.c prepep.i
 */
```


### IO
```c
#include <stdio.h>
#include <string.h>

// console io
int main(){

    //printf("Format String", variables);
    // format string = simple character or strings, conversion specifier, escape character or sequence.
    // console IO :
        // 1) Formatted : printf(), scanf() since we have to specify the format of input and output while taking input and output.
        // 2) unformatted : getch(), putch(), gets(), puts(), getchar(), putchar()
    int var = 15;
    char str[] = "Value 1";
    // here the format is %dd d stands for width of the columns
    // this is format specifer
    float f = 1124.12313;
    // here 10 is the width and 1 is the precision ((width.precision))
    printf("%10.1f\n",f);
    printf("%-10d %20s\n",var,str);
    printf("%-10d %15s\n",var,str);
    printf("%-10d %10s\n",var,str);
    printf("%-10d %5s\f",var,str);
    //positive d justifies the character to the right
    // negative d justifes the character to the left

    char ch[100];
    // here sprintf prints the value to the character array not to the screen
    sprintf(ch,"this is format string\n"); // sprintf() is a function available in c 
    printf("%s",ch);
    
    char anch[100];
    scanf("%s",anch);
    printf("%s",anch);
    getchar();
    putchar(anch[0]);
    //getch, getche, getchar, fgetchar() only getchar() works rest all doesnot works 
    //putch putchar() fputchar() they can only work with one character 
    // format of scanf()
    // scanf("format string", address of variable)
    // why don't we pass the address of the string in case of %s -> Becuase the name of the array points to the address of the zeroth index 4


    char gtc[100];
    gets(gtc);
    puts(gtc); // puts and gets can only work with one string at a time 
    // fgetc() & fputc() is used for file 
    // we can keep on taking input by applying for loop
    int flag = 1;
    while(flag){
        gets(gtc);
        int len = strlen(gtc);
        puts(gtc);
        if(len == 0){
            flag = 0;
        }
    }
    return 0;
}

/**
 * Operating System has its own facility for inputting and outputting data from and to the files and devices.
 * We can write a small programme to link C compiler to link with io facility of c
 * write code for linking language with IO and keep it in libraray compiler will link OS facility of IO with programe
 * C has no provision for I/O
 * types of OS : 
 *  1) Console IO 
 *  2) File
 *  3) Database
 * 
 * Console is basically combinatino of keyboard and screen
 * Format specifier tells in what format the value of the variable will be printed
 * while passing the values from keyboard we will seperate the values with blanks, tabs or newlines
 * sscanf( ) function allows us to read characters from a string and to convert and store them in C variables according to specified formats.
 */

```



### Loops
```c
// for, while, do while, the odd loop, break , continue
// a++ post increment
// --a pre incerment
#include <stdio.h>


int main(){

    //below given both of them are true.
    while(1==2)
        printf("False");
    
    while(1!=1){
        printf("False");
    }

    //this is the block of code 
    {
        int a = 14;
        printf("%d",a);
    }

    // variations of while loop
    int i = 0; //this is a loop counter 
    while(++i<10){
        printf("Increaising\n");
    }

    while(i++ < 20){
        printf("Post increasing\n");
    }

    while(i<30){
        printf("INcreasing in  block itself\n");
        i++;
    }

    //this will run but it will run for infinite time
    // there can be a null expression but not zero expression.
    // initialization, condition and increment/decrement part of for can be replaced with any expression 
    // null is also a valid equation.
    int j;
    for(;j<10;j++){
        printf("%d\n",j);
    }

    int k ;
    // here we can say initializatino works for just one time
    // here instead of incrementing we are taking input and checking if the gien input is correct
    // here initialization only works for once 
    for(scanf("%d",&k);k<10;scanf("%d",&k)){
        printf("Yes\n");
    }
    /**
     * for(loopcouter_initial_Value;condition;increment_or_decrement){
     *  loop body// 
     * }
     * 1) Initialize 
     * 2) Check condition if true execute if false remove 
     * 3) Increament or decrement
     */

    // there can be multiple expression in initialization and increment but there can be only in condition checking
    // this is also correct form
    for(int l =0,m=4,n =2; l<10; l++,m++,--n){
        printf("%d",l);
    }


    return 0;
}


// LOOPS : Loops are approach or control instructions in computer programming that helps to execute some code iteratevly or repeatedly  until some condition is met for fixed amount.



// while 
/**
 * while loops keeps executing until the condition returns true or expression evaluated to non-zero values
 * the statements which are executed after while returns true is called body of the while loop it can be  single or a block of statement
 * It is short to impliment
 * While and for is used when condition is pre known to us.
 */

// do while 
/**
 * THis is used when we are not prior known about the condition.
 * Do while executes atleast for one time
 * THis is also called odd loop
 * In while condition is checked before executing the condition and in do while condition is checked after executing the do body
 * do while is used so that the loop is ececuted atleast once.
 */


// BREAK
// Break is used to immediately come out of the loop
// the control is passed to the first statement after the loop in which break is used
// in case of nested looop control is passed to the outside loop in which nested loop was placed


// CONTINUE 
// continue passes control to the begining of the loop by bypassing the everystatment after continue is appeared.


// all of the above statements are control flow statement.
// types of control statements : if, else-if, else, switch.
```


### Dynamic memory

```c
#include <stdio.h>


int main(){



    return 0;
}


// malloc -> malloc() takes the size of memory (no of bytes) to be allocated. malloc(10)
// it assigns the the memory and returns the base address
// the address it returns is always a void pointer* 
// so it has to be cased
// pointer means address
```


### Mesc 
```c
#include <stdarg.h>
#include <stdio.h>

typedef enum day da;
typedef int a;

#define male 1;
#define female 0;
#define married 1;
#define unmarried 0;


// bit fields this works fine
struct emp{
    unsigned gender:1;
    unsigned marriedStatus:2;
    // here gender will take 1 bit and married staus will take 2 bit
};

typedef struct emp em;

int aloo(){
    printf("HEY\n");
}

int *value(int *a){
    static int b;
    return &b;
}

void vairable(int c, ...){
    // there varibles are needed to work with this 
    //va_arg va_end va_start va_list va_copy
    // printf() // runs through the format specifier and finds out the no of variables in printf() function

}

union aliean {
    int age;
    char name[10];
};

int main(){
    enum day{
        sunday, monday=104, tuesday, wednesday, thursday, firday, saturday
    };
    // here sunday has 0 but tueday has 105 next is +1 of previous
    // variable d is of type day which has value tuesday it cannot have any other value than given above 
    enum day d= tuesday;
    printf("%d\n",d); // by default its int so we have to use int while applying operations on it 

    em e;
    e.gender = male;
    e.marriedStatus = married;
    
    printf("%d %d\n", e.gender, e.marriedStatus);


    printf("%p",aloo);
    
    // here we are declaring the function pointer 
    int (*func_ptr)();
    func_ptr = aloo;

    (*func_ptr)();
    func_ptr();

    int b  = 14;
    int *val = value(&b);
    printf("%p\n",val);
    // if the function returns the local address it disappers becuase the address disappers after the function is returned 
    printf("%p\n",&b);

    union aliean a;
    union aliean *at;
    at = &a;
    // here the memory allocted to age and name is same
    a.age = 15;
    // we are manuplating the first byte of name but our age is being manuplated becuase they share same memory
    a.name[0] = '1';
    printf("%p\n",at);
    printf("%p\n",&a.age);
    printf("%p\n",&a.name);

    printf("%d",a.age);
    return 0;
}

// enum
// typedef
// typecasting
// bitfields
// function pointer
// function with variable number of arguments
// unions


// enums :
/**
 * Enumeration 
 * - Are used to define the datatype which can take fixed no of values 
 * - Like day is datatype with possible values sunday, monday, tuesday, wednesday, firday, saturday, sunday
 * - C has int data type but what sort of value it can take is left upto the user 
 * - But for enum you have to define datatype along with all the possible values
 * - The values of enums are called enumerator, internally they are treaded as int by compiler like sunday is 1, monday is 2 etc 
 * - We can change this by assinging value to it the next value in enumerator is +1 of the previous eneumerator 
 * - In first part define the datatype and in second part assing values to it.
 * - Same functionality can be acived with macros but they are lengthly and have global scope
 */



// typdedef
/** typedef is used to redefine the name of the data type
 * they can also be used to rename pointer data types
 * they can only be used with datatype
 */


// typecasting
/** 
 * typecasting is used to convert the one datatype into another according to compatibility 
 * like void can be converted into int 
 * int can be into float
 * eg 
 * float a = (float) 5/2; result 2.5
 * above is the syntax of type conversoin 
 */


// bit fields 
/**
 * They are used to save the space 
 * Suppose there is just a no one and zero which can be packed in 1 bit so why to waste 4 bytes of memory
 * This can be acieved using bit fields 
 * bit fields are used to make more data in a byte
 */



// pointer to a function 
/**function also has address in c
 * we can simple get functions address my mentioning its name
 * they are used for dynamic binding of the function at run time
 * function name itself has an address
 */


// function returning the pointer
/**
 * function shoudl always return a static pointer or a global pointer becuase if it returns the local pointer it will be disappered when functions returns and hence returns nil.
 * it can return any type of pointer but has to specify while declaring it
 */


// functino with variable no of arguments
/** functions are often called routine
 * 
 */


// UNIONS 
/** Unions are similar to struct just that they use the same space for all the variables.
 * what does that means ?
 * Means that variables cannot have distinct values.
 * All of them will have the same value since they share the same memory
 * If the varabiles have different size then the size of the union is total size of the largest variable.
 * unions can be nested into strucutre or structures can be nested into unions
 */




// Volatile 
/**
 * Volatile is a qualifier that alerts the compiler that this variable value can be changed any time and hence each time it is used it has to be accesed from the meemory which is current value
 * What compiler does it inorder to opitmize the programe it sotres the value in register which is not fetched again and again 
 * but volatile say compiler no don't optimize it becuase it's value can change any time
 * 
 */


// NOTE: 
/*
* Register variable has no memory adress;
* 
*/
```#include <stdlib.h>
#include <stdio.h>
#include "included.c"
#include <string.h>

typedef struct member m; // shoretning code
// this is the decleration of strucutre and it's variable at same time 
// this doesnot reserves a space in  a memeory.
// they are mostly defined in another file to keep it safe and simple.
// this is the type declaration of the strucutre i.e. this strucutre is of type member.
struct member{
    char name[50]; 
    char desig[100];
    int age;
}a,b,c;

// here z is declared and defined only once at same time.
int x=4;
int y;
int y;
int x; // this is both defined and declared 
extern int i; // this is the only case where variable is declared but not defined else it is defined and declared at same time
/**THis wont work 
 * int x = 14;
 * int x = 15;
 */


union computer{

};

struct engine{
    int hp;
    char fuel_type; 
};
struct car{
    char name[10];
    int model;
    struct engine e;
};


void printstruct(struct car *c){
    // we have to use arrow operator access the elemets using the pointer notation
    printf("%d\n",c->model);
    printf("%d\n",c->e.hp);
}


int main(){

    int x;
    // int x ; gives here 
    struct st{
        int id;
        char name[16];
    }st1;

    printf("%p\n",&y);
    printf("%p\n",&y);
    printf("%p\n",&x);
    printf("%d\n",*(&x));
    // printf("%p\n",&i); // here we are trying to access the variable which is undefined 

    // we have just declared it and it has been asigned a value.
    // here we can access the memory address of each field in the struct seperately.
    m m1, m2,m3;
    // here m1 and m1.name will have same address since m1 will always point to the first element of strucutre
    printf("%p\n",&m1);
    printf("%p\n",&m1.name);
    printf("%p\n",&m1.age);
    printf("%p\n",&m1.desig);
    printf("%p\n",&m2);
    printf("%p\n",&m3);

    printf("%s",m1.name);

    
    m mem[10];
    // mem will point to first address of array
    // when we increament mem it will point to the next address of the same type.
    // here total size of m is 154 bytes but compiler assigns 156 bits by adding padding of 2 bytes to make number divisible by 4
    // because elements are allocated memeory continiously and they integer at address 150 or 151 cannot be accessed so two bits padding is added.
    //compiler aligns every element of a structure at an address that is multiple of four.
    printf("%lu\n",sizeof(m1));
    // this will print same value since array always points to the address of first element
    // this is called as struct pointer 
    m *me = mem;
    printf("%p\n",mem);
    printf("%p\n",&mem[0]);
    // while incrementing it will point to the next address of the same variable 
    printf("%p\n",me+=3); // this is same as mem[3];
    printf("%p\n",&mem[1]);

    // value of one struct can be copied to another struct
    // reason is yet to be readed 
    m1 = m2;
    // we can also nest strucutre into another strucutre 
    // structure being nested should always be previously defined before nesting strucutre
    struct car c1,c2;
    c1.model = 2022;
    c1.e.hp=1400;
    c2=c1;
    //strucutres can be passed to another function as well, it can be done with pass by value or pass by reference
    printstruct(&c1);
    return 0;
}


/**
 * primitive data types : int, float ,char etc 
 * Non-primitive : derived from primitive 
 * Primitive are atomic data types.
 * Array is a collection of multiple atmoic data types of same type.
 * structure is a process of grouping mutiple atomic datatypes together to form single entity. This data types may or may not be of same type.
 * Declare, Define, Access
 * Strucutre defines the new data type which is grouping of multiple atomic data types.
 * THe space allocated to the structure elements are always adjacent to each other.
 * elements of strucutre are always stored in contigious memeory location
 * They are accessed using dot operator 
 * working of arrays of char, int , float , struct or any other work in same way.
 * linkfloat() helps to link floating point emulator into application. Since floating point emulator helps to work with float values.
 */



/*
Decleration : When we specify the type and identifier of the variable. No memory is assigned when variable is declared.
Decleration initialization, assignment initialization.
Defination : Variable is deinfed when memory is allocated  it the variable. or when it is assgined a value
Initialize : To assign an initial value to the variable.
Access : To reterive the value at given memory location.
You can declare variable with same name multiple times outsite the main function. But cannot define variable with same name multiple times.
But this is not possible inside main function.
*/

/**
 * why strucutres are not object 
 * -> Because they just have data not any behaviour applied to it.
 * -> access modifers are not available in c so there in no public private and default modifiers in c strcut but available in cpp.
 */


```

### Strucuture : 
```c
#include <stdlib.h>
#include <stdio.h>
#include "included.c"
#include <string.h>

typedef struct member m; // shoretning code
// this is the decleration of strucutre and it's variable at same time 
// this doesnot reserves a space in  a memeory.
// they are mostly defined in another file to keep it safe and simple.
// this is the type declaration of the strucutre i.e. this strucutre is of type member.
struct member{
    char name[50]; 
    char desig[100];
    int age;
}a,b,c;

// here z is declared and defined only once at same time.
int x=4;
int y;
int y;
int x; // this is both defined and declared 
extern int i; // this is the only case where variable is declared but not defined else it is defined and declared at same time
/**THis wont work 
 * int x = 14;
 * int x = 15;
 */


union computer{

};

struct engine{
    int hp;
    char fuel_type; 
};
struct car{
    char name[10];
    int model;
    struct engine e;
};


void printstruct(struct car *c){
    // we have to use arrow operator access the elemets using the pointer notation
    printf("%d\n",c->model);
    printf("%d\n",c->e.hp);
}


int main(){

    int x;
    // int x ; gives here 
    struct st{
        int id;
        char name[16];
    }st1;

    printf("%p\n",&y);
    printf("%p\n",&y);
    printf("%p\n",&x);
    printf("%d\n",*(&x));
    // printf("%p\n",&i); // here we are trying to access the variable which is undefined 

    // we have just declared it and it has been asigned a value.
    // here we can access the memory address of each field in the struct seperately.
    m m1, m2,m3;
    // here m1 and m1.name will have same address since m1 will always point to the first element of strucutre
    printf("%p\n",&m1);
    printf("%p\n",&m1.name);
    printf("%p\n",&m1.age);
    printf("%p\n",&m1.desig);
    printf("%p\n",&m2);
    printf("%p\n",&m3);

    printf("%s",m1.name);

    
    m mem[10];
    // mem will point to first address of array
    // when we increament mem it will point to the next address of the same type.
    // here total size of m is 154 bytes but compiler assigns 156 bits by adding padding of 2 bytes to make number divisible by 4
    // because elements are allocated memeory continiously and they integer at address 150 or 151 cannot be accessed so two bits padding is added.
    //compiler aligns every element of a structure at an address that is multiple of four.
    printf("%lu\n",sizeof(m1));
    // this will print same value since array always points to the address of first element
    // this is called as struct pointer 
    m *me = mem;
    printf("%p\n",mem);
    printf("%p\n",&mem[0]);
    // while incrementing it will point to the next address of the same variable 
    printf("%p\n",me+=3); // this is same as mem[3];
    printf("%p\n",&mem[1]);

    // value of one struct can be copied to another struct
    // reason is yet to be readed 
    m1 = m2;
    // we can also nest strucutre into another strucutre 
    // structure being nested should always be previously defined before nesting strucutre
    struct car c1,c2;
    c1.model = 2022;
    c1.e.hp=1400;
    c2=c1;
    //strucutres can be passed to another function as well, it can be done with pass by value or pass by reference
    printstruct(&c1);
    return 0;
}


/**
 * primitive data types : int, float ,char etc 
 * Non-primitive : derived from primitive 
 * Primitive are atomic data types.
 * Array is a collection of multiple atmoic data types of same type.
 * structure is a process of grouping mutiple atomic datatypes together to form single entity. This data types may or may not be of same type.
 * Declare, Define, Access
 * Strucutre defines the new data type which is grouping of multiple atomic data types.
 * THe space allocated to the structure elements are always adjacent to each other.
 * elements of strucutre are always stored in contigious memeory location
 * They are accessed using dot operator 
 * working of arrays of char, int , float , struct or any other work in same way.
 * linkfloat() helps to link floating point emulator into application. Since floating point emulator helps to work with float values.
 */



/*
Decleration : When we specify the type and identifier of the variable. No memory is assigned when variable is declared.
Decleration initialization, assignment initialization.
Defination : Variable is deinfed when memory is allocated  it the variable. or when it is assgined a value
Initialize : To assign an initial value to the variable.
Access : To reterive the value at given memory location.
You can declare variable with same name multiple times outsite the main function. But cannot define variable with same name multiple times.
But this is not possible inside main function.
*/

/**
 * why strucutres are not object 
 * -> Because they just have data not any behaviour applied to it.
 * -> access modifers are not available in c so there in no public private and default modifiers in c strcut but available in cpp.
 */
```


### String in c
```c
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void xstrcat(char *target, const char *source){
    while (*target != '\0')
    {
        ++target;
    }
    
    while (*source != '\0')
    {
        *target = *source;
        ++target;
        ++source;
    }   
    //custom strcat function to concatinate the strings 
    //here we are not checking the size of the string
}

int main(){
    //shortcut to initialize the string
    char str[10]="anuj"; //'anuj' string literal constant here \0 is not necessary c inserts automatically
    char loneg[10]={'a','b','c'};
    int len = sizeof(str)/sizeof(char);
    for(int i =0; i < len; i++){
        printf("%c\n",str[i]);
        printf("%c\n",loneg[i]);
        printf("%d",loneg[i]);
        if(str[i]=='\0'){
            printf("%d",str[i]); //ascii value of \n = 0
            printf("Found\n");
        }
    }
    printf("%s\n",str);
    printf("%s\n",loneg);

    char word[100]="HEy";
    char nerd[5]="nerda"; //here the length of array should be always one greater than size of string
    puts(word); // puts put cursor in next line unlike in printf we have to use linebreak.
    puts(nerd);
    scanf("%[^\n]s",word);

    printf("This is nred string");
    // we can assing literal to a string or to a address
    char ch[]="Idea is noice"; //this is not reassignable 
    char *cr="This is nice"; //this is not modifiable
    // ch[1] = 'a';//this works
    // ch = "THis gives error";
    //ch="This is to be changed"; // this won't work
    // cr = "How is it fine"; //this works fine
    // cr[2]='a'; //this gives run time error


    //string functions 
    //in string one character is equal to one bite
    // no of character in a string is equal to the length of string null character is excluded
    char strr[]="This is new string";
    char strr2[]="This is new string";
    int slen = strlen(strr);
    printf("%d\n",slen);

    // strcpy
    char target[]="This is working here un limited here";
    char source[]="Fucking getting copied";

    strcpy(target,source); // here this works because one by one characters are copied into the target variable
    // here strcpy takes base address of the strings instead the whole string and keeps increasing it
    printf("%s\n",target); 

                //below is immutable
    char *p = "String pointer"; // here pointer points to the first address of the first character.
    p = "jey";
    printf("%p\n",p);
    printf("%s\n",p); //percent %s aspects pointer the string not the address of specific character where * derefresencing refrences to the specific character.
    // printf("%s\n",*p) this is wrong
    printf("%c\n",*p); //this is correct and is the first character of the string.
    printf("%p\n",&p);
    p = "New string"; // string literal has an address i.e "New string has an address"
    printf("%s\n",p);
    printf("%p\n",p);
    printf("%p\n",&p);

    //strcat
    char starcatt[100]="this is target variable";
    char sourcestr[]="and appended here";
    strcat(starcatt,sourcestr);
    printf("%s\n",starcatt);

    char new[100] = " To be appended";
    char modd[] = "Appended";

    xstrcat(new,modd);
    printf("%s\n",new);



    //difference between char cr[] & char *ptr;

    char mutable[] = "this is mutable string"; //this is stored in mutable array which is created in stack 
    // first mutable array is created for size 1 greater than string then it each character is coped into the stack.
    // arrays are modifiable since they are stored in stack
    char *ptrrr = "this is immutable string"; // this is immutable string and literal is stored in read only section of programme 
    //*ptrrr is stored in stack which points to the first address of immutable string
    // since literal is stored in the read only memmory so they cannot be modified.
    // ptrrr points to first address
    // *ptrrr points to first character

    int k = strcmp("Jerrt","Jerry");
    printf("%d\n",k);
    // strcmp returns 0 if string are same
    // is they are not same if will return the differnece between the character ascii value of first index e.g [ascii(y) - ascii(t)]
    // here the intention is just to find out wheather they are same or not

    // two dimensional character array
    // they are similar to 2d int array;
    char twodar[][10]={
        "ida",
        "idea",
        "Noida",
        "Voida",
        "Soida",
    };
    //we can also achieve same functinality using array of pointer
    char *arrpte[10];

    char string[199];
    
    // printf("%d",strlinglen); // strlen returns the length of the string which is not null character or the length before the null character.

    char *pp;
    for (int i = 0 ; i < 10; i++){
        printf("Enter the new Name\n");
        scanf("%s",string);
        int strlinglen = strlen(string);
        pp = malloc(strlinglen+1);
        strcpy(pp,string);
        arrpte[i]=pp;
    }
    for (int i = 0 ; i < 10; i++){
        printf("%s\n",arrpte[i]);

    }

    char strrrr[4]="anuj"; // if we do this s continuously reads the next value until it finds the null character "\0";
    char strrrrr[6]="verma";
    printf("%s",strrrr);

    return 0;
}

/**
 * String is an array of character
 * A string constant is a one-dimensional array of characters terminated by a null ( ‘\0’ )
 * If a collection of character is not terminated by '\0' it is not a string it's just a collection of string.
 * \0 and 0 are different \0 ascii value is 0 where as 0 = 48
 * \ ecape sequence \0-> null character 
 * array elements are stored in contiguous memory locations and on incrementing a pointer it points to the immediately next location of its type.
 * %s can be used to print collection of character or string itself.
 * gets() and puts are used to receive space seperable words
 * we can assing literal to a string or to a address we can modify string of an address not not of char array becuase it a constant pointer.
 * Also, once a string has been defined it cannot be initialized to another set of characters. Unlike strings, such an operation is perfectly valid with char pointers
 * For arrays, you cannot reassign the array name to a different array or string. This is because the array name is treated as a constant pointer to the first element of the array1
 * Here in string each constant literal has an address where is stored e.g "This also has an adress"
 * String literals are stored in read only memory i.e in code or text segment while initializtion or compiling the code
 * string literals are initialized and stored in read only memory.
 * Pointer points to the first address of the string.
 * String literal in c are immutable.
 * in C constants are defined by Capital letters that is the convention
 * %s takes the base address and keep iterating until it reaches the null character 
 * C style string is terminated by null character '\0'
 * We can work with string in three manners 
 * Array[]="some value"
 * *pointer to literal || *ptr = "Literal";
 *  dynamic memory allocation;
 *  array of pointers to string is preferred
 *  string is a collection of character
 */
```


### Switch
```c
#include <stdio.h>


int main(){
    int idea;
    switch(idea){
        case 1:
            printf("HEY");
            break;
        case 2:
            printf("Hello");
            break;
    }

    // d can ve any valid expression
    // cases == only char or int
    int d;
    
    switch (scanf("%d",&d))
    {   
        // this statement will never get executed at all.
        printf("This won't work\n");
        case 1:
            // here we can write multiple statement that will be followed if case statemnet is followed.
            printf("Week Day Monday\n");
            goto label;
            int c = 'a'+'b';
        case 2:
            printf("Week Day Tuesday\n");
        case 3:
            printf("Week Day Wednesday\n");
        case 4:
            printf("Week Day Thursday\n");
        case 5:
            printf("Week Day Friday\n");
            break;
        case 6:
            printf("Weekend Saturday\n");    
        case 7:
            printf("Weekend Sunday\n");
            break;
        default:
            printf("ENter valid day\n");
            // there is no need of break statement after default.
            // since control comes out of the loop any way.
    }

    label:{
        printf("Hey THis is goto statment\n");
        printf("%d",2+4);
    }

}



// switch-case-default
/**
 * Swtich subject to change
 * swithc-case-default is a control statement that allows us to select from multiple choises 
 * switch executes the case where a match is found and all the subsequent cases and the default as well until no break is encountered
 * switch cases only accept integers that is int and char(since it is converted into ascii value) 
 * we cannot use any comparison in case in switch
 * case must always have a constant value
 * Break and continue cannot be used with control statements like if, else-if 
 * there can be a nested switch but it is rarely done
 * Switch is fater then if-else ladder but due to restriction of being used only with char and it it's use is limited
 */

/**Working of switch 
 * if-else comparision is performed on runtime 
 * in switch look-up or jump table is created during compilation.
 * and when expression is fed it simply checks ths jump table to check which statement to execute.
 * Creation of jump table takes time so if-else ladder with less complex expression or less no-of comparision will take less time.
 * 
 */


// goto KEY WORD
/**
 * We should always avoid using goto becuase we never know how the control will be transfered to the certain block of the code.
 * goto helps to transfer the control to certain part of code.
 * there is lalbel and there is expression assigned to a lebel 
 * lalbel:print("HYe");
 * if we use goto to pass control to certain block of code the conrtol never reached back to caller of goto.
 * The usage of the goto keyword should be avoided as it usually violets the normal flow of execution
 */
```


### Comiliation Flags in gcc and g++
### C and C++ Compilation Flags

### 1. Basic Compilation Flags
- **`-c`**: Compile source files to object files without linking.
- **`-o <file>`**: Specify the output file name.
- **`-I <dir>`**: Add directory to the list of directories to be searched for header files.
- **`-L <dir>`**: Add directory to the list of directories to be searched for libraries.
- **`-l<library>`**: Link with a specific library.
- **`-std=<standard>`**: Specify the C/C++ standard to compile with (e.g., `-std=c11`, `-std=c++14`, `-std=c++17`).

### 2. Optimization Flags
- **`-O0`**: No optimization (default).
- **`-O1`**: Basic optimization.
- **`-O2`**: Moderate optimization, balancing speed and code size.
- **`-O3`**: High optimization, focusing on performance.
- **`-Os`**: Optimize for size.
- **`-Ofast`**: Optimize aggressively, disregarding some standard-compliance rules.
- **`-Og`**: Optimize for debugging experience while retaining good performance.

### 3. Debugging Flags
- **`-g`**: Generate debugging information.
- **`-g3`**: Include extra debugging information (like macros).
- **`-ggdb`**: Generate debugging information specifically for GDB.

### 4. Warning and Error Flags
- **`-Wall`**: Enable most compiler warnings.
- **`-Wextra`**: Enable additional warnings beyond `-Wall`.
- **`-Werror`**: Treat all warnings as errors.
- **`-Wpedantic`**: Issue warnings for non-standard code.
- **`-Wshadow`**: Warn about variable shadowing.
- **`-Wconversion`**: Warn about implicit conversions that may alter a value.
- **`-Wunused`**: Warn about unused variables, functions, etc.
- **`-Wuninitialized`**: Warn about uninitialized variables.
- **`-fmax-errors=<n>`**: Limit the number of errors to `n`.

### 5. Linking Flags
- **`-shared`**: Create a shared library.
- **`-static`**: Create a static binary, linking all libraries statically.
- **`-rdynamic`**: Pass all symbols to the dynamic linker.
- **`-pie`**: Create a position-independent executable.
- **`-fPIC`**: Generate position-independent code (typically for shared libraries).
- **`-fPIE`**: Generate position-independent executable.

### 6. Preprocessor Flags
- **`-D<macro>`**: Define a macro.
- **`-U<macro>`**: Undefine a macro.
- **`-E`**: Stop after the preprocessing stage; do not compile.
- **`-P`**: Inhibit generation of line markers in the preprocessed output.

### 7. Profiling and Analysis Flags
- **`-pg`**: Enable profiling for `gprof`.
- **`-fprofile-arcs`**: Generate coverage information.
- **`-ftest-coverage`**: Generate test coverage information.
- **`-fno-inline`**: Disable function inlining, useful for profiling.

### 8. Language-Specific Flags
- **`-fno-exceptions`**: Disable exception handling in C++.
- **`-fno-rtti`**: Disable Run-Time Type Information (RTTI) in C++.
- **`-fno-threadsafe-statics`**: Disable thread-safe initialization of static variables in C++.
- **`-std=gnu++11`**: Use GNU extensions with a specific C++ standard.

### 9. Linker Flags
- **`-Wl,<option>`**: Pass specific options to the linker.
- **`-Wl,-rpath,<path>`**: Set runtime library search path.
- **`-Wl,-Map=<file>`**: Generate a map file.
- **`-Wl,--as-needed`**: Link only needed libraries.

### 10. Miscellaneous Flags
- **`-v`**: Show the commands executed by the compiler.
- **`-pipe`**: Use pipes rather than temporary files for communication between processes.
- **`-pthread`**: Link with the POSIX threads library.
- **`-m<architecture>`**: Compile for a specific architecture (e.g., `-m32`, `-m64`).

### 11. Experimental and Non-Standard Flags
- **`-fconcepts`**: Enable concepts (experimental in some versions of GCC).
- **`-fmodules`**: Enable C++ modules (experimental).

### 12. Cross-Compilation Flags
- **`--target=<target>`**: Specify the target architecture for cross-compilation.
- **`--sysroot=<dir>`**: Use the specified directory as the system root for cross-compilation.
