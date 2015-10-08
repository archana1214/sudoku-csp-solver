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

def variable_domains(problem,sudoku):
    """ Add variables with domain 1-9 for each variable
    we have to somehow translate all the sudokuchars to constraints. i.e. if (1,1) = 1 at init, there needs to be a constraint over variable (1,1) so that its domain is only [1]. 
    """
    for row in range(SUDOKU_SIZE[0]):
        for col in range(SUDOKU_SIZE[1]):
            if sudoku[row][col] == 0:
                problem.addVariable((row + 1, col + 1), range(1,10))
            else:
                problem.addVariable((row + 1, col + 1), [sudoku[row][col]])
    return problem

def sudoku_constraints(problem):
    """ Add constraints standard for all sudokus """

    # Add constraints
    # constraint id: 1 = AllDifferentConstraint()
    for i in range(1,SUDOKU_SIZE[0]):        
        problem.addConstraint(1, [(i,1), (i,2), (i,3), (i,4), (i,5), (i,6), (i,7), (i,8), (i,9)])
    for j in range(1,SUDOKU_SIZE[1]):
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

def rewrite2array(solution):
    """ rewrites an solution of the form  {(1,1): [4], (1,2): [5] , .... (9,9) : [1]} to an 2dimensional array.
        this is useful if we want to output it in a human readable form.
        this is also used as intermediate step for rewriting the sudoku back to the original format.
    """
    sudoku_array = []
    for i in range(SUDOKU_SIZE[0]):
        sudoku_array.append([])
        for j in range(SUDOKU_SIZE[1]):
            sudoku_array[i].append(0)
    for variable, assignment in solution.iteritems():
        if len(assignment) == 1:
            #<<<<<<< HEAD
            #print variable[0], variable[1]
            #=======
            #>>>>>>> 1993cac983cbff69d5093dde8943ee82d1d6877d
            sudoku_array[variable[0] -1][variable[1] - 1] = assignment[0]
    return sudoku_array

def rewrite2output(solution_array):
    """ rewrite a 2dimensional array to long string, just like the input.

    """

    outputstring = ""
    for i in range(SUDOKU_SIZE[0]):
        for j in range(SUDOKU_SIZE[1]):
            outputstring += str(solution_array[i][j])
    return outputstring

def output_data(outputfile, output):
    """ outputs the solutions to the specified outputfile
    """
    with open(outputfile, 'w') as f:
        for sudoku in output:
                f.write(sudoku)
                f.write("\n")

def print_statistics(output_stats):
    runtime = 0
    avg_backtracks = 0
    avg_splits = 0
    for problem_stat in output_stats:
        runtime += getattr(problem_stat,'runtime')        
        avg_backtracks += getattr(problem_stat,'backtracks')        
        avg_splits += getattr(problem_stat,'splits')    
    n_Sudokus= len(output_stats) 
    avg_backtracks *= 1/n_Sudokus
    avg_splits *= 1/n_Sudokus
    print "runtime: %s, avg_backtracks: %s, avg_splits: %s" %(runtime, avg_backtracks, avg_splits)

def main(arg, forward_checking = False, minimal_remaining_values=False):
    print_to_file = False
    outputfile = ""
    forward_checking = True
    minimal_remaining_values = True

    # User input size sudoku
    if len(arg) > 3:
        size = arg[3].split('x')
        SUDOKU_SIZE = (int(size[0]), int(size[1]))

    if len(arg) > 2 and arg[2][-4:] == ".txt":
        print_to_file = True
        outputfile = arg[2]

    # Read sudokus from text file
    read_sudokus(arg[1])

    # output is OR outputted to the screen, or to the outputfile. This is a buffer where we save all solutions as a string of 81 characters for 1 sudoku.
    output = []
    output_stats = []
    for sudoku in SUDOKUS:
        if sudoku == SUDOKUS[0]:
            problem = Problem(forward_checking = forward_checking, minimal_remaining_values = minimal_remaining_values)

            problem = variable_domains(problem,sudoku)
            # Add standard sudoku constraints
            problem = sudoku_constraints(problem)
            # Get solution (this is of the form {(1,1): [4], (1,2): [5] , .... (9,9) : [1]})
            solution = problem.getSolution()
            statistics = problem.getStatistics()
            solution_array = rewrite2array(solution)
            if not print_to_file:
                pprint(solution_array)
            else:
                output.append(rewrite2output(solution_array))
            output_stats.append(statistics)
    # EXTRA PRINT        
    pprint(solution_array)
    print_statistics(output_stats)
    #if an outputfile is specified
    if outputfile:
        output_data(outputfile, output)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print "Please give a input filename, outputfilename and the size of the sudokus"
        print "If no size given, than default sudoku size is 9x9"
        print "if no outputfile is given, the solutions will be outputted on the screen"
        print "Example: python sudoku.py \"input.txt\" \"output.txt\" "
    else:
        main(sys.argv,forward_checking = True, minimal_remaining_values=True)
        main(sys.argv,forward_checking = True, minimal_remaining_values=False)
        main(sys.argv,forward_checking = False, minimal_remaining_values=True)
        main(sys.argv,forward_checking = False, minimal_remaining_values=False)


