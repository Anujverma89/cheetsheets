# HTMl 

* 1) Raw HTML
|-- DOM (Document Object Model)

* 1) Raw CSS
|-- CSSOM

* 2) DOM + CSSOM = ( Render Tree ) 

* 3) Layout ( Reflow )
  * Which element goes where.
  * Height, widht, x, y

* 4) paint the UI
  * Paint engine + Rasterizer
 
* 5) Show the UI ( GPU + Compositor)
 

* You can think of the browser like this:

Browser Engine
coordinates everything

Rendering Engine
HTML Parser → DOM

CSS Parser → CSSOM
Layout + Paint

JavaScript Engine
executes JS (like V8)

UI Backend
draws basic widgets (buttons, scrollbars)

Networking
fetches HTML, CSS, JS from internet

GPU / Compositor
final rendering

# React & Rendering : 
 * 1) Development in react.
   2) Build application
   3) Generates necessary components like menifest.json. js bundle, css and html file
   4) js bundle : React Library + Main Js file
   5) Rendering happens in browser. 




