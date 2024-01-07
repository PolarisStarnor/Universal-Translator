import 'dart:async';
import 'dart:io';

import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:path_provider/path_provider.dart';
import 'package:record/record.dart';

class Recorder {

  AudioRecorder audioRecorder = AudioRecorder();

  Future<void> start() async {

    final directory = await getApplicationCacheDirectory();
    var path = directory.path;
    print(path);
    File('$path/input.wav').createSync(recursive: true);

    audioRecorder = AudioRecorder();
    // Check and request permission if needed
    if (await audioRecorder.hasPermission()) {

      const encoder = AudioEncoder.wav;
      const config = RecordConfig(encoder: encoder, numChannels: 1);

      // Start recording to file
      await audioRecorder.start(config, path: '$path/input.wav');

    }
  }

  Future<String?> end() async {

    final path = await audioRecorder.stop();
    audioRecorder.dispose();

    return path;

  }

}