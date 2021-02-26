import math
import decimal

def MED(values):
    suma = 0 

    for i in values:
        suma += i
    
    med = suma / len(values)
    
    return med

def SUM(values):
    suma = 0

    for i in values:
        suma += i
    
    return suma

def REST(values):
    subs = values[0]

    for i in values:
        if i != values[0]:
            subs -= i

    return subs

def DIV(values):
    div = values[0]

    for i in values:
        if i != values[0]:
            div /= i

    return div

def MULT(values):
    mult = values[0]

    for i in values:
        if i != values[0]:
            mult *= i 
    
    return mult

def POT(values):

    decimal.getcontext().prec = 500

    pot = decimal.Decimal(values[0])

    for i in values:
        if i != values[0]:
            pot = math.pow(pot, i)
    
    return pot

def SQRT(values):
    return None
