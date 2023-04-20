"""
Tests for our array class
"""

from array_class import Array

def test_str_1d():
    shape = (4,)
    strArray = Array(shape, 1, 2, 3, 4)
    boolArray = Array(shape, True, False, True, True)
    floatArray = Array(shape, 1.5, 2.3, 4.6, 7.8)

    assert str(strArray) == "[1, 2, 3, 4]"
    assert str(boolArray) == "[True, False, True, True]"
    assert str(floatArray) == "[1.5, 2.3, 4.6, 7.8]"

"""
Every arethmetic test will include arrays of both int and float. The tests will check if it's possible to 
do arethmetic operations with two arrays, one array and an integer, one array and a float in 
different combinations. The tests will also test if r-methods work as they should. In addition 
there is tests to see if its possible to do operations with objects of two different 
types as in Numpy (f.eks: array[1, 2, 3] + 2.5 = [3.5, ...]) 
"""

def test_add_1d():

    """
    Testing __add__ and __radd__ from array_class.py
    """
    shape = (4,)
    intNumb = 5
    floatNumb = 10.5

    intArray1 = Array(shape, 2, 3, 1, 0)
    intArray2 = Array(shape, 10, 20, 30, 40)

    floatArray1 = Array(shape, 10.5, 20.2, 30.3, 40.4)
    floatArray2 = Array(shape, 20.5, 30.2, 40.3, 50.4)
   
    assert intArray1 + intArray2 == Array(shape, 12, 23, 31, 40)
    assert intArray2 + intArray1 == Array(shape, 12, 23, 31, 40)
    assert intArray1 + intNumb == Array(shape, 7, 8, 6, 5)
    assert intNumb + intArray1 == Array(shape, 7, 8, 6, 5)
    assert intArray1 + floatNumb == Array(shape, 12.5, 13.5, 11.5, 10.5)
    assert floatNumb + intArray1 == Array(shape, 12.5, 13.5, 11.5, 10.5)
    assert floatArray1 + floatArray2 == Array(shape, 31.0, 50.4, 70.6, 90.8)
    assert floatArray2 + floatArray1 == Array(shape, 31.0, 50.4, 70.6, 90.8)
    assert intArray1 + floatArray1 == Array(shape, 12.5, 23.2, 31.3, 40.4)
    assert floatArray1 + intArray1 == Array(shape, 12.5, 23.2, 31.3, 40.4)
    assert floatArray1+intNumb == Array(shape, 15.5, 25.2, 35.3, 45.4)
    assert intNumb+floatArray1 == Array(shape, 15.5, 25.2, 35.3, 45.4)
    assert floatArray1+floatNumb == Array(shape,21.0, 30.7, 40.8, 50.9 )
    assert floatNumb+floatArray1 == Array(shape, 21.0, 30.7, 40.8, 50.9)

def test_sub_1d():
    """
    Testing __sub__ and __rsub__ from array_class.py
    """
    shape = (4,)
    intNumb = 5
    floatNumb = 10.5

    intArray1 = Array(shape, 2, 3, 1, 0)
    intArray2 = Array(shape, 10, 20, 30, 40)

    floatArray1 = Array(shape, 10.5, 20.2, 30.4, 40.4)
    floatArray2 = Array(shape, 20.5, 30.2, 40.4, 50.4)

    assert intArray1 - intArray2 == Array(shape, -8, -17, -29, -40)
    assert intArray2 - intArray1 == Array(shape, 8, 17, 29, 40)
    assert intArray1 - intNumb == Array(shape, -3, -2, -4, -5)
    assert intNumb - intArray1 == Array(shape, 3, 2, 4, 5)
    assert intArray1 - floatNumb == Array(shape, -8.5, -7.5, -9.5, -10.5)
    assert floatNumb - intArray1 == Array(shape, 8.5, 7.5, 9.5, 10.5)
    assert floatArray1 - floatArray2 == Array(shape, -10.0, -10.0, -10.0, -10.0)
    assert floatArray2 - floatArray1 == Array(shape, 10.0, 10.0, 10.0, 10.0)
    assert intArray1 - floatArray1 == Array(shape,-8.5, -17.2, -29.4, -40.4)
    assert floatArray1 - intArray1 == Array(shape, 8.5, 17.2, 29.4, 40.4)
    assert floatArray1 - floatNumb == Array(shape, 0.0, 9.7, 19.9, 29.9)
    assert floatNumb - floatArray1 == Array(shape, 0.0, -9.7, -19.9, -29.9)
    assert intNumb-floatArray1 == Array(shape, -5.5, -15.2, -25.4, -35.4 )
    assert floatArray1 - intNumb == Array(shape,5.5, 15.2, 25.4, 35.4 )
   

