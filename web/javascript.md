# Javascript
* High-level , Dynamic, Untyped, Garbage collected, Interpreted language
* Output, input and other major parts of the language is not defined by the language but by the host.
* Expression (evaluates values)
* Statement (Manuplates code) alters the programs 
* Reserved identifers are keyword in js
* Javascript 
    * Core Javscript 
        * Which can be used in both node and client side
        * Like data types 
        * classes 
        * Objects 
        * Modules 
        * Server side 
        * Regular Expression 
        * String(Text)
        * Math
    * Client-side Javscript


### Basics 
```js
var b=null;
console.log(b);* High-level , Dynamic, Untyped, Garbage collected, Interpreted language
* Output, input and other major parts of the language is not defined by the language but by the host.
* Expression (evaluates values)
* Statement (Manuplates code) alters the programs 
* Reserved identifers are keyword in js
console.log(c);
var c=17;
console.log(c);

// arrow functions is unnamed function which is passed as argument to another function 

function heelo(){
    console.log(1);
}

heelo();


// javascript objectsvar b=null;
console.log(b);
console.log(c);
var c=17;
console.log(c);var b=null;
console.log(b);
console.log(c);
var c=17;
console.log(c);

// arrow functions is unnamed function which is passed as argument to another function 

function heelo(){
    console.log(1);
}

heelo();


// javascript objects

console.log(obj);

var obj = {
    a:1,
    f: function(){
        console.log("This is method");
    }
}

obj.f();

// arrow functions is unnamed function which is passed as argument to another function 

function heelo(){
    console.log(1);
}

heelo();


// javascript objects

console.log(obj);

var obj = {
    a:1,
    f: function(){
        console.log("This is method");
    }
}

obj.f();

console.log(obj);

var obj = {
    a:1,
    f: function(){
        console.log("This is method");
    }
}

obj.f();
```


> Modes   
    Two modes
    Strict mode
    Normal mode   

> Variable decleration   
Using var, let , const 

```js
// this is valid in js since it used unicode character system
// like HTML is also supports unicode and unicode escape sequencevar b=null;
console.log(b);
console.log(c);
var c=17;
console.log(c);

// arrow functions is unnamed function which is passed as argument to another function 

function heelo(){
    console.log(1);
}

heelo();


// javascript objects

console.log(obj);

var obj = {
    a:1,
    f: function(){
        console.log("This is method");
    }
}

obj.f();
const π = 3.14;
const sí = true;
```

`When no explicit semicolon is present javascript implicitly adds it to the statement only when it is non parsable else treats the line break as a semicolon `


>web developmnet is actually a software development that requires to write a code for both clinet side and server side 
if you are developing a android we will develop a frontend application that will probably get data from reset framework developed using any backend.

>If you are a web developer it is recommeded to use mozilla's MDN for doucmentation purpose 

### Statements 
```js
"use strict"


//instruction are called statements 
//multiple expressions combined together are called as statement
//combination of multiple phrases are statements 
//expression produces a value and those expression that also causes something to happend in programme is a statement.
//statement changes the state of the programme i.e it has side effect of programme 
//statements can be condition, loops , jumps.
//statement can be single, compound and empty

if(1<3)
    console.log("hey");
    //above is single statement

if(1<3){
    //here we combine multiple statements and create a compound statement
    console.log("Compound statement");
    console.log("Second stmt of compound statement");
}

if(1<3); //this is and empty statement
//empty statement has no body



//conditional statements 
//they are also called as statements 

//if else and if else ladder and nested if else
if(4<3){

    //combined 
}else if(4>3){

}else{

}

let a ;

try{
    console.log(a); 
}catch(e){
    throw Error(e);
}finally{
    console.log("Executed");
}   

//switch
//switch is used when condition is dependend of the same expression  and heave to check for multiple values of expression 
let exp=4;

switch(exp){
    case 1:
            console.log("One");
            break;
    case 2:
            console.log("Two");
            break;
    case 3: 
            {
                console.log("THree");
                console.log("compund");
            }
            break;
    case 4: {
                console.log(4);
                console.log("Compound");
            }
            return;
    default:
            console.log("Default");
}
//break statement helps to go at the end of the block 
//we can also use return in place of break in js 


/** LOOPS 
 * for
 * for of //works with iterable object 
 * for in 
 * while(){}
 * do{} while()
 * we will discuss for of and for in soon 
 */





/** Labeled statements
 * Break and continue only uses statement labels 
 * 
 */

let i = 0;
idea:while(i++ <= 15){
    console.log("RUnning");
    if(i%4 == 0){
        console.log("Skipping");
        continue idea;
        
    }
}


/**Jump statements 
 * Continue :Only breaks the loop for current iteration and starts the loop again skipping the current one 
 * The current iteration is terminated and next is continued 
 * 
 * Break : goes to the end of the programme and ends it 
 * 
 * return : only used in the body of the function 
 * 
 * yield : used as return but only in generator function as on ES6 we will understand it in upcoming generator and interator 
 * 
 * throw : is used with try catch and finally 
 * 
 * try catch finally : error handeling mechanism 
 * 
 */


//with & debugger & use strict 
//debugger is used to debugging purpose 
//use strict is a directive 

```

