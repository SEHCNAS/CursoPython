Frase = 'Python é uma linguagem'
# Validar se um texto é mebro da frasw
print('py' in Frase)
print('ing' in Frase)
print('ing' not in Frase)
print(len(Frase))

# deixar o texto em minuscula
FraseLower = Frase.lower()
print(FraseLower)

# deixar o texto em maiuscula
FraseUpper = Frase.upper()
print(FraseUpper)

# quebrar o texto
FraseSplit = Frase.split()
print(FraseSplit)

FraseSplit = Frase.split('a')
print(FraseSplit)
