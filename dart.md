# Dart : 
* Dart is both general purpose and scripting language.

# Package in dart : 
* package in dart is differnet than that of java.
* every package contains pubspec.yaml file
* It only exposes the lib folder
* importing package "package:app_name/folder/filename.dart"
* In your package the file.dart has to be present inside the lib

_______



# 📁 project strucutre

``` 
my_app/
├── lib/
│   ├── utils/
│   │   └── helper.dart
│   ├── models/
│   │   └── user.dart
│   ├── services/
│   │   └── api_service.dart
│   └── main.dart
├── test/
│   └── main_test.dart
├── assets/
│   ├── images/
│   └── fonts/
├── pubspec.yaml
└── README.md
```
________


# Control flow : 
###### Loops 
* `for , while, do-while, for in , break , continue, labels`
* patterns are used with if case.


###### Branches 
* `switch, if, if-case`
###### Exceptions : 
* `assert, try , catch , throw, finally`
* `assert` is only used for debugging purpose

# Types in Dart : 
* `we define variable with type that means the literal of that specifc type can only be assigend to that variable`.
* When we say the variable is type of int, it means that type of int literal can only be assigned to that variable.
* Literal is a constant value that is assigned to the variable. It's the instance of specifc type.
* Every variable refers to an object.
* So the literal is an instance of a class.
* Constructors can be used to create object like Map().

* Number
* String
* Boolean
* Function
* List
* Record
* Set
* Maps
* Runs
* Symbols
* Value null

###### Other types 
* Stream, Future, Object, Enum, Iterable, Never, dynamic, void 
* we can add any type of values in List, set, Map if we don't sepcify the type while declaring

###### String : 
* String holds the sequence of UTF-16.
* It can be created using both single quote '' & double quote "".
* String interpolation means to add some dyanamic values in string using `'THis is $dyamic value'` $dynamic get's replaced with actual value in string. Putting the value of expression inside string.
* Can define multiline string using three quotes """ expanding in multiple lines""". Multiline strings are printed on the console in the same way they are defined.
* We can add escape sequence in string.
* Concatination of string can be done using `s1+s2` that is using + operator.
* Raw string in a dart is string whose escape sequence are not processed they remain same. `"Hello brother\n`.


###### Runes in dart : 
* They represent the unicode value corresponding to character.
* The value that represent a character in unicode is runes.
* `  String a ='ab';
  print(a.runes);`

###### Grapheme clusters : 
* Are the characters that are represented as a single character but are made up of multiple runes like '🇮🇳';


###### Symobls : 
* Symbols are used as a indentifer for a variable
* `Symbol sumb1 = #variablename`

###### Records : 
* Records are immutable hetrogenrous data type that can hold any value of anylength;

```dart
// types in dart 
// number(int double)

int a = 13; // number
// no float like other languages 
double b = 13.4; // number

// we can use num for int and double whenever needed
num value1 = 13; // can also capture 13.4 or 13 depending 

String name = "Anuj"; // string
bool value = true; // boolean

// type record
Record datab = ("name","surname","idea");
// type function
int Function(int age) nameoffunc = (int a){
  return a;
};

// type list 
// if we don't define the list with type any type of value can be added in it

List ablist = [12,2,3,4,"anujd"];

// the below list is not valid
// List<int> ablist = [12,2,3,4,"anujd"];


// set is mutable with unqie elements 
Set<int> set1 = {1,2,3,34};
// this is valid 
Set set2  = {"Anuj",1,2,3};

Map dict = {"Anuj":13,"Ajay":13};



// escape character in string `\` this is escape character  
String comma = 'Anuj\'s\n';

String multilien = """ THis is
  multi line
  String """;


void main(){
  for(var v in ablist){
    print(v);
  }
  for(var s in set1){
    print(s);
  }

  // conversion of string to int and int to string 
  String val = "13";
  // String val = "this"; // this will produce an error
  print(int.parse(val) is int);

  int intval = 13;
  print(val.toString() is String);

  print(comma);

  String rawstring = r"this is raw string\n";
  print(rawstring); // this will print same as above the \n will not be processed;

  for(var k in set2){
    print(k);
  }
   String multline = """ This is multiline
      String""";
    
    print(multline);

  String a ='ab';
  String heart = '💙';
  print(a.runes);
  print(heart.runes);
  
}
```

