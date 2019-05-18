import subprocess, sys

# def test_wrong_play_results_in_repeated_question():
#     cp = subprocess.run(
#         [sys.executable,"rockpaperscissors.py"],
#         stdout=subprocess.PIPE,
#         encoding="utf-8",
#         input="bla\nrock\n",
#         check=True)
#     assert cp.stdout.count("rock, paper or scissors?") == 2

def run_rps(input):
    return subprocess.run(
        [sys.executable,"rockpaperscissors.py"],
        stdout=subprocess.PIPE,
        encoding="utf-8",
        input=input,
        check=True)

def test_wrong_play_results_in_repeated_question():
     cp = run_rps("bla\nrock\n")
     assert cp.stdout.count("rock, paper or scissors?") == 2
