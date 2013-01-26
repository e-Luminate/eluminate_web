Requirements
============

1 the LESS compiler (lessc)
   - first you need Node.js, download it at http://nodejs.org/
   - then install npm from http://npmjs.org/
   - then install LESS:

     $ npm install less

2 Watchdog
   - requires Python
   - install via pip

     $ pip install -r requirements.txt

   NOTE: we'll be using the `watchmedo` script included with Watchdog

3 make sure both `watchmedo` and `lessc` are in your PATH

We launch it with honcho.