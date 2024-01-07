import 'dart:io';
import 'dart:async';
import 'dart:convert';
import 'dart:typed_data';

Future<String> main() async {
  File file = File("test_audio/stuff_to_do.mp3");
  var bytes = file.openRead();

  // File file2 = File("test_audio/test_write.mp3");
  // file2.writeAsBytes(bytes);

  List<int> output = ([]);

  Socket.connect("24.65.114.193", 14000).then((socket) async {
    await socket.addStream(bytes);

    var fromByte = new StreamTransformer<Uint8List, List<int>>.fromHandlers(
      handleData: (data, sink) {
        sink.add(data);
      });

    Uint8List data = Uint8List.fromList([]);
    socket.transform(fromByte).listen((e) => output);
    socket.destroy();
  });

  return utf8.decode(output);
}
