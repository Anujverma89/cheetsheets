# Flutter 

## Flutter execution 



## Flutter Navigation 
### Method 1 : 
* Drawbacks :
  * It doesnot preserves the state.
  * Everytime you switch to new screen and switch back you will loose every setting.
  * 
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

# Trees : 
* Widget tree
* Element tree
* Render tree


## Cleanup : Flutter cleanup is needed in dispose : 
* Controller
* Animation controller 
* stream subscription
* timers
* Focus nodes

* Dart objects are automatically managed by garbage collector. 


## Flutter widget lifecycle : 
```dart
  * Widget
  * void initState(){super.initState()}
  * build(){widget building}
  * void dispose(){super.dispose()}

  * Build happens for multiple times,
  * each time we run setState() wiget rebuild's itself. 
```

### Method 2 : PageView 


### Method 3 : IndexedStack


### StatefulShellRoute & Goroute for production grade apps



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
       
```dart
// Implicit animation builtin classes
AnimatedContainer(
  duration:Duration(seconds: 2)
  child: Image.asset("filepath")
  curve : Cruves.Linear,
)

Hero(
  tag:"name"
  child: Image.asset("path_to_image")
)
AnimatedOpacity(
 opacity : isAnimated ? 1 : 0,
 child : Container(
   height : 40,
   width : 100,
 )
AnimatedRotation(
 turns : 0.5
 child : Container (
  child : Text("something") 
 )
// here turns is actually angle 1 means 360 degrees of rotation 
)

)

```

Note : For complex animation which are difficult to express in terms of code use lottie or jitter.video to generate a json format and use it in mobile.


### Using custom theme : 
* 




### Layout : 

* Wrapper layout :
```dart
  row(
    children:[
      item1, item2, item3,
    ]
    mainAxisAlignment : MainAxisAlignment.Center
    crossAxisAlighment : CrossAxisAlignment.end 
  )

  column(
    children:[
      item1,
      item2,
      item3,
    ]
    mainAxisAlighment : MainAxisAlighment.Center
    crossAxisAlignment : CrossAxisAlighment.end
  )

GridView()

ListView()

Stack()

```

* Design Layout :
  
```dart

  container(
  decoration: BoxDecoration(
    gradient : LinearGradient(
      colors:[Colors.red, Colors.green, Colors.blue]
      begin : Alighment.TopLeft,
      end : Alighnment.BottomRight,
      )
    )
  )

  Text(
    "HEy"
    style : TextStyle()
  )

  TextField(
    decoration : InputFieldDecoration()
  )

  
```
Note : In flex in web devleopment justify content is in main axis if row then mainAxis is horizontal, if column mainAxis is vertical.


### Accessibility : 
* Semantics : Meaning of something
* Syntax : Grammatical rules for something.
* Inorder to make flutter accessible to every one we can wrap a object inside a container called semantic
```dart
  Semantics(
    child: Text("This is an accessibility system")
    label : " Read out loud"
    enabled : true,
  )

  MergeSemantics(
    child:Row(
        Text("Text 1"),
        Text("Text 2"),
      )
  )

ExcludeSemantics()

// merge Semantics will read both of them as one
```

### Widgets : 

``` dart
  ConstrainedBox(
    child : Text("This is constrained box"),
    maxWidth : 100,
    minHeight : 40,
  )
  // this can also be achieved using sizedbox.expan()

```

#### Grid View 
* Gridview is used to align arrange the items in 2d layout in a view that is in form of rows and columns.
* Gridview always scrolls vertically by default.
* Main Axis is the axis of scroll direction.
```dart

  GridView.count(
    scrollDirection : Axis.Vertical // by default can be omitted in code
    crossAxisCount : 5; // here this will have five columns
    mainAxisSpacing : 10
    corssAxisSpacing : 10
    children:[
      
    ]
  )

```

#### Overflow box :
* this is used when we wnat child to take it's own space rather than the parents space.
```
OverflowBox(
  child: Image.asset("path_to_image")
)
 
```


#### Flow : 
* Flow is used when we want a custom animation and we want a full control on different aspets of flow.
* Main Purpose of Flow
* Efficient Animated Positioning
* Especially when many children move frequently.

Example:
* expanding menus
* radial menus
* particle effects
* animated galleries
* floating chip layouts
```dart
  Flow(
    delegate : CustomFlowDelegate()
    child:[]
  )
```

