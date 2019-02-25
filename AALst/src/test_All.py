from SeqADT import *
import StdntAllocTypes
from AALst import *
from DCapALst import *
from SALst import *
from Read import *

from pytest import *

class TestSeqADT:
    def test_start(self):
        dept = ['civil', 'chemical', 'electrical', 'mechanical',
                     'software', 'materials', 'engphys']
        seqA = SeqADT(dept)
        seqA.start()
        assert seqA.i == 0

    def test_next(self):
        dept = ['civil', 'chemical', 'electrical', 'mechanical',
                     'software', 'materials', 'engphys']
        seqA = SeqADT(dept)
        element = seqA.next()
        assert seqA.i == 1
        assert element == 'civil'

#boundary value
    def test_next(self):
        dept = ['civil']
        seqA = SeqADT(dept)
        element = seqA.next()
        assert seqA.i == 1
        assert element == 'civil'


    def test_next_StopIteration_exception(self):
        dept = ['civil']
        seqA = SeqADT(dept)
        element = seqA.next()
        with raises(StopIteration):
            element = seqA.next()

    def test_end_not(self):
        dept = ['civil', 'chemical', 'electrical', 'mechanical',
                     'software', 'materials', 'engphys']
        seqA = SeqADT(dept)
        element = seqA.next()
        assert not seqA.end()

    def test_end(self):
        dept = ['civil']
        seqA = SeqADT(dept)
        element = seqA.next()
        assert seqA.end()