# Null safety : 
* NUll safety prevents the access of the variable that has null value.
* nullable variable : int ? a;
* non-nullable variable : int b=13; // must be initialized at decleration
* variable declared using var keyword without initialization is nullable. e.g var ab; ab= "string", ab = null, ab = 13 // all are correct
* variable declared using var keyword with initializtion is non-nullable unless assigned with null, after initialization it's value if infered and locked for lifetime.
* variable declared using var keyword with intialization value equals to null is same as uninitialized because in both case value is null.

# Late variable : 
* Variable declared with late keywords are used to creat not null variable whose value can be assigned later.
* It has no value unless it's initialized.
* when initialized as nullable it has null value initially late int ?? b; can have null or int
* This is called lazy initialization.


# Reference : 
* To assign value to variable.

# Dereference : 
* To access value from variable.


# Hashcode : 
* very object has a hashcode.
* Object with same content has same hashcode which can be used to compare the equality.

________



# Comments: 

``` dart
// Single line comment : // here is the comment
// Multi line comment :
/* here is
  multi line
the comment
*/
// single line Doc comment : /// this is doc comment
```
```
/** this is
multiline
doc comment
*/
/**
  Doc comments are used as a tooptip in some ids like vscode
  they are also used to generate the docs
*/
// there is not multiline comment in python. But can be written in multi line string which is ignored when not assigned to value

```

___________



# Final & Const 
* They both are used to work with variable whose value doesnot change.
* Final : Final is used for varible whose value will be assigned at runtime. Like network request, datetime
* const : whose value is known at compile time.
* Both final and const can be null depending upon the null safety synatx but has to be declared and initialized at the same time.
* Class level const are declared as static const;
* Instance variables can be final but not const.
* When we define varible with const is shared and only created once.
* const cannot be used insite class for instance variable becuase each of the instance have differnet values which disobeys const to share one value
* Instnace variable can be const but static const.
* When two const variables have same value they have same hashcode, they point to the same object in the memory. this saves the space. This is called canonicalized approach.
* In canonicalization dart uses same memory for two or more idential vairable.
* In final this is not the case.


```dart
  final int a = 13 //valid
  const int c = Datetime.now() // invalid since the value is known at runtime
  const int b = 134; // valid

  const f  = "string" //valid

  class human{
    static const name = "string"; // valid
    const name = "something"; //invalid 
  }
```

___________

# wild card variable : 
* declared using _
* Wild card variable is a variable that get's value but it's by convention used to ingore it.
  
```dart
  int _ = 14; // this is wildcard variable.
  
```
________


# Concurrency : Handling multiple tasks at a time though one thing is done at a time but due to high speed we get an illusion of concurrency. 
* Asyncronous : Async , await, await for stream
* Async function returns Future
```dart
  Future<void> asyncfunc() async{
    int id = await http.get("url");
    print(id);
  }

  void main(){
    print("this is async function");
  
    // so async function can be handled in two ways:
    // either use await to wait for value or use then() to parse the future.
    // if we use await we will have to make function async()
    Future<int> id = asyncfunc();
    id.then((value){
      print(value)
    }).catchError((e){
      print(e)
    })
  }


  // await for can only be used with stream
  await for(int v in values){
      print(v)
  }

```


* **Isolates( threads in box) :**
  * Isolates are container which is responsible for executing certain code, with it's own memory and event loop.
  * Isolates run their code independently and after execution is completed they  transfer the memory containing the result to the main one.
  * They don't share memory and have their own event loop
  * Run in an Isolate is like a control that makes the code execution concurrent.
  * run() is a control flow operator to run in parallel.

  * **Types**
  * Short Lived Isolates.
  ```
  //Created using Isolate.run()
    int varone = await Isolate.run();
  
  ```
  * Long Lived Isolates.
  
