# React : Is a Javascript library for rendering UI
### UI : cobination of elements like button, images and texts .

# concepts
* Components
* JSX : Javascript XML 
* State management
* Props
* Rendering elements
* Event handling
* Conditional rendering
* Lists and keys
* Forms and form validation
* Hooks (Updates the UI)
* LifeCycle 
* High order components 

### Additional Libraries 
* PStyling
* Redux ( Can be used with any librarys like Vue or react)
* Redux toolkit
* Zustand 
* Context api
* React Routers 
* React Fibres 
* Axios 
* Gatsby 
* Next.js
* Mobx
* Recoil 
* React Helmet 
* React Hook Form
* Formik
* Emotion 
* React query
* Yub
* Babel 
* Webpack 
* Vite
* JEst 
* React spring
* appwrite (BASS APPS Backed as a service)
* Express 
* NOde
* Fibre
* Virtual DOM 
* Diff algorithm 
* Hydration 


### Why react 
* When we have a complex frontend to work with we have to use react.
* Else if we need a protfolio website we can use our plain html, javascript and css
* React was introduced to keep UI consitent with update that is solve ghost problem or phantom problem 


#### Best practises :
* Using linter tools like ESlint
* Proper folder structure
* Implement Lazy loading
* Employ reusable hooks
* Logging and monitoring 
* Combining css and JS using tailwind css or emotion
* Using JSX(javascript XML)(HTML, CSS & JS in single file)

***


# JSX(Javascript XML)
* HTML, CSS & JS all in one file. 
* First JSX is converted into Javascript using a Transpiler.
* Transpiler for JSX is babel
* JSX was introduced since later on maximum of content was generated using html so why not to used html and javscript in same file so jsx was introduced.
* We can use JSX with or without React is is independent of react


### Rules for JSX
* aria-* and data-* is written as it was in html 


* Always Return a Single Root Element
```js
return (
  <div>
    <h1>Hello World!</h1>
    <p>This is my first React component.</p>
  </div>
)

//wrong
return (
  <h1>Hello World!</h1>
  <p>This is my first React component.</p>
)
```
* Use className Instead Of class
```html
// Good
<div className="my-class">This element has a CSS class.</div>

// Bad
<div class="my-class">This element has a CSS class.</div>
```

* Use Curly Braces for JavaScript Expressions
```html
    <div>{myVariable}</div>

    <!-- // Bad -->
    <div>myVariable</div>
    <!-- //example -->
    <p>The total cost is {25*10}</p>
```

* Use camelCase for Most Things In JSX
```html
// Good
<button onClick={handleClick} className="btn">Click me!</button>

// Bad
<button onclick={handle_click} class="btn">Click me!</button

```

* Always Close Tags

```html
// Good
<div></div>

// Bad
<div/>
```

* Use Self-Closing Tags for Empty Elements
```html
// Good
<img src="my-image.jpg" alt="My Image"/>

// Bad
<img src="my-image.jpg" alt="My Image"></img>

```

#### Transpiler is a software which convertes one source code into another source code(emits high level language)


>React Componets are typical javascript functions that but they must start with capital letter.  
>They only export one component 

```js

function profile(){

}

export default home(){
  
}

export profile 

import {profile} from '.loaded.js'

```

>JSX(Javascript XML) RULES  
>ALL tags must close   
>Shoud only return single element   
> It's javascript XML because it is strict than html and XML is strict than html   
>Always have to use camel case 


#### Use of curly braces 
To pass text  
To pass attributes  
Basically to pass strings and numbers  we use single curly braces {} 

`Double curlies are used to pass objects`
```js
#They can be used immediatley after equal to
{{
  background-color :red,
  height : 400,
}}

```



#### Passing Properties(props to components)
They are a way to communicate between parents   
They can be passed from parent to child  
Props are passed as an argument to a function.  
Componets only accept props as an argument
We have to use distructuring structure syntax while reading props
We can also forward props 
When we nest component inside a component it receives that component as children.  
Props are immutable.  
You can pass default value to prop and that value is taken when no argument is pass or it's undefined


#### Conditional rendering 
&&  
||  
? : operator   
When its zero on the left of && it simply makes all the condition zero and react renders it as zero..


> There are two types of export in Javascript  
>i) Named Module export  
>ii) Default Export  

```
React is rendered using render Tree which holds component dependency.
```


