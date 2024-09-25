# Crie um programa que receba vários números do usuário e some-os até que o número 0 seja digitado, momento em que o programa deve exibir o valor total.
# Inicializa a soma
soma = 0

# Loop para receber números do usuário
while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    # Verifica se o número é 0
    if numero == 0:
        break  # Sai do loop se 0 for digitado
    
    # Adiciona o número à soma
    soma += numero

# Exibe o valor total
print(f"A soma total dos números digitados é {soma}.")