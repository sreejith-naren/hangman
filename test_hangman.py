import random
from timeit import repeat

import hangman

random.seed(0)

def test_no_proper_noun():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("John\n")
        f.write("Mango\n")
        f.write("beautiful\n")
    for _ in range(10):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "beautiful"

def test_word_correct_length():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("lie\n")
        f.write("chair\n")
        f.write("consiousness\n")
    for _ in range(20):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "chair"

def test_word_no_punctuation():
    with open("/tmp/wordlist.txt", "w") as f:
        f.write("italy's\n")
        f.write("ravi's\n")
        f.write("meghalaya\n")
    for _ in range(20):
        word = hangman.get_secret_word("/tmp/wordlist.txt")
        assert word == "meghalaya"

def test_masked_single():
    secret_word= "elephant"
    guesses= ["l"]
    ret= hangman.mask_word(secret_word, guesses)
    assert ret== "-l------"   

def test_masked_multiple():
    secret_word= "elephant"
    guesses= ["e"]
    ret= hangman.mask_word(secret_word, guesses)
    assert ret== "e-e-----" 

def test_masked_mixed():
    secret_word= "elephant"
    guesses= ["e","x","h"]
    ret= hangman.mask_word(secret_word, guesses)
    assert ret== "e-e-h---"              
 

def test_create_status_normal():
    secret_word = "monument"
    guesses = ["m", "x", "o"]
    remaining_turns = 5
    assert hangman.create_status(secret_word, guesses, remaining_turns) == """Word: mo--m---
Guesses: m x o
Remaining turns : 5
"""

def test_create_status_no_guesses():
    secret_word = "monument"
    guesses = []
    remaining_turns = 8
    status = hangman.create_status(secret_word, guesses, remaining_turns)
    assert status == """Word: --------
Guesses: 
Remaining turns : 8
"""

def test_play_correct_guess():
    secret_word = "hangman"
    guesses = []
    remaining_turns = 7
    guess = "a"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
    assert guesses == ["a"]
    assert remaining_turns == 7
    assert repeat == False
    assert finished == False

def test_play_correct_repeat_guess():
    secret_word = "hangman"
    guesses = ["a"]
    remaining_turns = 4
    guess = "a"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
    assert guesses == ["a"]
    assert remaining_turns == 4
    assert repeat == True
    assert finished == False

def test_play_wrong_guess():
    secret_word = "hangman"
    guesses = ["a"]
    remaining_turns = 7
    guess = "x"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
    assert guesses == ["a", "x"]
    assert remaining_turns == 6
    assert repeat == False
    assert finished == False

def test_play_complete():
    secret_word = "hangman"
    guesses = ["h", "a", "n", "g", "m"]
    remaining_turns = 7
    guess = "n"
    remaining_turns, repeat, finished = hangman.play_round(secret_word, guesses, guess, remaining_turns)
    assert finished == True
    assert repeat== False

   
    

    
                          
    
