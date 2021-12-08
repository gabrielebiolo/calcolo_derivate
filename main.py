from sympy import *
from sympy.parsing.sympy_parser import (split_symbols, standard_transformations, implicit_multiplication_application, convert_xor)
import sympy.printing as printing

pprint(diff(parse_expr(input("Inserire la funzione: ").strip(), transformations=(standard_transformations + (split_symbols, implicit_multiplication_application, convert_xor))), x = symbols('x')))