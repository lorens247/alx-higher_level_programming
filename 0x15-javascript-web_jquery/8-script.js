$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
    // Inside the callback function, loop through the fetched data (movies) and append their titles to the UL#list_movies
    data.results.forEach(function(movie) {
        // Create a new list item
        const listItem = $('<li></li>');

        // Set the text content of the list item
        listItem.text(movie.title);

        // Append the list item to the UL#list_movies
        $('#list_movies').append(listItem);
    });
});
