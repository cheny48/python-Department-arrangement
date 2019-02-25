## @file StdntAllocTypes.py
#  @author Yujing Chen
#  @brief recording needed data and data type
#  @date 02/11/2019
from SeqADT import *


## @brief data for Gender
class GenT:

    male = "male"
    female = "female"


## @brief data for DeptT
class DeptT:

    civil = "civil"
    chemical = "chemical"
    electrical = "electrical"
    mechanical = "mechanical"
    software = "software"
    materials = "materials"
    engphys = "engphys"


## @brief structure type of SInfoT
class SInfoT:

    def __init__(self, fname, lname, gender, gpa, choices, freechoice):
        self.fname = fname
        self.lname = lname
        self.gender = gender
        self.gpa = float(gpa)
        self.choices = choices
        self.freechoice = freechoice
