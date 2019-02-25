## @file SeqADT.py
#  @author Yujing Chen
#  @brief General function for SeqADT
#  @date 2019/02/11


## @brief An abstract data type that represents a Sequence
class SeqADT:
    ## @brief SeqADT constructor
    #  @details initilize a SeqADT for a sequence, s for sequence, i for index
    #  @param x sequence of T
    def __init__(self, x):
        self.i = 0
        self.s = x

    ## @brief start change the index to start of Seq
    #  @return N/A
    def start(self):
        self.i = 0

    ## @brief next return the current value and add 1 to index
    #  @return value of s[i]
    def next(self):
        if self.i >= len(self.s):
            raise StopIteration
        out = self.s[self.i]
        self.i += 1
        return out

    ## @brief end returns whether the Seq has end
    #  @return boolean, True if Seq end, false if not
    def end(self):
        return self.i >= len(self.s)
