$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
    // Inside the callback function, extract the character name from the fetched data
    const characterName = data.name;
    
    // Use jQuery to select the DIV#character element and update its content with the character name
    $('#character').text(characterName);
});
