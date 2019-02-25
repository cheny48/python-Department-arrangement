## @file SALst.py
# @author Seva Skvortsov
# @brief SALst
# @date 08/02/2019
from StdntAllocTypes import *
from AALst import *
from DCapALst import *


## @brief local tuple class to represent a student
class __StudentT__(NamedTuple):
    macid: str
    info: SInfoT


## @brief An abstract object to represent the Student Association List
class SALst:
    @staticmethod
    ## @brief local function to get gpa of a student
    # @param m string representing macid of student
    # @param s list of students
    # @return gpa of the student
    def ___get_gpa__(m, s):
        for i in s:
            if i.macid == m:
                return (i.info).gpa

    @staticmethod
    ## @brief initialize the list
    def init():
        SALst.s = []

    @staticmethod
    ## @brief adds a student to the list
    # @exception throws KeyError if student already in list
    # @param m string representing macid
    # @param i student information of type SInfoT
    def add(m, i):
        for t in SALst.s:
            if t.macid == m:
                raise KeyError
        newstudent = __StudentT__(m, i)
        SALst.s = SALst.s + [newstudent]

    @staticmethod
    ## @brief removes a student from the list
    # @exception throws KeyError if student not in list
    # @param m string representing macid of student to remove
    def remove(m):
        raise_e = True
        for i in SALst.s:
            if i.macid == m:
                raise_e = False
                SALst.s.remove(i)
        if raise_e:
            raise KeyError

    @staticmethod
    ## @brief tells you if a student is in the list
    # @param m string representing macid of student
    # @return True if student in list False if he is not
    def elm(m):
        for i in SALst.s:
            if i.macid == m:
                return True
        return False

    @staticmethod
    ## @brief tells you info of a student
    # @exception throws KeyError if student not in list
    # @param m string representing macid of student
    # @return info of the student of type SInfoT
    def info(m):
        for i in SALst.s:
            if i.macid == m:
                return i.info
        raise KeyError

    @staticmethod
    ## @brief sorts student by gpa and a function
    # @param f is the condition all student info (type SInfoT) has to pass
    # @return a list of macids sorted from highest to lowest gpa which passed condition
    def sort(f):
        outputlist = []
        for i in SALst.s:
            if f(i.info):
                outputlist = outputlist + [i]
        outputlist.sort(key=lambda i: i.info.gpa, reverse=True)

        outputlist = [i.macid for i in outputlist]
        return outputlist

    @staticmethod
    ## @brief calculates the average of a subset of the list of students
    # @exception Throws ValueError if no student passed the condition
    # @param f is the condition all student info (type SInfoT) has to pass
    # @return the GPA average of the subset of students
    def average(f):
        studentlist = []
        for i in SALst.s:
            if f(i.info):
                studentlist = studentlist + [i]
        if studentlist == []:
            raise ValueError
        else:
            gpa_sum = 0
            number_of_students = 0
            for i in studentlist:
                gpa_sum += i.info.gpa
                number_of_students += 1
            return gpa_sum / number_of_students

    ## @brief allocate all student from SALst object to AALst object
    # @exception throws RuntimeError if cannot allocate a student
    def allocate():
        AALst.init()
        f = SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0)
        for m in f:
            ch = SALst.info(m).choices
            AALst.add_stdnt(ch.next(), m)
        s = SALst.sort(lambda t: (not (t.freechoice)) and t.gpa >= 4.0)
        for m in s:
            ch = SALst.info(m).choices
            alloc = False
            while ((not alloc) and (not ch.end())):
                d = ch.next()
                if AALst.num_alloc(d) < DCapALst.capacity(d):
                    AALst.add_stdnt(d, m)
                    alloc = True
            if not alloc:
                raise RuntimeError
