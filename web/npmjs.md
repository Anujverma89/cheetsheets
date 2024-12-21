# NPM : Node package manager 

### npm is a package manager that is used to work with different packages & libraries availalbe for use.
### It is a opensource and comes bundled with nodejs.
### It is fully customisable and we can also customise its regsitry from where it fetches the packages.
### We can configure it's registory

### Commands 
* npm -ls (see all the installed libraries)
* npm install (to install pakcages)
* npm search pakcagename (to search things on npm registry)


### npm uses to mode local and global 
* local is in project's current directory ./node_modules
* if you want to use global use -g flag
  * example npm install -g packagename
* global modules are available at **npm_config_prefix/lib/node_modules** & **$npm_config_prefix/bin**


### working 
* npm installs all the packages listen in package.json
* if the package.json contains the git url it will download from the git repository using **git command** and will generate an error if it is not installed.
* If we want to install the native node package like bcrypt which is written in cpp it will node-gyp for compilation to work with nodejs if it fails it will use the javascript version of bcrypt.
* node-gyp is a cross platfrom command line tool that is used to compile native add-on for node.js.
* native add-on is a piece of code that is written in cpp and can be compiled to work with node.js.

### To install dev dependeincies : 
* npm install --only=dev
* this is used when we want to install packages that are only needed while we are in development

### To install prod dependencies : 
* npm install --only=prod


## For more commands visist 
[Link to npm commands](https://docs.npmjs.com/cli/v11/commands/npm-start)
