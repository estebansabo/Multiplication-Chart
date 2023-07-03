# Esta función multiplica x * y

def multiplicar(x, y):
    resultado = x * y
    return resultado


# Esta segunda función ejecuta las preguntas de los números a multiplicar
def main():
    primer_numero = int(input("Ingresa el primer digito: "))
    segundo_numero = int(input("Ingresa el segundo digito: "))

    resultado = multiplicar(primer_numero, segundo_numero)
    print("El resultado es:", resultado)


if __name__ == "__main__":
    main()
    print("Felicidades, haz logrado ejecutar tu primer codigo")