def test_mul_1d():
    """
    Testing __mul__ and __rmul__ from array_class.py
    """
    shape = (4,)
    intNumb = 2
    floatNumb = 2.5

    intArray1 = Array(shape, 2, 3, 1, 0)
    intArray2 = Array(shape, 10, 20, 30, 40)

    floatArray1 = Array(shape, 2.5, 3.5, 1.5, 0.5)
    floatArray2 = Array(shape, 3.5, 4.5, 5.5, 1.5)

    assert intArray1*intArray2 == Array(shape, 20, 60, 30, 0)
    assert intArray2*intArray1 == Array(shape, 20, 60, 30, 0)
    assert floatArray1*floatArray2 == Array(shape, 8.75, 15.75, 8.25, 0.75)
    assert floatArray2*floatArray1 == Array(shape, 8.75, 15.75, 8.25, 0.75)
    assert intArray1*floatArray1 == Array(shape, 5.0, 10.5, 1.5, 0.0)
    assert floatArray1*intArray1 == Array(shape, 5.0, 10.5, 1.5, 0.0)
    assert intArray1*intNumb == Array(shape, 4, 6, 2, 0)
    assert intNumb*intArray1 == Array(shape, 4, 6, 2, 0)
    assert intArray1*floatNumb == Array(shape, 5.0, 7.5, 2.5, 0.0)
    assert floatNumb*intArray1 == Array(shape, 5.0, 7.5, 2.5, 0.0)
    assert floatArray1*intNumb == Array(shape,5.0, 7.0, 3.0, 1.0)
    assert intNumb*floatArray1 == Array(shape,5.0, 7.0, 3.0, 1.0)
    assert floatArray1*floatNumb == Array(shape,6.25, 8.75, 3.75, 1.25)
    assert floatNumb*floatArray1 == Array(shape,6.25, 8.75, 3.75, 1.25)

def test_eq_1d():
    """
    Testing __eq__ from array_class.py
    """
    intNumb = 5
    floatNumb = 5.5
    boolean = True
    shape = (4, )
    eqArray1 = Array(shape, 1, 2, 3, 4)
    eqArray2 = Array(shape, 1, 2, 3, 4)
    eqArray222 = Array(shape, 1, 2, 1, 1)

    shape2 = (5,)
    eqArray3 = Array(shape2, 3.3, 2.3, 4.2, 5.4, 6.3)
    eqArray4 = Array(shape2, 3.3, 2.3, 4.2, 5.4, 6.3)
    eqArray5 = Array(shape2, True, False, True, False, True)
    
    assert eqArray1 == eqArray2
    assert eqArray2 == eqArray1
    assert eqArray3 == eqArray3
    assert eqArray3 == eqArray4
    assert eqArray4 == eqArray3
    assert eqArray3 != eqArray5
    assert eqArray1 != eqArray5
    assert eqArray1 != intNumb
    assert intNumb != eqArray1
    assert eqArray1 != floatNumb
    assert floatNumb != eqArray1
    assert eqArray1 != boolean
    assert boolean != eqArray1
    assert eqArray1 != eqArray3
    assert eqArray3 != eqArray1


