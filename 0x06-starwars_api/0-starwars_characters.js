#!/usr/bin/node

const request = require("request");
const url = "https://swapi-api.alx-tools.com/api/";
const argv = process.argv;


request(`${url}films/${argv[2]}`, {json: true}, (e, r, b) => {
	if (e || r.statusCode !== 200) return;

	function recurFetch(i, chrtrs) {
		if (i >= chrtrs.length) return;

		request(chrtrs[i], {json:true}, (e_, r_, b_) => {
			if (e_ || r_.statusCode !== 200) return;

			console.log(b_.name);
		})

		recurFetch(i + 1, chrtrs);
	}

	recurFetch(0, b.characters);
});

