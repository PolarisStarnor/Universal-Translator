import 'package:audioplayers/audioplayers.dart';
import 'package:universal_translator/languages.dart';
import 'package:flutter_tts/flutter_tts.dart';


Future<void> playSound(String path) async {

  final player = AudioPlayer();
  await player.play(DeviceFileSource(path));

}

Future<void> textToSpeech(String text, String ietf) async {

  FlutterTts tts = FlutterTts();
  tts.setLanguage(ietf);
  tts.speak(text);
  tts.awaitSpeakCompletion(true);

}