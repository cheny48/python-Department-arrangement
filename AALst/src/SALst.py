## @file SALst.py
#  @author Yujing Chen
#  @brief create the SALst for the program
#  @date 02/11/2019
from AALst import *
from StdntAllocTypes import *
from DCapALst import *


class SALst:

    s = {}

    ## @brief initialize of SALst
    #  @return N/A
    @staticmethod
    def init():
        SALst.s = {}

    ## @brief add student information to SALst
    #  @param m the student id of the student
    #  @param i the SInfo of the student
    #  @return N/A
    #  @exception KeyError when element already in the list
    @staticmethod
    def add(m, i):
        for id in SALst.s:
            if id == m:
                raise KeyError
        SALst.s[m] = i

    ## @brief remove the student from the SALst
    #  @param m the student id of the student
    #  @return N/A
    #  @exception KeyError when element not in the list
    @staticmethod
    def remove(m):
        if m not in SALst.s:
            raise KeyError
        else:
            del SALst.s[m]

    ## @brief find if a student is in the SALst
    #  @param m the student id of the student
    #  @return true if the element in the list, false if not
    @staticmethod
    def elm(m):
        for id in SALst.s:
            if id == m:
                return True
            else:
                return False

    ## @brief return the student infomation of m
    #  @param m the student id of the student
    #  @return the coresponding student information
    #  @exception KeyError when element is not in the list
    @staticmethod
    def info(m):
        if m not in SALst.s:
            raise KeyError
        else:
            return SALst.s[m]

    ## @brief function to return student's gpa
    #  @param m the student id of m
    #  @return the gpa of m
    @staticmethod
    def get_gpa(m):
        return SALst.s[m].gpa

    ## @brief sorting student according to their gpa
    #  @param f the function that the student info need to satisfy
    #  @return the sorted list
    @staticmethod
    def sort(f):
        temp = []
        for i in SALst.s:
            if f(SALst.s[i]):
                gpa = SALst.get_gpa(i)
                temp.append((i, gpa))
        temp.sort(key=lambda x: x[1], reverse=True)
        sorted = []
        for i in temp:
            sorted.append(i[0])
        return sorted

    ## @brief calculate the average of a group of student
    #  @param f the function that a student info must satisfy
    #  @return average
    #  @exception ValueError when the list is empty
    @staticmethod
    def average(f):
        temp = []
        for i in SALst.s:
            if f(SALst.s[i]):
                gpa = SALst.get_gpa(i)
                temp.append((i, gpa))
        if len(temp) == 0:
            raise ValueError
        average = sum([i[1] for i in temp]) / len(temp)
        return average

    ## @brief allocate student to coresponding AALst
    #  @param N/A
    #  @return N/A
    #  @exception RuntimeError when a student can't be allocate
    @staticmethod
    def allocate():
        F = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in F:
            ch = SALst.s[m].choices
            AALst.add_stdnt(ch.next(), m)
        S = SALst.sort(lambda t: t.freechoice is False and t.gpa >= 4.0)
        for m in S:
            ch = SALst.s[m].choices
            alloc = False
            while alloc is False and ch.end() is False:
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if alloc is False:
                raise RuntimeError
