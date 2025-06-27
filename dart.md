# Dart : 
* Dart is both general purpose and scripting language.

# Package in dart : 
* package in dart is differnet than that of java.
* every package contains pubspec.yaml file
* It only exposes the lib folder
* importing package "package:app_name/folder/filename.dart"
* In your package the file.dart has to be present inside the lib



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

# wild card variable : 
* declared using _
* Wild card variable is a variable that get's value but it's by convention used to ingore it.
  
```dart
  int _ = 14; // this is wildcard variable.
  
```

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
* Isolates( threads in box) :
  * Isolates are container which is responsible for executing certain code, with it's own memory and event loop.



# wrting folder strucuture and branching 
&#x251C; - branching 
&#x2514; - end of branch 
&#x2502; - vertical line 
