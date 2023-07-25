#!/usr/bin/node
// reads and prints the content of a file

const myFile = require('fs');

myFile.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
