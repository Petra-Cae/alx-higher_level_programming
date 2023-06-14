#!/usr/bin/node
const args = process.argv;
const size = parseInt(args[2]);
let h;
let b;
let sq = '';

if (!size) {
  console.log('Missing size');
} else {
  for (h = 0; h < size; h++) {
    for (b = 0; b < size; b++) {
      sq = (sq + 'X');
    }
    console.log(sq);
  }
}