### Variables 
```js
// mainly primitive and non-primitive 
/**Primitive 
 * Numbers (integer & Floating points)
 * Strings(Text)
 * Boolean
 * null
 * Undefined 
 * Symbol
 * Primitive types are non mutable 
 * 
 * 
 * 
 * 
 * Non-primitives 
 * Objects 
 * 
 * It automatically performs type conversion 
 * JS is non typed lanuage. The data that is allowed to manuplate in langugae is called types allowed in language.
 * 
 * classes and object are special kind of object in javascript
 * Only objects have method and rest all assume to have  methods 
 * == is conversion operator in js
 * === is eqality operator in js 
 * 
 * 
 * 
 */

"use strict"


let obj = new Object();
let arr = new Array();
arr.push(4);
let date = new Date();
console.log(arr);
console.log(date);

//NUmbers 
// numbers are numbers in js 
let n = 14; //decimal 
let n1= 14.1; //real no 
let n2 = 15.15;
let n3 = 0xf; //hexadecimal
let n4 = 0o3452; //octet
let n5 = 0b01001; //binary
console.log(n3);
let decimal = 3.5e10;
console.log(decimal);
let nibble_seperator = 100_100_100; //for better readbility 
console.log(nibble_seperator);
// Arithmetic in JavaScript does not raise errors in cases of overflow, underflow, or division by zero.
//infinity +infinity (When number is larger than largest value that a variable can hold)
//- infinity (when number is smaller than the smallest no that a variable can hold)
//division by zero is not an error in js 
//when js is unable to convert data to meaning full number it converts to NaN
console.log(0/0) //NaN
console.log(Infinity/Infinity); //NaN
console.log(Infinity*Infinity);
console.log(Math.sqrt(-1)); //NaN
console.log(14+'t');
let neg_infi = Number.MIN_VALUE / 2;
let pos_infi = Number.MAX_VALUE *2;
console.log(neg_infi);
console.log(pos_infi);

// javascript defined negative zero and positive zero and both of them acts similar and nearly indistinguishable
let x = NaN; 
let y = NaN;
console.log(x===y); //equality operator cannot be applied on NaN
console.log(Number.isNaN(x));
console.log(Number.isNaN(y));
console.log(-0 === 0); //both negative and positive are zero 

//there is BigInt in js they are written as string of digits followed by letter n 

let bigint = 239723487638235623n; //this is big int 

console.log(bigint)

// value equality == and this is performed by converting one type into another and then checks the result.
//== flexible equality operator
// type equality + value  ===
//strict equality operator ===

//Data is a class and DateTime is an object but also provides mechnasim to manuplate the numbers associated with it 

let dt = new Date();
console.log(dt.getTime())
console.log(dt);
console.log(dt.toISOString)




//strings 
// string every value in a string is 16 bitt 
let a_string = "HEllo this is string";
console.log(a_string.length)
// printing the length of the a_string.length this technique is called string literal and they can expand in many lines 
let a = `this is ${Number.MAX_VALUE}, this is ${Number.MIN_VALUE}`
console.log(a)
let newString = "THere is nothing new to work";
console.log(newString);
console.log(a.toUpperCase());
// Strings are immutable in js, i.e primitive values are immutable in js and objects are mutable in js 
// strings can be included in 'Single Quotes' , "double quotes", `backticks`
// backslash acts as a escape sequence \ 
//there are different other methods available to work with strings in js 
//there is also presense of regx to work with pattern matching in js 





// boolean values
//true or false ture means 1 and false means 0 or empty string or empty array etc 
console.log(2==2);
let em= "he";
console.log(isFinite());
//boolean values have toString() method available 

// null and undefined 
//null means no value
//undefined also means absense of value when value is not initailized or doesnot exisits
let b = null;




// symbols
// symbol always give different result though derived from same string
let s1 = Symbol("hello");
let s2 = Symbol("hello");
console.log(s1);
console.log(s2);
console.log(s1==s2);




//GLOBAL
// this global object is available at the start of the programme 
// in browser is the global variable available to all the members.
//globalThis is used to refere global objects 
console.log(globalThis)
console.log(global)







//type conversion 
//implicit is performed by js whenever needed 
// explicit conversion 
let cn = Number("4");
let sst = String(4);
let bln = Boolean(undefined);
console.log(cn, sst, bln);
console.log(typeof(sst))

//except null and undefined every other types has toString() method available 
let value=4;
value.toString();
console.log(typeof(value.toString()))

//method available in numbers are toFixed() toPrecision() toExponential()
//pareseInt() & pareseFloat() are global functions works on string to  convert into numbers 

let int = parseInt("              01         ",2); //$45 produces nan 
console.log(int);
let float = parseFloat("              56.34");
console.log(float);



// object to primitive conversion takes by using 3 algorithms in place
//object to primitive conversion algorithm 
//prefer string
//prefer number
//no preference 
//date object is converted to primitve using prefer-string algorithm that is toString() ratherthan valueOf()
let arrr = [1,2,4,5];
let str = arrr.toString();
console.log(arrr.toString(),str);

let func = function(){
    console.log("THIs is desired function");
}
console.log(func.toString());

//calling above func() function
func();


let dttt = new Date();
console.log(dttt);
console.log(dttt.valueOf());




// variable decleration 
//it is a global convention to use all caps for constant values
const LL="value";
let l = "new value"; //no variable hoisting
var varr = "hosted variable" //this performs variable hositing when declared with var keyword 

// distructuring assignment also can declare variable this way
let [newd,newr,newt,...arrar]= [1,2,4,"5","y",2,3,4];
//here last elements acts as array and holds all remaining values 
console.log(newd);
console.log(arrar);

//the numbers in left and right is note expected to exactly same the left one will be undefined 
let [le,ge,gee,re] = "hee";
console.log(re);

//the values in righthand side must be iterable to work with distructuring assignment
let [ewew,werwe,werw]="hasdfhakjsdhf";
console.log(ewew,werwe,werw);

//NULL and UNDEFINED 
let nll = null; //null meand no value but the variable exists 
let undf = undefined; // variable may or may not exist but the value is undefined 
```

