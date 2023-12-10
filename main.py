import sys
import math
import numpy
from decimal import *
import argparse

def riemann_area(f, a, b, n):
    h = str((b-a)/n)
    h_i = 0
    L = [0]
    sum = 0
    for i in range(0, n):
        h_i = Decimal(h) + h_i
        L.append(h_i)
    for i in range(1, n):
        sum += (f(L[i]) + f(L[i+1]))/2
    
    return Decimal(sum)*Decimal(h)

def sin_funcion():
    return lambda x: (math.sin(math.sqrt(x**2)))

def div_funcion():
    return lambda x: (Decimal(x)**Decimal((2*numpy.e))) / Decimal((numpy.sqrt(x+1)))

def main(): 
    parser = argparse.ArgumentParser(description='Computar integrales de Riemann.')
    parser.add_argument("--sin", action='store_true', help='funcion seno')
    parser.add_argument("--div", action='store_true', help='funcion división')
    parser.add_argument("-n", type=int, help='Cantidad de intervalos')
    args = parser.parse_args()

    if args.sin: 
        f = sin_funcion()

    elif args.div:
        f = div_funcion()

    a = 0
    b = 1
    print("El cálculo de la integral es: ", riemann_area(f, a, b, args.n))
 
if __name__=="__main__": 
    main() 
