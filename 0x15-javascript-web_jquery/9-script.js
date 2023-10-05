$(document).ready(function() {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function(data) {
    // Inside the callback function, extract the translation of "hello" from the fetched data and update the content of DIV#hello
    $('#hello').text(data.hello);
  });
});
