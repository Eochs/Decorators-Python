from misc import Failure

class profiled(object):
    def __init__(self,f):
        self.__count=0
        self.__f=f
        self.__name__=f.__name__
    def __call__(self,*args,**dargs):
        self.__count+=1
        return self.__f(*args,**dargs)
    def count(self):
        return self.__count
    def reset(self):
        self.__count=0

"""
class traced(object):
    #prints out an ASCII art tree of the recursive calls (of the decorated function) and their return values
    def __init__(self,f):
        self.__count = 0 
        self.__f = f
        self.__name__= f.__name__
        self.__result = None

    def print_pipes(self, depth):
        #helper function that prints "depth" number of | at the beginning of each line
        string = ''
        for pipe in range(depth):
           string += '| '
        return string
    
    def __call__(self,*args,**dargs):
        s = self.print_pipes(self.__count) # prints the "| | | ..." at beginning
        s = s + ',-'
        argsString = ', '.join([repr(argument) for argument in args])
        dargsString = ', '.join([key + '=' + repr(value) for key, value in dargs.items()])
        print s + self.__name__ + "(" + argsString + dargsString +")"
        
        self.__count += 1
        
        result = self.__f(*args,**dargs) # call f on args         
        if result: # not None
            self.__result = result        
        
        # decreasing part of the art tree
        self.__count -= 1 # decrease on the way back down the art tree
        s = self.print_pipes(self.__count) # prints the "| | | ..." at beginning
        print s + ',-' + repr(self.__result)
 
        if self.__count == 0: # final line
            print repr(self.__result)
""" 


class traced(object):
    #prints out an ASCII art tree of the recursive calls (of the decorated function) and their return values
    __level = 0 # counts number of levels of the ascii art tree to print
    def __init__(self, f):
        # initialize traced object by storing function, name, and output string
        self.__f = f
        self.__name__ = f.__name__
        self.__out = ""

    # helper function for accessing levels variable. Returns number of times 
    # function has recursed
    def level(self):
        return self.__level

    def __call__(self, *args, **dargs):
        # print pipes for number of recursive calls
        for level in range(self.level()):
            print "| ", # out += "| "
        # print ",- [function name]( [arguments] )"
        out = ",- " + self.__name__ + "("
        out += ', '.join([repr(arg) for arg in args])
        out += ', '.join([key + '=' + repr(val) for key, val in dargs.items()])
        out += ")"
        print out 
        # increase the nesting level of ascii tree
        traced.__level += 1
        # call the function itself and catch any exceptions
        try:
            rv = self.__f(*args,**dargs)
            # keep calling function and writing new line of ascii art tree
            # until hit exception, or end of recursive function call. 
        except Exception:
            # nesting level adjusted down to level where exception is caught
            traced.__level -= 1
            raise ChangeException
        # on way back down the ascii tree, decreasing the levels and printing
        # the results of the respective function calls
        traced.__level -= 1
        for level in range(self.level()):
            print "| ",
            if(level == self.level() -1):
                print "`-" + repr(rv)
        # print last line "`- [result of function call]"
        if self.__level == 0:
            print "`-" + repr(rv)
            return rv
        # return rv (return value) for lines higher in ascii tree than last
        return rv


"""
class traced(object):

    def __init__(self,f):
        self.__f = f
        self.__name__= f.__name__
        self.__level = 0
        self.result = None

       
    #Helper function for printing the | at the start of each line
    def print_pipes(self, depth):
        out = ''
        for level in range(depth):
            out += '| '
        return out
 
    def __call__(self, *args, **dargs):
        # print line of function call with number of pipes representing depth
        # of recursion
        out = self.print_pipes(self.__level)
        out += ',-' + self.__name__ + '('
        out += ', '.join([repr(arg) for arg in args])
        out += ', '.join([key + '=' + repr(val) for key, val in dargs.items()])
        out += ')'
        print out
        # increase level of ascii tree
        self.__level += 1
        # call function again recursively
        result = self.__f(*args, **dargs)
        # if no exception is thrown and result comes from called f
        if result: # if result != None
            self.result = result
            
        self.__level -= 1
        # start printing the receding lines of the ascii tree with result values
        out = self.print_pipes(self.__level)
        out += '`- ' + repr(self.result)
        print out
        # if at very last level print resulting value from total calculation
        if self.__level == 0:
            print repr(self.result)
"""
       

class memoized(object):
    def __init__(self,f):
        # replace this and fill in the rest of the class
        self.__name__="NOT_IMPLEMENTED"

# run some examples.  The output from this is in decorators.out
def run_examples():
    for f,a in [(fib_t,(7,)),
                (fib_mt,(7,)),
                (fib_tm,(7,)),
                (fib_mp,(7,)),
                (fib_mp.count,()),
                (fib_mp,(7,)),
                (fib_mp.count,()),
                (fib_mp.reset,()),
                (fib_mp,(7,)),
                (fib_mp.count,()),
                (even_t,(6,)),
                (quicksort_t,([5,8,100,45,3,89,22,78,121,2,78],)),
                (quicksort_mt,([5,8,100,45,3,89,22,78,121,2,78],)),
                (quicksort_mt,([5,8,100,45,3,89,22,78,121,2,78],)),
                (change_t,([9,7,5],44)),
                (change_mt,([9,7,5],44)),
                (change_mt,([9,7,5],44)),
                ]:
        print "RUNNING %s(%s):" % (f.__name__,", ".join([repr(x) for x in a]))
        rv=f(*a)
        print "RETURNED %s" % repr(rv)

@traced
def fib_t(x):
    if x<=1:
        return 1
    else:
        return fib_t(x-1)+fib_t(x-2)

@traced
@memoized
def fib_mt(x):
    if x<=1:
        return 1
    else:
        return fib_mt(x-1)+fib_mt(x-2)

@memoized
@traced
def fib_tm(x):
    if x<=1:
        return 1
    else:
        return fib_tm(x-1)+fib_tm(x-2)

@profiled
@memoized
def fib_mp(x):
    if x<=1:
        return 1
    else:
        return fib_mp(x-1)+fib_mp(x-2)

@traced
def even_t(x):
    if x==0:
        return True
    else:
        return odd_t(x-1)

@traced
def odd_t(x):
    if x==0:
        return False
    else:
        return even_t(x-1)

@traced
def quicksort_t(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=quicksort_t([x for x in l[1:] if x<pivot])
    right=quicksort_t([x for x in l[1:] if x>=pivot])
    return left+l[0:1]+right

@traced
@memoized
def quicksort_mt(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=quicksort_mt([x for x in l[1:] if x<pivot])
    right=quicksort_mt([x for x in l[1:] if x>=pivot])
    return left+l[0:1]+right

class ChangeException(Exception):
    pass

@traced
def change_t(l,a):
    if a==0:
        return []
    elif len(l)==0:
        raise ChangeException()
    elif l[0]>a:
        return change_t(l[1:],a)
    else:
        try:
            return [l[0]]+change_t(l,a-l[0])
        except ChangeException:
            return change_t(l[1:],a)

@traced
@memoized
def change_mt(l,a):
    if a==0:
        return []
    elif len(l)==0:
        raise ChangeException()
    elif l[0]>a:
        return change_mt(l[1:],a)
    else:
        try:
            return [l[0]]+change_mt(l,a-l[0])
        except ChangeException:
            return change_mt(l[1:],a)



