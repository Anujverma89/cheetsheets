# Java Programming Overview

### Syntax
- Basic structure and format of Java programs.

### Data Types
- Primitive Data Types: `int`, `float`, `char`, `boolean`, etc.
- Reference Data Types: Objects, Arrays.

### Operators
- Arithmetic Operators: `+`, `-`, `*`, `/`, `%`.
- Relational Operators: `==`, `!=`, `>`, `<`, `>=`, `<=`.
- Logical Operators: `&&`, `||`, `!`.
- Bitwise Operators: `&`, `|`, `^`, `~`, `<<`, `>>`, `>>>`.
- Assignment Operators: `=`, `+=`, `-=`, `*=`, `/=`, `%=`.

### Control
- `if`, `else`, `switch` statements.

### Loop
- `for`, `while`, `do-while` loops.

### Methods
- Declaration and invocation.
- Return types, parameters, and method overloading.

## Object-Oriented Programming (OOPs)

### Classes
- Blueprint for creating objects.
- Fields and methods.

### Abstraction
- Hiding implementation details and exposing only functionality.

### Encapsulation
- Bundling of data (variables) and methods into a single unit (class).
- Use of access modifiers (`private`, `public`, `protected`).

### Polymorphism
- Ability to take many forms.
- Method Overloading (Compile-time Polymorphism).
- Method Overriding (Run-time Polymorphism).

### Inheritance
- Mechanism where one class acquires properties (fields and methods) of another class.
- Use of `extends` keyword.

### Interfaces
- A reference type, similar to a class, that can contain only constants, method signatures, default methods, static methods, and nested types.

## I/O
- Input and Output operations in Java using classes like `Scanner`, `BufferedReader`, `PrintWriter`, etc.

## Exception Handling
- Mechanism to handle runtime errors using `try`, `catch`, `finally`, `throw`, and `throws`.

## Packages
- Grouping of related classes and interfaces.
- Use of `package` keyword.
- Importing packages using `import`.

## Threads
- Multithreading in Java.
- Thread creation using `Thread` class and `Runnable` interface.
- Thread lifecycle and synchronization.

## Generics
- Allows types (classes and interfaces) to be parameters when defining classes, interfaces, and methods.
- Provides type safety and eliminates the need for type casting.

## Java Collection Framework
- Provides implementations for commonly reusable collection data structures.
- Includes `List`, `Set`, `Map`, `Queue`, etc.

## Strings
- Handling strings in Java using `String`, `StringBuilder`, `StringBuffer`.
- Common operations: concatenation, comparison, substring, etc.

## Networking
- Java networking features like Sockets, URLs, and networking APIs.

## GUI

### Swing
- Java's GUI widget toolkit.

### AWT (Abstract Window Toolkit)
- AWT is Java's original platform-dependent windowing, graphics, and user-interface widget toolkit.

## Advanced Topics

### JDBC (Java Database Connectivity)
- API for connecting and executing queries with databases.

### ODBC (Open Database Connectivity)
- Standard API for accessing database management systems.

### Enumerations, Annotations, Autoboxing
- Enumerations (`enum`) for defining a set of named constants.
- Annotations for providing metadata.
- Autoboxing for automatic conversion between primitive types and their corresponding object wrapper classes.

### Lambda Expression
- Introduced in Java 8.
- A way to provide a clear and concise syntax for representing anonymous methods.

## History and Evolution

### Programming Languages Overview
- **BASIC, COBOL, FORTRAN (Formula Translation), Pascal, B**: Based on `goto` structure.
- **C**: Structured or procedural programming language.
- **C++/Java**: Object-oriented programming languages.
- **Pascal**: Structured language but not optimized for efficiency.
- **BSPL**: Predecessor to C.

### Programming Language Hierarchy
- **C** → **C++**
- **C & C++** → **Java (Syntax and Architecture)**

### Implementing the SOLID Principles
- Need is the mother of invention.

