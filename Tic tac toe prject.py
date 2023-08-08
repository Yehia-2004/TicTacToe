game_board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]


def play(game_board,symbol=None):
    def print_game_board(game_board):
        show = '----------------------------------\n'
        element_counter = 0
        for row in game_board:
            for element in row:
                show += f"|    {element}    |"
                element_counter += 1
                if element_counter % 3 == 0:
                    show += "\n----------------------------------\n"
        return show
    turns = []
    while True:
      try:
        i = int(input("Enter the row number you want from 1 to 3: "))-1
        game_board [i]
        j = int(input("Enter the column number you want from 1 to 3: "))-1
        game_board [i][j]
      
      except ValueError:
         print("You should enter only numbers")
         continue
      except IndexError:
         print("You should enter numbers in range (from 1 to 3), please try again")
         continue
      
      
      symbol = input("Enter your symbol: ")

      if len(turns) == 0:
        turns.append(symbol)
      elif len(turns) > 0:
         if turns[-1] == symbol:
            if symbol.lower() == "x":
                print("This is player's O turn, please try again")
                continue
            if symbol.lower() == "o":
                print("This is player's X turn, please try again")
                continue
         elif turns[-1] != symbol:
            turns.append(symbol) 
      
      if (symbol.upper() != "X") and (symbol.upper() != "O"):
         print("You should enter X or O only")
         continue
      
      if (game_board[i][j] != " "):
        print("This location is already inputed, please try again")
        continue
            
      game_board[i][j] = symbol.upper()
      print(print_game_board(game_board))
      
      def check_winner(game_board,symbol):
         for i in range(3):
            if (game_board[i][0] == game_board[i][1] == game_board[i][2] == "X") or (game_board[i][0] == game_board[i][1] == game_board[i][2] == "O"):
               print(f"The game has been won by {symbol.upper()}, Congratulations")
               return True
            elif (game_board[0][i] == game_board[1][i] == game_board[2][i] == "X") or (game_board[0][i] == game_board[1][i] == game_board[2][i] == "O"):
               print(f"The game has been won by {symbol.upper()}, Congratulations")
               return True
         if ((game_board[0][0] == game_board[1][1] == game_board[2][2] == 'X') or (game_board[0][2] == game_board[1][1] == game_board[2][0] == 'X')) or ((game_board[0][0] == game_board[1][1] == game_board[2][2] == 'O') or (game_board[0][2] == game_board[1][1] == game_board[2][0] == 'O')):
            print(f"The game has been won by {symbol.upper()}, Congratulations" )
            return True
      if check_winner(game_board,symbol) == True:
        break
      
      def check_tie(game_board):
        filled_counter = 0
        for lst in game_board:
           for element in lst:
              if element != " ":
                filled_counter += 1
        if filled_counter == 9:
           print("The game has been tied")
           return True
      if check_tie(game_board) == True:
         break

play(game_board)
   