## State Management 
```
States are component-specific memeory in react 
we can use useState hook in react to work with state in react.

```


### Media Queries :
> Large screen : Design for desktops from 1280×720 to 1920×1080  
> Mid screen : Design for tablets from 601×962 to 1280×800  
> Small screen : Design for mobiles from 360×640 to 414×896 max 480 px


>Link   
```js

css properties 
https://www.w3schools.com/cssref/playdemo.php?filename=playcss_font-variant

icons and css resources
https://www.science.co.il/internet/html/CSS.php
```

### React Versioning 
```js
    // Major.minor.patch
    // when major realease is done it breaks the backword compativility 
    // minor is added when new feature is added that is backword compatible
    // patch is used to fix the bug that exits in the system

```

# Components 
```js
  // component is a javascript function that we can sprinkle with markup
  // Components name must start with Capital Letter (Becase React componets are also used in angular braces so to descrimite between html and react component)
  // IN JSX every opening component has closing bracket

  function normal(){
      console.log("THis is wrong");
  }

  function Newcomponnet(){
      const idea = "new Idea";
      return(
          <>
            {idea}
            {normal()}
            {{backgroundColor:'red', color:'blue'}}
            <h1 className={idea}>HEY</h1>
          </>
      )
  }
// double curlies means {{object}}
// inline properites like 
// calling function in jsx 
// box-shadow = boxShadow
```


# PROPS 
```js
    // props are the infromation that you pass to the JSX tag
    // we can pass props to component using traditional method of function parameter  or by distrucutring each items 
    // Props are not static their value may change at any time
    // Props reflect a component’s data at any point in time, rather than only in the beginning.
    // The props are immutable i.e when the value of prop is updated the older prop is rolled out and new one is created and olders memory is clamied by javascript engine
    //Nested JSX like <Card><Avatar /></Card> will appear as Card component’s children prop.
    //Props are read-only snapshots in time: every render receives a new version of props.
    //You can’t change props. When you need interactivity, you’ll need to set state.

    function COmponet({prop1, prop2}){

    }

    // also correct
    function Componet(prop){
      {prop.prop1}
      {prop.prop2}
    }

    // passing default values 
    function component({prop1, prop2 = "something"}) // this is default value

    // using spread syntac we can pass all the values to clidren from parent 

    function Parent(prop){
        <component {...prop}/>  // this is spread syntax to pass prop
    }  
   
    // we can also pass the jsx into the componet that will be by defualt received in a children 

    function Parent({children}){

      return(
        <>
          <h1>{children}</h1>
        </>
      )
    }

    function Child(){

      return(
        <>
          "HYRBRID"
        </>
      )
    }

    function Main(){
        return(
          <>
            <Parent> <Child /> </Parent>
          </>
        )
    }


```


# Conditional Rendering 
```js
    // we can return different components on the basis of different logics 
    // In React, you control branching logic with JavaScript.
    // You can return a JSX expression conditionally with an if statement.
    // You can conditionally save some JSX to a variable and then include it inside other JSX by using the curly braces.
    // In JSX, {cond ? <A /> : <B />} means “if cond, render <A />, otherwise <B />”.
    // In JSX, {cond && <A />} means “if cond, render <A />, otherwise nothing”.
    // The shortcuts are common, but you don’t have to use them if you prefer plain if.
      function Dosome({item, value}){
        if(value == 0){
          return(
            <>
              <h1>HEY bro</h1>
            </>
          )
        }
        else{
          return(
            <h1>
              FUck oFF
            </h1>
          )
        }
    }

    export default function DoSomething(){
        return(
            <Dosome 
              item = "IDea"
              value = {0} // passing number to a prop value
              ></Dosome>
        )
    }

    // when we don't want to render anything we can return null instead of JSX

    // we can also render conditionally inside a jsx itself using ternay operator 
    //But JSX elements aren’t “instances” because they don’t hold any internal state and aren’t real DOM nodes. They’re lightweight descriptions, like blueprints. 

```

# List rendering 
```js

    // we can use map or fileter to work with array of data
    arr=[12,4,24];
    arr.map(arr=>
      <li key ={arr}> {arr} </li>
    )
    // here key is important part 
    // key tells react which item of an arry the componenet corresponds to 
    // it is important when the arrays elements are moved around react will still have the information about the data 
    //File names in a folder and JSX keys in an array serve a similar purpose. They let us uniquely identify an item between its siblings. A well-chosen key provides more information than the position within the array. Even if the position changes due to reordering, the key lets React identify the item throughout its lifetime.
    // Fragemnt is used <Fragment></ Fragment>
    // Key is not a prop in component but it is only used be react for refernce 
```