### Early Programming
- Initially, programming was done by toggling binary machine instructions using the front panel.
- Assembly language was then developed.
- Languages like Pascal and FORTRAN used `goto` as their basic control mechanism.
- **C (1970 by Dennis Ritchie)**: The first structured language.
- **C++, Java, C#**: Object-oriented languages.
- Java initially developed as a platform-independent language, then adopted internet features due to increasing demand.

## Java Development Kit (JDK)

### Java Compiler
- Compiles Java source code into bytecode.

### Java Runtime Environment (JRE)
- Platform-dependent.
- Contains JVM to run Java programs.

### Java Virtual Machine (JVM)
- An encapsulated environment to run Java programs.
- Provides security through a restricted environment called "sandbox".

#### Just-In-Time (JIT) Compiler
- Compiles code when necessary, unlike ahead-of-time compilers.

#### Ahead-of-Time Compiler
- Compiles code before execution by the JVM.

### C# and Java
- C# is realted with Java.

## Java Internet Features

### Applet
- Used to run on a browser.
- Java plugin required in the browser to run the applet (removed in JDK 11).

### WebStart
- Runs on its own (removed in JDK 11).

### jlink
- Added in JDK 9.

### Servlet
- Uses Common Gateway Interface (CGI).

## Java Evolution

### Java 1.0
- Initial release.

### Java 1.1
- Added features and enhancements.

### Java 1.2 (J2SE)
- Added Swing and Collection Framework.

### Java 1.3 & Java 1.2
- Source code compatible.

### Java 1.4
- Added `assert`, chained exceptions, channel-based I/O.

### Java 1.5 (JDK 5, J2SE 5)
- Major update with new features:
  - Generics
  - Annotations
  - Autoboxing and auto-unboxing
  - Enumerations
  - Enhanced for-each style for loop
  - Variable-length arguments (varargs)
  - Static import
  - Formatted I/O
  - Concurrency utilities

### Java 1.6 (JSE)
- Further enhancements and performance improvements.

### Java 1.7 (JSE 7)
- New features:
  - A `String` can now control a `switch` statement.
  - Binary integer literals.
  - Underscores in numeric literals.
  - Try-with-resources statement for automatic resource management.
  - Type inference with the diamond operator.
  - Enhanced exception handling (multi-catch).

  - NIO (New Input & Output).
  - Fork/Join framework for parallel programming.

### Java 1.8 (JDK 8, JSE 8)
- Lambda expressions (`->` syntax).
- New Stream API.
- `java.util.function` package for lambda expressions.
- New Date and Time API.
- Default methods in interfaces.

### Java 9 (JDK 9, JSE 9)
- Module system.
- jlink tool.
- Applet deprecated.
- JMOD file type.
- jshell tool.
- Search feature in javadoc.

### Java 10 (JDK 10, JSE 10)
- Major release every 6 months.
- Local variable type inference (`var` keyword).

### Java 11 (JDK 11, JSE 11)
- Use of `var` in lambda expressions.
- HTTP Client API (`java.net.http`).
- Removed support for applets and Java WebStart.
- JavaFX not included in JDK 11 (open source project).

### Java 21 (as of December 15, 2023)
- Latest Long-Term Support (LTS) version.

## Java Program Structure

### Program Structure
- **Program = Code + Data**

### Programming Paradigms
- **Procedural Programming**: Focuses on "what is happening."
- **Object-Oriented Programming**: Organizes code around "who is being affected."


# Main Component
# Main Component

## Abstraction
- Hiding the implementation details.
- Used to prevent complexity.
- Related to design.
- Achieved using `abstract class` and `interfaces`.

# Three Components

## Encapsulation
- Wrapping up data and code as a single unit.
- Used to prevent unauthorized access.
- Related to implementation.
- Deals with privacy and access controls.
- Achieved through classes.

## Inheritance
- Mechanism where one class acquires properties (fields and methods) of another class.
- Promotes code reusability.

## Polymorphism
- Ability to take many forms.
- Method Overloading (Compile-time Polymorphism).
- Method Overriding (Run-time Polymorphism).