### Objects 
```js
//object can inherit properties called prototype.
//everything in js is an object excpet string, number, null, symbol, undefined 
//objects have properties and properties can be inherited
//properties can be writeable, configurable, enumerable
// there is property and prototype
// when no prototype is passed in object to inherit is inherits object.prototype

// here we can see that object p is prototype for object a 
let p = {
    a : 14,
    b :15,
}


let a = new Object(p);
a.name = 14;
console.log(a.name);
a.age = "Fourteen"
console.log(a.b)
console.log(a.age)
console.log(p.prototype)
let c = new Date();
console.log(Date.prototype)
console.log(c);

// ways to create an object 

let new_obj={
    a:"Anuj",
    b:"No ANuj",
}

// another way to create 

let an_obj = new Object();
an_obj.name="Anuj";
an_obj.idea="Solve problem";

// this is an object literal  a ={ a:b,b:c}
//object created by object literal have same prototype

let new1ob = Object.create(Object.prototype);
console.log(new1ob.prototype)
console.log(new1ob.a)
console.log(new1ob)


// javascript objects are associative arrays that can be accessed just like arrays by passing named index as string
// Associative arrays are arrays where we access values by name not by index no
//in Javascript object can inherit properties from another object and they are called as prototype.
//inheritance occurs when querying properties not while setting properties lets see and exmaple

let set = {
    a:14,
    b:15,
    c:5,
}

let set1= Object.create(set);
set1.d = 11;
set1.e= 16;
// now set1.b is inherited while querying but while setting the original is not being modified.
set1.b=3;

console.log(set1.b);
console.log(set.b);


// querying properties 
console.log(set1["a"]);
set1.g="hellobro";




// deleteing properties from objects 
//when not in strict mode wherether property is deleted or not delted it always return true
//when in strict mode it return false if it cannot delete properties
//delete cannot delete inherited properties 

console.log("d" in set1);
delete set1.d;
console.log(set1.d);


// checking if property exists in the object

console.log("d" in set1);
console.log(set1.hasOwnProperty("g")); //checks if the object has own property not the inherited one 
console.log(set1.propertyIsEnumerable("g"));


// enumerating properties 
// using for in loop


for(let p in set1){
    console.log(set1[p])
}

// ways to get array of all keys present in object
let arr = Reflect.ownKeys(set1);
console.log(Reflect.ownKeys(set1));
console.log(Object.keys(set1));
console.log(Object.getOwnPropertyNames(set1));
console.log(Object.getOwnPropertySymbols(set1));

for(a of arr){
    console.log(a)
}


// we can also extend objects by assigining values to another object 
//all below functions can be used to extend objects 
// Object.assign();
// Object.merge();
// Object.substract();
// Object.restrict();

// object seraialization 
let st = JSON.stringify(p); //convert object to string
JSON.parse(st); //convert string to object

let val = Infinity;
let anval = Infinity;
console.log(val+anval);



// object methods
//toJSON()
//valueof()
//toLocaleString()
//toString()
let q = p.toString();

console.log(q);


// es6 syntax shorthand properties
let x =4, y = 5;
let newshrt = {x,y}; //this is object having 4 and 5 value



// can use computed propoertie names that is it can be variable 
var value ="prop_name";
let com_obj = {
    [value]:"HELlo anuj",
}


//can use symbol as properties



console.log(com_obj[value]);
//spread operator 
let newwwobj = {...p,...a};
console.log(newwwobj.a);

//when a function is defined as value of property it is called as method;
//getter ans setters


let getter={
    data:null,
    id:null,
    set d(data){this.data=20},
    get d(){return this.data},
    set i(id){this.id=id},
    get i(){return this.i},
    com(){console.log(this.data+this.id)},
}

getter.data=15;
console.log(getter.data);


//object reference 
let newobj = {
    ob_d:"THis is ob data",
}

let newobj3 = {
    ob_d:"THis is ob data",
}

//heere newboj1 is not having the copy but instead it is refereing to the same object and it called reference variable in js

let newobj1 = newobj;
console.log(newobj1);
console.log(newobj);

newobj1.idea = "THis is new idea";
newobj3.idea = "THis is new idea";
console.log(newobj);

//while comparing two objects it compares whethere they are refering to same object not the actual value that they are holding

console.log(newobj == newobj1); //this evaluates to true because they are refering to the same values 
console.log(newobj === newobj3); //this evaluates to false becuase two of the references are pointing to different object not to the same




//rich boject 

let sym= Symbol("oneSymbol");
let arcnm = "idea";

let richoj ={
    [sym]:1,
    [arcnm]:2,
    doc(){
        console.log("Documentation functinon ");
    },
    idea:"fourteen_work"
}

richoj.doc();

console.log(Object.keys(richoj));

for(let o in richoj){
    console.log(richoj[o]);
}
console.log(richoj[sym]);
```

### Let, Var, Const
```js
// let var and const

let a = 14;
var b = 17;




const c = 18;
// we cannot assign values to constant variable in js which is declared as const 
c = 18;
console.log(c);


//ojbects are not nested in they just point to another one 
```

