from fractions import Fraction
import math
import numpy as np
from sklearn.linear_model import LinearRegression

def sumatoria ():
    num1sum = float(input("primer número: "))
    num2sum = float(input("segundo número: "))
    num3sum = float(input("tercer número: "))
    result1 = num1sum + num2sum + num3sum
    print("Su operacion equivale a: ", result1)

def Resta ():
    num1rest = float(input("primer número: "))
    num2rest = float(input("segundo número: "))
    num3rest = float(input("tercer número: "))
    result2 = num1rest - num2rest - num3rest
    print("Su operacion equivale a: ", result2)

def Multiplicacion ():
    num1mul = float(input("primer numero: "))
    num2mul = float(input("segundo numero: "))
    num3mul = float(input("tercer numero: "))
    result3 = num1mul * num2mul * num3mul
    print("Su operacion equivale a: ", result3)

def Division ():
    num1div = float(input("primer numero: "))
    num2div = float(input("segundo numero: "))
    if num2div == 0:
        print("Error: No se puede dividir entre cero.")
        return
    result4 = num1div / num2div
    print("Su operacion equivale a: ", result4)

def Porcentaje ():
    num1por = float(input("primer numero: "))
    num2por = float(input("segundo numero: "))
    result5 = (num1por * num2por) / 100
    print("Su operacion equivale a: ", result5)

def fraccion():
    print("Crear fracciones")
    a1 = int(input("Fracción A1: "))
    b1 = int(input("Fracción B1: "))
    f1 = Fraction(a1, b1)

    a2 = int(input("Fracción A2: "))
    b2 = int(input("Fracción B2: "))
    f2 = Fraction(a2, b2)

    print("\n1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    opcion = int(input("Elija operación: "))

    if opcion == 1:
        print("Resultado:", f1 + f2)
    elif opcion == 2:
        print("Resultado:", f1 - f2)
    elif opcion == 3:
        print("Resultado:", f1 * f2)
    elif opcion == 4:
        print("Resultado:", f1 / f2)
    else:
        print("Opción inválida")

def Potencia ():
    num1pot = float(input("Ingrese la base: "))
    num2pot = float(input("Ingrese el exponente: "))
    result6 = num1pot ** num2pot
    print("su potencia equivale a: ", result6)

def Raizcuadrada ():
    numraiz = float(input("Ingrese el radicando: "))
    if numraiz < 0:
        print("Error: No se puede calcular raíz cuadrada de un número negativo.")
        return
    result8 = math.sqrt(numraiz)
    print("Su raíz equivale a: ", result8)

def Seno ():
    angulo1 = float(input("Ingrese el ángulo: "))
    result9 = math.sin(math.radians(angulo1))
    print("El seno de tu ángulo es: ", result9)

def Cos ():
    angulo2 = float(input("Ingrese el ángulo: "))
    result10 = math.cos(math.radians(angulo2))
    print("El coseno de tu ángulo es: ", result10)

def Tan ():
    angulo3 = float(input("Ingrese el ángulo: "))
    if angulo3 >= 90:
        print("Error: Ángulo mayor a 90°. No es posible calcular en tangente.")
        return
    result11 = math.tan(math.radians(angulo3))
    print("La tangente de tu ángulo es: ", result11)

def Cdm ():
    cmdlist = [float(n) for n in input("Ingrese datos (dato por separado): ").split()]
    if not cmdlist:
        print("no ingresó datos.")
        return
    result12 = sum(cmdlist) / len(cmdlist)
    print("El cálculo de media que realizó es: ", result12)

def DevEst ():
    DevEstList = [float(n) for n in input("Ingrese datos (dato por separado): ").split()]
    result13 = np.std(DevEstList)
    print("La desviación estándar es de: ", result13)

def Varianza ():
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

def RegLin ():
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


print("\n****************** CALCULADORA ********************")
print("1)Calculos estándar (+/-/x/÷/%/—/x²/√)")
print("2)Calculos científicos (sin(cos/tan/log/∛/in/xʸ/eˣ/π))")
menu1 = int(input("\nEliga el tipo de cálculo que quiere realizar: "))

if menu1 == 1:
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicación")
    print("4) División")
    print("5) Porcentaje")
    print("6) Fracción")
    print("7) Potencia")
    print("8) Raíz cuadrada")
    menuCE = int(input("\nEliga el tipo de operación que quiere realizar: "))
    if menuCE == 1:
        sumatoria()
    elif menuCE == 2:
        Resta()
    elif menuCE == 3:
        Multiplicacion()
    elif menuCE == 4:
        Division()
    elif menuCE == 5:
        Porcentaje()
    elif menuCE == 6:
        fraccion()
    elif menuCE == 7:
        Potencia()
    elif menuCE == 8:
        Raizcuadrada()
elif menu1 == 2:
    print("¿Qué tipo de función avanzada desea realizar?")
    print("1) Trigonometría")
    print("2) Estadistica/Probabilidades")
    print("3) Logarítmica/Exponenciales")
    print("4) conversión y notación científica")
    menu1C = int(input("\nEliga el tipo de función avanzada que quiere realizar: "))
    if menu1C == 1:
        print("1) Seno (sen, Cateto opuesto/Hipotenusa)")
        print("2) Coseno (cos, Cateto adyancente/Hipotenusa)")
        print("3) Tangente (tan, Cateto opuesto/Cateto adyacente)")
        menuT = int(input("Elija que relación trigonometrica quiere elegir: "))
        if menuT == 1:
            Seno()
        elif menuT == 2:
            Cos()
        elif menuT == 3:
            Tan()
        else:
            print("Opción no existente.")
    elif menu1C == 2:
        print("1) Cálculo de media (promedio)")
        print("2) Desviación estándar")
        print("3) Varianza")
        print("4) Regresión lineal")
        print("5) Cuadrática")
        print("6) Exponencial")
        print("7) Premutaciones (nPr)")
        print("8) Combinaciones (nCr)")
        print("9) Factorial (!)")
        menu1EP = int(input("\Elija que operacion Estadística/probabilidades le gustaría realizar: "))
        if menu1EP == 1:
            Cdm()
        elif menu1EP == 2:
            DevEst()
        elif menu1EP == 3:
            Varianza()
        elif menu1EP == 4:
            RegLin()