### Delegates : 
```

```



### slivers : 
* Slivers  are small independent scrollable areas inside a large scrolable areas which are used to avoid nested scrolls.
```
CustomScrollView(
  : <Widget>(
    sliverList(),
    slivGrid(),
  )
)

```




#### Layout Builder : 
* Layout builder is used to define layout according to the screen size and adopt to the layout.
```


```


#### Custom Paint : 
* Custom paint is used to gain access to low level paint api and do handful of manual art work and paints. 
```dart
```



#### Scrolling : 
* ListView :
  
* GridView :
  
* CarouselView :
  
* CustomScrollView : custom scroll view only works with sliver.
```dart
  CustomScrollView(
    Slivers:<widget>[
      sliverAppBar(),
      sliverList(),
      sliverGrid(),
      sliverFillRemaining(),
      sliverPersistantHeader(),
      sliverToBoxAdapter(),
      sliverPadding(),
      sliverFixedExtentList(),
      sliverChildBuilderDelegate(),
      sliverChildListDelegate()
      SliverToBoxAdapter(
         child: Container(
              color : Colors.red,
           )
      )
    ]
  )

```




#### Styling : 
* Theme
```dart
 theme : ThemeData{
 textTheme : TextTheme();
 colorScheme : const ColorScheme.light()
 }
```
* MediaQuery
* Padding



# Sheets in flutter : 
* Backdrop sheets
* Side sheets ( Libraries : side_sheet, awesome_side_sheet ) 
* Bottom sheets
  * Modal sheets.
  * Standard sheets or persitant sheets.
  * Expanding bottom sheets.
* Navigation drawer 



# RichText : 
* Regular Text() is used when we want to display a string with same style but for string with different styles we have take a RichText()
```dart

body: Container(
 text:RichText(
  text: " This is a bold text"
  textStyle : TextStyle(fontWeight : FontWeight.bold, fontSize: 24);
 )
 children: <TextSpan>[
   TextSpan(),
   TextSpan(),
 ]
)

```
* Note : Texts are not selectable by default and also they lack interaction.
* You can wrap text into `SelectionArea()` for selection. `SlectionArea.Disabled()` to disable the selection.
* You can wrap into `GestureDectector()` and apply `GestureDectector.onTap()` to apply certain events. You can also apply InkWell to add event to certain event.



# Custom launcher : done 
# Custom Icons : Done 
# Page Navigation : Done 
# Custom Theme : Waiting



# Ways to design OS adaptive application : 
* Use adaptive where ever possible.
```dart
 Icons.adaptive.share
 switch.adaptive()
 Slider.adaptive()
CircularProgressIndicator.adaptive()
Checkbox.adaptive()
cons.adaptive.arrow_back
```

* Manual check while scaffolding :
```dart
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final platform = Theme.of(context).platform;

    if (platform == TargetPlatform.iOS) {
      return const CupertinoPageScaffold(
        navigationBar: CupertinoNavigationBar(
          middle: Text('Dashboard'), // Centers automatically on iOS
        ),
        child: SafeArea(child: HomeBody()),
      );
    }

    return Scaffold(
      appBar: AppBar(
        title: const Text('Dashboard'), // Left-aligns automatically on Android
      ),
      body: const HomeBody(),
    );
  }
```

* Native popup and Dialogs 
```dart
 void showNativeAlert(BuildContext context) {
   showAdaptiveDialog(
     context: context,
     builder: (context) {
       return AlertDialog.adaptive(
         title: const Text('System Alert'),
         content: const Text('Do you want to save these changes?'),
         actions: [
           TextButton(
             onPressed: () => Navigator.pop(context),
             child: const Text('Cancel'),
           ),
           TextButton(
             onPressed: () => Navigator.pop(context),
             child: const Text('Save'),
           ),
         ],
       );
     },
   );
 }
```


#### Adaptive Containers : 
```dart
 switch.adaptive()
 slider.adaptive()
 checklist.adaptive()
 radio.adaptive()
 switchListTile.adaptive()

 circularProgressIndicator.adaptive()
 refreshIndicator.adaptive()
 showDialog.adaptive()

 Icons.adaptive.share()
 Icons.adaptive.arrow_back()
 Icons.adaptive.arrow_forward()
 Icons.adaptive.flip_camera()

```



