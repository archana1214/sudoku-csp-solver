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

    def addConstraint(self, constraintID, constrained_variables=None):
        """ Add a constraint over the variables to the problem

        @param constraint: an instance of one of the constraint classes,
                           defines a constraint over the variables given
        @type  constraint: an instance of one of the constrain classes
        @param  variables: a list of variables over which the constraint
                           works. Default is all variables.
        @type   variables: a list
        """
        if constraintID == 1:
            constraint = AllDifferentConstraint(self.variables, constrained_variables)
            self.constraints.append(constraint)
        pass

    def addVariable(self, variable, domain):
        """ Add a single variable to the Problem with a given domain

        @param variable: variable that we add to our problem variables
        @type variable:  some single value, for example a string, an int. In the sudoku case, it's a tuple.
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

    def mapVarToConstraints(self):
        """ Based on variables and constraint list make dictionary that
        maps variables to their constraints
        """
        var_constr_dict = {}
        for variable in self.variables:
            var_constr_dict[variable] = []
        for constraint, variables in self.constraints:
            for variable in variables:
                var_constr_dict[variable].append(constraint)
        return var_constr_dict

    def getSolution(self):
        """
        Returns a solution for the CSP-problem

        @rtype: ?

        """
        """ HEURISTIEK OPTIES
        1. most constrained variable
        2. smallest domain variable
        3. mix of 1 and 2
        MORE IDEAS? """

        var_constr_dict = self.mapVarToConstraints()
        # Use dict to choose most constrained variable 
        
        # Order variables by domain size
        ordered_vars = [(len(self.variables[var]), var) for var in self.variables]
        ordered_vars.sort()


        return True


class Solver(object):
    pass


class BacktrackingSolver(Solver):
    """ Solver that uses backtraching.

    example
     0 9 _ 7 _ _ 8 6 _
     _ 3 1 _ _ 5 _ 2 _
     8 _ 6 _ _ _ _ _ _
     _ _ 7 _ 5 _ _ _ 6
     _ _ _ 3 _ 7 _ _ _
     5 _ _ _ 1 _ 7 _ _
     _ _ _ _ _ _ 1 _ 9
     _ 2 _ 6 _ _ _ 5 _
     _ 5 4 _ _ 8 _ 7 _

    Steps:
    1. kies volgens een heuristiek een leeg vakje (bijvoorbeeld (1, 3))
        2. kies volgens een heuristiek een assignment (bijvoorbeeld '2')
        check de constraints waar de variabele in voorkomt. True? --> ga naar 1, False? --> verwijder de assignment (in het voorbeeld '2') uit het mogelijke domein en ga naar 2.
        Als het domein leeg is, ga terug naar het voorgaande leeg vakje en ga naar stap 2.

    Volgens mij is dit een OK naive implementatie?


    """

    pass


# if we need multiple constraint types with similair functionality, we could inherit this class.
# class Constraint(object):
#     pass


class AllDifferentConstraint(object):
    """ init a constraint over variables. If these variables are not given, the constraint will be over all variables.
    """

    # '_' shows that it's a internal variable.
    _constrained_variables = {}

    def __init__(self, variables, constrained_variables=None):
        """ init a constraint. 
            
            @param constrained_variables: variables over which the constraint is. the default is all variables
            @type constrained_variables: a list. for example [11,12,13]
        """

        for var in constrained_variables:
            self._constrained_variables[var] = variables[var]
            # print "added " + var + ", " self.constrained_variables
        for k, v in self._constrained_variables.iteritems():
            print k, v

    def solve(self):
        """ gets a solution for a constraint.
            
        """
        if self._constrained_variables is not None:
            pass
        else:
            # over all variables
            pass


class Domain(list):
    """
        Im not sure yet if we need a Domain class yet, but it could prove usefull in the future, for now, unused.
    """
    pass