# Fragment 
```js
  // Fragmnets are used to group the data items together without adding any extra node or div in the DOM.
  <></> // this is shorthand fragment syntax, here we cannot pass any key
  <Fragment></Fragment> // this is a long and clear fragment syntax this is used to pass key while list rendering

```

# Routing In react 
```js
    // here rounting mainly requires : 
      /*
        1) Link to : to add href 
        2) Routes : Region where different routers are rendered 
        3) Router : 
        4) Route : path to add componet 
        5) Borwser Router : 
      */
```

### PURE Functions
```js
    // pure functions only do somecomputation nothing else
    //pure functions always minds it's own business : doesnot changes the content of the programme
    //one output for one input:
    // React is made on the concept of pure function 
      // i.e same output for same input
    // Components should only return their JSX, 
    //and not change any objects or variables that existed before rendering—that would make them impure!
    //React offers a “Strict Mode” in which it calls each component’s function twice during development. By calling the component functions twice, Strict Mode helps find components that break these rules.
    // when function modifies the variable it is called mutation 
    // pure function doesn't mutate

    // In react we can only read three things , but they shouldn't be modified
      // state, 
      // prop
      // context
    // inorder to modify the state we must use setState() and not update the variable directly

    // local mutation is allowed that is we can change the local variables inside a component

    // Sideeffects : change in UI or variable after the rendering is done due to some functional calls is sideeffects.
      // sideeffects always take place after the rendering 
    // sideeffects in react mostly happens inside event handlers whenever any actions is performed it is handled by event handler

    // WHY Purity : 
      // Since every componet is pure it can render to multiple request at a time
      // Everytime the ui doesnot needs to be changed 
      //If some data changes in the middle of rendering a deep component tree, React can restart rendering without wasting time to finish the outdated render. Purity makes it safe to stop calculating at any time.

    

    // React elements are rendered as a tree like browsers and other mobile apps
    // The the root node is the root of the tree 

```

# React parsers 
```js
  //react-dom : to work with browsers  & talk with DOM
  //react-native : to work with mobile apps
  // Behind the scene there is a react dom which is a virtual dom which talks with actual dom and works 
```

# Adding interactivity 
```js
```
# States 
```js
    // The data that changes over time is called state
    // Events are some actions 
    // Event handlers are some function those handles some events
    // Functions must be passed to event handlers and not be called okay
      <Button btname="ALert" functionn={callme}/> // correct
        <Button btname="ALert" functionn={callme()}/> // incorrect
        e.stopPropagation()
        e.preventDefault()
```

# Creating React 
```js
    // using CRA : npx create-react-app
      // npx = node package executable 
      // npm = node package manager
    // using vite or other bundlers 

    // adding react to existing project 
      //using node modules 
      // or CDN 

```

# Hooks 
```js

  // Hooks : Hooks are special functions that are only available while React is rendering (which we’ll get into in more detail on the next page). They let you “hook into” different React features.

    // everything that start with use is called hook in react
    // usestate
      // maintains the state in different renders
      // tells react to render the component and the value changes
      // use state returns the array with two values 
      const [index, setindex] = useState(0);
      // it is a way for component to remember the state 
      // useState takes initial value of state

    NOTE :
      Hooks cannot be called  inside loops or conditions. they can only be called in the top level of the component.
```


### Hydratation Rendring
```js
    // In react rendring occurs in two phases 
      // initial phase while page loads
      // Second phase when state changes
    // trigger a render
      // initial render : while page loads : render root component
      // second or re-render : when state changes
    // render : 
      // Initial render : nodes like h1,div etc are created 
      // re render : only changed portion is re-rendered
    // commit : 
      // initial commit : react uses appendChild()
      // re-render commit : it only updates the changed values
    

    //“Rendering” means that React is calling your component, which is a function. 
    // State doesnot gets updated until it is rendered 

    // Snapshot is basically the state of component at a given time. It is fixed and never changed for the given state.
    // The state value gets changed in other state and there different snapshot is taken
    // React keeps the state values “fixed” within one render’s event handlers.
    // Like recurssion the function component's use their own state when they are called that is every function call has own stack record which can be used inside that same function call.

    //batching : Process when UI is only rendered after event handler completes executing

    // Mutation is when we change something. Example changing the object's property
    // Mutation is possible but we shouln't try to mutate
    // eg. 1 is immutable that is 1 cannot be chaged to 2. 2 is different instance and 1 is different instance 
    // Objects are mutable in react
    // Local mutation is allowed while the global mutation may lead to some issue.
    // 

```