# Storage system in mobile : 
* Backend API
* File based Database (Sqlite)
* Secure storage ( for auth related data ) 
* Shared preference  



# Designing for both IOS and Android : 
* Use MaterialApp() : Becuase it can render both CupertinoWidgets and Material Widgets
* Use Adaptive containers whenever for widgets those have adaptive UI.
* Check platform and provide the Native widgets if adaptive is not available.
* Provide the cupertinoTheme setting in Theme.
* Use the SafeArea while rendering the UI



# Colors : 
* In general design principle :
  * Primary : Means most used color use for atleat of 60%. 
  * Secondary : Less used for atleast 30%
  * Tertiary : Color used for 10%
* In Material design system :
  * Primary : Brand color
  * Secondary : action color
  * tertiary color : action color
  * Surface color : background
  * On Surface container : 



# use of colors: 
* Primary : used for main action in the page
* Secondary : Interactive but not the main action of the page
* Tertiary : Used to contrast the Primary :
  * When you have two actions to take but you want to influnece the user of what decision to take like ( primary for high priority , teritary for low priority)



# Comprehensive widget list 
* Row
* Column
* Stack
* Wrap
* Flex
* Expanded
* Flexible
* Spacer
* Container
* SizedBox
* Padding
* Align
* Center
* AspectRatio
* ConstrainedBox
* FractionallySizedBox
* Positioned
* SafeArea
* Scaffold

# Scrolling 
```
ListView
GridView
SingleChildScrollView
CustomScrollView
NestedScrollView
PageView
Scrollbar
RefreshIndicator : used to show a refreshing indicator above while scrolling
```

# Text 
```
Text
SelectableText
RichText
DefaultTextStyle
EditableText
```


# Selection 
```
Chip
ChoiceChip
FilterChip
ActionChip
InputChip
SegmentedButton
ToggleButtons
```
# Expansion Widgets 
```
ExpansionTile
ExpansionPanel
ExpansionPanelList
ExpansionPanelList.radio
```
# Menus & Dropdowns
DropdownMenu
DropdownButton
PopupMenuButton
MenuAnchor
MenuBar
SubmenuButton
# Navigation
BottomNavigationBar
NavigationBar
NavigationRail
NavigationDrawer
Drawer
TabBar
TabBarView
BottomSheet
showModalBottomSheet()
showDialog()
showMenu()
# Cards & Surfaces
Card
ListTile
Divider
VerticalDivider
Material
Ink
InkWell
InkResponse
# Images
Image
FadeInImage
CircleAvatar
Icon
# Progress Indicators
CircularProgressIndicator
LinearProgressIndicator
RefreshProgressIndicator
# Feedback Widgets
SnackBar
Banner
MaterialBanner
Tooltip
AlertDialog
SimpleDialog
AboutDialog
# Date & Time Pickers
showDatePicker()
showDateRangePicker()
showTimePicker()
CalendarDatePicker
# Animation Widgets
AnimatedContainer
AnimatedOpacity
AnimatedAlign
AnimatedPadding
AnimatedPositioned
AnimatedSwitcher
AnimatedCrossFade
Hero
TweenAnimationBuilder
AnimatedBuilder
# Gesture Widgets
GestureDetector
InkWell
InkResponse
Dismissible
Draggable
DragTarget
InteractiveViewer
# Lists
ListTile
ReorderableListView
Dismissible
ExpansionTile
CheckboxListTile
RadioListTile
SwitchListTile
# Adaptive (iOS)

Flutter also provides Cupertino widgets:

CupertinoButton
CupertinoSwitch
CupertinoAlertDialog
CupertinoNavigationBar
CupertinoTabScaffold
CupertinoPicker
CupertinoDatePicker
# Useful Material Components
AppBar
BottomAppBar
NavigationBar
NavigationRail
NavigationDrawer
Drawer
BottomSheet
PersistentBottomSheet
FloatingActionButton
ScaffoldMessenger
# Common Dialogs
showDialog()

showGeneralDialog()

showModalBottomSheet()

showBottomSheet()

showMenu()
# Miscellaneous Widgets
Hero
FutureBuilder
StreamBuilder
Builder
LayoutBuilder
OrientationBuilder
Visibility
Offstage
Opacity
Placeholder