# Class and Object

## Class
- A logical construct that defines the structure and behavior of objects.
- Contains:
  - **Member Variables**: Also known as data or instance variables.
  - **Member Functions (Methods)**: Represent behavior or code.

## Object
- A physical entity that is created based on the structure defined by a class.

# Code Components

### `public static void main()`
- **`public`**: Main method must be accessible from outside of the class.
- **`static`**: Main method is the first method to run and can be called without creating an instance of the class.

### Code Block
- `{ }`: Anything between these braces is considered a code block.
- Used to create a logical grouping of statements.

# Programming Elements

### Keywords
- Reserved words in Java that have predefined meanings (e.g., `class`, `public`, `static`, `void`).

### Identifiers
- Names given to variables, methods, classes, etc.

### Variables
- Containers for storing data values.

### Literals
- Fixed values assigned to variables.

### Operators
- Symbols used to perform operations (e.g., `+`, `-`, `*`, `/`).

### Separators
- Symbols used to separate statements or elements (e.g., parentheses `()`, braces `{}`, brackets `[]`, semicolons `;`, commas `,`, periods `.`, colons `:`, ellipses `...`, ampersand `&`).

### Whitespace
- Spaces, tabs, and line breaks used to separate tokens in code.

# Important Notes

### Program Structure
- A program consists of code and data.

### Conditional Blocks
- `if` and `else if` blocks can be run without braces `{}`, but only one line after the condition will execute.

### Memory Allocation
- Memory is not allocated to a variable unless it is initialized, even if it is declared.

### Unicode
- Java uses Unicode for character encoding, which supports a wide range of characters from different languages.

## Abstraction
- Hiding the implementation details.
- Used to prevent complexity.
- Related to design.
- Achieved using `abstract class` and `interfaces`.

# Three Components

## Encapsulation
- Wrapping up data and code as a single unit.
- Used to prevent unauthorized access.
- Related to implementation.
- Deals with privacy and access controls.
- Achieved through classes.

## Inheritance
- Mechanism where one class acquires properties (fields and methods) of another class.
- Promotes code reusability.

## Polymorphism
- Ability to take many forms.
- Method Overloading (Compile-time Polymorphism).
- Method Overriding (Run-time Polymorphism).

# Class and Object

## Class
- A logical construct that defines the structure and behavior of objects.
- Contains:
  - **Member Variables**: Also known as data or instance variables.
  - **Member Functions (Methods)**: Represent behavior or code.

## Object
- A physical entity that is created based on the structure defined by a class.

# Code Components

### `public static void main()`
- **`public`**: Main method must be accessible from outside of the class.
- **`static`**: Main method is the first method to run and can be called without creating an instance of the class.

### Code Block
- `{ }`: Anything between these braces is considered a code block.
- Used to create a logical grouping of statements.

# Programming Elements

### Keywords
- Reserved words in Java that have predefined meanings (e.g., `class`, `public`, `static`, `void`).

### Identifiers
- Names given to variables, methods, classes, etc.

### Variables
- Containers for storing data values.

### Literals
- Fixed values assigned to variables.

### Operators
- Symbols used to perform operations (e.g., `+`, `-`, `*`, `/`).

### Separators
- Symbols used to separate statements or elements (e.g., parentheses `()`, braces `{}`, brackets `[]`, semicolons `;`, commas `,`, periods `.`, colons `:`, ellipses `...`, ampersand `&`).

### Whitespace
- Spaces, tabs, and line breaks used to separate tokens in code.

# Important Notes

### Program Structure
- A program consists of code and data.

### Conditional Blocks
- `if` and `else if` blocks can be run without braces `{}`, but only one line after the condition will execute.

### Memory Allocation
- Memory is not allocated to a variable unless it is initialized, even if it is declared.

### Unicode
- Java uses Unicode for character encoding, which supports a wide range of characters from different languages.




# Programming Concepts :