def test_same_1d():
    """
    Testing is_equal() from array_class.py
    """
    shape = (4,)
    intNumb = 4
    floatNumb = 3.4
    boolList = [True, True, False, True]
    boolList2 = [False, True, True, False]
    boolList3 = [False, False, True, True]
    boolList4 = [False, False, True, False]
    sameArray1 = Array(shape, 1, 2, 4, 4)
    sameArray2 = Array(shape, 1, 2, 3, 4)
    sameArrayFloat1 = Array(shape, 1.2, 2.3, 3.4, 4.5)
    sameArrayFloat2 = Array(shape, 2.3, 2.3, 3.4, 4.6)
    assert sameArray1.is_equal(sameArray2) == boolList
    assert sameArray2.is_equal(sameArray1) == boolList
    assert sameArrayFloat1.is_equal(sameArrayFloat2) == boolList2
    assert sameArrayFloat2.is_equal(sameArrayFloat1) == boolList2
    assert sameArray1.is_equal(intNumb) == boolList3
    assert sameArrayFloat1.is_equal(floatNumb) == boolList4

def test_smallest_1d():
    """
    Testing min_element() from array_class.py
    """
    shape = (4,)
    sameArray1 = Array(shape, 10, 20, 5, 30)
    sameArray2 = Array(shape, 2.3, 100.23, 55.8, 0.3)

    assert sameArray1.min_element() == 5
    assert sameArray2.min_element() == 0.3

def test_mean_1d():
    """
    Testing mean_element() from array_class.py
    """
    shape = (4,)
    meanArray1 = Array(shape, 1, 2, 3, 4)
    meanArray2 = Array(shape, 2.3, 10.4, 5.8, 1.3)

    assert meanArray1.mean_element() == 2.5
    assert meanArray2.mean_element() == 4.95

# 2D tests (Task 6)

def test_add_2d():
    """
    Testing __add__ and __radd__ from array_class.py with 2d-array
    """
    shape2d = (3,2)
    intNumb = 10
    floatNumb = 5.5
    
    intArray1 = Array(shape2d, 1, 2, 3, 4, 5, 6)
    intArray2 = Array(shape2d, 1, 2, 3, 4, 5, 6)
    
    floatArray1 = Array(shape2d, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5)
    floatArray2 = Array(shape2d, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5)

    assert intArray1 + intArray2 ==  Array(shape2d, 2, 4, 6, 8, 10, 12)
    assert intArray2 + intArray1 ==  Array(shape2d, 2, 4, 6, 8, 10, 12)
    assert intArray1 + floatArray1 == Array(shape2d, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5)
    assert floatArray1 + intArray1 == Array(shape2d, 2.5, 4.5, 6.5, 8.5, 10.5, 12.5)
    assert intArray1 + intNumb == Array(shape2d, 11,12,13,14,15,16)
    assert intNumb + intArray1 == Array(shape2d, 11,12,13,14,15,16)
    assert intArray1 + floatNumb == Array(shape2d, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5)
    assert floatNumb + intArray1 == Array(shape2d, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5)
    assert floatArray1 + floatArray2 == Array(shape2d, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0)
    assert floatArray2 + floatArray1 == Array(shape2d, 4.0, 6.0, 8.0, 10.0, 12.0, 14.0)
    assert floatArray1+intNumb == Array(shape2d, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5)
    assert intNumb+floatArray1 == Array(shape2d, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5)
    assert floatArray1+floatNumb == Array(shape2d, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0)
    assert floatNumb+floatArray1 == Array(shape2d, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0)


    
