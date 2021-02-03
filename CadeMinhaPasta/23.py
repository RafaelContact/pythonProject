#leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados. Unidade , dezena , centena e etc.
n = input('Digite um número qualquer de 0 a 9999 : ')
n1 =n.ljust(4)
print(f'Milhar : {n1[3]}')
print(f'Centena : {n1[2]}')
print(f'dezena : {n1[1]}')
print(f'Unidade: {n1[0]}')
#print(n.find(sub=)) também pensei em usar, mas ele busca um valor entre uma parte e outra ? entendi bolinhas
# toda vez que é pesquisado o resultado em uma lista e esse resultado não foi adicionado manualmente retorna o valor como falha


