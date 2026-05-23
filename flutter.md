# Flutter 

## Flutter execution 



## Flutter Navigation 
### Method 1 : 
```dart
int currentIndex = 0;
List<Widget> pages =[Home(), Bookings()];

boyd:pages[currentIndex];
bottomNavigationBar : BottomNavigationBar(
items : <BottomNavigationBarItem>[
  BottomNavigationBarItem(icon:Icon(Icons.something), label:"something"),
  BottomNavigationBarItem(icon:Icon(Icons.something1), label:"something1"),
],
onTap : onTapped(int index){setState((){currentIndex = index})};
)

```



## Custom Icons 

```
  * Create svg files for you icons.
  * add them in a folder inside asset as svgicons.
  * Go to [fluttericon](https://www.fluttericon.com/)
  * drag and drop all the icons
  * now click on download
  * zip file will be download
  * place the .ttf file in assets/fonts
  * place .dart file in lib folder
  
  Add following in pubspec.yaml
    fonts:
       - family: MyCustomIcons
         fonts:
           - asset: path_to_custom_font.ttf
  
  
  * Now use it using className.iconsName, in my case its MyCustomIcons.iconsname
```



### Custom Fonts 

```
```



## Adding launcher icons : Launcher icon is used to show the mobile app logo in mobile phones. 
* Add your Flutter Launcher Icons configuration to your pubspec.yaml.

```yaml
dev_dependencies:
  flutter_launcher_icons: "^0.14.4"

flutter_launcher_icons:
  android: "launcher_icon"
  ios: true
  image_path: "assets/icon/icon.png"
  min_sdk_android: 21 # android min sdk min:16, default 21

\\ commands to run after you have added above snippet in yaml file.
\\ flutter pub get
\\ dart run flutter_launcher_icons

```



### Custom Theme 
```
```





### Adding splash screen 
* Splash screen in flutter is created actually before app loads and is not done by flutter.
* It takes place before flutter loads in memory.

* There are two ways to add splash screen :
* Add a package in pubspec.yaml
* brading is used to put the tag or something at the bottom of the screen
  
```pubspec.yaml

  dependencies:
    flutter:
      sdk: flutter
    flutter_native_splash: ^2.4.7


  flutter_native_splash:
  color: "#42a5f5"
  image: assets/images/text_logo.png
  fullscreen: true
  android_12:
    color: "#42a5f5"
    image: assets/images/text_logo.png
    icon_background_color: "#111111"
  branding: assets/images/branding.png

run : Flutter pub get
and : dart run flutter_native_splash:create

* Do it manually :

```
NOTE : 

  * Icon should be 960*960 with background and fit in 640 pixels diameter. 
  * Icon should be 1152*1152 without background and the fit inside 768 pixels diameter
  * size of branding image should be 800*320  



### Animation : 
* Flutter animation
  * Drawing based animation ( Used for heavy animation like drawing or something)
    * Use tools like lottie or Rive and export in flutter.
  * Code based animation
    * Implicit Animation.
      * We won't have to write code to animate. they get animated on their own. we just declare the animation and it's available.
    * Explicit Animation.
      * We have to define everything for animation.
        * When it repeats forever.
        * When it is discontinious.
        * When multiple widgets animate together.
    
      

