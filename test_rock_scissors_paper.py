import pytest
import math

import rock_scissors_paper as rsp

def test_check_validity_rock():
    rock: str = 'rock'
    expected: int = 2

    # Act
    actual: int = rsp.check_validity(rock)

    # Assert
    assert actual == expected

def test_check_validity_paper():
    paper: str = 'paper'
    expected: int = 0

    # Act
    actual: int = rsp.check_validity(paper)

    # Assert
    assert actual == expected

def test_check_validity_scissors():
    scissors: str = 'scissors'
    expected: int = 1

    # Act
    actual: int = rsp.check_validity(scissors)

    # Assert
    assert actual == expected

def test_check_validity_error():
    word: str = 'word'

    # Act
    with pytest.raises(ValueError) as ex:
        rsp.check_validity(word)

    assert str(ex.value) == "illegal game option"

def test_check_validity_upper_lower_case():
    papers = ['papeR', 'PAPER', 'paPER']
    for choice in papers:
        assert rsp.check_validity(choice) == 0

    rocks = ['Rock', 'ROCk', 'roCK']
    for choice in rocks:
        assert rsp.check_validity(choice) == 2

    scissors = ['scissorS', 'SCISSORS', 'SCIssoRS']
    for choice in scissors:
        assert rsp.check_validity(choice) == 1

def test_check_winner_error_player1():
    # Act
    with pytest.raises(ValueError) as ex:
        rsp.check_winner(4, 1)

    assert str(ex.value) == "illegal choice"

def test_check_winner_error_player2():
    # Act
    with pytest.raises(ValueError) as ex:
        rsp.check_winner(1, 4)

    assert str(ex.value) == "illegal choice"

def test_check_winner_error_player1_player2():
    # Act
    with pytest.raises(ValueError) as ex:
        rsp.check_winner(None, 4)

    assert str(ex.value) == "illegal choice"

def test_check_winner_all():
    # 0 = paper
    # 1 = scissors
    # 2 = rock
    options = {(0, 0): 0, (0, 1): 2, (1, 0): 1,
               (0, 2): 1, (2, 0): 2, (1, 2): 2,
               (2, 1): 1, (1, 1): 0, (2, 2): 0}
    for (player1, player2), expected in options.items():
        #key == (0,0) value 0
        # player1 = key[0]
        # player2 = key[1]
        actual: int = rsp.check_winner(player1, player2)
        assert actual == expected


def test_check_winner_rock_rock():
    # Arrange
    x: list[list[str]] = [['rock', 'rock'], ['rock', 'paper'], ['rock', 'scissors'],
                          ['paper', 'rock'], ['paper', 'paper'], ['paper', 'scissors'],
                          ['scissors', 'rock'], ['scissors', 'paper'], ['scissors', 'scissors']];

    expected: list[int] = [0, 2, 1, 1, 0, 2, 2, 1, 0];

    # Act
    actual: list[int] = [];
    for item in x:
        player1_choice: int = rps.check_validity(item[0]);
        player2_choice: int = rps.check_validity(item[1]);
        actual.append(rps.check_winner(player1_choice, player2_choice));

    # Assert
    assert actual == expected;