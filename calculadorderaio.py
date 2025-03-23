import math

def calcular_area_circulo(raio):
    return math.pi * (raio ** 2)

def main():
    raio = 5  # Raio fixo
    area = calcular_area_circulo(raio)
    print(f"A área do círculo com raio {raio} é: {area:.2f}")

if __name__ == "__main__":
    main()
