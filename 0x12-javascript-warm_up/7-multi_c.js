#!/usr/bin/node
const args = process.argv;
const num = parseInt(args[2]);

if (!num) {
  console.log('Missing number of occurences');
} else {
  for (let a = 0; a < num; a++) {
    console.log('C is fun');
  }
}
