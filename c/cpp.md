# CPP or CC (Mid level programming language)

## Basics
```cpp
    /**
 * There are different ways of writing the programe and everyone's algorithm is different and unique but we select the unique one.
 * 
 * 
 */
#include <iostream>

using namespace std;


/*
Comment should be about what does the programme does rather than how it does;
this is multiline comment
*/

// single line comment

int main(){

    cout<<"Excertion operator"<<endl; // insertion operator 
    int a; 
    cin>>a; // extraction operator input operator 
    cout<<a<<endl;
    int t = 5;
    cout<<t<<endl;
    return 0;
}



/**
 * NOTE 
 * in cpp every identifier has a namespace. the default namespace is global & it can be accessed using :: empty scope resolution operator
 * A string evaluates to itself.
 * cout and cin are objects and endl is a manuplater. 
 * output to a file ./a.out >>output.txt <<input.txt (io redirection)
 * syntax : contrustion rule or grammer to form sentence or statement
 * symantic : meaning of a sentence or statement
 * 
 * program : keyword, characterset, operators and rule guiding all of them.
 * 
 * The smallest individual unit of a program written in any language is called a token.
 * token = special symbol, identifer, word symbols
 * 
 * special symbol (+, - , *, /, ., ;, ?, , <=, =>, == , != , blank)
 * word symbols : reserved keywords
 * identifers : name of variable, constant, functions (can only be made of letter, digit and underscore)
 * cout is a predefined identifer whose meaning can be re written
 * keyword's meaning cannot be redefined but predefined identifer's meaning can be re written ore re defined
 * c++ identifers can be of any length
 * you shouldn't start identifer with underscore because it causes the compiler to distinguish between vendor specific and user defined identifer
 * whitespace : space, tab , linebreak etc 
 * 
 * 
 */

```

## Start
```cpp
    #include <iostream>
#include "included.cpp"
#include "included.cpp"
#include <math.h>
#include <time.h>

// we are defining here that x is already present somewhere outside
extern int x;



using namespace std;
// this creates ambugity;
using namespace Multiply;
// using namespace Divide;


int main(){
    cout << "\a"<<endl;
    // this clears
    cout<<Multiply::calculate(4,5)<<endl;
    cout<<Divide::calculate(20,10)<<endl;
    Multiply::idea = 14;
    Divide::idea = 16;
    cout<<ceil(2.5)<<endl;
    cout<<floor(2.5)<<endl;
    cout<<time(0)<<endl;
    // here idea takes the default scope of multiple since we have declared using namespace Multiply
    cout<<idea<<endl;
    cout<<x<<endl;
    int x = 4;
    cout<<::x/x<<endl;
    return 0;
}



/**s
 * Types of programming 
 * 1) Declerative
 * 2) Procedural
 * 3) Structural 
 * 4) Object-oriented
 * 5) Functional Programming
 * 
 */

// Execution and file creation at different steps 
/**
 * Generate file with preprocessed  g++ -E filename.cpp -o filename.i
 * Ececutable stage g++ filename.cpp -o filenameg
 * generate assembly code : g++ -S filename.c -o file.s
 * generate object fiel : g++ -c filename.c -o file.o
 */

// \ this is scape character when compined with words like n t forms scape sequence 
// \n \t etc are escape sequence


/**Namespace 
 * Or we can say namespace is the process of grouping identifiers and giving it a context or declerative region to avoid naming conflicts.
 * namespace is a way to avoid naming conflits of the variable in cpp.
 * They are needed when you want one or more variables and functions to be on same name. 
 * We ofetn use namespace with scope resolution operator :: 
 * Namespace is a declerative part that helps to define the scope of varibles and functions collectively calling identifiers
 * They can only be defined globally.
 * If the identifers  doesn't have any identifier than it has by default global namespace.
 * Using is a derecitve that elemintes specifying the scope of the identifer.
 * Namespaces can be nested into another namespace.
 * Namespace provides context to the identifier whereas the scope provides visibility to the identifer 
 * A namespace is a group of software components with the same name prefix
 */

/**OOPS 
 * 
 * inheritance : 
 *  -> Inheriting the properties from ansestors
 * 
 * 
 * polymorphism: 
 *  -> When object can behave differently in different situations
 *  1) method overloading : compile time polymorphism 
 *  2) method overriding : run time polymorphism 
 *  3) Operator overloding
 *  4) Shallow copy and deep copy;
 *  5) STL standard template language;
 * 
 * 
 * Abstraction
 *  -> Hiding the implementation detail i.e. how but what is done is always known.
 * 
 * 
 * Encapsulation
 *  -> Data and functions are grouped together to form an object i.e. functions can be called on data without explictly having to pass data to function.
 *  -> This helps to save data from careless manuplations.
 *  -> Members of a function can only be changed using it's own function hence outsider's cannot manuplate the data of the object.
 *  -> Private data is not exposed i.e. it is a data hiding.
 * 
 */

// Strucutral programming : Set of modules and functions are used to develop programmes. They use the control instruction. 
// Object oriented programming : Set of objects are used to develop programme
// procedural programming : function,routine or procedure calls where one routine calls other for execution.


// differnce between ceil and floor : 
// ceil rounds up to the nearest up integer 2.7 = 3
// floor rounds up to the nearest down integer 2.7 = 2
// parameter are used while defining the function
// argumetns are used while calling the function


// function prototype is the name of the function with its return type, no of params.
// it define the strucutre and let the compiler know about the function.

// BLOCK of code 
// one or more than one statement grouped together using {} is called block of code.
// {
    // this is a block of code 
//}


// enumerators is the name given to the integer values. 
// enum is datatype that takes fixed no of values.


// global variables are variable that are available to every part of the programme despite of where it is declared.
// while declaring the global vairable every file that uses the global variable must declare it as a extern except the one declaring it.
// when you declare global variable in header file varible will be instantiated for every file including the header file and produce link error. so it should be defined in the source file. 
// so what we do is we declare all the global variables in a external.h file and we include this file wherever we want so that we don't have to include it again and again.
// to use variable of global namespace we use :: unary scope resolution operator


// storage classes : 
// 1) auto/local :: variable created without any storageclass is auto or local
// 2) register
// 3) extern 
// 4) static


// SCOPE 
// fielscope : declared outsite the main function contains a file scope or outside of any function body
// functoin scope : only accesible inside a function 
// block scope : variables only accessible inside a block scope 
// function prototype scope : Identifers declrared inside function prototype



//constant function tells the compiler that the function doesn't modify the variable.
// constant variable are to be initialized immediately they are declared
// const helps us to achieve principle of least privilege



// inline function 
// short function not called but replace with code on inline function inside calling function


// calling function 
// call by value void func(a,b)
// call by reference void func(a,b);
// call by reference with pointer void func(*a, *b); 


/** Computer history 
 *  Abacus first calculating device 
 *  Pascaline also for sum  
 *  Holes on a punchcard were used to feed instruction to ancient computers.
 *  Charles babbage : difference enginer, analytical engine(input, processing, output)
 *  Tabulating machine company is called IBM today
 *  Mark I first computer like machine , 52 feets, 50 tons, 750000 parts.
 *  Today's computer architecture : Jhon vonn neumann in 1940
 *  UNIVAC : universal and automatic computer in 1951
 *  1956 : transistors , fortran, cobol for software industry
 *  1970 : microprocessor and entire cpu on a single chip
 *  1977 : apple 
 *  1981 : IBM's first personal computer 
 * 
 *  Components : 
 *      Main memory is an ordered sequence of cells,
 * 
 *  Electronic device uses Electronic signals 
 *      types of electronic signals : 
 *          1) Analog 
 *          2) Digital singnals 1,0
 *          Computer uses digital singals and the language that computer understands is machine language.
 *          machine language : 1 or 0 i.e. binary digits 
 *          bit = One binary digiat : Either 1 or 0 
 *          sequence of 8 bit's is = 1 byte 
 *          1024 byte = 1kb, 1024kb = 1mb, 1024mb = 1gb, 1024gb = 1tb 
 *          computers uses ascii to store information like letters and texts or characters which has corresponding ascii value 
 *          conversion
 *          [character -> Ascii -> binary]
 *          
 *          types of encoding : Ascii : 128 characters 0 - 127 - 7 bits 
 *          Unicode 65,536 characters : 16 bits : used for development
 *          EBCDIC : 256 characters : 8 bits used by IBM
 *          
 *          Sets of binary programme differs from computer to computer hence machine laguage differs from machine to machine
 *          assembly language provide a mnemonic form to code 
 *          assembler converts -> assembly code into machine code 
 *      
 *          compiling of cpp into machine language code : 
 *             
 *          high-level code --> preprocessing - > error checking -> object code -> Linker(links library code into programme) -> Loader Code(loads programme into main memory)
 * 
 *          
 *          [object code = equivalent machine code]
 * 
 *          -> .i extension = preprocessed file
 *          -> .s extension = assembly code 
 *          -> .o file = self compiled filed without linking 
 * 
 * 
 *          Programming : 
 *              1) problem solving 
 *              2) Analysing the problem 
 *                  1) outlining the requirements
 *                  2) Stake holders being affected 
 *                  3) User intraction
 *                  4) Data manuplation 
 *                  5) Produce output
 *                  6) Break it into subproblems 
 *              4) desigining the steps
 *          
 * 
 *      NOTE : 
 *          we must spend enough time to analyse the problem. Because analysis is done on pen and paper.
 * 
 * 
 *      TYPES : 
 *             structured : breaking down a problem into sub problem and finding a solution of that and combining them together to create a software
 *                          also called as : top-down design, bottom-up design, stepwise-refinement and modular programming
 *              object oriented Design : A problem is broken down into the components called objects and how they interact with one another.
 *                          operations on object'd data. Language that implements the OOD is called object oriented programming.
 *              Nearly every language today supports both strucuted and oops for different purposes.
 *              
 *              c & cpp was developed in 1980's in bell laboratories by bjarne stroustrup 
 *  
 *              ANSI : American national standard institution 
 *              ISO : International Standard Organization established in 1990's to define standard for c++;
 *              
 *              I will crack FLIP CART PPI for sure.
 */


/** writing a programe (Progrme life cycle)
 * Understand a problem: 
 *      breaking a problem into sub problem 
 *      understanding the requirements of the problem
 *      stake holder it affects
 *      all possible solution 
 *      implimenation of best one 
 * write a alogrithm
 * write a code
 * preprocessing
 * compiling
 * linking (different libraries and other object codes)
 * loading
 * running
 */

```


