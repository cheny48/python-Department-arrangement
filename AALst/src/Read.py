## @file Read.py
#  @author Yujing Chen
#  @brief read the input data from serveral file
#  @date 02/11/2019
import StdntAllocTypes
from DCapALst import *
from SALst import *

import ast


## @brief read the student information from a file, and store it into SALst
#  @param s a string s corresponding to a filename
#  @return N/A
def load_stdnt_data(s):
    SALst.init()
    with open(s) as f:
        for line in f:
            (id, fname, lname, gender, gpa, choices,
             freechoice) = line.split(', ')
            choices = ast.literal_eval(choices)
            freechoice = ast.literal_eval(freechoice)
            student = SInfoT(fname, lname, gender, gpa,
                             SeqADT(choices), freechoice)
            SALst.add(id, student)


## @brief read the department depth information from a file
#  and add it into the DcapAlst
#  @param s a string s corresponding to a filename
#  @return N/A.
def load_dcap_data(s):
    DCapALst.init()
    with open(s) as f:
        for line in f:
            (key, val) = line.split(', ')
            DCapALst.add(key, int(val))
