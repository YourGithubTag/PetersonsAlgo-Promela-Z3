from z3 import Solver, sat, And, Consts


##QUESTION 5

def swap1(a, b):
    tmp = b
    b = a
    a = tmp
    return a, b

def swap2(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

def main():

    from z3 import IntSort

    # Initialise the solver
    s = Solver()

    a, b = Consts('a b', IntSort())

    s.add(swap1(a,b) == swap2(a,b))


    if s.check() == sat:
        print('equivalent')
    else:
        print(' not equivalent')
# Calling the main function in python
if __name__ == '__main__':
        main()