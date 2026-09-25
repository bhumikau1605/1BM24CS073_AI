#TIC TAC TOE
import random
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game_still_going = True
winner = None
current_player = "Human" 
while game_still_going:
    print("\n" + board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8] + "\n")
    if current_player == "Human":
        position = int(input("Choose a position from 1-9: ")) - 1
        if board[position] == " ":
            board[position] = "X"
            current_player = "System" 
        else:
            print("Spot already taken. Try again!")
    elif current_player == "System":
        print("System is making a move...")
        while True:
            position = random.randint(0, 8)
            if board[position] == " ":
                board[position] = "O"
                current_player = "Human" 
                break
    if (board[0] == board[1] == board[2] != " ") or \
       (board[3] == board[4] == board[5] != " ") or \
       (board[6] == board[7] == board[8] != " ") or \
       (board[0] == board[3] == board[6] != " ") or \
       (board[1] == board[4] == board[7] != " ") or \
       (board[2] == board[5] == board[8] != " ") or \
       (board[0] == board[4] == board[8] != " ") or \
       (board[2] == board[4] == board[6] != " "):
        if current_player == "System": 
            winner = "Human"
        else:
            winner = "System"
        game_still_going = False
    elif " " not in board:
        winner = "Tie"
        game_still_going = False
if winner == "Human":
    print("🎉 You won!")
elif winner == "System":
    print("💻 System won!")
else:
    print("🤝 It's a tie!")
