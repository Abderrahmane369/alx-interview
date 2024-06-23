#!/usr/bin/node

const request = require("request");
const url = "https://swapi-api.alx-tools.com/api/";
const argv = process.argv;


request(`${url}films/${argv[2]}`, {json: true}, (e, r, b) => {
	if (e || r.statusCode !== 200) return;

	b.characters.forEach((v, _) => {
		request(v, {json:true}, (e_, r_, b_) => {
			if (e_ || r_.statusCode !== 200) return;

			console.log(b_.name);
		})
	});
});