### Data types in cpp
```cpp
enum days{
    // here the values are called enumerators.
    // emumerators are the ordered set of values;
    // value of enumerator is an indetifer that takes and integer value;
    sunday=6, monday, tuesday, wednesday, thursday, firday, saturday
}d;

enum month{
    // here every month is a variable and since they are variable they cannot be used repedtly in the same block;
    januar, feburary, march, april, may, june, july, august, sepetember
};

// anonumis type decleration 
// here we cannot define the variable of the anonummis type apart from declaring it
// we cannot passs it to the function.
enum {idea, none, gerat, good}bfg;

//typedefs are used to define the alias for the already defined type names;

int main(){

    int b = 'A';
    cout<<b<<endl;

    float c = 5.3;
    float d = ++c; // preincrement
    cout<<d<<endl;

    d = saturday;
    enum days d2 = monday;
    d = days(d+4); // casting the values are allowed direct operations are not allowed
    cout<<d2<<endl;
    cout<<d<<endl;

    // relational operator are allowed on enumerations

    bfg = idea;
    
    return 0;
}

    /**
 * Simple : integer , floating, enumeration
 *      integeral :char, short, int, long, bool, unsigned char, unsigned short, unsigned int, and unsigned long.
 *      floating : float , double , long double;
 *      enumeration : helps programmer to define their own data type with fixed set of permissible values;
 *      simple data types are the types that can hold a single at a time.


 * 
 * strucutre : Similar to class but all members are public be default.
 *          arrys, strings, structures 
 *          strucutred data types are the collection of simple data types.
 
 
 *  
 * pointer 
 * 
 * expression : statement that evaluates to a value;
 * statement : anything that gives instruction to a comptuer;
 * 
 * 
 * casting in cpp can be done in two ways 
 * c like csting : int a = int('A');
 * c++ casting : int b = static_cast<int>('A')
 * Named constants are memeory location whose content cannot be modified.
 * the default type of floating point number is double
 * variable is named memroy location whose value can be changed at runtime.
 * when computer turns, every cell of memory takes some value which remains unchanged unless we explictly put some value into it. this is how variable gets value when it is declared.
 * cells have the value from the last operation which are not directly assigable becuase pointer is lost to them. which are seen when we declare but not assign the values. which is a garbage value.
 * 
 * variables can be assigned using two ways initialization and input read.
 * 
 * increment and decrement : pre and post
 * 
 * \ is escape character \n is a scapr sequence
 * 
 * string is a collection of characters; they are not default one.
 * 
 * prprocessor directives are the statements that instruct computer to peroform some sort of preprocessing before starinting some compilation.
 * preproessor directive tells the compiler which header file to include in the code.
 * 
 * we always return 0 in cpp or c to tell that the programme has successfully executed non-zero means programme has not successfylly executed.
 * 
 * user defined data types : 
 * enum, struct, classes, unions, typedef 
 * 
 */

```

### Control Strucutre 
```cpp
    /**Control strucutre
    * selection : if, else, if-else, switch
    * repetation : for, while, do-while
    * conditional operator 
    * break and continue
    */
```


### Arrays in cpp

```cpp
     // decleration and initialization together
    // there is a subscripted assgnment no direct assginment in cpp
    int a = 1, b = 2, c[sizee]={1,2,4,4,};
    int d[sizee]; // initialize later
    int *ptr = d;
    // here ptr and d will have same address
    cout<< ptr<<endl<<     /**Control strucutre
    * selection : if, else, if-else, switch
    * repetation : for, while, do-while
    * conditional operator 
    * break and continue
    */
    // value inside the double quoted sting is a character or string const which cannot be modified;
    ptrr = "This is null value";
    //ptrr[1] = 'a'; // this will produce error
    ptrr = "this is nice you now";
    char name[] = "Its nice weather";
    // name ='a'; // this gives error becuase arryy name is constant pointer to the first address of an array;
    cout<<name<<endl;
    // NOTE : 
    // if we have character array without null character or string terminiator we won't be able to apply string functions 
    // multidimensional array 
    // int arr[a][b]; // here is the multidimensinoal array


    /**Arrys size 
    * arrays size should be constant
    * the name of the array is the const pointer to the first element of the array
    * in java array is an object with the data and the length propertry but in cpp it's just a constant pointer to the first element
    */

```

### Functions 
```cpp

    void functionn(int a = 14, int b = 14){
        cout<<a+b<<endl;
        cout << a <<endl;
    }

    // overloading
    void functionn(int a=10, int b=12, int c=14){
        cout << a+b+c <<endl;
    }


    // call by reference 
    int* referenceser(int &a){
        return &a;
}
    // arugmets are assgined to the parameters from right to left order so 10 gets assgined to a not to b;
    // functionn(10);
    // here ambugity is created in overloading since compiler doesn't know whom to refer becuase both of them have default values
    // functionn();

    // the belwo one works fine
    functionn(1,2,4);
    // functionn(1,2); this will stil not work
    // ctrl+z or ctrl+d produces end of file command.


        /**
    * call by value
    * call by reference
    * call by reference with pointer
    * 
    */

    // by default the reutrn type is int 
    // this gives warning but it runs 
    // c++ is more strict than c so this wont work in cpp
    int main(){
        printf("this is another programe");
    }
    // two types of functions 
// value returning function 
// void function - function that doesnot include a return statement.

// Heading of function : Name of function, No of parameter, types of each parameter, return type
// body of the function : code of the logic
// combining the body and header forms a defination of a function.


// formal paramter : parameters used while defining or declaring the function
// actual parameter : parameters used while calling the function. Actual parameter is also known as argument.
// when arguments are passed in function while calling the actual parameters are copied into the formal parameters.
// curly braces are always needed to define the function to limit the scope, to group code together and present as one unit.


// function type , return type or return type of a data type.

// Expression : always returns value;
// statement : line of code terminated by value semi-colon; doesnot return a value. Every line of code is statement but that which return value is expression.
// statement says computer to do something i.e. instruction.
// Once a function returns something, the function call statement is replaced by the value returning function, but is not true for void functions.


// function prototype is a heading of a function.

#include <iostream>

using  namespace std;

// function cannot be define more than once.
// hence this will produce an error
// void nonne(){};
// but this won't produce any error
//return x, y;
//only the value of y will be returned becuse return only returns the last value.
void nonne();

// void paramter
void another();

int main(){
    int a = 14;
    int &b = a;
    cout<<b<<endl;
    int c = 15;
    b = c;
    cout<<b<<endl;
    cout <<"This is a function programe"<<endl;
}

void nonne(){
    cout<<"HEY";
}


    /***
    * function calls : 
    *      call by value
    *      call by reference 
    *      call by pointer 
    *      
    *  reference is an alias for the object i.e. the conetnet of reference is the content of the varible which it refers to 
    *  pointer's content is the address of the variable is points to.
    * 
    *  we can use value returning function directly into expression 
    *  
    * 
    *  we use pass with reference in 3 cases :
    *      when we want to modify the actual parameter
    *      when we to save time and memeory
    *      when we have to more than one value from function
    *  
    *  in reference paramter when actual parameter is passed the formal paramter points to the acutal paramter
    *  in pass by value when actual parameter is passed the values of actual parameters are copied into the formal paramter 
    *  formal paramter's have their own memeory location
    *  variables names have no memory storage, the address they points to have memory storage. 
    *  variable names are used by programmers to operate on variable, compiler uses the address and offset of the variable to operate on the operand
    *  reference variable once assigned cannot be changed;
    *  global identifiers are recommended to declare as constant
    *  global variable is by default static
    *  automatic members are created and delted when control reaches block and leaves the block
    *  we can access the global varaible with same name that of local variable using scope resolution operator.
    * 
    *  drivers are the programe that check the function programe 
    *  stubs are the functions with same as return type of actual function but not the correct value.
    * 
    * 
    *  Overloading : two definations having different formal parameter list.
    *  i.e different no of parameters or different types of parameters.
    * 
    * 
    *  signature of function : name and formal paramter lists signature of the function doesnot include the return type.
    *  some programmer calls function prototype or heading as a signature.
    *  
    *  when we change the reutrn type it comes under the function overriding.
    * 
    *  overlading: chaning the formal paramter list ,types or numbers
    *  overirding : chaning the defination of the function .
    *  in function overloading no of parameters passed defines which type of function will be called.
    */
```


