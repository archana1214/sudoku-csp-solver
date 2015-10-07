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

def add_variables(problem):
    # Add variables with domain 1-9 for each variable
    for row in range(SUDOKU_SIZE[0]):
        for col in range(SUDOKU_SIZE[1]):
            problem.addVariable((row + 1, col + 1), range(1,10))
    return problem

def sudoku_constraints(problem):
    """ Add constraints standard to all sudokus """



    # for i in range(1, 10) :
    #     problem.addVariables(range(i*10+1, i*10+10), range(1, 10))

    # Add constraints
    # constraint id: 1 = AllDifferentConstraint()
    for i in range(1,10):
        problem.addConstraint(1, [(i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8), (i,9)])
    for j in range(1,10):
        problem.addConstraint(1, [(1,j), (2,j), (3,j), (4,j), (5,j), (6,j), (7,j), (8,j), (9,j)])

    problem.addConstraint(1,[(1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)])
    problem.addConstraint(1,[(1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5),(3,6)])
    problem.addConstraint(1,[(1,7),(1,8),(1,9),(2,7),(2,8),(2,9),(3,7),(3,8),(3,9)])

    problem.addConstraint(1,[(4,1),(4,2),(4,3),(5,1),(5,2),(5,3),(6,1),(6,2),(6,3)])
    problem.addConstraint(1,[(4,4),(4,5),(4,6),(5,4),(5,5),(5,6),(6,4),(6,5),(6,6)])
    problem.addConstraint(1,[(4,7),(4,8),(4,9),(5,7),(5,8),(5,9),(6,7),(6,8),(6,9)])

    problem.addConstraint(1,[(7,1),(7,2),(7,3),(8,1),(8,2),(8,3),(9,1),(9,2),(9,3)])
    problem.addConstraint(1,[(7,4),(7,5),(7,6),(8,4),(8,5),(8,6),(9,4),(9,5),(9,6)])
    problem.addConstraint(1,[(7,7),(7,8),(7,9),(8,7),(8,8),(8,9),(9,7),(9,8),(9,9)])
    return problem

def main(arg):
    
    # User input size sudoku
    if len(arg) > 3:
        size = arg[3].split('x')
        SUDOKU_SIZE = (int(size[0]), int(size[1]))
    
    # Read sudokus from text file
    read_sudokus(arg[1])


    for sudoku in SUDOKUS:
        if sudoku == SUDOKUS[0]:
            problem = Problem()

            problem = add_variables(problem)
            # Add standard sudoku constraints
            problem = sudoku_constraints(problem)
            # Get solution
            problem.getSolution()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "Please give a input filename, outputfilename and the size of the sudokus"
        print "If no size given, than default sudoku size is 9x9"
        print "Example: python sudoku.py \"input.txt\" \"output.txt\" "
    else:
        main(sys.argv)
        pprint(SUDOKUS[0])
