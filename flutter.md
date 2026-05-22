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
* Go to (Image)[https://www.fluttericon.com/]
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
