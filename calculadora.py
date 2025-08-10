def main():
    print("Hola, aprendices!\n")

def addmultiplenumbers():
    num1=int(input("Dame un numero "))
    num2=int(input("Dame otro numero "))
    return num1+num2

def multiplymultiplenumbers():
    num1=int(input("Dame un numero "))
    num2=int(input("Dame otro numero "))
    return num1*num2

def isiteven():
    num1=int(input("Dame un numero "))
    if (num1%2==0):
        return ("Tu numero es par")
    else :
        return("Tu numero es impar")

def isitaninteger(num):
    try:
        num=float(input("Dame un numero con o sin decimales "))
        return "Tiene decimales" if "." in str(num) else "No tiene decimales"
    except:
        return "Error: entrada no valida"

main ()

operacion= int(input("Que quieres hacer? " \
"Sumar:1 " \
"Multiplicar:2 " \
"Numero par o impar:3 " \
"Tiene punto decimal:4"))
if operacion==1:
    print("Resultado", addmultiplenumbers())
elif operacion==2:
    print("Resultado", multiplymultiplenumbers())
elif operacion ==3:
    print(isiteven())
elif operacion ==4:
    print(isitaninteger(None))
else :
    print("Tu operacion no es valida")