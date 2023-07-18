let board = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
let currentPlayer = "X";

function makeMove(position) {
    if (board[position] === " ") {
        board[position] = currentPlayer;
        document.getElementsByClassName("cell")[position].textContent = currentPlayer;
        
        if (checkWin()) {
            alert("Player " + currentPlayer + " wins!");
            resetBoard();
        } else if (isTie()) {
            alert("It's a tie!");
            resetBoard();
        } else {
            currentPlayer = currentPlayer === "X" ? "O" : "X";
        }
    }
}

function checkWin() {
    const winningCombos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], // rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8], // columns
        [0, 4, 8], [2, 4, 6] // diagonals
    ];

    for (let combo of winningCombos) {
        if (board[combo[0]] !== " " && board[combo[0]] === board[combo[1]] && board[combo[1]] === board[combo[2]]) {
            return true;
        }
    }

    return false;
}

function isTie() {
    return !board.includes(" ");
}

function resetBoard() {
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "];
    currentPlayer = "X";

    const cells = document.getElementsByClassName("cell");
    for (let i = 0; i < cells.length; i++) {
        cells[i].textContent = " ";
    }
}