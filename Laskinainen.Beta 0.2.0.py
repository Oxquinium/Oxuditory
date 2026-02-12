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
}
    print(" ")
    print("1) Trigonometría.")
    print("2) Estadística/Probabilidades.")
    print("3) Funciones logarítmicas/exponenciales.")
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
        print("10) Vovler.")
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
        print("4) volver.")
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
        result14Rad = math.asin(angulo4)
        if angulo4 < -1 or angulo4 > 1:
            print("Error: Arcsen solo admite valores entre -1 y 1.")
            return
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
        print("4) volver.")
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
        result16Rad = math.acos(angulo6)
        if angulo6< -1 or angulo6 > 1:
            print("Error: Arcos solo admite valores entre -1 y 1.")
            return
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
        print("4) volver.")
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
        if angulo3 >= 90:
            print("Error: Ángulo mayor a 90°. No es posible calcular en tangente.")
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
            1: Logaritmo10,
            2: LogaritmoN,
            3: Funciones_Exponenciales,
        }
        print(" ")
        print("1) Logaritmos (log).")
        print("2) Logaritmo natural (base e / ln).")
        print("3) Funciones exponenciales (eˣ, 10ˣ).")
        print("4) volver.")
        print(" ")
        op = int(input("Elija la función logarítmica/exponencial que desea realizar: "))
        if op in funciones_LE_menu:
            funciones_LE_menu[op]()
        elif op == 4:
            print("Volviendo atrás...")
            print(" ")
            return
        else:
            print("Opción inválida. Intente de nuevo.")
            print(" ")
            return
    
def Logaritmo10 ():
    while True:
        Numlog = float(input("Ingrese el número que quiera utilizar para su logaritmo: "))
        Logbas = float(input("Ingrese la base del logaritmo: "))
        logresult = math.log(Numlog, Logbas)
        print("Su logaritmo es: ", logresult)
        if not desea_continuar("¿Desea seguir realizando logarítmos? (s/n): "):
            break

def LogaritmoN ():
    while True:
        LogN = float(input("Ingrese el número al que quiera pasar a su logarítmo natural: "))
        LogNresult = math.log(LogN)
        print("su logarítmo natural es: ", LogNresult)        
        if not desea_continuar("¿Desea seguir realizando logarítmos naturales? (s/n): "):
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

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    imprimir_banner_diagonal_bandas("Laskinainen.Beta")
    Calculadora()