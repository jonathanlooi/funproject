import sys # sys deals with system functions and parameters
from datetime import datetime as dt # importing with alias

print(dt.now())

def newline():
    print("\n")

newline()

# advanced strings
print("Advanced Strings")
name = "Jonathan"
print(name[- 1]) # last letter
sentence = "this is a sentence."
print(sentence[:4]) # prints a range
print(sentence[10:-1]) # prints last word
print(sentence.split())
sentence_split = sentence.split()
sentence_join = " ".join(sentence_split)
print("Sentence join: " + sentence_join)

newline()
quoteception = "I said, \"give me all your money\""
print(quoteception)

print("A" in "Apple") # this returns true. The in determines if it is in the string
letter = "a"
word = "Apple"
print(letter.upper() in word)
newline()

word2 = "Blowhale"
print(letter.lower() in word.lower() and not (letter.lower() in word2.lower()))

lotsofspace = "       hello                "
print(lotsofspace.strip()) # gets rid of spacing

rating = "absolutely hate"
print("I {} the movie The Hangover.".format(rating))
