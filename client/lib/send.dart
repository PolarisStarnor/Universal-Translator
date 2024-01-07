send(Uri file) async {
  var uri = Uri.https('24.65.114.193', 'create')
  var request = http.MultipartRequest('POST', uri)
    ..fields['user'] = 'universal_translator'
    ..files.add(await http.MultiPartFile.fromPath(
        'package', await File.fromUri(file).readAsBytes(),
        contentType: MediaType('audio', 'mp3')
    ))

  request.send().then((response) {
      if (response.statusCode == 200) print("Uploaded");
  })
}
