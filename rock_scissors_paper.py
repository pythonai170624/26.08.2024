# TDD
# Test Driven Development

def check_validity(choice) -> int:
    """
    check if choice is correct
    rock, scissors, paper
    if not- raise error ValueError "wrong choice"
    :return:
    0 1 2
    """
    if not choice.lower() in ["paper", "scissors", "rock"]:
        raise ValueError("illegal game option")
    match choice.lower():
        case "paper": return 0
        case "scissors": return 1
        case "rock": return 2

def check_winner(player1, player2) -> int:
    """
    check who won (or tie) between player1, player2
    if player1 and player2 not in range[1,2,3]- raise error
    :param player1: 0 1 2
    :param player2: 0 1 2
    :return:
    winner 1 or 2 or 0 for draw
    """
    if not player1 in [0, 1, 2] or not player2 in [0, 1, 2]:
        raise ValueError("illegal choice")

    options = {(0, 0): 0, (0, 1): 2, (1, 0): 1,
               (0, 2): 1, (2, 0): 2, (1, 2): 2,
               (2, 1): 1, (1, 1): 0, (2, 2): 0}

    result: int = options.get( (player1, player2) )
    return result

def play_game():
    player1: str = None
    player2: str = None
    while True:
        try:
            player1 = input("Player1: Enter your choice [rock, scissors, paper]:")
            player1 = check_validity(player1)
            break
        except:
            print("try again...")
    while True:
        try:
            player2 = input("Player2: Enter your choice [rock, scissors, paper]:")
            player2 = check_validity(player2)
            break
        except Exception as ex:
            print(ex)
    result = check_winner(player1, player2)
    if result == 1 or result == 2:
        print(f"Player {result} won!")
    else:
        print(f"Tie!")



    guess2: str = input("Enter your choice [rock, scissors, paper]:")

# player1 = rock scissors paper
# def validate("rock" "scissors" "paper")
#                 2        1      0  Error
# player2 = rock scissors paper
# who won? tie
# def check_win (int, int)
#                check 0 1 2 x 2 Error
#                (1, 1) --> tie
# 0 0, 1 0, 1 0
# 2 1, 2 2, 2 0, 0 2

# test- flow e2e (?) input simulation, print simulation