### Functions
```js
// function in js 
//functions are also called as subroutine or procedures 
//function also holds this keyword along with arguments and the value of this is the context of the invocation 
//function can be constructor can be method and can be just a function 
//functions are object so properties can be set on them and can also invoke methods on them 
//functions also act as clousre in js i.e they can be nested inside a funcitno 
//functinos can be declared in three ways 
//Arrow function 
//function decleration 
//function expression 
//calling of function is called as invocation of function 
//there are also immediately invoked function expression 

"use strict";

fe();
//function decleration method 
//this function has ability of hoisting that is it can be called before it is defined 
//it is available to the top level or hosting environment.
//its name is variable that holds the enitre function as boject 
function fe(){
    console.log("Decleartion function");
    console.log(this); //this prints the global object when in non strict mode and undefined when in strict mode
    return ; //this will return undefined since there is no any return value
}
//funtions returns either undefined or a value to it calling expression or invocatin expression 

//function invocation when invoked this referes to the global object and also there is no need to use this keyword  
//return value is undefined if there is no explicit return value
//this basically refers to exection context 
//when a function is executed the control is returned to the calling context 
//for every function call a context is maintained in a stack 







//function expression 
//HEre name is an optional property
//it cannot be called before it is written i.e no hoisting
//we careate a function expression and assign as object as cosntant or variable 
//func(); //this gives error 
const func = function (){
    console.log("Expression funciton ")
    //this will also return undefined since there is no return statement 
}
//this executes fine 
func();





// arrow function 
//this doesnot supports the hoisting
//this function inherits the value of this keyword 
//this funciton has no prototype so it cannot be used as constructor in classes 

//we have to use empty braces when there is no parameter 
let arr = ()=>{console.log("Arrow function type 1")};
arr()

//we can omit curly braces when there is single parameter
let arr2 = x=>{console.log(`Arrow function type ${x}`); return 1; /*this will return 1 */};
console.log(arr2(2))


//when one return is there we can ommit curly brases 
let arr3 = (x) => console.log(`Arrow function type ${x}`);
arr3(3);

let arr4= ()=>{console.log(this)};
arr4();





//nested functions 

//method invocation 
//is similar to the function invocation but the only difference is that the context is the object calling it 
//i.e this refers to the object and can access object using this
//object is the invocation context
//every method has a implict argument that is object that is operated on 

let obj = {
    a:1,
    func(){
        let self= this;
        fg();
        console.log(this);
        //nexted functions
        
        function fg(){
            //this will print undefined as it doesnot inherit this keyword 
            console.log(this);
            //this prints the current object ans it is a hack
            console.log(self);
        }
        //this inherits the value of this keyword that is object context 
        let arr = ()=>{console.log(this)};
        arr();
    }
}
obj.func();




//constructors invocation 
//constructors invocation is leaded by new keyword 

//both are correct
//they do not have return value because they  initialize & implicitly  return the new  object 
//but constructors can return value, i.e either primitive or object is not object the code will reject and accepte object 
//new object is invocation context for constructors 

let ob1j = new Object();
let obj2= new Object; 


// indeirect invocation we can use call() or apply() to invoke method as functions are object and object have method and they can be called 

//implicit calling of methods
//toString() when converting to string 
//valueOf() when working with numerical value implicitly it is called 
//getters() and setters() are called when accessing and setting properties implicitly 
//proxy object()
//tagged template literals 


//parameters list of calling function 
//when we pass less no of parameters than expected the last not given values are treated as undefined 
function furrey(idea, noidea){
    //here no idea becomes undefined
    console.log(idea+noidea);
}

//pass default value while definfing paramet in es6
function def(idea , noidea="Great idea"){
    console.log(idea+noidea);
}

furrey("HEy");
def("working around ")


//rest parameters and varargs function 
function varargs(varr, var1, ...varrr){
    //the rest parameter is always an array it can be empty but no default value is legal for this
    console.log(varrr);
}

//this will print and array of varrr;
varargs(undefined, undefined, 1,243,4,5);


//befoer of rest paramaeter argument was used and it was used in body of the function as argument 
//argument was used as an object and passed to function as and object below is the representation 
function argfunc(x){
    console.log(arguments);
}

argfunc(1,2,4,4,5);

//must not use arguments instead use rest parameters 

//spread operators in js is used to unpack iterable objects 
function sepread(){
    let arr = [1,3,4,5,5];
    let anrr = [...arr];
    console.log(anrr);
    return (arr)
}


console.log(sepread());


//distructuring arguments there are multiple combinatin of object distructing and can be used with different combinatinos
function destructoire(arr,arr2,{a,b=5}){
    console.log(arr[0],arr[1]);
    console.log(arr2[0],arr[1]);
    console.log(a,b)
}

destructoire(["anuj","vera"],["idea","hack"],{a:1,b:2});
destructoire(["anuj","vera"],["idea","hack"],{a:1});

//functinos in js are not just syntax they are also values that they can be assigned to the variables or constants

//types of arguments 
//As js is not types lanuage it can accept any type of argument and then it matches with requried type.

//function as namespace basically deals with solving the conflicting problem of declaring same variable in namespace.


//closure : function object and the local environment where the function's variable are resovled 
//it references the the variables in which it was scoped
//javascript functions are executed using the scope they are defined in not the scope they are called from 


//properties of functions 
//prints function
console.log(typeof(destructoire));
//length property
console.log(destructoire.length);
//name property
console.log(destructoire.name);

console.log(destructoire.prototype) //an empty prototype


//call and apply 

function con(){
    console.log(this);
}

let newobl = {
    ida:12,
    nida:13
}

con.call(newobl); //the context is passed as paramenter // acepts argument as a parameter
con.apply(newobl);


//bind() functions
//bind() binds the object to the function and returns the new function which is then called to call the previous funciton
//toString() converts to string 

//new Function() //creates dynamic function at runtime
// it is actually a function constructor 
//functions are objects that can be manipulated by JavaScript, and this enables a functional style of programming.
```