### Updating state of an object 
```js
  //State can hold any kind of JavaScript value, including objects. But you shouldn’t change objects that you hold in the React state directly. Instead, when you want to update an object, you need to create a new one (or make a copy of an existing one), and then set the state to use that copy.
  // You can use immer to udpate the nested objects that solves the problem of repetetive code 
  //  We can use immer with both the array and object for better code 
```

# Diffing algorithm , Fibre , Reconciliation 
```js
  // Diffing : comparing the actual and Virtual DOM 
  // Reconciliation : It is an algorithm that react uses to differentiate between two tress and decide which parts need to be updated
  // new tree is generated i.e rendering starts when there is a state change which is compared with previous tree 
  // react can be rendered on DOM , IOS native , Android views. 
  // reconciler computes what changes are to be made 
  // renderer renders the component
  //This separation means that React DOM and React Native can use their own renderers while sharing the same reconciler, provided by React core.
  // fibre is a rewrite of an algorithm called reconcilier.
```


### Mangaing state 
```js
  // we declerative rather than imperative 
  // only use required states
  // Now that the state is “flat” (also known as “normalized”), updating nested items becomes easier. 
  // in flat states there are no nested states
  // Lifting up is used when we want to change the states of two componenets at smae time
  // here we put the state in closest parent and pass it as a prop to the childs
  // When the component is moved to new place or removed the state also disappers 
  //React preserves a component’s state for as long as it’s being rendered at its position in the UI tree. If it gets removed, or a different component gets rendered at the same position, React discards its state.
  //Same component at the same position preserves state
  // if two component have the same position in the tree they will preserver the state this is becuase they have a call stack which are different so this occurs 
  //As a rule of thumb, if you want to preserve the state between re-renders, the structure of your tree needs to “match up”
  // react destroys the state when it deletes component from tree
  //This is why you should not nest component function definitions. they are different for different renders
  //State is tied to a position in the render tree 
  //Resetting state at the same position 
    // Use Key attribute in div
    // Render at different position
    // when we talk about postion we explicity talk about the position inside the div
  
  // we can preserve the state of a lost node by 
    // uplifting the state up 
    // by saving it locally in localstorage
    // by hiding it using css 

```


### Reducers (Must be pure function)
```js
  // Reducers are the functions outside the component that are used to handle update logic of states 
  // Reducers are the functions which are only used to manage the states
  // it takes a action into dispatch and updates the state
  // reducers take task and action to return the state which becomes the current state of the componet
  
  function reducer(state, action){
    // we have to use switch statement inside the reudcers 
  }

  // reducers are named after the reduce operation that are present in node array
  // we can use useReducer() instead of useState() in react 
  // we can also write reducers with immer 

  // reducers return state and disptach, take reducer function and initial state
  // reducer function performs some logic and changes the state on the basis of the type fo the reducer
  // we can update multiple states just by using one reducer using type in disptacher
  // disptach triggers reducer function and passes action type to the action and task is returned 
  // state and action is passed for the reducer itself using initialstate 
  // to change multiple states using reducer we have to use object and then we can update the reducer using array distrucuting and creating new array
  // we can use immer to implimnet reducers
  

  // use reducer is easy to impliment

```

