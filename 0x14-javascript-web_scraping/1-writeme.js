#!/usr/bin/node
// Writes a string to a file

const myFile = require('fs');

myFile.writeFile(process.argv[2], process.argv[3], error => {
  if (error) {
    console.log(error);
  }
});
