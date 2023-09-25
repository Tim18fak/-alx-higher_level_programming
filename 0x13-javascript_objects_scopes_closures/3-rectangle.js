#!/usr/bin/node
/**
 * Check the parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let myVar = '';
      for (let y = 0;y < this.width; y++) {
        myVar += 'X';
         }
      console.log(myVar);
    }
  }
}
module.exports = Rectangle;
