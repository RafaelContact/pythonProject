#Pergunte o nome de uma cidade e verifique se ela começa ou não com a palavra santo
city = str(input('Digite o nome de sua cidade: '))
list = city.lower().split()
var = list[0]
print(var.find('santo'))