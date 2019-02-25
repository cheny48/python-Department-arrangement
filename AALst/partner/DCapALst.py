## @file DCapALst.py
# @author Seva Skvortsov
# @brief DCapALst
# @date 08/02/2019

from StdntAllocTypes import *
from typing import NamedTuple


## @brief abstract object for Department Capacity Association
class DCapALst:
    ## @brief local tuple class to represent tuple of department and its capacity
    class __Tuple__(NamedTuple):
        dept: DeptT
        cap: int
    ## @brief initializes the abstract object
    @staticmethod
    def init():
        DCapALst.s = []
    ## @brief add a tuple of a department and its capacity
    # @exception throws KeyError if department already in list
    # @param d is a department of type DeptT being added
    # @param n is the capacity of the department
    @staticmethod
    def add(d, n):
        for i in DCapALst.s:
            if i.dept == d:
                raise KeyError
        DCapALst.s = DCapALst.s + [DCapALst.__Tuple__(d, n)]

    @staticmethod
    ## @brief removes a tuple of a department and its capacity from list
    # @exception throws KeyError if trying remove a department not in list
    # @param d the department of type DeptT you want to remove
    def remove(d):
        raisee = True
        for i in DCapALst.s:
            if i.dept == d:
                raisee = False
                DCapALst.s.remove(i)
        if raisee:
            raise KeyError

    @staticmethod
    ## @brief tells you if a department is in the list
    # @param d department name you want to see if in the list
    # @return True if department is in list False if its not
    def elm(d):
        for i in DCapALst.s:
            if i.dept == d:
                return True
        return False

    @staticmethod
    ## @brief tells you the capacity of a department
    # @exception throws KeyError if trying to find capacity of department not in list
    # @param d the department of type DeptT you want to find the capacity of
    def capacity(d):
        for i in DCapALst.s:
            if i.dept == d:
                return i.cap
        raise KeyError
