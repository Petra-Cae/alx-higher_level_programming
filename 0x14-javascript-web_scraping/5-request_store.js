#!/usr/bin/node
/*
Gets the content of a webpage and stores it in a file
*/

const fs = require('fs');
const req = require('request');
const url = process.argv[2];
const file = process.argv[3];

req(url).pipe(fs.createWriteStream(file));