### Front-end
```js
let doc = document.getElementById("") //returns single element
let doc2 = document.getElementsByClassName("") //retuns array of names 
let doc3 = document.getElementsByName("") //returns same as doc2

//onSubmit() should be applied on form not on button 
//it works fine while added with eventListner not with onsubmit
//all the data is there in target[].value
```
### Expression 
```js
//expression can be evaluated and produce a value 
//literal is actually a constant 
//expression evaluates to value and complex expression is made up of simple expression 
//simple expressions are made up of operands, operators, identifiers, keywords etc 
//Operators are the part of expression that helps to perfrom logical, arithematic, relational operation.

//object and array initializer 
//array initializer expression 

// "use strict"

let array = [1+2,3,,,5,5];
for(let a of array){
    console.log(a);
   
}
console.log(array.length)

//object initializer  expression 
let obj = {a:1,b:2,c:3};
console.log(obj);

//function declartion syntax
//compact function declaration 
let func = (()=>{
    console.log("HEY");
})

//long function declartion syntax
let fn = function(){
    console.log("ANother function f");
}
//can call using fn 

function fall(){
    console.log("this is fall function ");
}

fn();
fall();
let retu = func(); //when no return type is there function returns type is always an undefined.
console.log("retur is "+ retu);
//object's property access expression 
//object.identifier(property)
//object[property];
console.log(obj.a);
console.log(obj["a"]);


//conditional access of the properties 
let new_obj = {
    a:"b",
    b:"c",
    c:"d",
    d:"2",
    func(){
        console.log(this);
    }
}
// new_obj = undefined;
//evaluates like if new_obj != undefined then proceed further else evaluate all as undefined as it is shortcurcit operator 
//this is called as conditional property access 
//there is also a concept of conditional method invocation that acts similar as conditional property access 
let cond = new_obj?.b;
console.log(cond);
//when method invocation takes place i.e function of a object is called this refers to the current object 
new_obj.func();

//object creation function 
let Newobj = new Object({number:1,number2:2});
console.log(Newobj.number);




//operator and operator presedence and associativity
//operator presedence which opeartor will be evaluated first when present in the compound expressoin.
//we can also decide the explicit order of execution by using parenthesis 
//associativity defines the order inwhich the operator with same presedence are executed.
//ternary operator in javascript
//some operators need their own type of operand whereas other convert given operand into required type.
//every value is truthy or falsy in js either it is true or it is false 
//lval are the values that appear in the left side of the expression like variable etc 
let ter = 4<3?true:false;
console.log(ter);

//operators takes multiple operands
//unary operators
//binary operators
//ternary opeartors 



//arithematic expression 
//Nan operating with any other number is always NaN
//expression = operands + operators 
/*/presedence 
    ** exponent highest
    * / %
    + -  
    = Lowest
*/
//this will always evaluate to NaN
let a = NaN + 14;
console.log(a);

//+ operator when one is string and another is number second also evaluates to number and reslts to string
let strn = 12+"str";
console.log(strn);

//concatination with string
//unary operator +, - , ++, --
console.log(obj+"dong");
//unary + opearator
console.log(+(-16));

//bitwise opeartors are also arithematic operators 
//rightshift with zero fill 

//arithematic expression  ++, --, +, - **, /, % ,* = 
//bitwise operators are part of arithematic operator (&, |, ~, >>, <<, >>>, ^)

//Relational expression (eqiality operator(==) & strict equality operator(===))
/** comparision(==, ===)
 * >
 * <
 * >=
 * <=
 * in operator (a in "apple")
 * instanceOf() checks if the object belons to certain class
 */

//Logical expression  (&&, || , !(not))
//Assignment expression and compound assignment expression (+=, -= , *= ) & bitwise compound assignment

//Evaluation expression  
console.log(eval("3+4"));
//eval() can be evaluated in strict mode , global eval() and only eval()
let dt = new Date();
console.log(dt instanceof Date);


//misceleneous ooperator 
//conditional or ternary ooperator 
let varr = 4>3?true:false;
console.log(varr);

let Mathh={
    sin:undefined,
}

//since Mathh.sin is undefined so the value of idea will be globalThis
// globalThis = undefined;
//we have also set globalThis as undefined so the value as 5000
//it gives the first defined value
//first defined
let idea = Mathh.sin ?? globalThis ?? 5000;
console.log(idea);

//typeOf operator used in js gives the type of literal or variable both of the below syntax are true.
console.log(typeof idea);
console.log(typeof(idea));

//delete operator deltes certain proteris 
console.log(globalThis);
delete globalThis; // we have deleted globalThis variable from global scope and this will be no more further obtained 
// console.log(globalThis);
let new_del_arr = [1,2,4,4];
delete new_del_arr[3]; //deletes the third item from array and also can delete anything property or object 
//however delete cannot be called on identifer on strict mode 
console.log(new_del_arr);


let del_obj = new Object({a:1});
delete del_obj;
console.log(del_obj);


//await keyword is a operator that say the object is waiting for asynchronous call
// we will discuss later on 

//ther is also comman operator that acts as seperator 
```

## OPPS
### Class
```js
//js classes work bit differently that their inheritance is bascially works in the principle of prototype inheritance 
//it follows prototype based inheritance 
//there is a prototype object that is inherited by all the objects of a class 
//all objects have prototype and only few have prototype property i.e prototye inside prototype
//classes may contains factory function and constructors 

class Try{
    //private method 
    #var1;
    #var2;

    constructor(work=null,research=null){
        this.work =work;
        this.research =research;
        this.#var1 = 0;
        this.#var2=2;
    }

    static tellcorrect(objnon){
        if(typeof objnon === "string")
        return true;
    }

    print_work(){
        this.work?console.log(this.work):console.log(this.research);
    }
    prototype={
        run(){
            console.log("RUnning prototype");
        },
        unrun(){
            console.log("Unrun");
        },
        prototype:"THis is prototype",
    }



    //getters and setters 

    get var1(){return this.#var1};
    get var2(){return this.#var2};
}


class Newtry extends Try{
    constructor(work){
        super(work)
        this.newwork= work;
    }
}

let object = new Try(undefined,"Software Engineer");
object.print_work();

//cannot call this method as it a consrtutor function 
// object.tellcorrect("idea");
let idea = Try.tellcorrect("HEy")
console.log(idea);

let newObj = new Try("software Engineering", undefined);
console.log(newObj.prototype.prototype);


let newnetry = new Newtry("IDeation");
console.log(newnetry.prototype);
console.log(newnetry.var1);

let ner = new Array();
console.log(Array.prototype);

console.log(newnetry instanceof Newtry);
//this is true if it inherits the property of prototype of class

//static , getters and setters

//static method is a property of constructor not a property of a class so it must be called using a constructor 

console.log(object.var1);
console.log(object.var2);
//when accessing private variable without get gives a undefined value 
```


