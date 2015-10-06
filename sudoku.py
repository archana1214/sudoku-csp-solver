#!/usr/bin/env python

# for a full implementation of a python constraint solver, see https://pypi.python.org/pypi/python-constraint.
# for a crashcourse on creating a CSP-solver in a weekend, see http://www.cs.northwestern.edu/~ian/GDCConstraintsHowTo.pdf

from constraintproblem import *
import sys
from pprint import pprint

SUDOKUS = []
SUDOKU_SIZE = (9,9)

def read_sudokus(filename):
    """import all sudoku's from file given by user"""
    try:
        with open(filename,'r') as f:
            # For each sudoku in the file
            for line in f:
                line = line.replace(".","0")
                sudoku = []
                row = []
                for character in line:
                    if character.isdigit():
                        row.append(int(character))
                    # Go to next row when all columns are read    
                    if (len(row) == SUDOKU_SIZE[1]):
                        sudoku.append(row)
                        row = []
                SUDOKUS.append(sudoku)
            f.close()
    except IOError as e:
        print "I/O error({0}): {1}".format(e.errno, e.strerror)

def sudoku_constraints(problem):
    """ Add constraints standard to all sudokus """

    # Add variables with domain 1-9 for each variable
    for row in range(SUDOKU_SIZE[0]):
        for col in range(SUDOKU_SIZE[1]):
            problem.addVariable((row + 1, col + 1), range(1,10))

    # for i in range(1, 10) :
    #     problem.addVariables(range(i*10+1, i*10+10), range(1, 10))

    # Add constraints
    # constraint id: 1 = AllDifferentConstraint()

    #problem.addConstraint(1, [(1,1), (1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9)])

    #pprint(problem.variables)
    return problem

def main(arg):
    
    # User input size sudoku
    if len(arg) > 2:
        size = arg[2].split('x')
        SUDOKU_SIZE = (int(size[0]), int(size[1]))
    
    # Read sudokus from text file
    read_sudokus(arg[1])

    problem = Problem()

    # for a normal size sudoku: add all the variables with their domain.
    #boxsize = (3,3)

    # Add standard sudoku constraints
    problem = sudoku_constraints(problem)

    for sudoku in SUDOKUS:
        
        # Get solution
        problem.getSolution()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "Please give a file name and the size of the sudokus"
        print "If no size given, than default sudoku size is 9x9"
        print "Example: python sudoku.py \"file.txt\" 9x9"
    else:
        main(sys.argv)
        print SUDOKUS[0]
