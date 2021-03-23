

# Keeps track of the board's spots
gameBoard = {'1': '   ', '2': '   ', '3': '   ',
             '4': '   ', '5': '   ', '6': '   ',
             '7': '   ', '8': '   ', '9': '   '}

keys = []

for key in gameBoard:
    keys.append(key)

# Function that draws board


def drawBoard(board):
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print('---------------')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('---------------')
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])


# Main function that runs the game
def playGame():

    # Keeps track of which player's turn it is, count that increments and a winner
    playerTurn = 'X'
    count = 0
    winner = False

    # Loops through the turns of the game asking players to select a row and column
    for i in range(10):
        drawBoard(gameBoard)
        column = input("\nIt is your turn player " +
                       playerTurn + ". Pick a column (0, 1 or 2): ")
        row = input("Now pick a row (0, 1 or 2): ")
        print("\n")

        # Keeps track of the selection players make with the boardSpot variable
        if column == '0' and row == '0':
            boardSpot = '1'

        elif column == '1' and row == '0':
            boardSpot = '2'

        elif column == '2' and row == '0':
            boardSpot = '3'

        elif column == '0' and row == '1':
            boardSpot = '4'

        elif column == '1' and row == '1':
            boardSpot = '5'

        elif column == '2' and row == '1':
            boardSpot = '6'

        elif column == '0' and row == '2':
            boardSpot = '7'

        elif column == '1' and row == '2':
            boardSpot = '8'

        elif column == '2' and row == '2':
            boardSpot = '9'

        else:
            print("Invalid option, please select a proper spot on the board.")
            continue

        # 'Draws' the X or O in the spot the player selected
        if gameBoard[boardSpot] == '   ':
            gameBoard[boardSpot] = playerTurn
            count += 1

        else:
            print(
                "This spot is already occupied. Please select another spot on the board.")
            continue

        # After 5 turns when a winner is possible, checks to see if someone has won
        if count >= 5:
            if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != '   ':
                drawBoard(gameBoard)
                print("\n\n Congratulations player " +
                      playerTurn + "! You have won!")
                winner = True
                break

            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != '   ':
                drawBoard(gameBoard)
                print("\n\n Congratulations player " +
                      playerTurn + "! You have won!")
                winner = True
                break

            elif gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != '   ':
                drawBoard(gameBoard)
                print("\n\n Congratulations player " +
                      playerTurn + "! You have won!")
                winner = True
                break

            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != '   ':
                drawBoard(gameBoard)
                print("\n\n Congratulations player " +
                      playerTurn + "! You have won!")
                winner = True
                break

            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != '   ':
                drawBoard(gameBoard)
                print("\n\n Congratulations player " +
                      playerTurn + "! You have won!")
                winner = True
                break

            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != '   ':
                drawBoard(gameBoard)
                print("\n\n Congratulations player " +
                      playerTurn + "! You have won!")
                winner = True
                break

            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != '   ':
                drawBoard(gameBoard)
                print("\n\n Congratulations player " +
                      playerTurn + "! You have won!")
                winner = True
                break

            elif gameBoard['3'] == gameBoard['5'] == gameBoard['7'] != '   ':
                drawBoard(gameBoard)
                print("\n\n Congratulations player " +
                      playerTurn + "! You have won!")
                winner = True
                break

        # Checks to see if there is a tie
        if count == 9 and winner == False:
            print("\n\n There is no winner! It is a tie!")

        # Swaps players every turn
        if playerTurn == 'X':
            playerTurn = 'O'

        else:
            playerTurn = 'X'


# Runs the game
if __name__ == "__main__":
    playGame()
