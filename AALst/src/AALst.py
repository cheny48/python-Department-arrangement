## @file AALst.py
#  @author Yujing Chen
#  @brief create the AALst for the program
#  @date 02/11/2019
import StdntAllocTypes


class AALst:

    s = {}

    ## @brief initialize the AALst
    #  @param N/A
    #  @details create the AALst in the form of {deparment: []}
    #  @return N/A
    @staticmethod
    def init():
        AALst.s = {}
        AALst.s["civil"] = []
        AALst.s["materials"] = []
        AALst.s["chemical"] = []
        AALst.s["electrical"] = []
        AALst.s["mechanical"] = []
        AALst.s["software"] = []
        AALst.s["engphys"] = []

    ## @brief add student to the AALst list
    #  @param dep department
    #  @param m student id
    #  @return N/A
    @staticmethod
    def add_stdnt(dep, m):
        if dep in AALst.s:
            AALst.s[dep].append(m)

    ## @brief give the student list of a department
    #  @param d string of department
    #  @return return the student list that assign to a department
    @staticmethod
    def lst_alloc(dep):
        return AALst.s[dep]

    ## @brief give the student list length of a department
    #  @param d string of department
    #  @return the length of the student list
    @staticmethod
    def num_alloc(dep):
        return len(AALst.s[dep])
