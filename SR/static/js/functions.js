function analyze_audiofile() {
  console.log("analyze");
  path_to_audio_file=getElementById('file').val()
  console.log(path_to_audio_file);
  // $.ajax({
  //     method: 'POST',
  //     url: 'ruta de tu vista definida en django'
  //     data: {
  //         'a': a,
  //         'b': b,
  //     },
  //     dataType: "json",
  //     success: function(response) {
  //         $('#outputR').val(response.resultado);
  //     }
  // });
};
// $('#analyze_audiofile').click(function () {
//   console.log("analyze");
//   path_to_audio_file=getElementById('file').val()
//   console.log(path_to_audio_file);
// })
