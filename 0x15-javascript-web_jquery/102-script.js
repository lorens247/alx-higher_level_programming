$(document).ready(function() {
  $('#language_code').keypress(function(event) {
      // Check if the pressed key is ENTER (key code 13)
      if (event.which === 13) {
          // Fetch the language code entered by the user
          const languageCode = $('#language_code').val();

          // Fetch the translation from the API based on the language code
          $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function(data) {
              // Update the content of DIV#hello with the fetched translation
              $('#hello').text(data.hello);
          });
      }
  });

  $('#btn_translate').click(function() {
      // Fetch the language code entered by the user
      const languageCode = $('#language_code').val();

      // Fetch the translation from the API based on the language code
      $.get(`https://www.fourtonfish.com/hellosalut/hello/${languageCode}`, function(data) {
          // Update the content of DIV#hello with the fetched translation
          $('#hello').text(data.hello);
      });
  });
});
