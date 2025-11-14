
'''

USER MANUAL:

ExactDE is A Python class for solving and analyzing ordinary differential equations (ODEs).

    Usage:
    >>> parse DE => ExactDE("2*x*y + x**2*y' = 0")
    >>> check if exact => de.exact
    >>> get solution => de.sol
    

    Attributes:
        sol (str): Returns the solution of the provided differential equation in string form.
        exact (bool): Returns True if the differential equation is exact, False otherwise.


    Example:
    #the class takes a string as parameter, it can be input by the user, 
    >>> equation = input()    
    >>> de = ExactDE(equation)

    #to see whether the equation is exact or not the 'exact' attribute can be called
    >>> print(de.exact)
    
    #to see the solution, the 'sol' attribute is called
    >>> print(de.sol)



'''
