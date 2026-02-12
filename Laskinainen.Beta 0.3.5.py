from fractions import Fraction
from functools import reduce
import math
import cmath
import operator
import numpy as np
from sklearn.linear_model import LinearRegression
from itertools import permutations
from itertools import combinations
from rich.console import Console, Group
from rich.text import Text
import os
import pyfiglet
from rich.style import Style
import time
from rich.live import Live
from typing import Callable
from sympy import Poly, expand, symbols, solve, simplify, parse_expr, Eq, lambdify
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import parse_expr
from mpl_toolkits.mplot3d import Axes3D
from sympy import symbols, Eq, solve, Poly, expand, lambdify, parse_expr
import numpy as np
import matplotlib.pyplot as plt
from sympy import Symbol, symbols, Eq, solve, Poly, expand, lambdify, parse_expr


COLORES = [
    (204, 204, 204),
    (59, 120, 255),
    (0, 55, 127),
    (98, 98, 98)
]
NUM_COLORES = len(COLORES)
FACTOR_ANCHO_BANDA = 4 
def aplicar_color_rgb(r, g, b, texto):
    """Aplica un color RGB a un texto individual."""
    return f"\033[38;2;{r};{g};{b}m{texto}\033[0m"
def imprimir_banner_diagonal_bandas(texto):
    fig = pyfiglet.Figlet(font='big')
    ascii_art = fig.renderText(texto)
    lineas = ascii_art.splitlines()
    if not lineas: return
    for y, linea in enumerate(lineas):
        linea_coloreada = ""
        for x, char in enumerate(linea):
            if char != " ":
                indice_color = ((x + y) // FACTOR_ANCHO_BANDA) % NUM_COLORES
                r, g, b = COLORES[indice_color]
                linea_coloreada += aplicar_color_rgb(r, g, b, char)
            else:
                linea_coloreada += " "
        print(linea_coloreada)

def Calculadora ():
    print("Tervetuloa! Este es un programa de calculador estándar/científica en desarrollo. es un proyecto para practicar") 
    print("caracteristicas de python. Además porque en el futuro me gustaría estudiar este tipo de cosas, especificamente")
    print("ingenieria informática, tema que me resulta fascinante no solo por las matemáticas, sino el hecho de poder crear")
    print("cosas en un entorno lógico y completamente libre.")
    print(" ")
    while True:
        menu_calculadora: dict[int, Callable[[], None]] = {
            1: Calculos_estandar,
            2: Calculos_cientificos,
            }
        print("1) Calculos estándar.")
        print("2) Calculos científicos.")
        print("0) Salir.")
        print(" ")
        op = input("Elija que desea realizar: ")
        if op == "1":
            Calculos_estandar()
        elif op == "2":
            Calculos_cientificos()
        elif op == "3":
            print("Saliendo...")
            break
        else:
            print("Ningún comando detectado. Vuelva a intentarlo.")
            print(" ")
            return

def Calculos_estandar ():
    while True:
        menu_estandar: dict[int, Callable[[], None]] = {
            1: Sumatoria,
            2: Resta,
            3: Multiplicacion,
            4: Division,
            5: Porcentaje,
            6: Fracciones,
            7: Potencia,
            8: Raiz_Cuadrada,
            }
        print(" ")
        print("1) Sumatoria.")
        print("2) Resta.")
        print("3) Multiplicación.")
        print("4) División.")
        print("5) Porcentaje.")
        print("6) Fracciones.")
        print("7) Potencia.")
        print("8) Raíz cuadrada.")
        print("9) Volver.")
        print(" ")
        op = int(input("Elija operación estándar: "))
        if op in menu_estandar:
            menu_estandar[op]()
        elif op == 9:
            print("Volviendo atrás...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
        
def Calculos_cientificos ():
    menu_cientifico = {
    1: Trigonometría,
    2: Estadistica_Probabilidades,
    3: Funciones_Logaritmicas_Exponenciales,
    4: Calculo_Algebra,
}
    print(" ")
    print("1) Trigonometría.")
    print("2) Estadística/Probabilidades.")
    print("3) Funciones logarítmicas/exponenciales.")
    print("4) Cálculo y Algebra.")
    print("5) Volver.")
    print(" ")
    op = int(input("Elija operación científica: "))
    if op in menu_cientifico:
        menu_cientifico[op]()
    elif op == 5:
        print("Volviendo atrás...")
        print(" ")
        return
    else:
        print("Opción inválida. Intente de nuevo.")
        print(" ")
    
def Pednum ():
    return [float(n)for n in input("Ingrese números separados por espacio: ").split()]

def Pedfracc ():
    Entradafract = input("Ingrese las fracciones separadas por coma (ej: 1/2, 3/4): ")
    listaFract = [Fraction(f.strip()) for f in Entradafract.split(",")]
    return listaFract

def desea_continuar(mensaje="¿Desea continuar? (s/n): "):
    while True:
        op = input(mensaje).lower()
        if op == 's':
            return True
        elif op == 'n':
            return False
        else:
            print("Opción inválida. Use 's' o 'n'.")
        
def Sumatoria ():
    while True:
        nums1 = Pednum()
        print("Su resultado de suma es: ", sum(nums1))
        if not desea_continuar("¿Desea seguir sumando? (s/n): "):
            break

def Resta ():
    while True:
        nums2 = Pednum()
        print("Su resultado de resta es: ", reduce(operator.sub, nums2))
        if not desea_continuar("¿Desea seguir restando? (s/n): "):
            break

def Multiplicacion ():
    while True:
        nums3 = Pednum()
        print("Su multiplicación equivale a: ", math.prod(nums3))
        if not desea_continuar("¿Desea seguir multiplicando? (s/n): "):
            break

def Division ():
    while True:
        nums4 = Pednum()
        if 0 in nums4[1:]:
            print("Error: No se puede dividir entre cero.")
            return
        print("Su división equivale a: ", reduce(operator.truediv, nums4))
        op = input("¿Desea seguir dividiendo? (s/n): ")
        if not desea_continuar("¿Desea seguir dividiendo? (s/n): "):
            break

def Porcentaje ():
    while True:
        nums5 = Pednum()
        porsum = sum(nums5)
        porcen = [(x / porsum) * 100 for x in nums5]
        print("Su porcentaje es: ", porcen)
        if not desea_continuar("¿Desea seguir utilizando porcentajes? (s/n): "):
            break

def Fracciones ():
    Fracc = Pedfracc()
    print("Estas son las fracciones de usted: ", Fracc)
    while True:
        correc = (input("¿Desea volver atrás para corregir el cálculo? (s/n): ")).lower()
        if correc == 's':
            Fracc = Pedfracc()
            print("fracciones actualizadas: ", Fracc)
        elif correc == 'n':
            break
        else:
            print("Opción inválida. Intente de nuevo.")
            continue
    menu_fraccion = {
        1: Sumatoria_de_Fracciones,
        2: Resta_de_Fracciones,
        3: Multiplicacion_de_Fracciones,
        4: Division_de_Fracciones,
    }
    print(" ")
    print("1) Suma.")
    print("2) Resta.")
    print("3) Multiplicación.")
    print("4) División.")
    print(" ")
    while True:
        try:
            op = int(input("Ingrese el número de la operación que desea realizar: "))
            if op in menu_fraccion:
                menu_fraccion[op](Fracc)
                break
            else:
                print("Opción inválida.")
        except ValueError:
            print("Ingrese un número válido.")

def Sumatoria_de_Fracciones (fracciones):
    while True:
        print("La suma de sus fracciones es: ", sum(fracciones, Fraction(0)))
        if not desea_continuar("¿Desea seguir sumando fracciones? (s/n): "):
            break

def Resta_de_Fracciones (fracciones):
    while True:
        print("La resta de sus fracciones es: ", reduce(operator.sub, fracciones))
        if not desea_continuar("¿Desea seguir restando fracciones? (s/n): "):
            break

def Multiplicacion_de_Fracciones (fracciones):
    while True:
        print("La multiplicación de sus fracciones es: ", math.prod(fracciones))
        if not desea_continuar("¿Desea seguir multiplicando fracciones? (s/n): "):
            break

def Division_de_Fracciones (fracciones):
    while True:
        print("La división de sus fracciones es: ", reduce(operator.truediv, fracciones))
        if not desea_continuar("¿Desea seguir dividiendo fracciones? (s/n): "):
            break

def Potencia ():
    while True:
        numpotbas = float(input("Ingrese la base de su potencia: "))
        numpotexp = float(input("Ingrese el exponente de su potencia: "))
        potencia = (numpotbas ** numpotexp)
        print("Su potencia equivale a: ", potencia)
        if not desea_continuar("¿Desea seguir utilizando potencias? (s/n): "):
            break

def Raiz_Cuadrada ():
    while True:
        numraiz = float(input("Ingrese el radicando: "))
        if numraiz < 0:
            print("Error: No se puede calcular raíz cuadrada de un número negativo.")
            return
        result8 = math.sqrt(numraiz)
        print("Su raíz equivale a: ", result8)
        if not desea_continuar("¿Desea seguir utilizando raíces cuadradas? (s/n): "):
            break

def Trigonometría ():
    while True:
        menu_trigonometría = {
            1: Seno_menu,
            2: Coseno_menu,
            3: Tangente_menu,
            }
        print(" ")
        print("1) Seno.")
        print("2) Coseno.")
        print("3) Tangente.")
        print("4) Volver.")
        print(" ")
        op = int(input("Elija la operación trigonométrica que desea realizar: "))
        if op in menu_trigonometría:
            menu_trigonometría[op]()
        elif op == 4:
            print("Volviendo atrás...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return

def Estadistica_Probabilidades ():
    while True:
        menu_estadistica_probabilidad = {
            1: Calculo_de_media,
            2: Desviacion_estandar,
            3: Varianza,
            4: Regresion_lineal,
            5: Cuadratica,
            6: Exponencial,
            7: Permutaciones,
            8: Combinaciones,
            9: Factorial,
        }
        print(" ")
        print("1) Cálculo de media.")
        print("2) Desviación estándar.")
        print("3) Varianza.")
        print("4) Regresión lineal.")
        print("5) Cuadrática.")
        print("6) Exponencial.")
        print("7) Permutaciones (nPr).")
        print("8) Combinaciones (nCr).")
        print("9) Factorial (!).")
        print("10) Volver.")
        print(" ")
        op = int(input("Elija la operación estadística/probabilística que desea realizar: "))
        if op in menu_estadistica_probabilidad:
            menu_estadistica_probabilidad[op]()
        elif op == 10:
            print("Volviendo atrás...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
    
def Seno_menu ():
    while True:
        seno_menu = {
            1: Seno,
            2: ArcSeno,
            3: Senh,
        }
        print(" ")
        print("1) Seno (Sen/Sin).")
        print("2) Arcoseno (Sen⁻¹/Sin⁻¹).")
        print("3) Función hiperbólica del seno (Senh/Sinh/sh).")
        print("4) Volver.")
        op = int(input("Elija la operación trigonómica de seno que desea realizar: "))
        if op in seno_menu:
            seno_menu[op]()
        elif op == 4:
            print("Volviendo atrás...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
        
def Seno():
    while True:
        angulo1 = float(input("Ingrese el ángulo: "))
        result9 = math.sin(math.radians(angulo1))
        print("El seno de tu ángulo es: ", result9)
        if not desea_continuar("¿Desea seguir realizando operaciones con seno? (s/n): "):
            break

def ArcSeno ():
    while True:
        angulo4 = float(input("Ingrese el ángulo: "))
        if angulo4 < -1 or angulo4 > 1:
            print("Error: Arcsen solo admite valores entre -1 y 1.")
            return
        result14Rad = math.asin(angulo4)
        result14Deg = math.degrees(result14Rad)
        print("El Arcoseno de su ángulo en radianes es: ", result14Rad)
        print("El Arcoseno de su ángulo en grados es: ", result14Deg)
        if not desea_continuar("¿Desea seguir realizando operaciones con arcoseno? (s/n): "):
            break

def Senh ():
    while True:
        angulo5 = float(input("Ingrese el ángulo: "))
        result15 = math.sinh(angulo5)
        print("El seno hiperbólico de tu ángulo es: ", result15)
        if not desea_continuar("¿Desea seguir realizando operaciones con la función hipérbolica del seno? (s/n): "):
            break

def Coseno_menu():
    while True:
        coseno_menu = {
            1: Coseno,
            2: Arccos,
            3: Cosh,
        }
        print(" ")
        print("1) Coseno.")
        print("2) Arcocoseno (cos⁻¹).")
        print("3) Función hiperbólica del coseno (cosh/ch).")
        print("4) Volver.")
        print(" ")
        op = int(input("Elija la operación trigonómica de coseno que desea realizar: "))
        if op in coseno_menu:
            coseno_menu[op]()
        elif op == 4:
            print("Volviendo atrás...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
    

def Coseno ():
    while True:
        angulo2 = float(input("Ingrese el ángulo: "))
        result10 = math.cos(math.radians(angulo2))
        print("El coseno de tu ángulo es: ", result10)
        if not desea_continuar("¿Desea seguir realizando operaciones con el coseno? (s/n): "):
            break
    
def Arccos ():
    while True:
        angulo6 = float(input("Ingrese el ángulo: "))
        if angulo6< -1 or angulo6 > 1:
            print("Error: Arcos solo admite valores entre -1 y 1.")
            return
        result16Rad = math.acos(angulo6)
        result16Deg = math.degrees(result16Rad)
        print("El Arcoseno de su ángulo en radianes es: ", result16Rad)
        print("El Arcoseno de su ángulo en grados es: ", result16Deg)
        if not desea_continuar("¿Desea seguir realizando operaciones con el arcocoseno? (s/n): "):
            break
    
def Cosh ():
    while True:
        angulo7 = float(input("Ingrese el ángulo: "))
        result16 = math.cosh(angulo7)
        print("El coseno hiperbólico de tu ángulo es: ", result16)
        if not desea_continuar("¿Desea seguir realizando operaciones con la función hipérbolica del coseno? (s/n): "):
            break
    
def Tangente_menu ():
    while True:
        tangente_menu = {
            1: Tangente,
            2: Arctan,
            3: Tanh,
        }
        print(" ")
        print("1) Tangente.")
        print("2) Arcotangente (tan⁻¹).")
        print("3) Función hiperbólica del seno (tanh/th).")
        print("4) Volver.")
        print(" ")
        op = int(input("Elija la operación trigonómica de tangente que desea realizar: "))
        if op in tangente_menu:
            tangente_menu[op]()
        elif op == 4:
            print("Volviendo atrás...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
    
def Tangente ():
    while True:
        angulo3 = float(input("Ingrese el ángulo: "))
        angulo_norm = angulo3 % 180
        if abs(angulo_norm - 90) < 1e-9:
            print("Error: La tangente no está definida para este ángulo.")
            return
        result11 = math.tan(math.radians(angulo3))
        print("La tangente de tu ángulo es: ", result11)
        if not desea_continuar("¿Desea seguir realizando operaciones con la tangente? (s/n): "):
            break

def Arctan ():
    while True:
        angulo8 = float(input("Ingrese el ángulo: "))
        result17Rad = math.atan(angulo8)
        result17Deg = math.degrees(result17Rad)
        print("El Arcoseno de su ángulo en radianes es: ", result17Rad)
        print("El Arcoseno de su ángulo en grados es: ", result17Deg)
        if not desea_continuar("¿Desea seguir realizando operaciones con el arcotangente? (s/n): "):
            break
    
def Tanh ():
    while True:
        angulo9 = float(input("Ingrese el ángulo: "))
        result18 = math.tanh(angulo9)
        print("El coseno hiperbólico de tu ángulo es: ", result18)
        if not desea_continuar("¿Desea seguir realizando operaciones con la función hipérbolica de la tangente? (s/n): "):
            break

def Calculo_de_media ():
    while True:
        cmdlist = [float(n) for n in input("Ingrese datos (dato por separado): ").split()]
        if not cmdlist:
            print("no ingresó datos.")
            return
        result12 = sum(cmdlist) / len(cmdlist)
        print("El cálculo de media que realizó es: ", result12)
        if not desea_continuar("¿Desea seguir realizando cálculos de media? (s/n): "):
            break

def Desviacion_estandar ():
    while True:
        DevEstList = [float(n) for n in input("Ingrese datos (dato por separado): ").split()]
        result13 = np.std(DevEstList)
        print("La desviación estándar es de: ", result13)
        if not desea_continuar("¿Desea seguir sumando? (s/n): "):
            break

def Varianza ():
    while True:
        optionV = int(input("Ingrese 0 para poblacional o 1 para muestral: "))
        if optionV == 0:
            Varlist = [float(n) for n in input("Ingrese datos (dato por separado): ").split()]
            varP = np.var(Varlist)
            print("Su varianza poblacional es: ", varP)
        elif optionV == 1:
            Varlist = [float(n) for n in input("Ingrese datos (dato por separado): ").split()]
            varM = np.var(Varlist, ddof=1)
            print("Su varianza muestral es: ", varM)
        else:
            print("Valor erróneo.")
            if not desea_continuar("¿Desea seguir utilizando la varianza? (s/n): "):
                break

def Regresion_lineal ():
    while True:
        Xr = [float(n) for n in input("Ingrese datos para X (dato por separado): ").split()]
        Yr = [float(n) for n in input("Ingrese datos para Y (dato por separado): ").split()]
        if len(Xr) != len(Yr):
            print("X e Y deben tener la misma cantidad de datos. Inténtalo de nuevo.")
            return
        print("X es igual a: ", Xr)
        print("Y es igual a: ", Yr)
        Xnp = np.array (Xr).reshape(-1, 1)
        Ynp = np.array (Yr)
        print("X convertido a bidimensional (Matriz): ", Xnp)
        print("Y convertido a unidimensional (Vector): ", Ynp)
        Model = LinearRegression().fit(Xnp, Ynp)
        print("Modelo entrenado. Score R2: ", Model.score(Xnp, Ynp))
        if not desea_continuar("¿Desea seguir utilizando la regresión lineal? (s/n): "):
            break
    
def Cuadratica ():
    while True:
        Acuad = float(input("Ingrese el valor de a: "))
        Bcuad = float(input("Ingrese el valor de b: "))
        Ccuad = float(input("Ingrese el valor de c: "))
        discr = (Bcuad ** 2) - (4 * Acuad * Ccuad)
        Sol1 = (-Bcuad - cmath.sqrt(discr)) / (2*Acuad)
        Sol2 = (-Bcuad + cmath.sqrt(discr)) / (2*Acuad)
        print("Las soluciones de su cuadrática son:")
        print(Sol1, "En el caso negativo (b)")
        print(Sol2, "En el caso positivo (b)")
        if not desea_continuar("¿Desea seguir utilizando la cuadrática? (s/n): "):
            break

def Exponencial ():
    while True:
        numpotbasE = float(input("Ingrese la base de su exponencial: "))
        numpotexpE = float(input("Ingrese el exponente de su exponencial: "))
        expo = (numpotbasE ** numpotexpE)
        print("Su potencia equivale a: ", expo)
        if not desea_continuar("¿Desea seguir realizando exponenciales? (s/n): "):
            break
    
def Permutaciones ():
    while True:
        nPrElements = Pednum()
        nPr = permutations(nPrElements)
        for p in list(nPr):
            print("Permutaciones: ", p)
        if not desea_continuar("¿Desea seguir realizando premutaciones? (s/n): "):
            break

def Combinaciones ():
    while True:
        nCrElements = Pednum()
        nCrCantidad = int(input("Número de grupos de numeros que se permiten combinar: "))
        nCr = combinations(nCrElements, nCrCantidad)
        print("Su lista de combinaciones es: ", (list(nCr)))
        if not desea_continuar("¿Desea seguir realizando combinaciones? (s/n): "):
            break
    
def Factorial ():
    while True:
        Fact = int(input("Ingrese el número que quiera factorizar: "))
        FactResult = math.factorial(Fact)
        print("Su factorial equivale a: ", FactResult)
        if not desea_continuar("¿Desea seguir factorizando números? (s/n): "):
            break

def Funciones_Logaritmicas_Exponenciales ():
    while True:
        funciones_LE_menu = {
            1: Funciones_log,
            2: Funciones_Exponenciales,
        }
        print(" ")
        print("1) Funciones logarítmicas (base e / ln, 10, personalizado).")
        print("2) Funciones exponenciales (eˣ, 10ˣ).")
        print("3) Volver.")
        print(" ")
        op = int(input("Elija la función logarítmica/exponencial que desea realizar: "))
        if op in funciones_LE_menu:
            funciones_LE_menu[op]()
        elif op == 3:
            print("Volviendo atrás...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return

def Funciones_log ():
    while True:
        funciones_L_menu = {
            1: Logaritmo10,
            2: LogaritmoN,
            3: LogaritmoP,
        }
        print(" ")
        print("1) Logaritmo decimal (base 10)")
        print("2) Logaritmo natural (base e)")
        print("3) Logaritmo personalizado")
        print("4) Volver.")
        print(" ")
        op = int(input("Elija el tipo de función logarítmica que desea realizar: "))
        if op in funciones_L_menu:
            funciones_L_menu[op]()
        elif op == 4:
            print("Volviendo atrás...")
            print(" ")
            return
    
def Logaritmo10 ():
    while True:
        Numlog = float(input("Ingrese el número que quiera utilizar para su logaritmo de base 10: "))
        logresult = math.log(Numlog, 10)
        print("Su logaritmo es: ", logresult)
        if not desea_continuar("¿Desea seguir realizando logaritmos en base 10? (s/n): "):
            break

def LogaritmoN ():
    while True:
        LogN = float(input("Ingrese el número al que quiera pasar a su logarítmo natural: "))
        LogNresult = math.log(LogN)
        print("su logarítmo natural es: ", LogNresult)        
        if not desea_continuar("¿Desea seguir realizando logaritmos naturales? (s/n): "):
            break
        
def LogaritmoP ():
    while True:
        Numlog = float(input("Ingrese el número que quiera utilizar para su logaritmo de base 10: "))
        logbas = float(input("Ingrese la base de su algorítmo: "))
        logresult = math.log(Numlog, logbas)
        print("Su logaritmo es: ", logresult)
        if not desea_continuar("¿Desea seguir realizando logaritmos personalizados? (s/n): "):
            break
        
def Funciones_Exponenciales ():
    while True:
        funciones_E_menu = {
            1: Exponencial_natural,
            2: Exponencial_base10,
        }
        print(" ")
        print("1) Exponencial natural (eˣ).")
        print("2) Exponencial base 10 (10ˣ).")
        print("3) Volver.")
        print(" ")
        op = int(input("Ingrese el tipo de exponencial que desea realizar: "))
        if op in funciones_E_menu:
            funciones_E_menu[op]()
        elif op == 4:
            print("Volviendo...")
            print(" ")
            return
        else:
             print("Opción inválida. Intente de nuevo.")
             print(" ")
             return

def Exponencial_natural ():
    while True:
        expoN = float(input("Ingrese el exponencial para su base natural: "))
        expoResult = math.exp(expoN)
        print("El resultado de su base natural y exponencial es: ", expoResult)
        if not desea_continuar("¿Desea seguir realizando exponenciales a base natural? (s/n): "):
            break
        
def Exponencial_base10 ():
    while True:
        expo10 = float(input("Ingrese el exponencial para su base 10: "))
        expo10Result = 10 ** expo10
        print("El resultado de su base 10 y exponencial es: ", expo10Result)
        if not desea_continuar("¿Desea seguir realizando exponenciales a base 10? (s/n): "):
            break

def Calculo_Algebra ():
    while True:
        calculo_algebra_menu = {
            1: Resolucion_ecuaciones,
        }
        print(" ")
        print("1) Resolucion de ecuaciones (lineales, cuadráticas, sistemas).")
        print("2) Derivadas.")
        print("3) Integrales.")
        print("4) Operaciones con matrices.")
        print("5) Operaciones con determinantes.")
        print("6) Números complejos.")
        print("7) Volver.")
        print(" ")
        op = int(input("Elija que tipo de operacion de cálculo y algebra desea realizar: "))
        if op in calculo_algebra_menu:
            calculo_algebra_menu[op]()
        elif op == 7:
            print("Volviendo...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
        
def Resolucion_ecuaciones ():
    while True:
        resolucion_ecuaciones_menu = {
            1: Lineal,
        }
        print(" ")
        print("1) Ecuaciones lineales.")
        print("2) Cuadraticas.")
        print("3) Sistemas.")
        print("4) Volver.")
        print(" ")
        op = int(input("Elija que tipo de resolución de ecuaciones que desea realizar: "))
        if op in resolucion_ecuaciones_menu:
            resolucion_ecuaciones_menu[op]()
        elif op == 4:
            print("Volviendo...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
    
def Lineal ():
    while True:
        resolucion_ecuaciones_menu = {
            1: Una_incognita,
            2: Dos_incognita,
            3: Mas_incognita,
            }
        print(" ")
        print("1) De una incógnita.")
        print("2) De dos incógnitas.")
        print("3) De tres o más incógnitas.")
        print("4) Volver.")
        print(" ")
        op = int(input("Elija la cantidad de incognitas que desea en su ecuación lineal: "))
        if op in resolucion_ecuaciones_menu:
            resolucion_ecuaciones_menu[op]()
        elif op == 4:
            print("Volviendo...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
    
def Una_incognita ():
    while True:
        x = symbols('x')
        print("Forma de uso: Usa '*' para multiplicar (ej: 2*x) y escribe la ecuación igualada a 0.")
        print("Ejemplo de uso: 2x + 3 = 7 // se escribe // 2*x + 3 = 7")
        entrada = input("Escriba su ecuación: ")
        partes = entrada.split("=")
        try:
            if "=" in entrada:
                izq_str, der_str = entrada.split("=")
                izq_expr = parse_expr(izq_str)
                der_expr = parse_expr(der_str)
                ecuacion = Eq(izq_expr, der_expr)
                expresion_grafica = izq_expr - der_expr
            else:
                expresion_grafica = parse_expr(entrada)
                ecuacion = Eq(expresion_grafica, 0)
            solucion = solve(ecuacion, x)
            print(" ")
            print("\n")
            print("┌" + "─"*58 + "┐")
            print("│" + " ANÁLISIS DE SU ECUACIÓN LINEAL (1 INCÓGNITA) ".center(58) + "│")
            print("└" + "─"*58 + "┘")
            print(" ")
            tipo = ""
            punto_x = None
            if isinstance(solucion, list) and len(solucion) == 1:
                tipo = "Compatible Determinado."
                punto_x = float(solucion[0].evalf())
                print(" ")
                print(f"Tipo de ecuación lineal: {tipo}")
                print(f"Explicación: Tiene una única solución (x = {solucion[0]}).")
                print(" ")
            elif isinstance(solucion, list) and len(solucion) > 1:
                print(" ")
                tipo = "Compatible indeterminado"
                print(f"Tipo de ecuación lineal: {tipo}")
                print("Explicación: Tiene infinitas soluciones. Las rectas son coincidentes.")
                print(" ")
            elif not solucion:
                tipo = "Incompatible"
                print(" ")
                print(f"Tipo: {tipo}")
                print("Explicación: No tiene solución. Las rectas son paralelas.")
                print(" ")
            f_num = lambdify(x, expresion_grafica, "numpy")
            centro = punto_x if punto_x is not None else 0
            x_vals = np.linspace(centro - 10, centro + 10, 400)
            y_vals = f_num(x_vals)
            if np.isscalar(y_vals):
                y_vals = np.full_like(x_vals, y_vals)
            plt.figure(figsize=(8, 5))
            plt.plot(x_vals, y_vals, label=f"f(x) = {expresion_grafica}", color='blue')
            plt.axhline(0, color='black', linewidth=1)
            plt.axvline(0, color='black', linewidth=1)
            if punto_x is not None:
                plt.plot(punto_x, 0, 'ro', label=f'Solución: {punto_x}')
            plt.title(f"Gráfica: {tipo}")
            plt.grid(True, linestyle='--')
            plt.legend()
            plt.show()
        except Exception as e:
            print("Error al procesar la ecuación.", e)
            print(" ")
            return
        if not desea_continuar("¿Desea seguir realizando ecuaciones lineales de una sola incógnita? (s/n): "):
            break
        
def Dos_incognita ():
    while True:
        x, y = symbols('x y')
        print("Forma de uso: Usa '*' para multiplicar.")
        print("Ejemplo: 2x + 3y - 6 = 0 // se escribe // 2*x + 3*y - 6 = 0")
        entrada = input("Escriba su ecuación: ")
        try:
            if "=" in entrada:
                izq_str, der_str = entrada.split("=")
                izq_expr = parse_expr(izq_str, local_dict={'x': x, 'y': y})
                der_expr = parse_expr(der_str, local_dict={'x': x, 'y': y})
                ecuacion = Eq(izq_expr, der_expr)
                expresion_grafica = izq_expr - der_expr
            else:
                expresion_grafica = parse_expr(entrada, local_dict={'x': x, 'y': y})
                ecuacion = Eq(expresion_grafica, 0)
            print(" ")
            print("\n")
            print("┌" + "─"*58 + "┐")
            print("│" + " ANÁLISIS DE SU ECUACIÓN LINEAL (2 INCÓGNITA) ".center(58) + "│")
            print("└" + "─"*58 + "┘")
            print(" ")
            tipo = ""
            pendiente = None
            plt.figure(figsize=(8,5))
            solucion_y = solve(ecuacion, y)
            if solucion_y:
                tipo = "Recta oblicua u horizontal"
                pendiente = solucion_y[0].coeff(x)
                ordenada = solucion_y[0].subs(x, 0)
                print(f"Tipo: {tipo}.")
                print(f"Pendiente (m): {pendiente}.")
                print(f"Ordenada al origen (b): {ordenada}.")
                f = lambdify(x, solucion_y[0], "numpy")
                x_vals = np.linspace(-10, 10, 400)
                y_vals = f(x_vals)
                plt.plot(x_vals, y_vals, label=str(ecuacion), color='blue')
            else:
                solucion_x = solve(ecuacion, x)
                if solucion_x:
                    tipo = "Recta vertical"
                    x_val = float(solucion_x[0].evalf())
                    print(f"Tipo: {tipo}.")
                    print(f"Ecuación equivalente: x = {x_val}.")
                    plt.axvline(x=x_val, color='blue', label=f"x = {x_val}")
                else:
                    print("No se pudo determinar la gráfica.")
            plt.axhline(0, color='black', linewidth=1)        
            plt.axvline(0, color='black', linewidth=1)
            plt.grid(True, linestyle='--')
            plt.legend()
            plt.title(f"Gráfica: {tipo}")
            plt.show()
        except Exception as e:
            print("Error al procesar la ecuación.", e) 
            print(" ")
            return
        if not desea_continuar("¿Desea seguir realizando ecuaciones lineales de dos incógnitas? (s/n): "):
            break

def Mas_incognita ():
    while True:
        ecuaciones = []
        print("Forma de uso: Usa '*' para multiplicar.")
        print("Ejemplo: 2x + 3y - z + w = 0 // se escribe // 2*x + 3*y - z + w = 0")
        entrada = input("Escriba su ecuación: ")
        try:
            letras = sorted(set([c for c in entrada if c.isalpha()]))
            variables = symbols(" ".join(letras))
            if isinstance(variables, Symbol):
                variables = [variables]
            local_dict = {str(var): var for var in variables}
            if "=" in entrada:
                izq, der = entrada.split("=", 1)
                eq = Eq(parse_expr(izq, local_dict=local_dict),
                        parse_expr(der, local_dict=local_dict))
            else:
                expr = parse_expr(entrada, local_dict=local_dict)
                eq = Eq(expr, 0)
            ecuaciones.append(eq)
        except Exception as e:
            print("Error al procesar:", e)
        if not ecuaciones:
            print("No se ha ingresado ecuaciones.")
            continue
        variables = list(ecuaciones[0].free_symbols)
        expr = expand(ecuaciones[0].lhs - ecuaciones[0].rhs)
        print(" ")
        print("\n")
        print("┌" + "─"*58 + "┐")
        print("│" + " ANÁLISIS DE SU ECUACIÓN LINEAL (1, 2, 3 o >3 INCÓGNITAS) ".center(58) + "│")
        print("└" + "─"*58 + "┘")
        print(" ")
        print("Variables: ", variables)
        print("Cantidad de ecuaciones: ", len(ecuaciones))
        print(" ")
        print("┌" + "─"*30 + "┐")
        print("│" + " TIPO GEOMÉTRICO ".center(30) + "│")
        print("└" + "─"*30 + "┘")        
        print(" ")
        n = len(variables)
        if n == 1:
            print("Ecuación de una variable.")
        elif n == 2:
            print("Representa una recta en R².")
        elif n == 3:
            print("Representa un plano en R³.")
        else:
            print("Representa un hiperplano.")
        print(" ")
        nota = "Nota: Esta función analiza una sola ecuación lineal. Para sistemas, use la opción 'Sistemas' del menú."
        ancho = len(nota) + 2
        print(f"┌{'─'*ancho}┐")
        print(f"│ {nota} │")
        print(f"└{'─'*ancho}┘")
        print(" ")
        print("┌" + "─"*30 + "┐")
        print("│" + " TIPO DE RECTA (2 VARIABLES) ".center(30) + "│")
        print("└" + "─"*30 + "┘")        
        print(" ")
        if n == 2:
            x, y = variables
            poly = Poly(expr, x, y)
            a = poly.coeff_monomial(x)
            b = poly.coeff_monomial(y)
            if b == 0 and a != 0:
                print("Tipo de gráfica: Recta vertical.")
            elif a == 0 and b != 0:
                print("Tipo de gráfica: Recta horizontal.")
            elif a != 0 and b != 0:
                print("Tipo de gráfica: Recta oblicua.")
            else:
                print("Tipo de gráfica: No se puede determinar.")
        print(" ")
        print("┌" + "─"*30 + "┐")
        print("│" + " GRAFICACIÓN ".center(30) + "│")
        print("└" + "─"*30 + "┘")        
        print(" ")
        if n == 2:
            try:
                x, y = variables
                poly = Poly(expr, x, y)
                a = poly.coeff_monomial(x)
                b = poly.coeff_monomial(y)
                if b != 0:
                    sol_y = solve(expr, y)
                    f = lambdify(x, sol_y[0], "numpy")
                    xs = np.linspace(-10, 10, 200)
                    ys = f(xs)
                    plt.plot(xs, ys)
                elif a != 0:
                    sol_x = solve(expr, x)
                    if sol_x:
                        x_val = float(sol_x[0])
                        ys = np.linspace(-10, 10, 200)
                        xs = np.full_like(ys, x_val)
                plt.plot(xs, ys)
                plt.plot(xs, ys)
                plt.grid()
                plt.title("Gráfica")
                plt.show()
            except Exception as e:
                print("No se ha podido graficar: ", e)
        elif n == 3:
            try:
                variables = sorted(variables, key=lambda v: v.name)
                x, y, z = variables
                sol_z = solve(expr, z)
                if sol_z:
                    f = lambdify((x, y), sol_z[0], "numpy")
                    xs = np.linspace(-5, 5, 30)
                    ys = np.linspace(-5, 5, 30)
                    X, Y = np.meshgrid(xs, ys)
                    Z = f(X, Y)
                    fig = plt.figure()
                    ax = fig.add_subplot(111, projection="3d")
                    ax.plot_surface(X, Y, Z)
                    plt.show()
            except Exception as e:
                print("No se ha podido graficar: ", e)
        if not desea_continuar("¿Desea seguir realizando ecuaciones lineales de dos incógnitas? (s/n): "):
            break
                
        
    
            
                






if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    imprimir_banner_diagonal_bandas("Laskinainen.Beta")
    Calculadora()