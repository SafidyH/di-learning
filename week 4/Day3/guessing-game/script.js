function playTheGame() {
    var play = confirm("Would you like to play the game?");
  
    if (!play) {
      alert("No problem, Goodbye.");
      return;
    }
  
    var userNumber = parseInt(prompt("Enter a number between 0 and 10:"));
  
    while (isNaN(userNumber) || userNumber < 0 || userNumber > 10) {
      userNumber = parseInt(prompt("Sorry, it's not a valid number. Enter a number between 0 and 10:"));
    }
  
    var computerNumber = Math.round(Math.random() * 10);
  
    compareNumbers(userNumber, computerNumber);
  }
  
  function compareNumbers(userNumber, computerNumber) {
    if (userNumber === computerNumber) {
      alert("WINNER");
      return;
    }
  
    if (userNumber > computerNumber) {
      userNumber = parseInt(prompt("Your number is bigger than the computer's. Guess again:"));
    } else {
      userNumber = parseInt(prompt("Your number is smaller than the computer's. Guess again:"));
    }
  
    if (isNaN(userNumber) || userNumber < 0 || userNumber > 10) {
      alert("Sorry, it's not a valid number. Goodbye.");
      return;
    }
  
    compareNumbers(userNumber, computerNumber);
  }