### Async 
```js
//asychronous programmes 
//promise
//async/await 
//for/await

//settimeout as async 




const fs = require("fs");


function work(){
    console.log("Doing some work as async" );
}
//runs the function once after the time condition is met 
setTimeout(work,6000)
//does somework after anInterval of time continiously until a condition is met 
//It does same thing as setTimeout() but what it does does repeatedly after the interval of time
let t=0;
let interval=setInterval(()=>{
    t+=1;
    console.log(`Time elapsed ${t} sec`)
    if(t==6){
        clearInterval(interval);
    }
},1000);


//asynchrounous there is code that is running and when certain event occurs it calls another function
//when any event occurs it gives a call to certain functin which is called as callback
let defen = function(value,callback){
    if(value%2===0){
        //this defen function is calling another function names as call back and this is the example of call back 
        callback(true,undefined);
        return true;
        
    }else{
        callback(undefined,false);
        return false;
        
    }
}


defen(7,(result=0,err=0)=>{
    if(result){
        console.log(result);
    }else{
        console.log(err);
    }
});

//when there is callback inside callback and callback inside a callback this causes inreadiblity of code which causes callback hell.


//promises 
//promises are returned before the computation is performed 
//as promises shows the future result which will be returned 
//doSomething().then((resultfunc).catch(errorhanlding));
//doSoemthing().then(resultfunc, errorfunc) //this is also correct 
//promise is an object that returns the reuslt of asynchronous computation
//promises either fullfilled or rejected it cannot be both. Once promise is fullfilled or rejected it is settled or else it is pending.


//there is also a promise chain 

//lets take an example of promise 
//XMLHttprequst is a callback based api 
//fetch api is promise based api 

function mise(value){
  return new Promise((resolve,reject)=>{
    if(value==false){
        reject("the promise is rejected");
    }else{
        setTimeout(resolve,6000);
    }
  })
}

function result(value){
    console.log(value);
    console.log("FIne");
}
function error(value){
    console.log(value);
    console.log("Not fine");
}

mise(true).then(result,error);



//promies chaining
//prmise0 , prmoise 1, promise 2
//asyncfunc().then().then()
//resolving and settling promises are two different things 
//promise is settelled when the callback function returns value not the promise
//promise is resolved when the callback function returns the another promise and that is to be resolved, in this case the 
//previous prmoise is resovled but it's settlement will be dependent on the callback's promise settlement
//catch() and finally() are ways to handle error in asynchronous code 
//promise().then(()).catch().finally() //finally is a cleanup code that runs
//finally() returns promise or callback but that is generally ignored 
//when we chain multiple then() the same error propogates to all the level of then until the error hadneling i.e catch()
//Since different then() are related to one another the error keeps propogating to the upper level 
//it is always a good practise to endup promises with catch()
//when throw throws error then it is catched by catch() block;
//the value returned by one stage of chain becomes the value for next stage of chain so we have to be careful about what are we returing
//we can use multiple catch with then 
/**
 * promise()
 *.then().catch()
 *.then().catch()
 *.then().catch() //this way we can chain up errors 
 * 
 */



//promise in parallel 
/**promise.all() //takes input of promies object if one is rejected all of other gets rejected
 * promise.allSettled() //is similar to promise.all()
 * promise.race() //retunrs the first promise object that is resolved 
 */


/**
 * New way of asynchronous coding using async & await 
 * when promises are resolved they return value
 * when they are rejcted they throw error like regular synchronous programme 
 * await is keyword that is like a return of promise based function 
 * it can either be a value or a error thrown 
 */

let awaitfun = async function(){
    return await 400;
}
console.log(awaitfun);
```

