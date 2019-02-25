## @file DCapALst.py
#  @author Yujing Chen
#  @brief create the DCapLst for the program
#  @date 02/11/2019
from StdntAllocTypes import *


class DCapALst:

    s = {}
    ## @brief intialize a DCapLst
    #  @param N/A
    #  @return N/A
    @staticmethod
    def init():
        DCapALst.s = {}

    ## @brief add department to the DCapLst
    #  @param d string of department
    #  @param n capacity number
    #  @return N/A
    #  @exception KeyError
    @staticmethod
    def add(d, n):
        for dep in DCapALst.s:
            if dep == d:
                raise KeyError
        DCapALst.s[d] = n

    ## @brief remove department from the DCapLst
    #  @param d string of department
    #  @return N/A
    #  @exception KeyError
    @staticmethod
    def remove(d):
        if d in DCapALst.s:
            del DCapALst.s[d]
        else:
            raise KeyError

    ## @brief define if an element is in the list
    #  @param d string of department
    #  @return True if element in the list, false if not
    @staticmethod
    def elm(d):
        for dep in DCapALst.s:
            if dep == d:
                return True
            else:
                return False

    ## @brief return the capacity of a department of the DCapLst
    #  @param d string of department
    #  @return the capacity of department d
    #  @exception KeyError
    @staticmethod
    def capacity(d):
        for dep in DCapALst.s:
            if dep == d:
                return DCapALst.s[dep]
        raise KeyError