### Context 
```js
  // contexts are the ways of passing data from parent to child or any other component below parent in a tree without passing them as a prop 
  // prop drilling is basically passing prop from parent to deeply neested child component through different other intermediaries node though they don't need the same 
  // prop drilling can be avoided using 
    // context api
    // state management libraries like : redux, zustand, mobx

  // context is an alternatinve to passing prop

  // useContext is also a hook;

  export default context= createContext(1);
  import context from "./context";

  let level = useContext(context);
  
  <context.provider value = {value}>
    <ChildComponent/>
  </context.provider>
  // we can wrap any no of component inside a provider wraper and they will be able to access the data using getContext()

  function ChildComponent(){
    cont value = getContext(context);
    return(
      <>  
        <h1>{value}</h1>
      </>
    )
  }
  
  if (!ref.current) ref.current = new Thing()
  // usecases : 
    1) Used in routing mechanism
    2) Theming
    3) Managing state
    4) current Account
```
### useRef hook
```js
    // useRef is a hook
    // refs are used to escape the rerendering of the react node 
    // refs are used when we want component to remember something but we don't want it to re-render the component
    // useref is plain javscript object whereas the states are speical functions in react 
    import {useRef} from 'react'
    function MyrefComponent(){
      const ref = useRef(0);
      // note ref returns the object 
      //{ current : 0 } 
      return(
        <>
          <div>
            {ref}
          </div>
        </>
      )
    }

    if (!ref.current) ref.current = new Thing() // this is where it renders the first 
    // chaning the ref value doesnot changes the state whatever the case 
    
    // most common use caseas of ref 
    // for DOM manuplation 
    // Don't read and write ref values during rendering
    // we can pass the node to the ref.current using the ref={rename} inside the component

```
### useEffect
```js
    // useEffect hook is used to perform the sideaffect logic
    // i.e it should only run after the commit of redering component
    // if we want to establish a connection , fetch data using API and any other things we have to do it after everything is rendered
    // Event handlers contains side effect like clicking button to add user using http
    // like in chatapplication connection to the server must be done while displaying the UI.
    // So useEffect is bascially used to handle the sideffects that are caused by rendering itself rather than any event

    // LIke displaying data in the screen Using API 
    // effect is caused by Affect (Affect is a verb and Effect is a noun);
    // Effect is caused by rendering and event is caused by event 
    // Effect runs at the end of the commit after screen updates.

    // we can sync external apis, http responses etc using useEffect
    // useEffect runs after every render of component that is any statechange triggers it to run 
    // we can add dependecny in useEffect() such that is only runs when that state is changed while rerendering
    // vist this for more https://react.dev/reference/react
    // we can add mnay dependenincs in array 
    // and even if one of them changes it will re-run okay 
    // we should write cleanup code while unmounting
    // react intentionally remounts components twice \
    // if you do something in useEffect u should undo it.
    // it helps to avoid bugs

    // while we make the use of useEffect we should always undo the changes that we have done.
    //React always cleans up the previous render’s Effect before the next render’s Effect.
    //If your Effect breaks because of remounting, you need to implement a cleanup function.
    //Components are mounted twice in development

    // react uses : 
      Object.is(obj1, obj2) // to compare the result; 
    

    // Life Cycle 
      // Start Synchoronizing 
      // Stop Synchoronizing : cleaning function()

```

### useMemo

```js
```

### Rendering , comminting and triggering
```js
    // Rendering is bascially planning of how things will be commited
    // Making a render tree or vritual dom is done while rendering
    // things done while rendering 
      // calling the render method -> react calls the functional component to return the JSX , calling the render method of functional dom
      // Reconciling creation and comparion of vitual dom 
      // calculating the diff
      // Preparing the sideeffects 
      // suspence handeling : lazy loading or async data 
      // Generating the render output : generating react element from JSX 
      // Scheduling updates : using fibre reconcilliation 
      // while our component is rendering we should not perform any side effects or operate with DOM.
      // if we write such code it will produce an error
      // but we can add setTimeOut() which will become async and it will run 
      // saying that we can run those code which defer it's execution
      // We warp sideeffects into a code that useEffect if we feel that it will run at render 
  
    // Commiting is basically painting the UI 
      // i.e. after the rendering process is done we perform commit
```

### There occurs a race condition in react as well
```js
  // We can avoid race condition my writing cleanup code inside the useEffect() function
```


### Clinet side routing techniques 
```js
  // React Query, useSWR, and React Router 6.4+
```

### Intersection Observer API 
```js
  // Lazy Loading
  // Infinite Scrolling
```

### Mounting and Unmounting
```js
  // mouting : inserting the html content of the component into the DOM 
  // unmounting : removing the html content of the component from the DOM 
```

### Component Life cycle 
```js
    1) Mount
    2) Update 
    3) Unmount
```

### DOM MANUPLATION IN REACT 
```
React first works on on Vrtual DOM 
Virtual DOM --> REAL DOM
Change is first made to virtual dom.
A snap of virtual dom is taken before making changes.
A virtual dom is updated
It is compared with snap shot
A node that is modified is only updated in Real DOM 
It improves performace
Meet your first Hook 