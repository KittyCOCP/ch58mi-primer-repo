# importar request
import requests
def trivago(number):
    # Realizar una petición GET a la API de NumbersApi añadir el numero ingresado a la API
    trivia_fetch = requests.get(f"http://numbersapi.com/{number}?json")

    # imprimir el código de estado de la respuesta, se espera 200
    # para una peticion exitosa se espera un código 200
    print("Codigo de estado:",trivia_fetch.status_code)

    # convertir el contenido en la respuesta a formato JSON
    # y almacenarlo en una variable
    trivia = trivia_fetch.json()
    print("Información de la trivia", trivia)
    print("Mensaje de la trivia", trivia['text'])
    print("Numero de la trivia", trivia['number'])
# Bloque principal
if __name__ == "__main__":
    #Pedir un numero al usuario
    number=input("Ingrese un numero: ")
    print("numero ingresado: ", number)
    # Llamar a la funcion pasando el numero
    trivago(number) # Debo llamar a la función con paréntesis


