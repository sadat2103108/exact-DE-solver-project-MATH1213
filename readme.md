'''

USER MANUAL:

ExactDE is a Python class for solving and analyzing ordinary differential equations (ODEs).

Usage:
    >>> de = ExactDE("2*x*y + x**2 + 4*y dy + 2*x*y + 3 dx")
    >>> de.getInfo()        # Get detailed info about the equation
    >>> de.isExact()        # Check if the differential equation is exact
    >>> de.getSolution()    # Get the solution of the exact differential equation

Public Methods:

    getInfo() -> dict
        Returns a dictionary containing:
            "Equation" : The original differential equation string
            "dM/dy"    : Partial derivative of M with respect to y
            "dN/dx"    : Partial derivative of N with respect to x
            "Exact?"   : Boolean indicating if the equation is exact

    isExact() -> bool
        Returns True if the differential equation is exact, False otherwise.

    getSolution() -> str
        Returns the solution as a string if the equation is exact,
        or a message "The equation is not exact." otherwise.

Example:

    >>> equation = input("Enter Differential Equation: ")
    >>> de = ExactDE(equation)

    # Get information about the equation
    >>> info = de.getInfo()
    >>> for k, v in info.items():
    >>>     print(f"{k}: {v}")

    # Check exactness
    >>> print("Is Exact?", de.isExact())

    # Get solution
    >>> print("Solution:", de.getSolution())

'''