```dart
  void main()async{
    int value = await Isolate.run(workerFunc);
    print(value); 
  }

  void main(){
    Future<int> value = Isolate.run(workerFunc);
    value.then((value){
      print(value);
    }).catchError((value){
      print(value);
    })
  }



  // implimenting the long lived Isolates

  void wrokerIsolate(SendPort mainIsolateSendPort){
    ReceivePort thisrecvport = ReceivePort();
    mainIsolateSendPort.send(thisrecvport.SendPort);

    thisrecvport.listen((data){
      print(data);
    })
  }


  void main(List<String> arglist){
    RecivePort mainrp = RecivePort();
    var workisolate = Isolate.spawn(wrokerIsolate, mainrp.SendPort);
    mainrp.listen((data){
      print(data);
    })
  }

```

__________



# Functions : 
* we cannot assign a function to a variable which is not declared a funtion variable.
* Every function returns a value.
* If the return type is void the `return null;` is added at the end of the body implicitly.
  
* Declaring a function varible :
```int Function(int) variablename = (){
    print("this is anonymus function");
    }
```


* **Arrow function**
```dart
  int function = (int x )=> x*x; //this is valid;
  int anotherfunction = (int y) => {return y*y}; // this is invalid in arrow function since cannot have {} block level in arrow function
```

* **Anonymus function** : 
```dart
  // anonymus function has no name
  // we can assign a function to a function variable or to var not to genreal int or string variable
  int func1 = (){
    return 1; // this is invalid function 
  }

  int Function() = (){
    //this is varid function
    return 13;
  }
```

* **Named function** :
```dart
  int namedfunction(){
    return 5+6;
  }

  var normalvar = namedfunction;
  int Function() = namedFunction;

```

* **Closure function**:
* Closure function is a function that is inside the another function and captures the values outside of it's lexical scope
```dart
// closure function in maximum times is a function inside the another function
  int valuefunc(int a){
    int innervalue(int b){
      return a +b;
    }
    innervalue(120); // this is the closure function innvervalue() is a closure function not the valuefunc()
  }  

// closure function is a function that captures the variable from it's nearby lexical scope.

```

* **Generator Function**
```dart
  // generator functions returns value over time either it is iterable or stream
  // iterable is sync
  // Stream is async
  Iterable<int> genfunc()sync*{
    for(var i =0; i<10; i++){
      yield i;
      sleep(Duration(seconds:1));
    }
  }

  Stream<int> genfunc2() async*{
    for(var i = 0; i < 10; i++){
      yield i;
      sleep(Duration(seconds:1));
    }
  }

  // we can yield* to yeild the value over time one by one like yield*[1,2,3,4]

```

_______

* **Tear-offs**
* When we create a refer a function with a variable without calling it, Dart creates a tear off that is function is teared function is assigned to variable.
* Tear offs are reference to a function not a calling to a function
* Constructor tear offs also exists.
* We can now call that function using that reference variable.
* pass named constructor as `class.constructorname` and unnamed consturctor as  `classname.new`
```dart
  // creating tear-offs
  int greet(String name){
    print("Hey, $name - Very good morning");
  }

  void main(){
    var greeter = greet;
    greeter("Anuj Verma");
  }

```
_________

* **Closure**
* Unlike Tear-Off closure also refer to the variable but they are called and then the returned value is assigned to the variable;
```dart
// defining closure

Function greeting(String name){
  return ()=>print("Good morning $name");
}

void main(){
  var greeter = greeting("Anuj");
  greeter();
}
``` 

* **External Function**
* External functions are defined with external keryword and defined somewhere else like extension of dart:js native css etc
* they cannot be defined in teh same file
```dart
  external void externalfunction(int a); // valid one
  external int externalinvalid(int a){return a*4}; // this is invalid one

  void main(){
    externalinvalid(14) // will produce error 
  }
```

___________


# Metadata
* Metadata gives more information about the code
* Metadata's are used to give hints to compiler, tools and even to developers.
* Decorator's in python work similar to metadata in dart `annotations`.
```dart
  // available metadatas;
  @deprecated
  @override 
  @required // this is deprecated use required instead
  required
  @pragma // to give instruction to the commpiler

```
_____
_____
_____

