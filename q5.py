def inverter_string(s):
    # Inicializa uma string vazia para armazenar o resultado
    resultado = ""
    
    # Percorre a string de trás para frente
    for i in range(len(s) - 1, -1, -1):
        # Adiciona cada caractere à string de resultado
        resultado += s[i]
    
    return resultado

# Exemplo de uso
minha_string = input("Digite o texto: ")
string_invertida = inverter_string(minha_string)
print(f"String original: {minha_string}")
print(f"String invertida: {string_invertida}")
