def suma(a: float, b: float) -> float:
    """Retorna la suma de dos números."""
    return a + b


def resta(a: float, b: float) -> float:
    """Retorna la resta de dos números."""
    return a - b


def multiplicacion(a: float, b: float) -> float:
    """Retorna la multiplicación de dos números."""
    return a * b


def division(a: float, b: float) -> float | str:
    """Retorna la división de dos números. Retorna un mensaje de error si b es cero."""
    if b == 0:
        return "Error: División por cero"
    return a / b


def main():
    print("Hello from is3-clase-versionado-26!")
    env = setup()
    print(f"Trabajando en entorno: {env}")
    operacion = "X"
    print("Selecciona una operación para que sea realizada: +, -, *, /")
    operacion = input("Ingrese la operación: ") 
    if operacion == "+":
        result = suma(5, 3)
        print(f"La suma de 5 y 3 es: {result}")
    elif operacion == "-":
        result = resta(5, 3)
        print(f"La resta de 5 y 3 es: {result}")
    elif operacion == "*":
        result = multiplicacion(5, 3)
        print(f"La multiplicación de 5 y 3 es: {result}")
    elif operacion == "/":  
        result = division(5, 3)
        print(f"La división de 5 y 3 es: {result}")


def setup():
    env = "dev"
    return env


if __name__ == "__main__":
    main()
    Principal()