### Inlude directive 
```cpp
    #ifndef INCLUDED_CPP

    #define INCLUDED_CPP
    int x = 14;
    namespace Multiply{
        int idea;
        int calculate(int a, int b){
            return a*b;
        }
    }

    namespace Divide{
        int idea;
        int calculate(int a, int b){
            return a/b;
        }
    }
    #endif

    // so this is checked here in the file to be included it checks if the contents are not already defined 
```



### String pointer 
```cpp

int main(){

    int a = 14;
    // pointer decleration and initializatoin
    int *ptr;
    ptr = &a;

    // type casting the value of the pointer to an integer
    cout<<(unsigned long long int)ptr<<endl;

    // constant pointer or pointer to a constant
    //char const *ptr; // this is a constant pointer
    //ptr = &a; // this is a constant pointer  this will give an error because constants have to assgined value immediately they are declared

    // if we are declaring a pointer that will point to constant it must also be declared as constant
    const int b=13; 
    // the statement below says that int is constant but not pointer
    const int *intptr; // here pointer is of type const integer , Here the we are defining the type of pointer not constant poitner
    // pointer is something that points to const integer 
    intptr = &b;
    intptr = &a;

    // inorder to declare a constant pointer we use 
    int * const ptrrr = &a; // this is the constant pointer of type integer  
    
    // using dereferencing pointer to print value
    cout<<*intptr<<endl;

    cout << sizeof(int)<<endl; // returns the size in bytes occupied by an element;

    const char *charpte = "this is pointer";
    char chtr[12]="1232342";
    cout<<sizeof(*charpte)<<endl; // here size of returns the size of the pointer variable
     cout<<sizeof(chtr)<<endl; // the size of returns the size of array
    return 0;
}

// the value of null is defined as 0 in iostream and several other header files
// functino pointer points to the address of the function; function name is the starting address of the function
// callback : when a function calls another function is called as call back.

```


### Primitives 
```cpp

// primitve types in cpp
/**
 * Module = %
 * cpp promotes the low level variable to higher level variable
 * = operator from right to left 
 * integer value of char is ascii value
 * Logic operator && || !
 * assignment operators
 * arithematic operator 
 */

```

### Structures 
```cpp
#include <iostream>

using namespace std;

void f(int const arr[]){
    for(int i = 0; i < 10; i++){
        // arr[i]=4 this statement cannot be run
        cout<<arr[i]<<endl;
    }
}

void d2(int const arr[][5]){
    for(int i = 0; i < 5; i++){
        // arr[i]=4 this statement cannot be run
        cout<<arr[i]<<endl;
    }
}

int main(){
    int arr[10];
    for(int i = 0; i < 10; i++){
        cout<<arr[i]<<endl;
    }
    // in cpp empty initializatin or partial initialization also leads to intitialize the array to 0
    int arr1[10]={};
     for(int i = 0; i < 10; i++){
        cout<<arr1[i]<<endl;
    }
    // passing array to the function
    f(arr);
    cout<<arr<<endl;
    cout<<&arr[0]<<endl;
    cout<<&arr<<endl;


    // name of the pointer is constant pointer that points to the first element
    // it holds the address of the first variable;
    // in cpp the function cannot return the array value


    // NOTE : 
            // any intergral type can be allowed as an array index i.e integer, char, bool i.e. they have real numbers.





    // cin.get only works with character not with string
    char idea[100];
    cin.get(idea,100);
    // no read after blank space
    string stringgg;
    cout<<idea<<endl;
    // the size of the item being passed to the function must match the defination of the function.
    // we can omit the first size of the 2d array.
    // we cannot omit the column length becuase computer has to know where row ends and another row starts
    int d2arra[5][5];
    d2(d2arra);
    return 0;
}


/**
 * Strucutred data type is a collection of simpler data types
 *  eg. list, arrays, string, structure etc
 * [] -> this is called array sub scripting operator.
 * we can also executre operation inside subscripting
 * static data items are intitialized by zero value by default.
 * 
 * aggerigate operation is a operation in cpp that manipulates the entire array at one
 * cpp prevents the aggrigate opertion on array i.e we have to operate on one element at a time
 * we can pass array to the function only using the reference not by anthing else so we omit the & symbol
 * we can prevent chaning the actual array by declaring the array parameter as a consBecause arrays are passed by reference only, you do not use the symbol & when declaring
an array as a formal parametetant parameter
 * 
 */

// compiler rembers the name of the array , the base address and no of components 
// name of the array points to the base address of the array
// the name of the array holds the base address of the array.



/** C-string or character array
 *  
 *  in c string is nothing but a array of character.
 *  inorder to be a string a char array must be null terminated
 *  inorder to work with cstring we have to include <cstring> 
 * 
 * 
 */
```

### String 
```cpp
    #include <iostream>


using namespace std;

int main(){

    // strings are always double quoted;
    // they cannot be single quoted;
    
    string name = "Anuj\0";
    string surname = "Verma";
    string surname1= "verma";
    cout<<name+" "+surname<<endl;
    cout<<name<<endl;
    cout<<name.length()<<endl;
    
    char name1[] = "Anuj verma";
    cout<<name1<<endl;

    // "This is the constant string"
    // "constant strings cannot be added"

    // manuplaction
    surname[4] = 'T';
    cout<<surname<<endl;
    // gives the alphabet at given index;
    cout<<surname.at(2)<<endl;
    //subscripting
    string newww = "adf";
    cout<<surname[2]<<endl;
    //append : include letter A at the end no of times
    cout<<surname.append(5,'A');
    cout<<surname.append("IsNice\n"); // string takes no of times
    // clears every character from string entire string
    surname.clear();
    cout<<"-----------------"<<endl;
    cout<<surname<<endl;

    // comparision;

    cout<<surname1.compare("verma")<<endl;
    cout<<newww.empty()<<endl; // returns 1-true if empty 0 is non-empty

    // size and length() gives the same result.
    cout<<surname1.size()<<endl;
    cout<<surname1.length()<<endl;


    // erase, find, insert, find_first_of(), replace, substr, swap
    string erasable = "Erasing String";
    cout<<erasable.erase(4,5)<<endl;
    cout<<erasable.erase()<<endl;

    string findingstring = "Finding the string in the string";
    cout<<findingstring.find("string");

    // substring 
    string str = "sub string";
    // substr(startindex, length)
    cout<<str.substr(5,3)<<endl;



    // inserting in string 
    // insert inserts the string at given position and extends the length;
    cout<<str.insert(4,"V")<<endl;

    str.swap(findingstring);
    cout<<str<<endl;
    cout<<findingstring<<endl;

    //converting the string to cstring
    //if needed we can convert the string into c string.
    str.c_str();
    cout<<str.length()<<endl;

    // mutalbe string
    // exept the below every string is mutable in cpp
    string baaf; 
    
    // immutable string;
    // this is immutable string at is c line string
    char const *ptr = "This is how it works";
    cout<<*ptr<<endl;

    // this is a get line function that takes blank space input in cpp
    getline(cin, baaf);
    cout<<baaf<<endl;

    return 0;
}

/**
 * C++ like string
 *      cpp string is not null terminated 
 *      available in <string>
 *      array of string 
 * c like string
 *      is always null temrinated 
 *      available in <cstring>
 *      2d c string is equivalent to array of string in cpp
 * 
 * 
 * both c and cpp has constant string they have and address;
 * both
 * 
 * 
 
 */


/**
 * Namespaces solves the problem of overlapping identifiers name.
 * suppose if global and local variables have same name then we use namespace to resolve this problem 
 * this provides a context and container to the variable which can be accessed using a namespace;
 * std is a namespace which means it is a standard objects or functions of a compiler
 * 
 */

// Resource acquasition is initializtion : 
// Desctrucotrs : hence finally is not used in cpp becuase when destrucotrs are called the resource is atuomatically freed 
// the main motive of the finally is to do some clean up code

// when we perform an arithematic operation on pointer :
// pointer points to the next element of the same type i.e increases by 1 element
// 1 element in 2d row means 1 row 
// 1 elements in struct means 1 strucutre etc etc i.e one element may have different meaning
```


