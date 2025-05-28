#checkEnd will check if the current board has a win or a loss
def checkEnd(board, currPlayer, gameplay):

  #check for tie
  if "[ ]" not in board:
    return 'None', False, False

  #check for win
  winConditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

  for condition in winConditions:
      if board[condition[0]] == board[condition[1]] == board[condition[2]] != "[ ]":
          if currPlayer:
            winner = "X"
          else:
            winner = "O"
          return winner, False, True
  return 'None', True, False



#change the player
def changePlayer(currPlayer):
  print()
  if currPlayer:
    return False
  else:
    return True

def printBoard(bd):
  print("   1     2     3")
  print(f"A {bd[0]} | {bd[1]} | {bd[2]} ")
  print("  ---------------")
  print(f"B {bd[3]} | {bd[4]} | {bd[5]} ")
  print("  ---------------")
  print(f"C {bd[6]} | {bd[7]} | {bd[8]} ")

def promptAndRead(board, currPlayer):

  x, y = input("Enter position in <letter><number> format (e.g., A1, B3): ")
  num = int(y)
  ind = 0

  if x.upper() == "A":
    ind = num - 1
  elif x.upper() == "B":
    ind = num + 2
  elif x.upper() == "C":
    ind = num + 5

  if currPlayer:
    if board[ind] == '[ ]':
      board[ind] = ' X '
    else:
      print()
      print("INVALID INPUT, TRY AGAIN")
      promptAndRead(board, currPlayer)
  else:
    if board[ind] == '[ ]':
      board[ind] = ' O '
    else:
      print("INVALID INPUT, TRY AGAIN")
      promptAndRead(board, currPlayer)
  print()
  print("---CURRENT BOARD---")
  printBoard(board)



def main():
  board = [ "[ ]", "[ ]", "[ ]",
            "[ ]", "[ ]", "[ ]",
            "[ ]", "[ ]", "[ ]"
          ]

  #True means X and false is O
  currPlayer = True

  winner = "None"
  gameplay = True

  #if true then win, if false then tie
  result = False

  printBoard(board)
  print()

  while gameplay:
    promptAndRead(board, currPlayer)
    winner, gameplay, result = checkEnd(board, currPlayer, gameplay)
    currPlayer = changePlayer(currPlayer)

  print()
  print("---GAME OVER---")

  print(f"Winner: {winner}")
  print(f"Result: {'Win' if result else 'Tie'}")


if __name__ == "__main__":
    main()
