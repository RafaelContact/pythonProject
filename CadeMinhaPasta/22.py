# leia o nome de uma pessoa e mostr: Todas mausculas, todas minusculas, quantas letras ao
# todo (sem espaços), quantas letras no priro nome e o nome.
nome = input('Digite um nome completo: ').strip()
print(nome.upper(),' <- Todas as letras maúsculas')
print(nome.lower(), '<- Todas as letras minusculas')
print(f"Tem {len(nome) - nome.count(' ')} letras.")
list = nome.split()
print('O primeiro nome é ', list[0],'e tem', len(list[0]),' letras.')
#Dica, nome.find(' ')

#se não for adicionado o segundo nome a lista vai retornar uma falha aqui.
#O código precisa retornar o valor dos caracteres sem os espaços