### Pointer 
```cpp
`#include <iostream>
#include <string>


using namespace std;


class robot{
    private:
        string type;
        int capacity;
    public:
        // either we can define defualt parameter here or 
        robot(string t, int c);
        void printDetail(robot const &r)const;
        virtual void printrobot();
};   

// we can define default parameter here
robot::robot(string t =" " , int c=0 ){
    this->type = t;
    this->capacity = c;
}

void robot::printDetail(robot const &r)const{
    cout << *&r.capacity << "  " << *&r.type <<endl;
}
void robot::printrobot(){
    cout << "Print robot"<< this->type << "  " << this->capacity <<endl;
}


class Humanoid:public robot{
    private:
        int price;
    public:
        Humanoid(int price, string name, int capacity);
        void printHumanoid();
        void printrobot();
};

Humanoid::Humanoid(int price, string name, int capacity):robot(name, capacity){
    this->price = price;
}

void Humanoid::printHumanoid(){
    robot::printrobot();
    cout<<this->price<<endl;
}

void Humanoid::printrobot(){
    cout<<"this is the function of humanoid ";
}


void printall(robot &r){
    r.printrobot();
}


int main(){
    int a=14;
    int *ptr = &a;
    int *ct=0;
    cout<<ct;
    cout<<&ct;


    // returns the address of int to the dyn
    int *dyn = new int;
    // memory for array
    int *arr = new int[10];
    delete dyn;
    delete [] arr;
    *dyn = 143;

    cout<<*dyn;


    cout <<endl;
    robot r("humanoid",100);
    r.printDetail(r);

    Humanoid h1(10000000,"Chitti",1000);
    h1.printHumanoid();

    // here both function are being called of type robot not of type humanoid since it's a compile time binding.
    // here the compile time binding happens, which is also called early binding or early binding
    printall(r);
    printall(h1);


    // to overcome the problem of this we have to declare a virtaul function in front of a overloaded function;
    // virtual functions make a run time binding of a function.
    // this is called as a late-binding, dynamic binding or run-time binding.
    // to do this we add a viratual keyword in front of a function in base class
    // it is recommended to declare the destructor of a base class as a virtual.

    return 0;
}



// POINTERs

/** In c we can also use new operator to allocate memory dynamicly or delte to delete memory dynamically.
 * pointer's have no type i.e their type is the type of the value that is stored in the location that they point to 
 * const int a = 13;
 * int cosnt *ptr = &a;
 * here ptr points to address of a so type of ptr will be type of value stored at a i.e int 
 * 
 * address of operator (&) and derefrensing operator(*)
 * derefrensing is also known as value at an address.
 * * derefrensing pointer gives the value stored at a memeory location.
 * 
 * In c and cpp the NULL macro is expanded to 0.
 * that is it's value is zero and NULL is a macro;
 * 
 * by default's pointer are not initialized i.e. they have no value when they are created;
 * you have to initialize it using a NULL or zero NULL is a macro that expands to 0
 * 
 * 
 * 
 * Operations on pointers
 *  increment
 *  decrement
 *  comparision and relational 
 *  
 */



/**Dynamic variables : i.e. dynamic memory allocation
 *  keywords : new to create memory
 *  del = to delete
 *  Variables created at programe execution.
 *  Dynamic arrys 
 *  int * ptr = new int[10]
 * 
 *  new allocates the memory and points the pointer to the allocated memmory
 * 
 *  delete keyword : 
 *      deltes the memory pointed by the pointer
 *  
 *  delete pointer
 *  delete [] arr;
 *  
 *  when we delete the pointer the location being be pointed by pointer gets free
 *  which can be allocated to other variables;
 *  sometimes resources being pointed may not be deleted and that situation that pointer is called dangling pointer.
 *  dangling pointer may point to some other address so to avoid this situation we point the pointer to the NULL;
 * 
 *  when pointer points to the new memory location and the memory of the pervious pointed location is not freed it called as memeory leak
 *  memory leak is the situatino when the unallocated resources cannot be allocated to other resources.
 *  
 * 
 *  Name of array is a constant pointer to the first address of an array so they cannot be incremented or decremented
 *  but when pointer points to the name it is not constant pointer
 */



/** call by value, call by reference , call by reference with pointer
 * pointer, references and pointer references
 * 
 * 
 */


/**Shallow copy and deep copy
 * 
 * shallow copy points the variable to the same address
 * deep copy creates a new memeory address copies all the values and then points the variable to the new address.
 * 
 * 
 * Pitfalls : 
 * we have to delte the pointer variable that dynamically allocates the memory
 * when we use a defautl assignment operator in objects and object has a pointer then it performs the shallow copy.
 * assingment operators by defualt does a shallow copy unless we explicitly overload it. to perform a deep copy
 * 
 * 
 * Default copy constructor : 
 *  there is a default copy constructor that copies the value of one object into another object.
 *  default copy constructor is always created by the compiler 
 *  default copy constructor uses shallow copy in two cases : 
 *      initialization of one object using another object  using member-wise copy 
 *      an object is passed by value and the default member-wise copying of data is allowed
 *      general syntac of copy constructor 
 *              className(const className& otherObject);
 * 
 *  copy constructor executes in three situation
 *      paramenter is passed by value
 *      function returns the object value
 *      object is declared and initialized using the object value
 *  
 *  For classes with pointer member variables, three things are normally done:
        1. Include the destructor in the class.
        2. Overload the assignment operator for the class.
        3. Include the copy constructor.
 * 
 * 
 *  virtual functions : we can pass the object of derived class to the type of parent class while calling the function.
 *  friend functions
 *  operator overloading
 *  STL & Vectors 
 *  
 */


/**Differnece between value, reference paramter and a pointer 
 * 
 * 
 */



/**Abstract classes :
 *  abstract classes are classes which provide a prototype for derived class.
 *  thier object's cannot be made
 *  the classes which have one or more pure virtual functions are called abstract classes
 *  pure virtual functions are functions with no defination in base class
 *  classes inheriting abstract class must define every pure virtual function
 *  
 * 
 *  & address of operator 
 *  int z ;
 *  int &y = z;
 *  here & is used to make alias of a vairalbe that is referencing
 * 
 * 
 */


/**Three principles of OOPS : 
 * Encapsulation : abiblity of class to group data and functions on data together. so that no data of class can be acessed outside except by objects.
 * Inheritance : ability of class to inherit the properties and methods of other class is inheritance
 * polymorphism : overloaidng and overriding.
*/

/** NOTE : 
 *  1. Explicitly overload the assignment operator
    2. Include the copy constructor
    3. Include the destructor

*/

using namespace std;

class shape{
    int length;
    int breadth;

    public:
        // pure virtual function
        virtual void definedhape() =0;

};

// the above class is a abstract class since it contains the pure virtual function

int main(){
    // the below line of code will produce an error the object of abstract is not allowed.
    // shape s;
    return 0;pointer
}

```

### Exception Handeling 
```cpp

    #include <iostream>
#include <string>
using namespace std;



int main(){

    int divident, divisor;
    cin >>divident>>divisor;
    // cout<<divident/divisor<<endl;


    try{
        if(divisor == 0){
            // now this statement error will be caught by string
            throw string("HEY");
        }
    }catch(int paramter){
        cout<<paramter<<endl;
    }catch(double v){
        cout<<v<<endl;
    }catch(bool b){
        cout<<b<<endl;
    }
    catch(string a){
        cout<<a<<endl;
    }
    catch(...){
        //this block catchs exception of all type
        // hence this should be used at last
        cout<<"something went wrong"<<endl;
    }
 
    // syntac : catch(type catchblockParameter){// print catchblockParameter param.what()}
    // param.what() prints the actual parameter.

    // we can define our own exception classes and can use to throw exceptoins.

    // we can also rethrow an exception in catch block which can be caught further by other code
    // rethrow is thrown in catch block.

    // catch have a catch block parameter 
    // thrown value is stored in a catch block parameter.
    // is there is no clock block paramter then error may not be accessible.
    // if error is not thrown it will not be catched in catch block for sure.
    // throw expressoin
    // catch block can caputre any expection of specifc type or all type of ex exception

    // types of expcetion : 
        // logical error
        // runtime_error

    // class exception
        // logical_error
            // invalid_argument
            // out_of_range
            // length_error
            // bad_alloc
        // runtime_error : are only occured while programe is running
            // overflow_error
            // underflow_error


    return 0;
}