# OOPS : Object Oriented programming.
* Every class in language like dart, python , java is an instance of Object they inherit implicitly, but in C++ it is different.
* Constructors
* Distructors

* **Types of Construcutors**
* **Default** : It is by default, this initializes every nullable attribute with null value and non nullable values must be initialized. They don't have name, neither parameter.
* **Generative Construcutor** : A construcutor with perameter, that is used to initialize the values. Also known as paramterized construcutors in language like cpp 
* **Named construcutor** : Dart allwos to define constructors with different names.
* **Constant construcutor** : Dart allows to define const construcutor in a class where all attributes are to be final. thus helping us to create fully immutable object.
* **Redirect Construcutor** : A constructor that helps to make object through another constructor. Since Dart doesn't allow to call construcutor in the body of another constructor.
* **Factory Construcutors** :  

* const constructors :
* Constant constructors are designed to produce immutable objects
* Constant constructors can only be defined in a class where all attributes are final.
```dart
  class Human{
    final String bloodgroup;
    final List<String> dna_structure;

    const Human(this.bloodgroup, this.dna_structure){};
    
  }
```

* **Factory Constructor**
* Factory constructors are used when class doesn't always return the new instance.
* It can return the existing instance.
* Factory constructor cannot access this.
* Factory constructors are used when we want to simply return an existing instance then to create it.
* We cannot return object inside a construcutor but can do inside a factory.
* Factory constructors are used to do the desired thing with class which cannot be done inside the constructor.
* Factory construcutors are classes level.
* They are not instance level we cannot use the instance inside the factory construcutor.

```dart
  // here we will study about factory constructor 
  class Analyser{
    String ? _subject;
    static final Analyser __Analyse = Analyser._internal("Science");
  
    factory Analyser(){
      return __Analyse;
    }
  
    Analyser._internal(this._subject);
  
  }
  
  class Analyseer{
    String ? _subject;
    static final Analyseer __Analysee = Analyseer._internal("Science");
  
    // we cannot do the same process as above in the current context
    Analyseer(this._subject);
  
    Analyseer._internal(this._subject);
  
  }
  
  void main(){
    Analyser anal = new Analyser();
    Analyser anal2 = new Analyser();
    print(anal._subject);
    print(anal2._subject);
    print(identical(anal, anal2));
  }
```

* **Initializer List**
* Initializer list is used to initialize the members attributes in constructors.
* They were designed to initialize the constant data members of the class, since they cannot be initialized inside the body of constructor.
* They were designed to call the super() function for inheriting classes
```dart
  class Human{
  final int limit;
  int ? age;
  String ? name;

  // this is the way we define a initializer list.
  // the list can be assinged all the values in a function
  Human(int limit, int age, String name):this.limit = 60, this.age =30, this.name = "Anuj";

  Human(this.age, this.name) :limit = 60{}

  Human(this.age, this.name, this.limit){}
  

  }
```
_____


# ways to initialize the attributes of super class.
* A subclass cannot inherit the constructor of a super class.
* It can only inherit the parameter of super class they are called super parameters.
* The super parameters can be initialized using `super.parameter` in the subclass constructors. 
```dart
  // using super.paramtername in subclass paramter list
  // using the super() construcutor
  class Animal{
    String ? name;
    int ? age_limit;
    Animal(this.name, this.age_limit);
  }
  
  class Dog extends Animal{
      int? age;
      String ? breed;
  
      Dog(super.name, super.age_limit, this.age, this.breed);
      Dog.Super(String name, String breed, int age, int age_limit) : this.age = age, this.breed = breed, super(name, age_limit);
  
      void bark(){
        print("Bhaw, bhaw");
      }
  
  }
  
  void main(){
    Dog Labra = Dog("Tyson", 20, 2, "Labrador");
    Dog samreen = Dog.Super("Samreen", "Germam Shipherd", 2, 34);
    print(samreen.age);
    Labra.bark();
}
```


