# cs130 pa6
# Spencer Ochs (A10259423)

from misc import Failure

class Vector(object):
    """Class that implements a vector of fixed length which has a set of operations """
    def __init__(self, l):
        """constructor"""
        # check if l is int or long    
        if ( isinstance( l, int ) | isinstance( l, long ) ):
            if l < 0: raise ValueError('length cannot be negative')
            else: 
                self.length = l
                self.values = [0.0] * l # list of l zeroes
        else: # l not instance of int or long
            # using duck typing to check if l is iterable
            try:
                self.values = [x for x in l]
                self.length = len( self.values )
            except TypeError:
                print 'object needs to be either int, long, or iterable'

    def __repr__(self):
        """returns string representation of the vector"""
        return "Vector(" + str(self.values) + ")"         
    # Problem 1b
    def __len__(self):
        """returns the length of the vector"""
        return self.length
    def __iter__(self):
        """returns object that can be iterated over""" 
        # yield makes v return each time a next() is called
        for v in self.values:
            yield v
    # Problem 1c
    # + returns new vector that is result of element-wise addition
    def __add__(self, other):
        """implementation of the binary + operation"""
        result = []
        for s,o in zip(list(self), list(other)):
            result.append( s+o ) 
        return Vector(result)

    def __radd__(self, other):
        """implementation of the binary += when left operand doesn't support
        the operation"""
        result = []
        for s,o in zip(list(self), list(other)):
            result.append( s+o ) 
        return Vector(result)
    # += modifies self element-wise with addition of values in other 
    def __iadd__(self, other):
        """implementation of the binary += operation""" 
        self.values = Vector([s+o for s,o in zip(list(self), list(other))])
        return self.values
    # Problem 1d
    def dot(self, other):
        """Returns the dot product (sum of the componant-wise products)"""
        result = []
        for s,o in zip(list(self), list(other)):
            result.append( s*o )         
        return sum(result)
    # Problem 1e
    def __getitem__(self, key):
        """returns value at index key"""
        try:       
            if key >= self.length: raise IndexError
            else:
                if key < 0: key = self.length + key # index from back of list
                return self.values[key]
        except TypeError: 
            print 'key must be integer value'
    
    def __setitem__(self, key, value):
        """sets value at index"""
        try:       
            if key >= self.length: raise IndexError
            else:
                if key < 0: key = self.length + key # index from back of list
                self.values[key] = value
                return self.values
        except TypeError: 
            print 'key must be integer value'            
    # (1f)
    def __getslice__(self, i, j):
        """returns values within slice from i to j"""
        try:       
            if j >= self.length: raise IndexError
            if j < i: raise IndexError
            if i < 0: raise IndexError
            else:
                if j < 0: j = self.length + j # index from back of list
                return self.values[i:j]
        except TypeError: 
            print 'indexes must be integer values'  

    def __setslice__(self, i, j, sequence):
        """sets slice from i to j to sequence"""
        try:       
            if j >= self.length: raise IndexError
            if j < i: raise IndexError
            if i < 0: raise IndexError
            if len(sequence) > (j-i): raise ValueError
            else:
                if j < 0: j = self.length + j # index from back of list
                self.values[i:j] = sequence
                return self.values[i:j]
        except TypeError: 
            print 'indexes must be integer values'   

    # (1g)
    def __eq__(self, other):
        """implementation of the binary == operation """
        if not isinstance(other, Vector):
            # use regular comparison between objects
            return self == other
        if self.length != other.length: return False
        for s,o in zip( list(self), list(other) ):
            if s != o: return False
        return True   
 
    def __ge__(self, other):
        """implementation of the >= operation""" 
        if not isinstance(other, Vector):
            # use regular comparison between objects
            return self >= other
        # compare max values of self and other. If max values are the same then
        # remove from the set and check next biggest values. If self has a 
        # bigger max value, return True, if other has a bigger max return False
        selfSet = set(self.values)
        otherSet = set(other.values)
        biggestSetLength = max( len(selfSet), len(otherSet) )
        while biggestSetLength > 0:
            if max(selfSet) > max(otherSet): return True
            elif max(selfSet) == max(otherSet):
                maxVal = max(selfSet)
                selfSet.remove(maxVal)
                otherSet.remove(maxVal)
                biggestSetLength -= 1
            else: return False # other has bigger max val then self
        return True # all values from two vectors are the same
  
    def __gt__(self, other):
        """implementation of the > operation"""
        if not isinstance(other, Vector):
            # use regular comparison between objects
            return self > other
        # compare max values of self and other. If max values are the same then
        # remove from the set and check next biggest values. If self has a 
        # bigger max value, return True, if other has a bigger max return False
        selfSet = set(self.values)
        otherSet = set(other.values)
        biggestSetLength = max( len(selfSet), len(otherSet) )
        while biggestSetLength > 0:
            if max(selfSet) > max(otherSet): return True
            elif max(selfSet) == max(otherSet):
                maxVal = max(selfSet)
                selfSet.remove(maxVal)
                otherSet.remove(maxVal)
                biggestSetLength -= 1
            else: return False # other has bigger max val then self
        return False # all values from two vectors are the same    

    def __lt__(self, other):
        """ implementation of the < operation"""
        if not isinstance(other, Vector):
            # use regular comparison between objects
            return self < other  
        selfSet = set(self.values)
        otherSet = set(other.values)
        biggestSetLength = max( len(selfSet), len(otherSet) )
        while biggestSetLength > 0:
            if max(selfSet) < max(otherSet): return True
            elif max(selfSet) == max(otherSet):
                maxVal = max(selfSet)
                selfSet.remove(maxVal)
                otherSet.remove(maxVal)
                biggestSetLength -= 1
            else: return False # other has smaller max val then self
        return False # all values from two vectors are the same     