/** Exceptions are the cases or events that occour beyond the general thought or statementz.
 *  And in computer science we have to handle the exception
 *  asser or if-else conditions are used to check for exception handeling.
 *  
 * 
 *  we try to execture a code in try 
 *  a code after error in try doesnot executes and throws error
 *  which is caught in catch block
 * 
 *  
 *  there can be multiple catch blocks all the catch block where the execption is match is executed and rest all catch blocks are ignored.
 * 
 * 
 *  
 *  Ways to handle exception :
 *      1) teminate the programme
 *      2) Log the error and continue the execution : when we don't want to terminate the programe
 *      3) Fix the error and continue : log and continue.
 * 
 */

```

### Strucutre
```cpp
    #include <iostream>


using namespace std;

// strucutre can have functions as well

struct amp{
    int age;
    string name;

    void namee();
    amp();
};

void amp::namee(){
        cout<<name;
}
amp::amp(){
    name = "ANuj";
};
int main(){

    struct amp a;
    //cout<<a<<endl; // this statemnt will produce and error
    a.namee();
    return 0;
}

// structre are also the type ofstrucutre struccutred data types that are made form simple datatypes line integer, float, enum
// struct is also known as record
// class is also a strucuted dataype.
// unions are also present in cpp 
// one aggrigate operation that is valid on string array is input and output of the array value;
// function can return a value of type struct
// structs can be passed by both value and reference0

// everythins is same in between strucutre and class except access modifier that class all are private and in struct all are public

```

### Templates 
```cpp
        #include <iostream>
    #include <typeinfo>

    using namespace std;

    // here we can have as many generic data's as required
    template <class t, class b>
    void idea(t data, b adb){
        cout<<typeid(data).name()<<endl;
    }

    template <class t, class d>
    class nan{
        public:
        t idea;
        d data;
        
        nan(t i, d da);
        void printNan()const;
    };
    template <class t, class d>
    nan<t,d>::nan(t i, d de){
        this->data = de;
        this->idea = i;
    }

    template <class t, class d>
    void nan<t,d>::printNan()const{
        cout<<this->data <<"  " << this->idea<<endl;
    }



    /// class nonan is inheriting the nan class and everyting is similar with nan and nonan in templates classes we have to use tempalte synatx
    template <class t, class d>
    class nonan:nan<t,d>{
        public: 
            string name;
            string college;

        nonan(string name, string college, t ter , d der);
        void printnonan()const;
    };

    template<class t, class d>
    nonan<t,d>::nonan(string name, string college, t ter , d der):nan<t,d>(ter,der){
        this->name = name;
        this->college = college;
    };

    template <class t, class d>
    void nonan<t,d>::printnonan()const{
        cout<<this->name<<" "<<this->college<<endl;
        nan<t,d>::printNan();
    }

    int main(){

        string s = "THIs";

        idea(s,1);
        idea("ANU",4);
        idea('A','r');
        idea(34,'2');
        idea(123.12,234);


        // while creating an object we can provide a type to an object and that will take required value accordingly;

        nan<int, int> newnan(5,4);
        newnan.printNan();

        nan<string, string> newstringbb("Anuj", "Help peoples");
        newstringbb.printNan();

        nan<string, float> newstringbbb("Anuj", 13.4);
        newstringbbb.printNan();



        nonan<int, float> newbiew("ANuj", "DKTE", 22, 2002);
        newbiew.printnonan();

        return 0;
    }

    /**
    * Templates are used for generalization or to define generic classes or function which are not dependent on the type of the data being passed to the fuction or classes
    * 
    */
```


# OOPS 


### Start oops
```cpp
    #include <iostream>
    #include <string.h>
    #include <string>

    #define MALE 1
    #define FEMALE 0


    using namespace std;



    struct  idea
    {
        private:
            int name;
        
    };

    const string STR = "verma ji ka beta";


    class Human{
        // class data memebers and methods have class scope.
        // independednt functions have class scopes
        private: 
        int age;
        char gender[10];

        public:
        Human(int age, const char *name):age(age){
            this->age = age;
            strcpy(this->gender,name);
        }

        void printDetail(){
            cout << "I'm " << gender << " & I'm " << age << "years old" << "\n";
        }

        ~Human(){
            cout<<"Distructor is called now for " << this->gender << endl;
        }
    };

    int main(){
        char srr[10]="idae";
        Human h1(22, "ANUJ");
        Human *h2 = new Human(19, "JAN");
        h1.printDetail();
        h2->printDetail();
        h2->~Human();
        // here assignment operator works without overloading.
        Human h3 = h1;
        h3.printDetail();
        cout << STR << endl;
        return 0;
    }

    // function of a class is called method 
    // class groups the attribute and behaviour of an real life entities together to from and object
    // It simulates real life objects.

    // Member access specifiers : 
    // public : data members and methods are accessible by every other component of the module.
    // private : priavte data members can only be accessed using object methods.
    // default : 

    // Methods : 
    // if methods are declared inside a class body they are already inlined
    // if methods body is defined outside the class body and we want to make it inline we have to declare it inline
    // Methods which change the data members are called commands
    // Methods which doesnot change the data members are called queires.


    // calling a method 
    // object.method()
    // objectPointer->method()
    // constructors
    // access methods
    // service methods
    // utility methods
    // Destructor ~ 



    // construcutor is a method of class with the same name of a class 
    // types of constructors : 
        // 1) default constructor : When no constructor is created in a classes. it is implictly created by compiler 
        // NO argument constructor created by user itself 
        // 2) parametrized constructor : with arguments 
        // 3) copy constructor : takes the argument of the same type and creates and object out of it.
            // In copy constructor the arguement shoudn't be call by value
            // the object being passed must be constant
        // 4) when no constructors are given compiler itself insertes a constructor
        // 5) Defaults constructos doesn't perform any operation
        // 6) Construcutors have no return type becuase of following reason : 
                // 1) implicit return : they implictly return the object instance
                // 2) initialization : Constructors are used to instantiate and initialize 
                // 3) To make compiler differentiate between the method and the construtor 
    /*

    NOTE : 
        1) Global methods and variables are initialized before any method are variables are initialized and destroys when main leaves or terminates.
        1) static methods are created when the flow reached where they are created declared and destroys when main exits.
        2) for automatic local constructors are called when they are called and destoryed and block leaves the scope.

        3) public data members can be accessed by outside of the class only by object name, reference to object, pointer to object.
        4) Priavte data members can only be accessed by public getters and setters 
        5) private members of a class can be accessed using friend of a class
        Both structures and classes have private, public and protected access. Default of classes is private, default for structure is public.
        BUt this is not applied to c because in c there is not any access modifiers.
        6) new keywords allocated memeory dynamically. and when we allocate memory dynamically we have to free it using destructor we have to call the destructor.
        7) inline functions are function whose code is replaced where it is called rather than making a function call. Inline is just a request like register compiler may agree or reject depending the type of function.
        8) When a function is declared inside a class it is be default inline.
        9) or you can use inline to declare inline function()
    */


    // class 
        // member function : methods 
        // member variables : data members


    // shallow copy : when pointer are pointing to the same object. Change in object will be reflected in both of the objects.
    // deep copy : seperate object of the same type and assigned the memory and pointer points to that memory. Change in one doesnot affects the other.


    // when object is passed by value the copy of an object is made by the compiler and work is done on the copy of an object not the object

    // In Java there is always call by reference and there is no call by value. 
    // In cpp cll by value is the default.


    // structure : 
    //c = no access modifier , no function, no constructors , distructors
    //c++ = access modifier , functions, constructors, distructors



    //OOD = object oriented design
    // classes :  class has members list (member functions and memeber variables) collectively all of them are called memebers.
    // classes help to group data and operations on data together.
    // when we define a class no memeory is allocated. It just announces it's  existence that class exists.
    // we declare a member functino as a const to prevent it from manuplating the member variable of a class.
    // by default it's private
    // object can be declared in a member functions or in a user programme
    // object declared in a member function can access the private as well public but declared in user programme can only access public.
    // object's only contains the memroy of varibles not the functions. 
    // member functions have just one copy and each member use the same.
    // . period opertor or member access operator.
    // assignment operator and . operator work with class object without overloading.
    // Actual parameter is a parameter that is passed by called 
    // formal parameter are parameter in method where the call by values get copied.
    // call be reference is a good way for function calls as only the address of objects is received by formal parameter
    // change to the actual object can also be prevented using a const keyword.
    // when we use a const value as a pass by value it still cannot be modiefed by any methods
    // class memebers and class functions are in the scope of class so we have to use scope resolution operator 



    /** UML notations
    * - private member
    * + public member
    * # protected 
    */
