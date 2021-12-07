# import sympy as sp
# import scipy as sgraph
# func = input()
# func = func.strip()
# if "^" in func:
#     func = func.replace("^", "**")
# x = sp.Symbol('x')
# y = x**3 + 5
# yd = sp.diff(y,x)
# print(str(yd).replace("**", "^").replace("*", ""))

from sympy import *
from sympy.parsing.sympy_parser import (split_symbols, 
                                        standard_transformations, 
                                        implicit_multiplication_application, 
                                        convert_xor)
import sympy.printing as printing

print("Inserire la funzione: ")
funzione = input()  # ricavo in input tutta la funzione
funzione = funzione.strip() # tolgo gli spazi alle estremità

# funzione = funzione.replace("^", "**")  # sostituisco gli esponenti tradizionali a come vuole python
# NB. LA STRINGA SUPERIORE E' STATA SOSTITUITA DALLA RIGA INFERIORE CON LA FUNZIONE "convert_xor"

transformations = (standard_transformations + (split_symbols, implicit_multiplication_application, convert_xor))
# salvo le trasformazioni necessarie:
#   - separa e moltiplica automaticamente in caso di più simboli (x, y, z)
#   - moltiplicazioni implicite, ovvero non devo scrivere "*" tra due elementi ES: "3x" -> "3*x" 
#   - auto-conversione degli esponenti da "^" a "**"

funzione = parse_expr(funzione, transformations=transformations)

x = symbols('x')    # dico che ogni X è simbolo

# DerivataFunzione = diff(funzione, x)  # calola la derivata
# print(str(DerivataFunzione).replace("**", "^"))    # stampa la funzione derivata

print("\n")
pprint(diff(funzione, x))   # calcola e stampa in modo carino la funzione derivata
print("\n")
