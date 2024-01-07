import 'dart:io';
// import 'dart:typed_data';

void send(String path) async {
  File file = File(path);
  var bytes = file.openRead();

  // File file2 = File("test_audio/test_write.mp3");
  // file2.writeAsBytes(bytes);

  Socket.connect("localhost", 14000).then((socket) async {
    await socket.addStream(bytes);
    socket.destroy();
  });
}
