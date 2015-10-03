#!/usr/bin/env python
# CSP-problem class by Ilse van der Linden & Sander van Dorsten

""" Module that has the ability for users model a Constraint Satisfaction Problem.


"""


class Problem(object):
    """ An instance of a CSP problem

    TODO: fill in the different methods of the class. I've added them but have not yet implemented them because I wanted to work on the program structure first.

    """

    def __init__(self, solver=None):
        """
        @param solver: Problem solver used to find solutions
                       (default is BacktrackingSolver)
        @type solver:  instance of a Solver subclass
        """
        self.solver = solver or BacktrackingSolver()
        self.constraints = []
        self.variables = {}

    def addConstraint(self, constraint, variables=None):
        """ Add a constraint over the variables to the problem

        @param constraint: an instance of one of the constraint classes,
                           defines a constraint over the variables given
        @type  constraint: an instance of one of the constrain classes
        @param  variables: a list of variables over which the constraint
                           works. Default is all variables.
        @type   variables: a list
        """

        pass

    def addVariable(self, variable, domain):
        """ Add a single variable to the Problem with a given domain

        @param variable: variable that we add to our problem variables
        @type variable:  a string (?)
        @param domain: Domain of the added variable
        @type domain:  instance of Domain, a list

        TODO: add exception and error handling.
        TODO: implement Domain() class? do we need this for just the sudoku
              CSP instance?
        """
        self.variables[variable] = domain

    def addVariables(self, variables, domain):
        """ Add multiple variables to the problem with the same given domain

        @param variables: variable that we add to our problem variables
        @type variables:  something we can iterate over, a list, a range.
        @param domain: Domain of the added variable
        @type domain:  instance of Domain, a list
        """
        for variable in variables:
            self.addVariable(variable, domain)

    def getSolution(self):
        """
        Returns a solution for the CSP-problem

        @rtype: ?

        """
        return True

class Solver(object):
    pass


class BacktrackingSolver(Solver):
    pass


class Constraint(object):
    pass


class AlldifferentConstraint(Constraint):
    pass


class Domain(list):
    """
        Im not sure yet if we need a Domain class yet, but it could prove usefull in the future, for now, unused.
    """
    pass

