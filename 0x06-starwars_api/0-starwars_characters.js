#!/usr/bin/node

const request = require("request");
const url = "https://swapi-api.alx-tools.com/api/";
const argv = process.argv;


request(`${url}films/${argv[2]}`, {json: true}, (e, r, b) => {
	if (e || r.statusCode !== 200) return;


	const characterNames = [];

	b.characters.forEach(url => {
		request(url, {json: true}, (err, res, body)=>{
			characterNames.push(body.name);

			if (characterNames.length === b.characters.length) {
				characterNames.forEach(name => console.log(name));
			}
		})
	})
});

