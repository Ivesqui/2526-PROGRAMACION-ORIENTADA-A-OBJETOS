"""
Servicio de conversión de temperatura (celsius a fahrenheit,
fahrenheit a celsius, celsius a kelvin y kelvin a celsius.
"""

def c_a_f(valor):
    return (valor * 9 / 5) + 32

def f_a_c(valor):
    return (valor - 32) * 5 / 9

def c_a_k(valor):
    return valor + 273.15

def k_a_c(valor):
    return valor - 273.15
