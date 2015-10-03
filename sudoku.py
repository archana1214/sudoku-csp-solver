#!/usr/bin/env python

# for a full implementation of a python constraint solver, see https://pypi.python.org/pypi/python-constraint.
# for a crashcourse on creating a CSP-solver in a weekend, see http://www.cs.northwestern.edu/~ian/GDCConstraintsHowTo.pdf

from constraintproblem import *
from pprint import pprint


def main():
    problem = Problem()

    # for a normal size sudoku: add all the variables with their domain.
    sudokudimensions = 9 * 9
    problem.addVariables(range(1, sudokudimensions+1), range(1, 10))
    pprint(problem.variables)
    print problem.getSolution()

if __name__ == '__main__':
    main()