# Access Modifiers : 
* Dart have only one access modifier that is private.
* Every variables , class , methods, mixins starting with this are private.
* Dart have implict public modifier, Every modifier without _ is a public variable which is accessible from anywhere.


# Initialization of attributes in dart : 
* Initialize while you declare it.`String name = "Anuj";` 
* By initializing the formal parameters `Human(this.age, this.name)`
* By using list initializer `Human() :(this.name = "Anuj"), :(this.age = 13)`



# this keyword 
* this keyword refers to the attributes and method of the current object.
* this is not available to use in factory constructor.
* this is not available to use in `super(this.something)` not allowed ✖️.
* this is not allwoed in the right side of assignement operators in initializer list. `constructor(String name) : this.name = this.age` ✖️ not allowed

# Interface : 
* Interface is a pre defined strucutre of what members variables and methods a implimenting class can have.
* Every class is a interface by default.
* Dart, java supports multiple inheritance through the interfaces.
* It supports single inheritance through extends.
```dart
  class HumanPrint{
    int ? age;
    String ? name;

    void printName();
  }

  class Human impliments HumanPrint{
    // here everything in HumanPrint has to overridden.
  }

```
# Methods : 
* Every function inside a class is a method.
* Types : Abstract, getter and setter

# Getters and Setters 
* Every memeber property has implicit getters and setters if applicable.
* In dart it is recommended to define getters and setters with same name as variable using set or get keyword.
* If we define with other names they act as normal method and can be worked around in same way
```dart

  class Blueprint{
    int ? age;
    String ? name;

    void greet(){
        print("hey");
    }
  }

  class Actual impliments Blueprint{
    int ? _age;
    String ? _ name;
    // we have to define getters and setters for the same
    set age(int ? age) => this._age = age;
    set name(String ?name) => this._name = name;

    int get age=> this._age;
    String get name => this._name;
  
  }

```

# Abstract classes : 
* Classes which have abstract methods
```dart
  abstract class Actions{
    void speak();
  }

  class Human extends Actions{

    void speak(){
      print("Hey");
    }  
  }

```


# Abstract methods : 
* Methods which have just decleration but no defination saying that they just have signature no body.
* Abstract method has to be implimented by a subclass inheriting a abastract class.
* they are functions without body inside a abstract class.
```dart
  abstract class Actions{
    void speak();
  }
```

# Mixins : 
* Mixin are the classes without the constructors, they are used to provide functionality to other class.
* They are called mixins becuase they can be mixed with other classes.
* Mixins are used to provide additional functionality to the class without extending or implimenting a class.
* with keyword is used to use the functionality of the mixins
* they are implimented with mixins, or mixins class.
* mixins, mixins class work in similar way.
* if mixins are declared with mixins class this class can be used both as super class and mixins.
* We can also define abastract methods in mixins and they has to be define the class using the mixin.
* THe on clause is used to limit the scope where mixin can be used. if we use on mixins can only be used in class that extends the class used with on in mixin.
```dart

  // here we can use the features of feature class with inheriting the features
  // here the Features can be extended
  // mixins are used to provide additional featurs to classes.

  mixin class Features{
    void SayHey(String ? name){
        print("Hello $name");
    }
  }
  
  
  class Actual with Features{
    String ? name;
    Actual(this.name);
  }
  
  
  class Bro extends Features{
    
    @override
    void SayHey(String ?name){
      print("HEy Brother");
    }
  }
  
  void main(){
    Actual ac = new Actual("Verma");
    ac.SayHey("ANuj");
    Bro bc = new Bro();
    bc.SayHey("ANuj");
  }

  class Animal {
    void move() => print("Animal moves");
  }

  mixin Flyer on Animal {
    void fly() {
      print("Flying");
    }
  }
  
  class Bird extends Animal with Flyer {}  // ✅ Works, because Bird extends Animal
  
  class Dog with Flyer {}  // ❌ Error: Dog does not extend Animal

```


