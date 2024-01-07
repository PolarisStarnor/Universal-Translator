import 'dart:io';
// import 'dart:typed_data';

void main() async {
  File file = File("test_audio/test.mp3");
  var bytes = file.openRead();

  // File file2 = File("test_audio/test_write.mp3");
  // file2.writeAsBytes(bytes);

  Socket.connect("24.65.114.193", 14000).then((socket) async {
    await socket.addStream(bytes);
    socket.destroy();
  });
}