### Basics : 
```java
    package Basics;
    public class Basic{
        public static void main(String args[]){
            if(1 > 0)
            System.err.println("Hello");

            int a = 10;
            System.err.println(a);

            

        }
    }
```

### Control
```java
package Basics;
import java.util.ArrayList;

public class Control {
    public static void main(String args[]){

    String exp="Neal";

    switch (exp) {
        case "Neal":
        //case values:
            System.err.println("Neal");
            break;
        default:
        //default has no case and value 
            System.err.println("Default starting");
            break;
        //no duplicate case values are allowed 
        //only constant literals are allowed 
        //value of expression is matched with value then if it matched then the block following case is executed 
        //is non of the cases are matched the default are executed
        //expression and case value must be type compatible
        // switch cases are the improvement over the if-else statements
        // we rerely have to use strings in swtich statements
        //switch only operates on equality and if else also works on boolean value 
        //switch is faster then if-else  
    }        
    
    int month=4;

    switch (month) {
        case 12:
        case 1:
        case 2:
            System.out.println("winter");
            break;
        case 3:
        case 4:
        case 5:
            System.out.println("Spring");
            break;
        case 6:
        case 7:
        case 8:
            System.out.println("Summer");
            break;
        case 9:
        case 10:
        case 11:
            System.out.println("Rainy");
            break;
        default:
            System.out.println("Bogus");
            break;
    }

    //nested switch 
    int data=0;
    int dt=12;
    switch(data){
        case 1:
            switch (dt) {
                case 0:
                    System.out.println("this is 0");
                    break;
                case 1:
                    System.out.println("This is 1");
                default:
                    break;
            }
        case 2:
    }

      //iterators 
    //while, do-while, for 
    //while without body is also valid lets see
    // int i = 1100;
    // while( i > 10); //this is valid syntax in java as it allows to 
        // i-=1;
    // System.out.println("hello");


    ArrayList<String> str = new ArrayList<>();
    str.add("ANuj");
    str.add("Verma");
    str.add("golden");
    str.add("temple");

    for(String s : str){
        // this loop runs for n no of times where n is no of element.
        // s will hold the data of that index from the array.
        //type of var is the type of data stored in str
        System.out.println(s);
    }


    }

    /*
     * for (initialization , condition , iteration)
     * for(empty;empty;empty) //this is also valid and it will run for infinite time tho there is a way to terminate a infinite loop
     * for-each or enhanced for loop for(iteration variable : collection){} break can be used with for-each also 
     * iteration variable is read-only , It can also be used for multidimensional arrays 
     * var variable == initializer (type) local variable inference
     * jump statements :- break, continue, return - One other way is exception handeling 
     * Jump statements are used to change the exection flow of programme (try, throw, throws, catch, finally )
     * 
     *  
     */


    //increment and decrement 
    
}



/* if, if-else, nested if-else, if else ladder, switch
 * for, while, do while, 
 */


/*if we try to run implement a main method without String and args it won't run because main method always expects String as an argument
 * Mjaorly 3 types of selection statements
 * Selection
 * Iteration
 * Jump
 * 
 * Switch is the alternate of ifelse ladder.
 * 
 */
```


