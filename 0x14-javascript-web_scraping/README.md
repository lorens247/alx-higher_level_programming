0x14. JavaScript - Web scraping

---

## Why JavaScript Programming is Amazing

JavaScript is amazing for several reasons:

- **Versatility:** JavaScript is a versatile language that can be used for both front-end and back-end development, allowing developers to work across the entire web development stack.

- **Ease of Learning:** JavaScript has a relatively simple and intuitive syntax, making it accessible for beginners. It's a great language to start with for new programmers.

- **Large Ecosystem:** There is a vast ecosystem of libraries, frameworks, and tools available, making development more efficient. Popular libraries like React and Node.js have strong communities and extensive documentation.

- **Async Programming:** JavaScript supports asynchronous programming, which is essential for building responsive and efficient web applications. This is done through features like callbacks, promises, and async/await.

- **Interactivity:** JavaScript allows developers to create interactive user interfaces and dynamic content on websites, enhancing the user experience.

## How to Manipulate JSON Data

JSON (JavaScript Object Notation) is a lightweight data interchange format. In JavaScript, you can manipulate JSON data using built-in functions and methods. Here are some common operations:

- **Parsing JSON:** You can use `JSON.parse()` to convert a JSON string into a JavaScript object.

  ```javascript
  const jsonString = '{"name": "John", "age": 30}';
  const obj = JSON.parse(jsonString);
  ```

- **Stringifying JavaScript Object to JSON:** You can use `JSON.stringify()` to convert a JavaScript object to a JSON string.

  ```javascript
  const obj = { name: "John", age: 30 };
  const jsonString = JSON.stringify(obj);
  ```

- **Accessing JSON Properties:** Once parsed, you can access JSON object properties like any other JavaScript object.

  ```javascript
  console.log(obj.name); // Output: John
  ```

## How to Use Request and Fetch API

- **Using Request (Node.js):**

  ```javascript
  const request = require('request');

  request('https://api.example.com/data', (error, response, body) => {
      if (!error && response.statusCode === 200) {
          const data = JSON.parse(body);
          console.log(data);
      }
  });
  ```

- **Using Fetch API (Browser):**

  ```javascript
  fetch('https://api.example.com/data')
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error(error));
  ```

## How to Read and Write a File Using fs Module (Node.js)

- **Reading a File:**

  ```javascript
  const fs = require('fs');

  fs.readFile('example.txt', 'utf8', (err, data) => {
      if (err) {
          console.error(err);
          return;
      }
      console.log(data);
  });
  ```

- **Writing to a File:**

  ```javascript
  const fs = require('fs');

  const content = 'This is the content that will be written to the file.';
  
  fs.writeFile('example.txt', content, (err) => {
      if (err) {
          console.error(err);
          return;
      }
      console.log('File written successfully.');
  });
  ```

These examples showcase the basics of working with JSON data, making API requests, and reading/writing files in JavaScript. Each of these concepts can be expanded upon for more complex use cases.