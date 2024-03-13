# Verifica se o número faz parte da sequencia de fibibacci
def esta_sequencia_fibo(num):
    a, b = 0, 1
    while b < num:
        a, b = b, a + b
    return b == num

def main():
    try:
        num = int(input("Digite um número inteiro: "))
        if esta_sequencia_fibo(num):
            print(f"{num} pertence à sequência de Fibonacci.")
        else:
            print(f"{num} não pertence à sequência de Fibonacci.")
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()