### Data types 
```java
package Basics;
public class Datat {

    public static void main(String args[]){
        //below given every declaration is valid;
        int a = 04; //octal
        int b = 0b1010; //binary 
        int c = 0x234abf; //hexadecimal
        int d = 10; //decimal
        Long sep = 123__234__234__123L; //with dash seperated iterals. this is used to enhance readibility.
        //you have to use L or l at the end 
        System.out.println(a+b+c+d+sep);
        System.err.println(sep);

        //float 
        float f = 6e1f;
        double doe = 34e4;
        System.err.println(f);
        System.err.println(doe);
        //we can also use p instead of e to represent the hexadecimal values
        double dbl = 0x12p3; //hexadecimal value 
        System.err.println(dbl);
        double underscore_dbl = 123_34.1_2; //this is also valid 
        System.err.println(underscore_dbl);

        //bolean 
        boolean bool = true; //cannot be bool = 1;
        boolean boolf = false; //cannot be boolf = 0;
        System.err.println(bool+ " " + boolf);

        //character insertion 

        char chr = 'a'; //always kept inside a single quotes
        char escapechr = '\''; // ways to add special character 
        System.out.println(chr + " " + escapechr);
        //you can also assign a character value using hexadecimal and ocatal by using following notatin 
        char octalchar = '\123';
        char hexalchar = '\u1234'; //four hexadecimal values must be there

        System.err.println(octalchar + " " + hexalchar);

        //string literals 
        String s = "New string"; //always encoded in double quotes 
        System.err.println(s); //above char implementation are also simlar in string and works fine
        //there is not multiline strings in java 


    }
    
}



/*
 * There are 8 primitive data types. They are also called as simple types. Other everything in java is Object except these.
 * byte -- 8 bits  
 * short -- 16 bits
 * int -- 32bits
 * long -- 64 bits 
 * float -- 32 bits 
 * double -- 64 bits 
 * char -- 16 bits (to make all unicode characters fit into it else Ascii can fit in just 8 bits)
 * boolean -- 8 bits 
 * 
 * They can be categorized into 4 types :
 * Integer : int, short , byte , long
 * floating types : Float , double
 * Character : char
 * boolean : bool
 * 
 * Size and range of datatypes in java is always same regardless of executing environment
 * There is no unsigned type in java 
 * Java uses unicode characters system instead a ascii character system
 */


 /* Literals 
  * int = 0-9 decimal 
  * int = 0-7 - octal leading 0 
  * int = 0-f - hexadecimal leading x0
  * int = 0-1 - binary leading 0b
  */
```

### Mesc data types 
```java
package Basics;
public class Mesc {
    public static void main(String args[]){
        boolean f = 2<=2;
        boolean t = 3>3;
        System.err.println(f&&t);

    }

}


//logical boolean operatoor
/*
 *  & true if both true
 *  | true if even is true
 *  ^ false if both are same 
 *  ! invert 
 *  && right operand is not exectued and result is 
 */
```