def test_mult_2d():
    """
    Testing __mul__ and __rmul__ from array_class.py with 2d-array
    """
    shape2d = (3,2)
    intNumb = 2
    floatNumb = 3.5

    intArray1 = Array(shape2d, 1, 2, 3, 4, 5, 6)
    intArray2 = Array(shape2d, 2, 3, 4, 5, 6, 7)

    floatArray1 = Array(shape2d, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5)
    floatArray2 = Array(shape2d, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5)
    
    assert intArray1*intArray2 == Array(shape2d, 2, 6, 12, 20, 30, 42)
    assert intArray2*intArray1 == Array(shape2d, 2, 6, 12, 20, 30, 42)
    assert floatArray1*floatArray2 == Array(shape2d, 8.75, 15.75, 24.75, 35.75, 48.75, 63.75)
    assert floatArray2*floatArray1 == Array(shape2d, 8.75, 15.75, 24.75, 35.75, 48.75, 63.75)
    assert floatArray1*intArray1 == Array(shape2d, 2.5, 7.0, 13.5, 22.0, 32.5, 45.0)
    assert intArray1*floatArray1 == Array(shape2d, 2.5, 7.0, 13.5, 22.0, 32.5, 45.0)
    assert intArray1*intNumb == Array(shape2d, 2, 4, 6, 8, 10, 12)
    assert intNumb*intArray1 == Array(shape2d, 2, 4, 6, 8, 10, 12)
    assert intArray1*floatNumb == Array(shape2d, 3.5, 7.0, 10.5, 14.0, 17.5, 21.0 )
    assert floatNumb*intArray1 == Array(shape2d, 3.5, 7.0, 10.5, 14.0, 17.5, 21.0 )
    assert floatArray1*intNumb == Array(shape2d,5.0, 7.0, 9.0, 11.0, 13.0, 15.0)
    assert intNumb*floatArray1 == Array(shape2d,5.0, 7.0, 9.0, 11.0, 13.0, 15.0)
    assert floatArray1*floatNumb == Array(shape2d, 8.75, 12.25, 15.75, 19.25, 22.75, 26.25)
    assert floatNumb*floatArray1 == Array(shape2d, 8.75, 12.25, 15.75, 19.25, 22.75, 26.25)


def test_same_2d():
    """
    Testing is_equal() from array_class.py with 2d-array
    """
    shape = (3,3)
    boolList = [True, True, False, True, False, True, True, False, True]
    boolList2 = [True, True, True, False, False, True, False, False, False]
    sameArray1 = Array(shape, 1, 2, 3, 3, 4, 5, 6, 6, 8)
    sameArray2 = Array(shape, 1, 2, 4, 3, 5, 5, 6, 2, 8)

    sameArrayFloat1 = Array(shape, 1.2, 2.3, 3.4, 4.5, 5.6, 6.7, 7.8, 8.9, 9.9)
    sameArrayFloat2 = Array(shape, 1.2, 2.3, 3.4, 2.3, 1.2, 6.7, 1.5, 9.9, 8.9)
    
    assert sameArray1.is_equal(sameArray2) == boolList
    assert sameArrayFloat1.is_equal(sameArrayFloat2) == boolList2

def test_mean_2d():
    """
    Testing mean_element() from array_class.py with 2d-array
    """
    shape2d = (4,2)
    meanArray1 = Array(shape2d, 1, 2, 3, 4, 5, 6, 7, 8)
    meanArray2 = Array(shape2d, 2.3, 10.4, 5.8, 1.3, 3.4, 5.6, 7.4, 9.3)

    assert meanArray1.mean_element() == 4.5
    assert meanArray2.mean_element() == 5.6875

if __name__ == "__main__":
    """
    Note: Write "pytest" in terminal in the same folder as this file is in to run all tests
    (or run them manually by running this file).
    Make sure to have pytest installed (pip install pytest, or install anaconda).
    """

    # Task 4: 1d tests
    test_str_1d()
    test_add_1d()
    test_sub_1d()
    test_mul_1d()
    test_eq_1d()
    test_mean_1d()
    test_same_1d()
    test_smallest_1d()

    # Task 6: 2d tests
    test_add_2d()
    test_mult_2d()
    test_same_2d()
    test_mean_2d()
