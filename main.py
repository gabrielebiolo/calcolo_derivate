import sympy as sp
# import scipy as sgraph
func = input()
func = func.strip()
if "^" in func:
    func = func.replace("^", "**")
x = sp.Symbol('x')
y = x**3 + 5
yd = sp.diff(y,x)
print(str(yd).replace("**", "^").replace("*", ""))