#Busque na fraze quantas letras 'a' foram digitadas. A posição da primeira e da ultima.
word = str(input('Digite uma fraze qualquer: '))
word.lower()
print(f"A fraze tem {word.count('a')}, letras 'a'")
print(word.find('a'))
print(word.rfind('a'))
#Malandragem é mato