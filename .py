# função para somar uma lista de números
def soma(numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    if(resultado != round(resultado)):
        print(f'{float(resultado)} é um número decimal!')
    elif (resultado%2) == 0:
        print("Par")
    else:
        print("Ímpar")
    if(resultado > 0):
        print(f'Positivo')
    else:
        print("Negativo")
    return resultado

# função para subtrair uma lista de números
def subtrai(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        resultado -= numeros[i]
    if(resultado != round(resultado)):
        print(f'{float(resultado)} é um número decimal!')
    elif (resultado%2) == 0:
        print("Par")
    else:
        print("Ímpar")
    if(resultado >= 0):
        print(f'Positivo')
    else:
        print("Negativo")
    return resultado

# função para multiplicar uma lista de números
def multiplica(numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    if(resultado != round(resultado)):
        print(f'{float(resultado)} é um número decimal!')
    elif (resultado%2) == 0:
        print("Par")
    else:
        print("Ímpar")
    if(resultado >= 0):
        print(f'Positivo')
    else:
        print("Negativo")
    return resultado

# função para dividir uma lista de números
def divide(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        if numeros[i] == 0:
            return "Não é possível dividir por zero"
        else:
            resultado /= numeros[i]
        if(resultado != round(resultado)):
           print(f'{float(resultado)} é um número decimal!')
        elif (resultado%2) == 0:
           print("Par")
        else:
          print("Ímpar")
        if(resultado >= 0):
          print(f'Positivo')
        else:
           print("Negativo")
    return resultado


# exibe as opções de operação para o usuário
print("Selecione a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# solicita ao usuário que selecione uma opção
opcao = input("Digite sua opção (1/2/3/4): ")

# solicita ao usuário que informe os números a serem calculados
numeros = input("Digite os números separados por vírgula: ")
numeros = [float(numero) for numero in numeros.split(",")]

# realiza a operação selecionada pelo usuário
if opcao == '1':
    print("Resultado da soma:", soma(numeros))
elif opcao == '2':
    print("Resultado da subtração:", subtrai(numeros))
elif opcao == '3':
    print("Resultado da multiplicação:", multiplica(numeros))
elif opcao == '4':
    print("Resultado da divisão:", divide(numeros))
else:
    print("Opção inválida")
