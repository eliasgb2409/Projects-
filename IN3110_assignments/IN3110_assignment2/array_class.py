"""
Array class for assignment 2
"""

from itertools import chain

class Array:

    def __init__(self, shape, *values):

        """Initialize an array of 1-dimensionality. Elements can only be of type:

        - int
        - float
        - bool

        Make sure the values and shape are of the correct type.

        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).

        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either int, float or boolean.

        Raises:
            TypeError: If "shape" or "values" are of the wrong type.
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """

        # Check if the values are of valid types

        # Check that the amount of values corresponds to the shape

        # Set class-variables
        
        self.shape = shape
        self.values = values
        self.array = []

        """
        Checking if shape is of wrong value. 

        Raise TypeError if not valid input for shape. 
        """
        if not (isinstance(self.shape, tuple)):
            raise TypeError("Shape input not tuple")

        for item in self.shape: 
            if not isinstance(item, int):
                raise TypeError("Not valid input value.")

        """
        Checking if values are of wrong value 
        """
        for value in self.values:
            if not (isinstance(value, int) or isinstance(value, float) or isinstance(value, bool)): 
               raise TypeError("Not correct value type.")
       
        """
        Checking if values are of the same type
        """
        for value in self.values:
            valueType = type(value)
            if not all(isinstance(elem, valueType) for elem in self.values): 
                raise ValueError("Values are not of all of the same type.") 

        # 2D-array: 
        if len(self.shape) > 1:
            if len(values) != int(self.shape[0]*self.shape[1]):
                raise ValueError("Values do not fit array shape.")
            counter = 0
            for i in range(self.shape[0]):
                self.array.append(list())
            counterIndex = 0
            for value in self.values:
                self.array[counterIndex].append(value)
                counter += 1
                if counter == self.shape[1]:
                    counterIndex += 1
                    counter = 0
        # 1D-array
        else:
            if len(values) != int(self.shape[0]):
                raise ValueError("Values do not fit array shape.")
            for value in self.values:
                self.array.append(value)

    def __getitem__(self, index):
        """
        Returns element in given index

        Returns: int, float or boolean (depends on what Array-type)
        """
        return self.array[index]

    def __str__(self): 
       
        """Returns a nicely printable string representation of the array.

        Returns:
            str: A string representation of the array.
        """
        returnString = (str(self.array))

        return returnString


    def __add__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
  
        #If number is either int or float - we add the number with the elemens in the array

        if isinstance(other, int) or isinstance(other, float): 
            values = [elem + other for elem in self.flat_array()]

        #If the the other-parameter is an array we add each element together.
        #The logic for the two if checks for int, float and array is the same in the other mathematical 
        #functions, just with different math symboles.

        elif isinstance(other, Array):
            if(self.shape != other.shape):
                raise ValueError("Arrays not same shape.")
            for elem in other:
                if isinstance(elem, bool):
                    return NotImplemented
            values = [sum(elems) for elems in zip(self.flat_array(), other.flat_array())]

        else:
            return NotImplemented

        return Array(self.shape, *values)
        # check that the method supports the given arguments (check for data type and shape of array)
        # if the array is a boolean you should return NotImplemented
        
        

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to add element-wise to this array.

        Returns:
            Array: the sum as a new array.

        """
        return self.__add__(other)

    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.

        Returns:
            Array: the difference as a new array.

        """

        if isinstance(other, int) or isinstance(other, float):
            values = [elem - other for elem in self.flat_array()]

        elif isinstance(other, Array):
            if(self.shape != other.shape):
                raise ValueError("Arrays not same shape.")
            for elem in other:
                if isinstance(elem, bool):
                    return NotImplemented
            values = [array1 - array2 for array1, array2 in zip(self.flat_array(), other.flat_array())]

        else:
            return NotImplemented
        
        return Array(self.shape, *values)

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number being subtracted from.

        Returns:
            Array: the difference as a new array.

        """
        if isinstance(other, int) or isinstance(other, float):
            values = [other - elem for elem in self.flat_array()]
        else:
            return NotImplemented
        return Array(self.shape, *values)


    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        if isinstance(other, int) or isinstance(other, float):
            values = [element * other for element in self.flat_array()]

        elif isinstance(other, Array):
            if(self.shape != other.shape):
                raise ValueError("Arrays not same shape.")
            for elem in other:
                if isinstance(elem, bool):
                    return NotImplemented
            values = [array1 * array2 for array1, array2 in zip (self.flat_array(), other.flat_array())]

        else:
            return NotImplemented

        return Array(self.shape, *values)

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.

        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.

        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.

        Returns:
            Array: a new array with every element multiplied with `other`.

        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.

        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.

        Args:
            other (Array): The array to compare with this array.

        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.

        """
        if not(isinstance(other,Array)):
            return False
        elif self.flat_array() == other.flat_array():
            return True
        return False

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.

        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.

        Args:
            other (Array, float, int): The array or number to compare with this array.

        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.

        Raises:
            ValueError: if the shape of self and other are not equal.

        """

        booleanList = []
        teller = 0

        if isinstance(other, int) or isinstance(other, float):
            for elem in self.flat_array(): 
                if elem == other:
                    booleanList.append(True)
                else:
                    booleanList.append(False)

        elif isinstance(other, Array):
            if other.shape != self.shape:
                raise ValueError("Not the same shape.")
            for elem in self.flat_array():
                if elem == other.flat_array()[teller]:
                    booleanList.append(True)
                else:
                    booleanList.append(False)
                teller += 1

        else:
            raise TypeError("Not an array or number.")

        return booleanList

    def min_element(self):
        """Returns the smallest value of the array.

        Only needs to work for type int and float (not boolean).

        Returns:
            float: The value of the smallest element in the array.

        """
        minElem = self.flat_array()[0]
        for elem in self.flat_array():
            if elem < minElem:
                minElem = elem
        return float(minElem)

    def mean_element(self):
        """Returns the mean value of an array

        Only needs to work for type int and float (not boolean).

        Returns:
            float: the mean value
        """

        allNumbers = 0

        for elem in self.flat_array():
            allNumbers += elem
        
        meanNumber = allNumbers/len(self.values)

        return float(meanNumber)

    def flat_array(self):
        """Flattens the N-dimensional array of values into a 1-dimensional array.
        Returns:
            list: flat list of array values.
        """
        flat_array = self.array
        for _ in range(len(self.shape[1:])):
            flat_array = list(chain(*flat_array))
        return flat_array
