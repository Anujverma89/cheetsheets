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

# Reference : 
* To assign value to variable.

# Dereference : 
* To access value from variable.


# Hashcode : 
* very object has a hashcode.
* Object with same content has same hashcode which can be used to compare the equality.

# wrting folder strucuture and branching 
&#x251C; - branching 
&#x2514; - end of branch 
&#x2502; - vertical line 
