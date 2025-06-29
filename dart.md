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
* We can now call that function using that reference variable.
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


# wrting folder strucuture and branching 
&#x251C; - branching 
&#x2514; - end of branch 
&#x2502; - vertical line 