### Arrays 
```js
//arrays are objects in js 
//array can be sparse and dense both 
//Elements can only be accseed using index no that starts from 0 till 2^31;
//array in js inheirts array.prototype that has plenty of methods available to manuplate 
//ES6 introduces typed array they have fixed length and fixed numeric type 
//creation fo array 
//using literal 
//using ...spread operator 
//using constructor 
//using array.of() or array.form()



let arr = [] //empty array
let arr1 =[1,2,3,4];
let arr3 = ["anuj",1,4];
let object_arr= [{a:1,b:2},{c:1,d:2}]; //array of objects 
let spare_arr = [1,,3,4,] //sparese array the value is undefined for ommitted one 


//using spread operator 

let spread_arr =[1,...arr1];
console.log(spread_arr);

let strin = "asdfarwera";
let new_str= [...strin]; //this converts string into array of character 
console.log(new_str);
let new_string = [..."hello another string"];
console.log(new_string);


//array constructor 
let const_arr = new Array(10); // this is the length of an array
const_arr.push(10);
const_arr.push(141); //.push method appends the data after the specified length
const_arr[0] = 124141;
const_arr[1] = 23414321; //this way we can pass the values to the array indexses 
console.log(const_arr.length);

for(let a of const_arr){
    console.log(a);
}

let const_arr_len  = new Array(1,2,4,4,5,5);

for(let a of const_arr_len){
    console.log(a);
}

//array.of() 
//this is used to create of single or more element unlike array constructor that treats single element as the length of the arrya 

let array_of  = Array.of(5); //creates sparese array 
console.log(array_of);
let more_arry = Array.of(4,5,6,6,);
console.log(more_arry);

//array.form() works  on array like object which take array and function as a second argument

//create array like and object 

let arrLike_obj = ["idea","func"];

let func = function(){
    console.log(arrLike_obj);
}

let new_arry = Array.from(arrLike_obj,func);
console.log(new_arry);


//all indexes are properties but all properties are not index they are only integers 
//in sparse array the length si greater than the no of element in the array 
//array's length is updated as we assign values to array object 

//adding items to array and delteing 
//deleteing causes sparese array 
//adding can be done using index 
//can use array.shift() to delete and shift the array at the space
//array.unshift() to add element at the begining
//array.splice() can be used as a general method 
arrLike_obj[4]=14;
arrLike_obj.push("this is idea");
console.log(arrLike_obj);


//iterating arrays
//for of // iterates through every element of an array wheather it is defined or undefined 
// for each // works similar ot for of but is sensetive to undeifined that it it doesnot skips the sparse index 


//multi dimentional arrays 
let mul_arr = [[1,2,3,4],[5,6,7,8]];
console.log(mul_arr[0][1])




//methods that are available in arrays 
//iterator method 
// foreach(function, array element optional, arrayindex options, array itself option)


//modifies the arrray 
let iterarr = [1,2,3,4,5,6,7];
//first arg is element, sencond is index ,t hird is array
let net_it = iterarr.forEach((value,arry_in,arr)=>{arr[arry_in] = value+5});
console.log(iterarr);


//returns new array 
let mappedarr = iterarr.map((value,idex,arr)=>{return value*value});
console.log(mappedarr);




//flat & flat map 
//flat is used to nesting of an array and convert it into single level array 
//array.flat(integer) // to convert into flat 
//flat.map is similar to map()
//first flats then maps

//array.concat(array) == to add to arrays 

//array as stack push, pop, shift() and unshift()

//subarray slice(start, end), splice(), fill(value, statindex) copywithin(replacementindex, startindex for reaplcement, end index for replacment);

//indexof(start) //lastIndexOf(end) start to end and end to start(lastIndexOf), include(), sort(), reverse()



//array to string .. 
console.log(mappedarr.toString());




//array like objects 
//array like objects are objects with non-negative interger properties and length properties

let obj = {0:"Idea",1:"execute",2:"execture"};
obj.length = 3;
console.log(obj.length);

//so now it array like object with length property 
//remember they are array like object not true arrays but maximum of methods work on them 
//no direct methods can be called on array like object they can be called using function.call
//like array.prototpye.join.call()
let new_array = Array.from(obj);
console.log(new_array);
//now you can call all the method directly


//stings as arrays
let string= "thisisarrayofstring";
console.log(string.length);//asychronous programmes 
//promise
//async/await 
//for/await

//settimeout as async 




const fs = require("fs");


function work(){
    console.log("Doing some work as async" );
}
//runs the function once after the time condition is met 
setTimeout(work,6000)
//does somework after anInterval of time continiously until a condition is met 
//It does same thing as setTimeout() but what it does does repeatedly after the interval of time
let t=0;
let interval=setInterval(()=>{
    t+=1;
    console.log(`Time elapsed ${t} sec`)
    if(t==6){
        clearInterval(interval);
    }
},1000);


//asynchrounous there is code that is running and when certain event occurs it calls another function
//when any event occurs it gives a call to certain functin which is called as callback
let defen = function(value,callback){
    if(value%2===0){
        //this defen function is calling another function names as call back and this is the example of call back 
        callback(true,undefined);
        return true;
        
    }else{
        callback(undefined,false);
        return false;
        
    }
}


defen(7,(result=0,err=0)=>{
    if(result){
        console.log(result);
    }else{
        console.log(err);
    }
});

//when there is callback inside callback and callback inside a callback this causes inreadiblity of code which causes callback hell.


//promises 
//promises are returned before the computation is performed 
//as promises shows the future result which will be returned 
//doSomething().then((resultfunc).catch(errorhanlding));
//doSoemthing().then(resultfunc, errorfunc) //this is also correct 
//promise is an object that returns the reuslt of asynchronous computation
//promises either fullfilled or rejected it cannot be both. Once promise is fullfilled or rejected it is settled or else it is pending.


//there is also a promise chain 

//lets take an example of promise 
//XMLHttprequst is a callback based api 
//fetch api is promise based api 

function mise(value){
  return new Promise((resolve,reject)=>{
    if(value==false){
        reject("the promise is rejected");
    }else{
        setTimeout(resolve,6000);
    }
  })
}

function result(value){
    console.log(value);
    console.log("FIne");
}
function error(value){
    console.log(value);
    console.log("Not fine");
}

mise(true).then(result,error);



//promies chaining
//prmise0 , prmoise 1, promise 2
//asyncfunc().then().then()
//resolving and settling promises are two different things 
//promise is settelled when the callback function returns value not the promise
//promise is resolved when the callback function returns the another promise and that is to be resolved, in this case the 
//previous prmoise is resovled but it's settlement will be dependent on the callback's promise settlement
//catch() and finally() are ways to handle error in asynchronous code 
//promise().then(()).catch().finally() //finally is a cleanup code that runs
//finally() returns promise or callback but that is generally ignored 
//when we chain multiple then() the same error propogates to all the level of then until the error hadneling i.e catch()
//Since different then() are related to one another the error keeps propogating to the upper level 
//it is always a good practise to endup promises with catch()
//when throw throws error then it is catched by catch() block;
//the value returned by one stage of chain becomes the value for next stage of chain so we have to be careful about what are we returing
//we can use multiple catch with then 
/**
 * promise()
 *.then().catch()
 *.then().catch()
 *.then().catch() //this way we can chain up errors 
 * 
 */



//promise in parallel 
/**promise.all() //takes input of promies object if one is rejected all of other gets rejected
 * promise.allSettled() //is similar to promise.all()
 * promise.race() //retunrs the first promise object that is resolved 
 */


/**
 * New way of asynchronous coding using async & await 
 * when promises are resolved they return value
 * when they are rejcted they throw error like regular synchronous programme 
 * await is keyword that is like a return of promise based function 
 * it can either be a value or a error thrown 
 */

let awaitfun = async function(){
    return await 400;
}
console.log(awaitfun);
//genral methods of arrayca cannot be called on it 
let newarryform = Array.from(string);
console.log(newarryform);


//to determine whether given object is type array or not 
console.log(Array.isArray(newarryform));


//you can come back for array method and refer the section here in the book that you have
```
### Modules 
```js
    // Modularity can be achieved with the help of class as well
    // But files are also considered as a module
    // Modules can be be a file containing class, code , variables and many more.

    // working with modules can be done in different ways : 
        // common js (module.export require())
        // require js
        // AMD : Asynchronous Module Defination 
        // UMD : Universal Module Defination
        // Webpack
        // Babel js 
        // ES style (impot & export)
        

    // To work with ES modules 
    // uses import and export 
    // user <script type="module" src="filenmae.js"></script>
    // To use ES script in node we have to declare file as .mjs
    // export default is ES module 
    
    // Export with ES Module 
    // default export 
    // named export 

    // Defualt export 
    export default function another(){
        console.log("Do something");
    }
    import anything from "./filename.js" // here the default export gets assinghed to any variable after import 

    // named export 

    export function this(){
        console.log("DO this");
    }
    import this from "./filename.js" // there the exporting name shoud be same in both the imopritng and exporting values 


    


    // to work with common js module 
    // module.exports = {modulename}
    // require()
    // Common js is mostly used in Node i.e backend and Es module is used in front end
    // module is an object which is provided by node itself
    // module contains many properties and exports is one of them which is dict
    // we can add different functions, properties in exports.
    // exports is a alias for module.exports which points to moudle.exports 

    exports = function idea(){
        console.log("HEY");
    }
    // here we are assigining new object to a exports alisa which breaks the linkage between module.exports and exports 
    // which results in empty dict i.e module.exports = {}

    //instead 
    exports.name = function(){
        console.log("Print Name");
    }
    //here we add property to a exports or module that exports.

    // OR 
    module.exports = {name};
    // here above is overridden so you will only get name in the imported file 
    // when we require("Filename") it returns the module.exports object which contains all the exported functions and properties and variables 



```
### MAP 
```js
    // It returns new array instead of modfying the original array
    arr.map(element => function(element));

```

