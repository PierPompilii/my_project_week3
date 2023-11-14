#takes a string as an argument and returns the number of words in that string.
from lib.count_words import *

def test_count_string_wordles():
    text = " "
    assert text == " "

def test_count_word():
    word = count_words("hello")
    assert word == 1

def test_count_two_words():
    word = count_words("hello world")
    assert word == 2

def test_count_5_words():
    word = count_words("hello world how are you?")
    assert word == 5