## @file SeqADT.py
# @author Seva Skvortsov
# @brief SeqADT
# @date 08/02/2019


## @brief An abstract date type to storing a sequence
class SeqADT:
    ## @brief init initial data structure
    #  @param x the sequence to store
    def __init__(self, x):
        self.s = x
        self.i = 0

    ## @brief returns the index of sequence to 0 (start)
    def start(self):
        self.i = 0

    ## @brief gives current element moves index to next element
    #  @exception throws StopIteration if the next index is out of sequence
    #  @return the element at the current index
    def next(self):
        if self.i >= len(self.s):
            raise StopIteration
        temp = self.i
        self.i += 1
        return self.s[temp]

    ## @brief tells you if you are at the end of the sequence
    #  @return True if index greater or equal to than length of the sequence False else
    def end(self):
        return (self.i >= len(self.s))