### Operators 
```java
package Basics;
public class Operators {
    public static void main(String args[]){

        //expression = operand & operator
        //the operand type for arithmetic operator must be numeric or char(since it is a subset of int)

        // addion assignment is a compound assignment operator += 
        //compund assignment operator is used to save time for efficiency
        //a+=1; a = a+1;


        int a = -1;
        int b = +a; //unary plus operator
        int c = -1; //unary minus operator
        System.out.println(b);

        int not = 42;
        int notop = ~not;
        System.err.println(notop);

        int n = 458;
        int sum = 0;
        while(n % 10 > 0){
            int mod = n%10;
            n /= 10;
            sum += mod;
            System.out.println(mod+" " + n);
        }

        System.out.println(sum);

        //left shift
        byte shiftt= 45;
        byte newshift_left = (byte)(45<<1);
        System.out.println(newshift_left);
        //when you apply left shift or right shift on byte the resultant value is always int so you have to typecast it into byte for its integirty.


        //assignment operator
        int assing , goassign = 100; //assigining at once

        //bitwise operators
        //all integers are stored as binary no with varying bit in java
        // eg 42 : MSB->00101010<-LSB 
        //every integer in java is signed except chars
        //ascii 48-57 0-9 integer
        //97-122 a-z small alphabet
        //65-90 A-Z capital alphabet
        //negavtive no's are always stored using twos compliment and we take two's compliment of two's compliment it is same.
        //range for signed = -2^(n-1) to (2^(n-1))-1)

        //lets take a two compliment and see how 128 values are stored 
        /*
         *                      10000000 -- this is negavtive no and is two's compliment lets see which no is this
         *                      01111111 -- taking 1's compliment 
         *                     +       1 -- taking two compliemnt
         *                    ____________
         *                      10000000  -- now we can see the no is 128 and is negative now again if we convert into 2's compliment it will result in the same
         * 
         *                      01111111
         *                     +       1
         *                   ____________
         *                      10000000
         *
         */                 
        
         
         //


        //operator presedence
        //assignment operator work from right to left 
        //rest all binary operator works from left to right
        /*Highest () 
         *   ++
         *  --
         *  * / %
         *  + - 
         * >> << >>>
         * > >= < <= instanseof
         * == !=
         * &
         * ^
         * |
         * &&
         * ||
         * ?:
         * ->
         * Lowest = op=
         */

    }
}


/* Mainly four type of operator
 * Arithmetic:
 * [ + Addition ]
 * [ - substraction]
 * [*- multiplication]
 * [/ - division]
 * [%- modulus]
 * 
 * 
 * [++ increment]
 * [-- decrement]
 * Increment & decrement operators increases and decreases operand by 1 respectively.
 * they can apper in both prefix and postfix form
 * when prefix first increment or dcrement is perfoemed than operation is performed
 * 
 * below are compound assignment operator
 * [+= addition assignment]
 * [-= substraction assignment]
 * [*= multiplication assignment]
 * [%= Moudlo assignment]
 * [/= division assignment]
 * 
 * logical operators these are also called short-circuit operators.
 * When these operator are used first left hand side equation is evaluated.
 * If left hand side is true than only right hand side is evaluated.
 * These are conditional statements and used to check condition 
 * [&& and] Conditional and
 * [|| or] Conditional or
 * [! not] Conditional not
 * 
 * Bitwise : They can be applied to several integer types like , byte, short, int, long. Modifies bit by bit.
 * [~ : not unary not]
 * [^ : XOR] -- if both are different then 1 else 0, When the second operand bit is 1 the first one is inverted if it is 0 first one is not inverted
 * [& : and ]
 * [| : or ]
 * [<< : left shift] -- shifts the value left by the no : the value is multiplied by 2 each time you shift a number. So can be used to write efficient programmes.
 * [>> : right shift] -- shifts the value right by the no : the value is divided by 2 and reminder is ignored. This is also called signed shift.
 * Sign extension is the concept when the values are filled with previous values. This is always true in java by default. this can be undone by using below operator.
 * [>>> : Shift right zero fill] : THis operartos perfroms same as right shift but onyl fills values with 0 instead of 1, also called unsigned right shift operator.
 * 
 * compund bitwise operator 
 * 
 * [>>=] a >>= b
 * [<<=] a <<= b
 * [~=] a ~= b
 * [^=] a ^= b 
 * [>>>=] a >>>= b
 * [&=] a &= b
 * [|= ] a |= b
 * 
 * 
 * Relational operator : Always produces boolean value.
 * [== equals to ]
 * [!= not equals to ]
 * [ > greater than]
 * [ < less than]
 * [>= greater than equals]
 * [<= less than equals]
 * true and false in java is different than that of c++ 
 * True and false are non numeric value in java False != 0 and true != 1.
 *  
 * Instanceof -- to check object is of which class type
 * arrow operator(->) 
 * 
 * 
 * Ternary operator 
 * condition ? if ture : else false 
 * 
 * 
 * https://www.eecis.udel.edu/~davis/cpeg222/AssemblyTutorial/Chapter-08/ass08_19.html <visit this site >
 * 
 * Negative representation 
 * MSB -- sign 
 * smallest no -- All Zero 
 * Highest no -- All ones 
 * Largest -ve no is -1 
 * Smallest -ve no is 1
 */


```


