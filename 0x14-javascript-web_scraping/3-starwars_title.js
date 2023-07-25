#!/usr/bin/node
/*
prints the title of a Star Wars movie where the episode number
matches a given integer
*/
const req = require('request');
const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

req.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  }
  console.log(JSON.parse(body).title);
});
