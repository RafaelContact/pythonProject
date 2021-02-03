#leia o nome de uma pessoa, e exiba separadamente o primeiro e o ultimo.
name = str(input('Digite seu nome completo: '))
list = name.split()
print(list.pop(0), list.pop())
print('Bora comitar')