#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request.get(apiUrl, (error, response, body) => {
	if (error) {
		console.error(error);
	} else {
		const todos = JSON.parse(body);
		const completedTasksByUser = {};
		todos.forEach(todo => {
			if (todo.completed) {
				if (completedTasksByUser[todo.userId] === undefined) {
					completedTasksByUser[todo.userId] = 1;
				} else {
					completedTasksByUser[todo.userId]++;
				}
			}
		});
		console.log(JSON.stringify(completedTasksByUser, null, 2));
	}
});
