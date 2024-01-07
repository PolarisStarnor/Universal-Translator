import 'dart:io';
import 'dart:async';
import 'dart:convert';
import 'dart:typed_data';

class IntConverter extends Converter<Uint8List, List<int>> {
  const IntConverter();

  List<int> convert(Uint8List data) {
    if (data is Uint8List) {
      return data.buffer.asInt64List();
    } else {
      return new Uint64List.fromList(data).buffer.asUint8List();
    }
  }
}

Future<String> main() async {
  File file = File("test_audio/stuff_to_do.mp3");
  var bytes = file.openRead();

  // File file2 = File("test_audio/test_write.mp3");
  // file2.writeAsBytes(bytes);

  String output = "";

  Socket.connect("24.65.114.193", 14000).then((socket) async {
    await socket.addStream(bytes);
    // listen for the returned data
    // await socket.listen((data) {
    //     print("Listening");
    //     output = new String.fromCharCodes(data).trim();
    // });

    socket.destroy();
  });

  return output;
}