### String 
```java
package Basics;
public class Variables {
    int a,b;
    int meth(int param){
        // every varaible declared inside meth will have local scope
        // prameters will also have method scope that is local scope
        int a; 
        a = param+10;
        param= param+10;
        System.err.println(param);
        return param;
    }
    public static void main(String args[]){
        //variables in java = datatype identifier = value 
        int val = 13; //val is the name of the variable 
        //declaring more than one variable 
        int a,b,c,d,e;
        //can be initialized at any time 

        //scopes 
        //class scope dipicted above 
        //methods scope
        Variables v = new Variables();
        int res = v.meth(val);
        System.out.println(res);
        System.out.println(val); //here we can see that original value is not affected by the method 

        //variable is created when scope is entered and destoryed and scope is left
        //variables cannot have same name as in outer scope



        //type casting 
        //implicit 
        //explict 

        long l = 12;
        //here l is long but assigned value of short it is implict conversion it is done with compatible varible type i.e. 
        //type compatible & destination variable is greater than source variable
        //This is also called widening conversion 
        
        //explict conversion : done when there is no type compatibility.
        //when long data type range is converted into small data type range 
        //this is also called as narrow conversion
        //when flaot is convert into int by type casting then it is called as truncation meaning that the fractinal value is lost.

        int i =(int) 1.34;
        System.out.println(i);

        byte bt = 1;
        byte ct = 2;
        int mt = bt*ct; //automatic type promotion means when value exceeds the given variable by expression 
        //all byte , short , char are promoted to int when any expression is applied on them like addition, subratction, multiplication or anything else
        //each value is promoted into its higher order of its operand

        byte bts =12;
        short cts = 14;

        //byte + short = int
        int result = bts+cts;

        /*examples 
         * Byte + int = int 
         * int + float = float
         * int + char = char
         * float + double = double 
         * byte + short = short
         */

        System.err.println(mt);

       
        //double is used when we require high precision
    }
}

```
### Break 
```java
package Basics;
public class Break {
    public static void main(String args[]){
        outer:for(int i=0;i<10;i++){
            for(int j=0; j<=5;j++){
                System.out.println(j);
                if (j==2)break outer; 
            }
        }


        couter:for(int i =0; i < 10; i++){
            for(int j =0; j < 10; j++){
                if (j == 5) continue couter;
                System.out.println(i);
            }
        }

        

        nextis: System.out.println("Nextis");
        inner : System.out.println("Target block ");
    }
}



/* The above code is the example of labeled break it acts as a organized go to 
 * it only works when we have nested loops only works for enclosing labels and not on any other which is not valid 
 * 
 * Continue && Break : Both break and continue can be used to goto statement.
 * break label 
 * continue label : this is used for early iteration, like go to the outermost layer .
 * return branches the code to the caller of the function i.e. control is passed to the caller of the method with data.
 * 
 */

```


### Arrays 
```java
package Basics;
public class Array {

    int[] res(){
        int arr[]= new int[10];
        return arr;
    }
    public static void main(String args[]){
        //collection of similar types of object 
        //ways of decleratin 
        int arr[]={1,2,4,5};
        int arr2[] = new int[5];
        int arr3[][]= new int[4][5];
        int arr4[][] = new int[4][]; //no of rows
        int[] arr5=new int[10];
        Array ar = new Array();
        int reuslt[] = ar.res();
        arr4[0] = new int[5]; // no of columsn in 1st row here the size of array can be of the size you want .

        for(int i =0 ; i < reuslt.length; i++){
            System.out.println(reuslt[i]);
        }


        //local variable type inference 
        // the type of the variable is inferred from the initializer 
        // var[] arr7 = new int[] //this is wrong declaration 
        //this can only be used with local variables and not with class instances
        //when var is used it must be initialized 
        // var data // this is wrong syntax must be initialized 
        // var arr = {1,2,3,4,5,6} cannot be used with array initializer
        // cannot be with exception type caught by catch block 
        //lambda expressions nor method references can be used as initializers.
        var data = 10;
        System.err.println(data);


    }
}

```


### String
```java
package Basics;
public class SString {
    public static void main(String[] args){
        //string is always constant in java 
        //string is neither a array of character nor a primitive data type
        String s = "This is string";
        //string is always constant
        //string is always enclosed in double quotes " "
        System.out.println(s);
    }
}

```

### Inheritance
### Polymorphism 
### Abstractino 
### Encapsulation
### Access Modifiers 