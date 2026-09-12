# Next.js BY Vercel

### Few Notes 
* Next.js only works with react 
* It is the Framework built on top of react
* It is a React framework to built a full stack web application
* It has built-in router feature 
* It provides server side rendering
* Static Site Generation (SSG)
* Server Side Rendering(SSR)

### using pnpm inplace of npm
* install : npm install -g pnpm

### creating next-app
* npx create-react-app@latest

### running next-app 
* npm run dev


### Types of routers 
* App Router & Page Router


### SSR 
```js
    //SSR : Server Side rendering (HTML is generated in the server and then sent to the browser)
    //Client side rendering : Minimal html is downloaded along with js then javascript created HTML browser.
    // SSG : Static site generation 
        // Contnet is pre rendered at a build time.
        // While SSR contenet is generated at each request and response.

```

### Package.json & package-lock.json
```js
    // package.json contains the range of version that can be instlled.
    // package-lock.json specifies the exact version to run or depend on. 
    // when we re-install dependencies using npm it reinstalls the exact version.
    // npm uses package-lock.json initally but if it doesn't exits it will use package.json
```


### App router
```js
    // 
```
### Page router