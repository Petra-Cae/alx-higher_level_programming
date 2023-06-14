#!/usr/bin/node
const args = process.argv;
const argLen = process.argv.length;

if (argLen <= 3) {
  console.log(0);
} else {
  const nargs = args.map(Number)
    .slice(2, argLen)
    .sort((a, b) => a - b);
  console.log(nargs[nargs.length - 2]);
}