class TestDCapALst:
    def test_constructor_s(self):
        DCapALst.init()
        assert DCapALst.s == {}

    def test_add(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        DCapALst.add(DeptT.chemical, 4)
        assert DCapALst.s[DeptT.civil] == 2
        assert DCapALst.s[DeptT.chemical] == 4

    def test_add_KeyError_exception(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        with raises(KeyError):
            DCapALst.add(DeptT.civil, 2)

# when n is different
    def test_add_KeyError_exception_number(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        with raises(KeyError):
            DCapALst.add(DeptT.civil, 4)

    def test_remove(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        DCapALst.add(DeptT.chemical, 2)
        DCapALst.remove(DeptT.civil)
        assert not DCapALst.elm(DeptT.civil)

    def test_remove_KeyError_exception(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        with raises(KeyError):
            DCapALst.remove(DeptT.chemical)

    def test_elm(self):
        DCapALst.init()
        DCapALst.add(DeptT.chemical, 2)
        assert DCapALst.elm(DeptT.chemical)
        assert not DCapALst.elm(DeptT.civil)

    def test_capacity(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        DCapALst.add(DeptT.chemical, 4)
        assert DCapALst.capacity(DeptT.civil) == 2
        assert DCapALst.capacity(DeptT.chemical) == 4


    def test_capacity_KeyError_exception(self):
        DCapALst.init()
        DCapALst.add(DeptT.civil, 2)
        with raises(KeyError):
            cap = DCapALst.capacity(DeptT.chemical)


class TestSALst:
    def test_constructor_s(self):
        SALst.init()
        assert SALst.s == {}

    def test_add(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        sinfo2 = SInfoT("first", "last", GenT.female, 8.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        assert SALst.s["stdnt1"] == sinfo1
        assert SALst.s["stdnt2"] == sinfo2

    def test_add_KeyError_exception(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        with raises(KeyError):
            SALst.add("stdnt1", sinfo1)

# when i is different
    def test_add_KeyError_exception_macid(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        sinfo2 = SInfoT("dthhd", "dthdt", GenT.female, 8.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        SALst.add("stdnt1", sinfo1)
        with raises(KeyError):
            SALst.add("stdnt1", sinfo2)

    def test_remove(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        sinfo2 = SInfoT("dthdt", "dthdt", GenT.female, 8.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.remove("stdnt1")
        assert not SALst.elm("stdnt1")

    def test_remove_KeyError_exception(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        with raises(KeyError):
            SALst.remove("stdnt2")

    def test_elm(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        assert SALst.elm("stdnt1")
        assert not SALst.elm("stdnt2")

    def test_info(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        assert SALst.info("stdnt1").fname == "first"
        assert SALst.info("stdnt1").lname == "last"
        assert SALst.info("stdnt1").gender == GenT.male
        assert SALst.info("stdnt1").gpa == 12.0
        assert SALst.info("stdnt1").choices.next() == DeptT.civil
        assert SALst.info("stdnt1").choices.next() == DeptT.chemical
        assert SALst.info("stdnt1").freechoice == True


    def test_info_KeyError_exception(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 12.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        SALst.add("stdnt1", sinfo1)
        with raises(KeyError):
            SALst.info("stdnt2")

    def test_sort(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 8.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        sinfo2 = SInfoT("srgseg", "lahdtst", GenT.female, 12.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        sinfo3 = SInfoT("fufahf", "aijsf", GenT.female, 2.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        sinfo4 = SInfoT("aggsg", "aijsagsgf", GenT.female, 6.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),False)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt3", sinfo3)
        SALst.add("stdnt4", sinfo4)
        assert SALst.sort(lambda t: t.freechoice) == ['stdnt2', 'stdnt1', 'stdnt3']
        assert SALst.sort(lambda t: t.gpa >= 4.0) == ['stdnt2', 'stdnt1', 'stdnt4']
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ['stdnt2', 'stdnt1']

    def test_average(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.male, 8.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        sinfo2 = SInfoT("sgrg", "srgsgs", GenT.female, 12.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        sinfo3 = SInfoT("fufahf", "aijsf", GenT.female, 2.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        sinfo4 = SInfoT("aggsg", "aijsagsgf", GenT.female, 6.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),False)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt3", sinfo3)
        SALst.add("stdnt4", sinfo4)
        assert SALst.average(lambda x: x.gender == GenT.male) == 8.0
        assert SALst.average(lambda x: x.gender == GenT.female) == (12.0 + 2.0 + 6.0)/3
        assert SALst.average(lambda t: t.gpa >= 4.0) == (8.0 + 12.0 + 6.0)/3


    def test_average_ValueError_exception_empty(self):
        SALst.init()
        with raises(ValueError):
            average = SALst.average(lambda x: x.gender == GenT.male)


    def test_average_ValueError_exception_noMale(self):
        SALst.init()
        sinfo1 = SInfoT("first", "last", GenT.female, 8.0,
                        SeqADT([DeptT.civil, DeptT.chemical]), True)
        sinfo2 = SInfoT("sgrg", "srgsgs", GenT.female, 12.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        sinfo3 = SInfoT("fufahf", "aijsf", GenT.female, 2.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),True)
        sinfo4 = SInfoT("aggsg", "aijsagsgf", GenT.female, 6.0,
              SeqADT([DeptT.materials, DeptT.engphys, DeptT.electrical]),False)
        SALst.add("stdnt1", sinfo1)
        SALst.add("stdnt2", sinfo2)
        SALst.add("stdnt3", sinfo3)
        SALst.add("stdnt4", sinfo4)
        with raises(ValueError):
            average = SALst.average(lambda x: x.gender == GenT.male)

    def test_sort_with_Read(self):
        load_stdnt_data("src/StdntData.txt")
        load_dcap_data("src/DeptCap.txt")
        assert SALst.sort(lambda t: t.freechoice) == ['macid1', 'brownc']
        assert SALst.sort(lambda t: t.gpa >= 4.0) == ['smithj', 'macid1', 'smithj2']
        assert SALst.sort(lambda t: t.freechoice and t.gpa >= 4.0) == ['macid1']

    def test_average_with_Read(self):
        load_stdnt_data("src/StdntData.txt")
        load_dcap_data("src/DeptCap.txt")
        assert SALst.average(lambda x: x.gender == GenT.male) == 6.699999999999999
        assert SALst.average(lambda x: x.gender == GenT.female) == 10.0
        assert SALst.average(lambda t: t.gpa >= 4.0) == (9.2 + 10.0 + 7.0)/3


    def test_allocate(self):
        AALst.init()
        load_stdnt_data("src/StdntData.txt")
        load_dcap_data("src/DeptCap.txt")
        expected = {'engphys': [], 'civil': ['smithj'], 'chemical': [],
                    'materials': [], 'electrical': [],
                    'mechanical': ['smithj2'], 'software': ['macid1']}
        SALst.allocate()
        assert AALst.s == expected

    def test_allocate(self):
        AALst.init()
        load_stdnt_data("src/student_data_small.txt")
        load_dcap_data("src/DeptCap2.txt")
        expected = {'engphys': [], 'civil': ['24ut9', 'b5vqg'],
                    'chemical': ['15vmp'], 'materials': ['k6loe'],
                     'electrical': ['9zsun'], 'mechanical': ['gjbrd', 'ufw30'],
                     'software': []}
        SALst.allocate()
        assert AALst.s == expected

    def test_allocate_RuntimeError_exception(self):
        AALst.init()
        load_stdnt_data("src/student_data_small.txt")
        load_dcap_data("src/DeptCap3.txt")
        with raises(RuntimeError):
            SALst.allocate()
