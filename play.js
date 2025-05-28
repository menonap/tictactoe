let board = Array(9).fill('[ ]');
let currentPlayer = true; // true for X, false for O
let gameActive = true;

const boardElement = document.getElementById('board');
const statusElement = document.getElementById('status');

// Build board UI
function createBoard() {
  boardElement.innerHTML = '';
  const rows = ['A', 'B', 'C'];

  for (let r = 0; r < 3; r++) {
    const row = document.createElement('tr');
    for (let c = 0; c < 3; c++) {
      const cell = document.createElement('td');
      const index = r * 3 + c;
      cell.dataset.index = index;
      cell.addEventListener('click', handleClick);
      cell.textContent = board[index] !== '[ ]' ? board[index].trim() : '';
      row.appendChild(cell);
    }
    boardElement.appendChild(row);
  }
}

function handleClick(event) {
  if (!gameActive) return;

  const index = parseInt(event.target.dataset.index);

  if (board[index] !== '[ ]') return;

  board[index] = currentPlayer ? ' X ' : ' O ';
  createBoard();

  const { winner, continueGame, win } = checkEnd(board, currentPlayer);

  if (!continueGame) {
    gameActive = false;
    statusElement.textContent = win ? `Winner: ${winner}` : 'It\'s a tie!';
  } else {
    currentPlayer = !currentPlayer;
    statusElement.textContent = `Current Turn: ${currentPlayer ? 'X' : 'O'}`;
  }
}

function checkEnd(board, currPlayer) {
  const winConditions = [
    [0,1,2], [3,4,5], [6,7,8], // rows
    [0,3,6], [1,4,7], [2,5,8], // cols
    [0,4,8], [2,4,6]           // diagonals
  ];

  for (let condition of winConditions) {
    const [a, b, c] = condition;
    if (board[a] !== '[ ]' && board[a] === board[b] && board[a] === board[c]) {
      return {
        winner: currPlayer ? 'X' : 'O',
        continueGame: false,
        win: true
      };
    }
  }

  if (!board.includes('[ ]')) {
    return { winner: 'None', continueGame: false, win: false };
  }

  return { winner: 'None', continueGame: true, win: false };
}

// Initialize
createBoard();
