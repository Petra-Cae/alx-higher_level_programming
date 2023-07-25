#!/usr/bin/node
/*
Prints the number of movies where the character
"Wedge Antilles" is present
*/

const req = require('request');
const url = process.argv[2];
const charId = '18';

let count = 0;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(charId)) {
          count += 1;
        }
      });
    });
    console.log(count);
  }
});
