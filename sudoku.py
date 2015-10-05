#!/usr/bin/env python

# for a full implementation of a python constraint solver, see https://pypi.python.org/pypi/python-constraint.
# for a crashcourse on creating a CSP-solver in a weekend, see http://www.cs.northwestern.edu/~ian/GDCConstraintsHowTo.pdf

from constraintproblem import *
from pprint import pprint


def main():

    # Load sudoku from file:
    # Can't we just use the stuff from last time?

    problem = Problem()

    # for a normal size sudoku: add all the variables with their domain.
    sudokusize = (9,9)
    boxsize = (3,3)

    # Add variables with domain 1-9 for each variable
    for row in range(sudokusize[0]):
        for col in range(sudokusize[1]):
            problem.addVariable((row + 1, col + 1), range(1,10))

    # for i in range(1, 10) :
    #     problem.addVariables(range(i*10+1, i*10+10), range(1, 10))

    # Add constraints
    # constraint id: 1 = AllDifferentConstraint()

    problem.addConstraint(1, [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9)])

    pprint(problem.variables)

    # Get solution
    print problem.getSolution()

if __name__ == '__main__':
    main()
