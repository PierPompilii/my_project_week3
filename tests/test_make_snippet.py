#test for a function to return a string as an argument and returns the first five words 
#and then a '...' if there are more than that.
from lib.make_snippet import *

def test_make_snippet_five():
    word = make_snippet ("hello goodbye day night home")
    assert word

def test_make_snippet_more_than_five():
    words = make_snippet ("hello goodbye day night home sleep")
    assert words == "hello goodbye day night home..."