# Enums , Enumerations, Sealed: 
* Enums are the classes with fixed no of constant values;
* they are called sealed becuase they cannot be inherited, mixed, implimented.
* they can simply be made like this `enum Color {blue, green, red}`
* they can also be implimented as class with some advancements and precautions.
* every enum extends the Enum class.
* Abstract class and mixins can extend Enum but it can only be used inside the enum not anywhere else.


# Extension methods : 
* Extension method is a way to extend the features of a class that don't we don't control.
* Like we can add some extra feature on String class.
* There can be unnamed extensions.
* There can be generic extensions as well.
* Extensions can’t access private members of the type.
* You’re not changing the original class — just adding new syntax sugar.
  
```dart
    // here we have added the extension to a String which can be used on any string;
  extension Maybe on String{
      String AddMaybe(){
        return this+" maybe";
      }
  }
  
  void main(){
    String name = "I's possible";
    String modified = name.AddMaybe();
    print(modified);
  }
```

# Extension Type : 
* Extension type is like defining a new type on top of existing type with some added and additional properties.
* It's similar to typedef but it creates complete new type where as typedef just creates and alias
* We can add custom features to type.
* It is experimental and it is new in dart 3.3 +
```dart
  extension Manybe on String{
    String AddMaybe(){
      return this+" maybe";
    }
  }
  
  // here we have created a intiger that is 100 times stronger than regular int.
  extension type BraveInt(int a){
      int braveInt(){
        return a*100;
      }
  }
  
  void main(){
    BraveInt ab = new BraveInt(14);
    print(ab.braveInt());
  
    String name = "I's possible";
    String modified = name.AddMaybe();
    print(modified);
  }

```


# Callable object : 
* Callable object in dart are object which can be called like functions.
* They can be created with call() function implimented in them.
* They are mostly used in flutter.
```dart
  extension Manybe on String{
  String AddMaybe(){
    return this+" maybe";
  }
}
    
    // here we have created a intiger that is 100 times stronger than regular int.
    extension type BraveInt(int a){
        int braveInt(){
          return a*100;
        }
    }
    
    class Callabe{
      String ? name ;
    
      Callabe(this.name);
    
      String call(){
        return "Hello $name";
      }
    }
    
    void main(){
      BraveInt ab = new BraveInt(14);
      print(ab.braveInt());
    
      Callabe c1 = new Callabe("Anuj Verma");
      print(c1());
    
      String name = "I's possible";
      String modified = name.AddMaybe();
      print(modified);
    }
```

# Class Modifiers : 
* They are use to modify and create class.
* they are `abstract base final interface sealed mixin`
* **Abstract** keyword is used to create abstract class.
* **Base class** A class marked with base can only be extended or implemented by other classes that are explicitly marked as base, final, or sealed.
* This prevents unintended or accidental subclassing by external libraries or in large codebases
* **final** keyword is used to create a class that cannot be further extend
* **interfaces** interfaces are ways to design compulsive implimentation.
* **Sealed**  sealed is used to define enums
* **mixin** mixins are used to create mixin class that can be used to other class

# Statement : 
* Statement is a line of code or block of code that says computer to do something. Like give instructions.
# Expressoin : 
* Expression is something that executes the value.

# Patterns : 
* Patterns are used to match against certain values.
* patterns are used to perfrom certain actions in dart like  Switch, Destructuring 
* swtich
* for in
* Destructuring
* List matching
* if case
* **cast** `(num, Object) record = (1, 's'); var (i as int, s as String) = record;`
```dart
  // patterns are just a syntatic category like expression , statement. 
  // they are used to match pattern and destrucuter a value or both.
  // using pattern 
  // 1) we can check shape of something 
  // 2) check if its constant
  // 3) check it's equal to something else
  // 4) has certain type.
  
  // types : 
  // 1) Swtich-case (constant matching)
  // 2) for , for -in 
  // 3) if-case
  void main(){
    List a  = [1,2,3,4];

    if(a case [1,2]){
        print("yes ");
    }else if (a case [1,2,3]){
        print("Yes");
    }else{
        print("NO");
      }
  }
```
  

# wrting folder strucuture and branching 
&#x251C; - branching 
&#x2514; - end of branch 
&#x2502; - vertical line 
