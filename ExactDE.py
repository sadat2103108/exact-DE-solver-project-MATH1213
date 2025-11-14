from sympy import *
import re

class ExactDE:
    def __init__(self, equation):
        self.__eqn = equation  # private
        self.__M, self.__N = self.__extractMN()  # private
        self.__dMdy, self.__dNdx = self.__checkExactness(self.__M, self.__N)
        self.__exact = (self.__dMdy == self.__dNdx)
        self.__solution = self.__findSol() if self.__exact else "The equation is not exact."


    # ----------------- Private Methods -----------------
    def __encode(self, eqn):
        eqn = eqn.replace("xy", "x*y").replace("yx", "y*x")
        eqn = re.sub(r'(\d+)([a-zA-Z(])', r'\1*\2', eqn)

        # Handle common functions
        all_funcs = ['sin','cos','tan','exp','sec','csc','cot',
                     'asin','acos','atan','asec','acsc','acot']
        for func in all_funcs:
            eqn = eqn.replace(f"{func}(x)", f"{func}(x)")
            eqn = re.sub(r'([a-zA-Z)])(' + '|'.join(all_funcs) + r')\(', r'\1(\2', eqn)
        eqn = re.sub(r'1\+y\*\*2', r'1+y**2', eqn)
        return eqn

    def __decode(self, expr):
        s = str(expr)
        s = re.sub(r'x\*\*([\d.]+)', r'x^{\1}', s)
        s = re.sub(r'\*\*', r'^', s)
        return s.replace("*", "")

    def __extractMN(self):
        s = self.__eqn
        i = 0
        n = len(s)
        M, N = "", ""

        # Extract M
        while i < n-1:
            if s[i]+s[i+1] == "dx":
                i += 2
                break
            M += s[i]
            i += 1
        
        # Extract N
        while i < n-1:
            if s[i]+s[i+1] == "dy":
                break
            N += s[i]
            i += 1

        return sympify(self.__encode(M)), sympify(self.__encode(N))

    def __checkExactness(self, M, N):
        x, y = symbols("x y")
        dMdy = diff(M, y)
        dNdx = diff(N, x)
        return dMdy, dNdx

    def __findSol(self):
        x, y = symbols("x y")
        F = integrate(self.__M, x, conds='separate')
        dFdy = diff(F, y)
        G = integrate(self.__N - dFdy, y, conds='separate')
        ans = F + G
        return self.__decode(ans) + " = Constant"

    # ----------------- Public Getter Methods -----------------
    def getInfo(self):
        info = {
            "Equation": self.__eqn,
            "dM/dy": self.__dMdy,
            "dN/dx": self.__dNdx,
            "Exact?": self.__exact
        }
        return info

    def isExact(self):
        return self.__exact

    def getSolution(self):
        return self.__solution




# ----------------- Example Use -----------------
if __name__ == "__main__":
    eqn = input("Enter Differential Equation: ")
    de = ExactDE(eqn)

    print("\nEquation Info:")
    for k, v in de.getInfo().items():
        print(f"{k}: {v}")
    
    print("\nIs Exact?", de.isExact())
    print("Solution:", de.getSolution())
