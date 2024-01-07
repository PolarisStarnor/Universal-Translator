import 'package:universal_translator/send.dart';
import 'package:test/test.dart';

void main() {
  test("Sending a file", () {
      final file = Uri.file(r'test_audio/stuff_to_do.mp3', windows: false);
      var result = send(file);

      final response = result.stream.bytesToString();

      expect(response, '200');
  });

}