```

### Abstraction 
```cpp
    // Hiding the implimentation detail 
    /**Separating the design details (that is, how the car’s engine works) from its use is called abstraction
    * Basically it focues on what not how.
    * seperating the logical entity form implementation detail.
    * 
    * Abstraction is bascially used for code organization. 
    * i.e seperate the implimentation detail from defination
    * 
    * Abstract data type (ADT): A data type that separates the logical properties from the implementation details.
    * To implement an ADT, you must represent the data and write algorithms to perform the operations.
    * ADT has three things : 
    *      1)type of ADT ;
    *      2) values associated with ADT;
    *      3) Operations on ADT
    *      EXAMPLE : 
    * 
    *          dataTypeName
                clockType
                domain
                Each clockType value is a time of day in the form of hours,
                minutes, and seconds.
                operations
                Set the time.
                Return the time.
                Print the time.
                Increment the time by one second.
                Increment the time by one minute.
                Increment the time by one hour.
                Compare the two times to see whether they are equal.
    
    * 
    * linkedlist as adt : we hide all implimentation detail we only show : 
    *      1) operations that can be performed on it. not how they are performed internally.
    * 
    */


    // NOTE :
    // C++ classes were specifically designed to implimnet ADT.
    // Classes are ways to impliment ADT (seperating the defination and Implimentation)



    #include <iostream>
    #include <string>

    using namespace std;


    // implementing ADt

    // ADT defination is below

    class computer{
        string type;
        int price;
        int ram;
        int ssd;
        int genration;


        public:
        computer();
        computer(string="MSI",int=80000,int=8,int=512,int=5);
        void getDetail()const;
    };

    // we have just defined it now we can sperate it's implimentation in seperate file by this way user can only know what is done not how it is done.
    // The only differnence in cpp class and struct is by default all members are public in struct and all are private in class.
    // classes are used to handle adt whereas struct are used to groping data together


    int main(){


        return 0;
    }



    /**Information Hiding 
    * 
    * Information hiding is basically allowing user's only to see what they are supposed to see. Not implimnetation detail.
    * we can achieve this by seperating the Decleration and implimenation seperately or deceleration and defination seperately.
    * 
    * If we have entire code written in same file and user can see entire source code he can tweak the code and make the private member as public member
    * this breaches the security and hence we must seperate the implimentation detail from defination(specification).
    * 
    * 
    * Note : 
    *  Specification file : which all things are available , functions, variables, etc. 
    *      they contain defination of a class
    *      They are also called header files.
    *      They are also called interface file. 
    *  Implimentation file : Implimenation detail how it is implimented
    *      they contain defination of a methods
    * 
    * 
    *  Information hiding is done basically between files.
    *  User program only contains main function rest other contains implimentation or specification;
    * 
    * 
    *  defination of a class is achieved when we declare the functions and members;
    * 
    *  object code is a code without linking process
    *  executabale code is a code with linking process
    * 
    * 
    *  steps in information hiding : 
    *      1) First create a header file specificatinfile.h
    *          this will conatins class defination
    *      2) Create a implimentation.cpp file which will contain the methods defination
    *          this must include header file i.e. specificatin file
    *          Object code is created to link with main file using cmd 
    *              g++ -c implimentation.cpp -> generated the implimentation.o file
    * 
    *      3) Create a Script file that contains main file
    *          this must include header file i.e. specificatin file
    *          compile the code with g++ file.cpp implimentation.o
    *          ->> this generates executables that links the implimentation file with main file 
    * 
    *      4) this is how information hiding is achieved that is no one can tweak the implimentation detail. and abstraction is achieved.
    *
    * 
    *      
    *      EXECUTABLE code is generated by linking differnet object files together.
    *      To link more than one object code file with a source code file, we list all of the
                object code files on the system command line. For example, to link
                A.obj and B.obj with the source code file test.cpp, we use the
                command:
                cc test.cpp A.obj B.obj
    * 
    */



    /** STATIC
    * Static is a member of a class not the instance so they can be accessed using scope resolution operator with a class name.
    * thus only one memeory is allocated for that variable of a class and every object point to the same.
    * Static function of a class is a method of a class that can be accessed using the class scope resolution
    * We cannot use not static members or functions inside a static one
    * 
    * The scope of static is the scope of the programme execution. when programme terminates the static member or variable also terminates.
    * public static members and function can be called using class name
    */


    /* STRUCTURE : 

    c = no access modifier , no function, no constructors , distructors
    c++ = access modifier , functions, constructors, distructors
    However we don't use structure we use classes 

    */

    /**Destructor 
    * There can only be one Destructors per class No return value no type of function, no parameter
    * structure ~classname()
    */

    /**Array of objects 
    * we can create array of objects and it is recommended that class must have a default constructor.
    */


    /**Accessor & mutators
    * 
    * 
    * the object variables are called instance variables as every object share the distinct memory.
        accessors : those member functions who access the member variables. As a safegaurd we use const at the end of the accessor function so that they cannot modify the members variable of that class;
            // Const member function cannot modify the instance variables. they are called constant function
            // constant member function of a class can only call other constant member functions of a class.
        Mutators : those functions which modify the member's variables or instance variables.
    * 
    */


    /**Passby reference over pass by value
    * 
    */

    // There are different files used to acheve abstration 
    //  specification file spec.h
    // implimentation file imp.cpp
    // testing file test.cpp

    //spec file spec.h


    class Clock{
    private:
        int hr;
        int min;
        int sec;
    public:
        Clock(){
            // with no parameter is default construtor.
            hr=0;
            min=0;
            sec=0;
        }
        Clock(int hr, int min, int sec);
        void setTime(int hr, int min, int sec);
        void getTime(int &hour,int &min, int&sec)const; // this avoid to change the member variables
        void printTime();
        // ~Clock();



    // implimentation file imp.cpp
    #include <iostream>
    #include "Clock.h"

    using namespace std;

    Clock::Clock(int hr, int min, int sec){
        this->hr = hr;
        this->min = min;
        this->sec = sec;
    }

    void Clock::setTime(int hr, int min, int sec){
        this->hr = hr;
        this->min = min;
        this->sec = sec;
    }
    // pass by reference but not pass by reference pointer
    // here hour, min , sec are the formal parameters
    void Clock::getTime(int &hour,int &min, int&sec)const{
        hour = hr;
        min= this->min;
        sec = this->sec;
    }

    void Clock::printTime(){
        cout<<hr<<min<<sec<<endl;
    }


    // this is the implimentation file 
    // this code is compiled and then linked in the main file 
    // this doesnot contain the main method.

    };


//specification file , interface file or header file
// Must be included by both the user programme and implimentation programe
// not required to include preprocessor directives
// this file must contain the comments to proper identify them.



```
### Encapsulation 
```cpp
    //combining data and code that operates on data together is encapsulation it is achived with the help of Class and strucutres in cpp
    // Benefits 
        // easy to undestand code
        // Data hiding using acess modifiers 
        // Reausibility 
