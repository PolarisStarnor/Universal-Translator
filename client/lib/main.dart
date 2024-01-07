import 'package:flutter/material.dart';
import 'package:ffmpeg_kit_flutter/ffmpeg_kit.dart';
import 'package:universal_translator/send.dart';
import 'package:path_provider/path_provider.dart';

import 'recorder.dart';
import 'languages.dart';
import 'player.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Universal Translator',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // TRY THIS: Try running your application with "flutter run". You'll see
        // the application has a purple toolbar. Then, without quitting the app,
        // try changing the seedColor in the colorScheme below to Colors.green
        // and then invoke "hot reload" (save your changes or press the "hot
        // reload" button in a Flutter-supported IDE, or press "r" if you used
        // the command line to start the app).
        //
        // Notice that the counter didn't reset back to zero; the application
        // state is not lost during the reload. To reset the state, use hot
        // restart instead.
        //
        // This works for code too, not just values: Most code changes can be
        // tested with just a hot reload.
        colorScheme: ColorScheme.fromSeed(seedColor: Colors.greenAccent),
        useMaterial3: true,
      ),
      home: const MyHomePage(title: 'Universal Translator'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  bool recording = false;
  var recorder = Recorder();
  Languages? inputLang = Languages.english;
  Languages? outputLang = Languages.english;

  Future<void> toggleRecording() async {
    setState(() {
      // This call to setState tells the Flutter framework that something has
      // changed in this State, which causes it to rerun the build method below
      // so that the display can reflect the updated values. If we changed
      // _counter without calling setState(), then the build method would not be
      // called again, and so nothing would appear to happen.
      recording = !recording;
    });

    if (recording) {
      //Start recording stuff
      recorder.start();
    } else {
      var path = await recorder.end();
      // final mp3 = await wavToMp3(path);
      String translation = await send("$path");
      textToSpeech(translation, outputLang!.val);
    }
  }

  Future<String> wavToMp3 (String? path) async {

    final directory = await getApplicationCacheDirectory();
    final dir_path = directory.path;

    String cmd = "-i $path -vn -ar 16000 -ac 2 -b:a 32k $dir_path/input.mp3";
    FFmpegKit.execute(cmd);
    print(cmd);

    return "$dir_path/input.mp3";

  }

  @override
  Widget build(BuildContext context) {
    // This method is rerun every time setState is called, for instance as done
    // by the _incrementCounter method above.
    //
    // The Flutter framework has been optimized to make rerunning build methods
    // fast, so that you can just rebuild anything that needs updating rather
    // than having to individually change instances of widgets.
    final TextEditingController inputLanguageController = TextEditingController();
    final TextEditingController outputLanguageController = TextEditingController();
    Icon recordIcon = const Icon(Icons.fiber_manual_record_outlined);

    return Scaffold(
      appBar: AppBar(
        // TRY THIS: Try changing the color here to a specific color (to
        // Colors.amber, perhaps?) and trigger a hot reload to see the AppBar
        // change color while the other colors stay the same.
        backgroundColor: Theme.of(context).colorScheme.inversePrimary,
        // Here we take the value from the MyHomePage object that was created by
        // the App.build method, and use it to set our appbar title.
        title: Text(widget.title),
      ),
      body: Center(
        // Center is a layout widget. It takes a single child and positions it
        // in the middle of the parent.
        child: Column(
          // Column is also a layout widget. It takes a list of children and
          // arranges them vertically. By default, it sizes itself to fit its
          // children horizontally, and tries to be as tall as its parent.
          //
          // Column has various properties to control how it sizes itself and
          // how it positions its children. Here we use mainAxisAlignment to
          // center the children vertically; the main axis here is the vertical
          // axis because Columns are vertical (the cross axis would be
          // horizontal).
          //
          // TRY THIS: Invoke "debug painting" (choose the "Toggle Debug Paint"
          // action in the IDE, or press "p" in the console), to see the
          // wireframe for each widget.
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            DropdownMenu<Languages>(
              initialSelection: Languages.english,
              controller: inputLanguageController,
              // requestFocusOnTap is enabled/disabled by platforms when it is null.
              // On mobile platforms, this is false by default. Setting this to true will
              // trigger focus request on the text field and virtual keyboard will appear
              // afterward. On desktop platforms however, this defaults to true.
              requestFocusOnTap: true,
              label: const Text('Input Language'),
              onSelected: (Languages? lang) {
                setState(() {
                  inputLang = lang;
                });
              },
              dropdownMenuEntries: Languages.values
                  .map<DropdownMenuEntry<Languages>>(
                      (Languages lang) {
                    return DropdownMenuEntry<Languages>(
                      label: lang.label,
                      value: lang,
                    );
                  }).toList(),
            ),

            const SizedBox(height: 30),

            DropdownMenu<Languages>(
              initialSelection: Languages.english,
              controller: outputLanguageController,
              // requestFocusOnTap is enabled/disabled by platforms when it is null.
              // On mobile platforms, this is false by default. Setting this to true will
              // trigger focus request on the text field and virtual keyboard will appear
              // afterward. On desktop platforms however, this defaults to true.
              requestFocusOnTap: true,
              label: const Text('Output Language'),
              onSelected: (Languages? lang) {
                setState(() {
                  outputLang = lang;
                });
              },
              dropdownMenuEntries: Languages.values
                  .map<DropdownMenuEntry<Languages>>(
                      (Languages lang) {
                    return DropdownMenuEntry<Languages>(
                      label: lang.label,
                      value: lang,
                    );
                  }).toList(),
            ),

            SizedBox(height: 20),

            IconButton(
              isSelected: recording,
              iconSize: 56,
              icon: const Icon(Icons.fiber_manual_record_outlined),
              selectedIcon: const Icon(Icons.stop_circle_outlined),
              onPressed: () {
                toggleRecording();
              },
            ),


          ],
        ),
      ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
}
