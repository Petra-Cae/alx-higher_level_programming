#!/usr/bin/node
/*
Prints all characters of a Star Wars movie using its movie ID
*/
const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;
let chars = [];

req(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const data = JSON.parse(body);
  chars = data.characters;
  getChars(0);
});

const getChars = (index) => {
  if (index === chars.length) {
    return;
  }

  req(chars[index], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    const charData = JSON.parse(body);
    console.log(charData.name);
    getChars(index + 1);
  });
};