```
### Inheritance 
```cpp 
    // IS-A realtionship : Iheritance 
    // Has-A relationship : Aggeregation & Copmosition
    #include <iostream>
    #include <string>
    /**
    * Has a realtionship
    * car has a engine
    * 
    */

    using namespace std;

    class engine{
        private:
            int cc;
            int hp;
            int mileage;
        public:
            engine(){

            };
            engine(int cc,int hp,int mil);
            void printEngine();
    };

    engine::engine(int cc,int hp,int mil){
        this->cc= cc;
        this->hp=hp;
        this->mileage = mil;
    }
    void engine::printEngine(){
        cout<<" "<<cc<<" "<<hp<<" "<<mileage;
    };

    class Car{
        private:
            string name;
            int model;
            int year;
            engine e;
        
        public:
            Car(string name, int model, int year, int cc, int hp, int mil);
            void printCar()const;
    };

    Car::Car(string name, int model, int year, int cc, int hp, int mil){
        this->name = name;
        this->model = model;
        this->year = year;
        e = engine(cc,hp,mil);
    }   

    void Car::printCar()const{
        cout<<name<<" "<<model<<" "<<year;
        engine en = this->e;
        en.printEngine();
    }   

    int main(){

        Car maruti("Maruti",2002,2016,1400,3200,40);
        maruti.printCar();
        return 0;

    }

    #include <iostream>
    #include "first.h"

    int main(){

        Employee em = Employee("Manf",4000000,50000,"ANuj");
        em.printDetail();

        return 0;
    }


    // CODE Reusability 

    /**
    * Inheritance (IS-A) : Conside Employe and person : Every employee is a person
    * Coposition(aggregation) (has-A)
    * 
    */



    /** INHERITANCE
    *  New class created from the existing class 
    *  New class is derived class
    *  Existing class is super class or base class
    * 
    *  Types : 
    *      single inheirtance : Single base class
    *      multiple inheritance : Multiple base class
    * 
    *  we also use member acccess specifier while inheriting classes.
    *      private, public , protected
    *  if we use no member specifier directly it is private by default.
    *  
    * Rules : 
    *  private memebers are always private to base class
    *  public members can either be inerited as public or private in derived class
    *  derived class can rederine the public member functions of the base class. (over riding)
    *  all member variable and functions of a base class are the members of derived class unless private.
    * 
    *  
    *  polymorphism:
    *  overriding : same name , same set of parameter, same return type  (run time polymorphism),
    *  overloading : same name, different set of parameter (compile time polymrphism)
    * 
    * 
    *  Note : no classes can be declared as public private or protected directly.
    *  Inorder to use the private members of the base class we use the public members function to reterive the data;
    *  Inorder to help constructor access the private members of a class 
    *  When we define the default constructor of a base class the defautl constructor of a base class is directly called.
    *  when we have to call the constructor of a base class we have to define it  explictly in derived class constructor heading
    *  when constructor of derived is called first constructor of base is called then drive is called.
    * 
    *  abstraction : hiding informatin(implimentation detail)
    *  encapsulation : hiding data
    *  
    * 
    * 
    *  when object is created without dynamic memeory allocation memory is deallocated itself.
    *  But when we use dynamic memory allocation we have to call destructors and free the space.
    *  to avoid multiple declerations of a file we must have to use #ifndef or #ifdef
    *  
    * 
    * 
    *  NOTE : if we want the memeber of a base class to be only accessed by the derived class we declare it as a protected member.
    * 
    * 
    *  we can inherit a class publickly , privately or protected 
    *  inheriting publickly : 
    *      All the public private and protected of base class reamins as it is in base class.
    * 
    *  privately :
    *      public , protected members become private in base class.
    *  
    *  protected : 
    *      public into protected, protected into protected and private are hidden to base class.
    * 
    *  
    *  protected and private members or function can be accessed using a friend function.
    * 
    * 
    *  The three basic principles of OOD are as follows:
    •
        Encapsulation—The ability to combine data and operations on that
        data in a single unit.

        • Inheritance—The ability to create new objects (classes) from existing
        objects (classes).

        • Polymorphism—The ability to use the same expression to denote
        different operations.



        while solving oops problem : 
            all nouns are classes
            all verbs are operations that is methods
            all properties or attributes are data 
    * 
    */

```
### Polymorphism 
```cpp
    // types : 
        // Run time : Function overriding / virtaul functions / pure virtual functions
        // compile time: function overloading

    // concepts : 
        // Abstraction 
        // Interfaces 
        // Overloading
        // overriding 
        // Virutal functions
        // pure virutal functions
        // Run time poly morphism 
        // compiletime polymorphism
```
### C++ Polymorphism: Concepts, Functions, and Gotchas

### 1. Introduction to Polymorphism
- **Definition:** Polymorphism allows objects of different classes to be treated as objects of a common base class. It enables a single interface to represent different data types and functions.
- **Types of Polymorphism:**
  - **Compile-time (Static) Polymorphism:** Achieved through function overloading and operator overloading.
  - **Run-time (Dynamic) Polymorphism:** Achieved through inheritance and virtual functions.

### 2. Compile-time (Static) Polymorphism
- **Function Overloading:**
  - **Concept:** Multiple functions can have the same name but different parameters (type, number, order).
  - **Example:**
    ```cpp
    int add(int a, int b) { return a + b; }
    double add(double a, double b) { return a + b; }
    ```
  - **Gotchas:** Overloading based solely on return type is not allowed.
  
- **Operator Overloading:**
  - **Concept:** Allows operators to be redefined and used for user-defined data types.
  - **Example:**
    ```cpp
    class Complex {
        double real, imag;
    public:
        Complex operator + (const Complex& obj) {
            return Complex(real + obj.real, imag + obj.imag);
        }
    };
    ```
  - **Gotchas:** Overloading must be intuitive; avoid making operators behave in unexpected ways.

### 3. Run-time (Dynamic) Polymorphism
- **Virtual Functions:**
  - **Concept:** A function in the base class is declared as `virtual`, allowing it to be overridden in derived classes.
  - **Example:**
    ```cpp
    class Base {
    public:
        virtual void show() { std::cout << "Base class\n"; }
    };
    class Derived : public Base {
    public:
        void show() override { std::cout << "Derived class\n"; }
    };
    ```
  - **Gotchas:** Ensure the base class destructor is virtual to avoid resource leaks.
  
- **Pure Virtual Functions and Abstract Classes:**
  - **Concept:** A pure virtual function has no implementation in the base class and must be overridden in derived classes. A class containing at least one pure virtual function is abstract and cannot be instantiated.
  - **Example:**
    ```cpp
    class Shape {
    public:
        virtual void draw() = 0;  // Pure virtual function
    };
    class Circle : public Shape {
    public:
        void draw() override { std::cout << "Drawing Circle\n"; }
    };
    ```
  - **Gotchas:** Derived classes must implement all pure virtual functions or they will also be abstract.

### 4. Virtual Destructors
- **Concept:** A virtual destructor ensures that when an object is deleted through a base class pointer, the derived class's destructor is called, preventing resource leaks.
- **Example:**
  ```cpp
  class Base {
  public:
      virtual ~Base() { std::cout << "Base destructor\n"; }
  };
  class Derived : public Base {
  public:
      ~Derived() { std::cout << "Derived destructor\n"; }
  };



### Constructors : 
```cpp
    /**Constructors 
    * when there are no constructors a random value is assigned to member variables
    * constructor : two types
    *      with parameter, without parameter
    *  without parameter or with all default parameter == Default parameter 
    * which constructor gets called depends on the type of parameter we pass to it.
    * Default constructor is generated by compiler if no constructor is passed and this default constructor doesnot initializes the vlaues
    * if we define a constructor then no default constructor is passed
    * constructor is invoked immediately an object is created from it.
    * we can also pass default parameters to a class constructors
    * we can say that a constructor that has no parameters, or has all default parameters, is called the default constructor.
    * we can declare array of an objects. but they must jave a default constructors
    * 
    * coustructor : 
    *  used for initialization.
    *  no return type becuase : used for initilization
    *  to differentiate between constructor and other member function
    *  becuase by default it's return type is a instance of a class.
    * 
    * 
    * 
    * 
    * NOTE :
    * If the type of the arguments does not match the formal parameters of any
        constructor (in the order given), C++ uses type conversion and looks for
        the best match. For example, an integer value might be converted to a
        floating-point value with a zero decimal part. Any ambiguity will result
        in a compile-time error.
    * If the values passed to a class object do not match the parameters of any constructor and if no type conversion is possible, a compile-time error will be generated.
    * 
    * 
    * 
    * 
    * 
    * Why compiler doesn't initializes the member variables by default if there is not defautl constructor :
    *  becuase member varibles are private by default and cannot be acccessed by outside of class.
    */

    /* Desctructors  
        class can only have one distructor
        its have no parameter no return type.

    */

    //OOD = object oriented design
    // classes :  class has members list (member functions and memeber variables) collectively all of them are called memebers.
    // classes help to group data and operations on data together.
    // when we define a class no memeory is allocated. It just announces it's  existence that class exists.
    // we declare a member functino as a const to prevent it from manuplating the member variable of a class.
    // by default it's private
    // object can be declared in a member functions or in a user programme
    // object declared in a member function can access the private as well public but declared in user programme can only access public.
    // object's only contains the memroy of varibles not the functions. 
    // member functions have just one copy and each member use the same.
    // . period opertor or member access operator.
    // assignment operator and . operator work with class object without overloading.
    // Actual parameter is a parameter that is passed by called 
    // formal parameter are parameter in method where the call by values get copied.
    // call be reference is a good way for function calls as only the address of objects is received by formal parameter
    // change to the actual object can also be prevented using a const keyword.
    // when we use a const value as a pass by value it still cannot be modiefed by any methods
    // class memebers and class functions are in the scope of class so we have to use scope resolution operator 


    // Invoking constructors : 
        // class object  -> invokes default
        // class(parameter) -> anonymus object
        // which constructor will be invoked depends upon what no of parameters are passed while creating an object.


    // Operators with work on objects without overloading
        // assignmnet operator(=) -> which does member wise copy to the variable
        // member access operator (.) -> used to access the member of class


    // all the private members are only accessible inside a class.


    // structured programming : 
        // control strucutre (selection)
        // loop strucutres (repetation)
```


