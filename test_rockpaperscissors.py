import rockpaperscissors, pytest

# def test_rock_is_valid_play():
#     assert rockpaperscissors.is_valid_play("rock") is True
#
# def test_paper_is_valid_play():
#     assert rockpaperscissors.is_valid_play("paper") is True
#
# def test_scissors_is_valid_play():
#     assert rockpaperscissors.is_valid_play("scissors") is True

# Nahradime parametrickym testem:
@pytest.mark.parametrize("play",["rock","paper","scissors"])
def test_is_valid_play(play):
    assert rockpaperscissors.is_valid_play(play) is True

# def test_spock_is_not_valid_play():
#     assert rockpaperscissors.is_valid_play("spock") is False

@pytest.mark.parametrize("play",["spock","","lizard"])
def test_is_not_valid_play(play):
    assert rockpaperscissors.is_valid_play(play) is False

def test_random_play_is_valid():
    # Uz mame otestovanou jinde fci is_valid_play, tak ji zde muzu pouzit
    assert rockpaperscissors.is_valid_play(rockpaperscissors.random_play())

def test_random_play_is_always_valid():
    # Je to nahodne, takze to potrebujeme otestovat vice nez jednou
    for _ in range(10000):
        assert rockpaperscissors.is_valid_play(rockpaperscissors.random_play())

def test_random_play_is_fair():
    plays = {"rock" : 0,
        "paper" : 0,
        "scissors" : 0}
    for _ in range(10000):
        play = rockpaperscissors.random_play()
        plays[play] += 1
    for value in plays.values():
        assert value>3000

# def test_rock_rock_is_tie():
#     assert rockpaperscissors.determine_game_result("rock","rock") == "tie"

# parametricky test
@pytest.mark.parametrize("play",["rock","paper","scissors"])
def test_same_is_tie(play):
    assert rockpaperscissors.determine_game_result(play,play) == "tie"

@pytest.mark.parametrize("human, computer",[("paper","rock"),("rock","scissors"),("scissors","paper")])
def test_human_wins(human,computer):
    assert rockpaperscissors.determine_game_result(human,computer) == "human"

@pytest.mark.parametrize("human, computer",[("rock","paper"),("scissors","rock"),("paper","scissors")])
def test_computer_wins(human,computer):
    assert rockpaperscissors.determine_game_result(human,computer) == "computer"
