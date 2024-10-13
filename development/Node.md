# Node - Open Source and Cross-Platform javascript run-time envrionment

### Bit-intro : 
* Uses V8 engine of google chrome
* It is a single process application
* It uses asynchronous operations for efficient performance 
* It can adopt ECMAScript standards without hurdle
* It can use both MJS(Module Javascript) and CJS(Common JS) 

### CJS (Common JS)
```js
    // File name : filename.js, filename.cjs
    // used only on server-side
    // not in strcit mode by default
    // load synchronously doesnot support asynchronous support
```

### Module.js (Module js) MJS or ES
```js
    // File-name : mjs if you want to work in server-side other than browser
    // in strict mode by default
    // syntax : import , export
    // can load asynchronously 
    // use introduced for browser initally
```

### Working with http
```js


```

### V8 Engine 
```js
    // V8 is a javascript engine that pareses and executes javascript 
    // API's are provided by broweser like DOM and other apis
    // they both make a run time envrionment
    // V8 engine is endepended of the browser it runs
        // Other engines : 
            // firefox -- SpiderMonkey
            // Safari -- Nitro
            // Edge -- Chakra previously previously
            // Edge -- CHromium and V8 
            // they all uses ECMA ES-262 standard which is also ECMAScript the standard used by javascript.
    // V8 is written in cpp
    // Javscript is not just interpreted in modern times they are compiled as well. it started in 2009 first in spider monkey
    // JS is internally compiled with Just-in-time(JIT) compilation to speed up the exection.
    // Every language like python and js are compiled as well interpreted

```
[https://v8.dev/]

### NPM 
```js
    // NPM is the registry of millions of packages (2.1 million+)
    // NPM : Node package manager
    // Alternatives : pnpm & yarn
    // pnpm : performant Node package manager

    // pnmp is faster then npm
    // pnpm supports every version of node whereas npm supports specific version of node
    
```


### NODE_ENV
```js
    // process is a object with in node 
    // which has nested object called env
    // there is nothing like NODE_ENV by default in node
    // it is a convention to add NODE_ENV in node for testing purpose
    // we can set in file or while running the command

    // Envrionment is the environment where the process runs
    // there are four types : production , development, staging, testing

    // while this is debatable topic it is both useful and has drawbacks as well.
```