### Operator overloading 
```cpp
        #include <iostream>


    using namespace std;


    class complexNo{
        friend complexNo find();
        friend complexNo operator+(complexNo, complexNo);
        friend ostream& operator <<(ostream& object,const complexNo &u);
        friend istream& operator >>(istream&, complexNo &a);
        private:
            int r;
            int i;
        public:
            complexNo(){};
            complexNo(int r, int i);
            void operator + ();
            void operator -();

            // it can also return a value as well
            complexNo operator *(const complexNo  &n)const;
            void printDetail()const;
    };

    complexNo::complexNo(int r, int i){
        this->r = r;
        this->i = i;
    }

    complexNo complexNo::operator*(const complexNo  &n)const{
        int i = this->i**&n.i;
        int r = this->r**&n.r; 
        complexNo c(i,r);
        cout<<"____________________________"<<endl;
        cout<<this->i<<this->r<<endl;
        cout<<*&n.i<<"---"<<*&n.r<<endl;
        cout<<"____________________________"<<endl;
        return c;
    }   

    void complexNo::printDetail()const{
        cout<<this->i<<" "<<this->r;
    };

    complexNo operator+(complexNo i, complexNo r){
        complexNo c;
        c.i = i.i+r.i;
        c.r = i.r+r.r;
        return c;
    }


    complexNo find(){
        // here friend function can access the private members of the class without calling any function
        complexNo c;
        c.i = 4;
        c.r = 5;
        return c;
    }

    // ostream overloading
    ostream& operator <<(ostream& object,const complexNo &u){
        object<<*&u.i<<*&u.r;
        return object;
    };

    // istream overloading


    int main(){
        complexNo c(8,9);
        complexNo d(6,6);
        // this is the synatx of using overloaded operator.
        complexNo e = c*d;
        d.printDetail();
        cout<<endl;
        e.printDetail();
        cout<<endl;
        d.printDetail();
        cout<<endl;
        complexNo f= find();
        f.printDetail();
        cout<<endl;
        complexNo g = operator+(c,d);
        g.printDetail();
        cout<<endl;
        cout<<d;
        return 0;
    }

    /**Operator overloading
    * the operators that cannot be overloaded are: ., .*, ::, ?:, sizeof
    * only existing operator can be overloaded no new can be created;
    * operator overlading can be done by declaring a member class or a non-member class that is a friend class
    * but few operator can only be overloaded as a member function they are : ( =, [], (), ->) becuase they need the instance to operate on.
    * << extraction and insertion >> operator can only be overloaded by being a friend of a class
    * inorder to overload a operator with non-member function we provide no of parameter equal to the default operands.
    * like binary operator takes 2 argument 
    * operator overloading without a member function but with a friend class.
    * friend returntype operator + (operand1, operand2)
    * 
    * 
    * operator overloading of of extraction << and insertion >> operator is only done through the friend function.
    * becuase cout and cin are the objects of ostream and istream
    * 
    * assignment operator creates a member-wise copy of the object members 
    * we must overload the assignment operator becuase the defualt assignment operators only allows the shallow copy not the deep copy
    * for a object with a pointer variable .
    * 
    * syntx : 
    * const classname& operator=(const classname&
    */

    /**this pointer
    * 
    * this is the reserved pointer which is maintained by every class.
    * this is the pointer which points to the object which invokes the method of the function. 
    */


    /**friend class and function
    * declared in the class in which we want to make a firend of 
    * can access any member variable
    * it is a non member function of a class i.e. it cannot be accessed using object
    */


    /**
    * array indexing and subcripting overloading.
    * 
    * array can be constant or non-constant and we have to overload for both the cases 
    * type& operator[](int index)
    * const Type& operator[](int index) const;
    * 
 */
```

### C++ Strings: Concepts, Functions, and Gotchas

#### 1. C-Style Strings
- **Declaration:** `char str[] = "Hello";`
- **Null-Termination:** C-style strings are null-terminated, meaning the last character is `'\0'`.
- **Common Pitfalls:**
  - **Buffer Overflow:** Ensure the array is large enough to hold the string and the null character.
  - **Manipulation:** Functions like `strcpy`, `strcat`, etc., do not check bounds, leading to potential security issues.

#### 2. `std::string`
- **Declaration:** `std::string str = "Hello";`
- **Features:**
  - **Dynamic Size:** `std::string` automatically adjusts its size when modified.
  - **Convenience:** Supports many useful methods like `length()`, `substr()`, `find()`, etc.
  - **Safety:** Unlike C-style strings, `std::string` handles memory management internally.
- **Gotchas:**
  - **Performance:** Although safer, `std::string` might be slower than C-style strings for low-level operations.
  - **Memory Management:** When passing to functions, prefer passing by reference (`const std::string&`) to avoid unnecessary copies.

#### 3. String Literals
- **Concatenation:** `"Hello, " "World!"` results in `"Hello, World!"` due to the automatic concatenation of adjacent string literals.
- **Immutable:** String literals are immutable; modifying them leads to undefined behavior.

#### 4. Common Operations
- **Concatenation:** Use `+` for concatenation with `std::string`.
- **Comparison:** Use `==`, `<`, etc., for comparing `std::string` objects.
- **Access:** Use `[]` or `.at()` to access characters within a `std::string`.

#### 5. Type Conversion
- **C-Style to `std::string`:** `std::string str = c_str;`
- **`std::string` to C-Style:** `const char* c_str = str.c_str();`
- **Gotcha:** The pointer returned by `c_str()` is valid only as long as the string isn’t modified.

### 6. `std::string` Functions

#### 6.1 Capacity
- **`size()` / `length()`**: Returns the number of characters in the string.
- **`max_size()`**: Returns the maximum number of characters that the string can hold.
- **`resize()`**: Changes the size of the string.
- **`capacity()`**: Returns the number of characters that can be stored before a reallocation is needed.
- **`clear()`**: Clears the contents of the string, making it empty.
- **`empty()`**: Checks if the string is empty.
- **`shrink_to_fit()`**: Reduces capacity to fit the current size.

#### 6.2 Element Access
- **`operator[]`**: Accesses the character at the specified position.
- **`at()`**: Accesses the character at the specified position, with bounds checking.
- **`front()`**: Returns the first character.
- **`back()`**: Returns the last character.
- **`data()` / `c_str()`**: Returns a pointer to the character array.

#### 6.3 Modifiers
- **`operator+=`**: Appends a character or string.
- **`append()`**: Appends characters or another string.
- **`push_back()`**: Appends a character to the end of the string.
- **`assign()`**: Replaces the contents of the string.
- **`insert()`**: Inserts characters or another string at the specified position.
- **`erase()`**: Removes characters from the string.
- **`replace()`**: Replaces part of the string with characters or another string.
- **`pop_back()`**: Removes the last character.
- **`swap()`**: Exchanges the contents of two strings.

#### 6.4 String Operations
- **`c_str()`**: Returns a pointer to a null-terminated array.
- **`copy()`**: Copies a substring into a character array.
- **`find()`**: Finds the position of the first occurrence of a substring.
- **`rfind()`**: Finds the position of the last occurrence of a substring.
- **`find_first_of()`**: Finds the first occurrence of any of the characters in a set.
- **`find_last_of()`**: Finds the last occurrence of any of the characters in a set.
- **`find_first_not_of()`**: Finds the first occurrence of any character not in a set.
- **`find_last_not_of()`**: Finds the last occurrence of any character not in a set.
- **`substr()`**: Returns a substring.
- **`compare()`**: Compares two strings.

#### 6.5 Conversion
- **`to_string()`**: Converts a number to a string.
- **`stoi()`, `stol()`, `stof()`, etc.**: Converts a string to an integer, long, float, etc.

#### 7. Advanced Topics
- **Memory Allocation:** `std::string` uses dynamic memory allocation internally, so be cautious of potential performance implications.
- **Move Semantics:** Take advantage of move semantics (`std::move`) to avoid unnecessary copies when dealing with temporary strings.
- **Unicode Support:** Handling Unicode requires additional libraries or wide character strings (`std::wstring`).

#### 8. Best Practices
- Prefer `std::string` over C-style strings for safety and ease of use.
- Use `std::string_view` for non-owning references to avoid unnecessary copies when passing strings around.
