#!/usr/bin/node
/*
Prints all characters of a specified Star Wars movie so long as
the integer matches the episode number
*/
const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }
  const data = JSON.parse(body);
  const charas = data.characters;
  for (const character of charas) {
    req(character, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      const charData = JSON.parse(body);
      console.log(charData.name);
    });
  }
});
