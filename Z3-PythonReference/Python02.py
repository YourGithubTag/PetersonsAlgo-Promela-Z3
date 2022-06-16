from z3 import Solver, sat, And, Consts


##QUESTION 6

def main():
    from z3 import DeclareSort,ForAll, Function, Exists, IntSort

    # Initialise the solver
    T = DeclareSort('T')        # A new Type "T"
    D = IntSort('D')
    s = Solver()

    f = Function('f',T,T,T,INT)
    x, y, z = Consts('x y z' , T)

    s.add(ForAll([x, y ,z], And(f(x,y,z) == f(y,z,x)))) 
    
    s.add(And(x == y,y == z, z == x))
    s.add(And(x >= 0))

    if s.check() == sat:
        #print('Solved:')
        #print(s.model())

        print('Result:')
        print('f: %s' % s.model()[f])
        
    else:
        print('Codes bad')



# Calling the main function in python
if __name__ == '__main__':
        main()