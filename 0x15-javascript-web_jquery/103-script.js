$(document).ready(function() {
  $('#language_code').keypress(function(event) {
      if (event.which === 13) {
          const languageCode = $('#language_code').val();

          $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function(data) {
              $('#hello').text(data.hello);
          });
      }
  });

  $('#btn_translate').click(function() {
      const languageCode = $('#language_code').val();

      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function(data) {

          $('#hello').text(data.hello);
      });
  });
});