### filter
```js
    // at also returns the new array instead of modfying the original array
    arr.filter(element=>function(element))
```

### Automatic syntaxes
```js
    // Distructing assignment {}
    // spread syntax {...objname}
    // Computed property name 
    [e.target.name] = e.target.value
    // spread syntax can be used with both array and objects 
   
    
```


### Functions
```js
    // functions are callable objects in javascript 
    // arrow functions ()=> 
        // types : 1) implicit return i.e without block body ()=> 1+2 (returns 3 implicitly )
        // 2) Explicit return i.e with block body ()=> 2+1 (retuns nothing unless explicity returned)
    // shorthand
    // named
    // unnamed
    arr => arr+1; //here arr is a parameter 

```

### Working with javscript in browser ES6 module
```js
    // type = "text/javascript" // this is by default when you don't specify type while adding in html file
        // this is actually working with ES6 module not with common js module
        // it is executed immediately it is encountered 
        // we can add defer to tell browser to load it letter
        <script type="text/javascript" src="./index.js" defer></script>
        // It doen't supports import and export 
    
    // type = "module"
        // by default is difer i.e exectued after dom is parsed
        // import and exports are available 
        // it is in strict mode by default 
        // browser enforces CORS mode when loaded from cross origin

    // node_modules 
        // node modules only work with node.js environment not with browser environment
        // and every node.js modules uses common.js from import and export 
        // so inorder to work with react or any other library directly in browser we have to use CDN or bundler tool

```

### Bundlers WEBPACK 
```js
    // react uses a webpack as a default bundler 
    // Babel is a javascript compiler & TS transpiler 

    // Bundlers helps to run node modules in browsers 
        // how ? 
            // It combines all the files and creates one single file which is injected into the browser while running the app 
            // It uses webpack dev server to launch the files 
    // can we run node modules without bundlers in browser ? 
        // yes CDNs like esm.sh, skypack.dev, or unpkg can serve Node modules as ES modules that are directly usable in the browser. These services convert Node modules into a format that browsers can understand.

    // Bundler builds the file into static file like css, js, jpg, png etc
    
```


# Holes : 
* Holes in javascript are the empty space in the array that occupy no values neither null, nor undefined.
* eg : const arr = new Array(6);
* Above code will create an Array of 6 digits with holes means nothing exists. it will return and empty value.
* The return of arr[1] will be empty ? 



### Remaining
```js
    : iterators : are used to iterator over values like array 
    : generators : Generators are the functions which can continiously return the value while normal functions return the value for once.
    : modules : Files with independed code.
    : asynchronous : Task that takes extra time to perform some work can be executed in another pipleline and other can execute the code without being blocked.
    : Node
```
