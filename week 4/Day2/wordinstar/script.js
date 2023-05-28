var wordInput = prompt("Enter several words separated by commas:");

var words = wordInput.split(",");

var longestWordLength = 0;
for (var i = 0; i < words.length; i++) {
  var word = words[i].trim();
  if (word.length > longestWordLength) {
    longestWordLength = word.length;
  }
}

var starsLine = "*".repeat(longestWordLength + 4);
var spacesLine = "*" + " ".repeat(longestWordLength + 2) + "*";

console.log(starsLine);
for (var i = 0; i < words.length; i++) {
  var word = words[i].trim();
  var spaces = " ".repeat(longestWordLength - word.length);
  console.log("* " + word + spaces + " *");
}
console.log(starsLine);