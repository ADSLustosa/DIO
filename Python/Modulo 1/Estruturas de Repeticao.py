import unidecode 

texto = input('Digite um texto: ')
VOGAIS = "AEIOU"

#REPETIÇÃO COM FOR INTERÁVEL
for letra in texto:
    if unidecode.unidecode(letra.upper()) in VOGAIS:
        print(letra.upper(), end=' ')
        print()

#REPETIÇÃO COM FOR RANGE
for numero in range(0, 51, 5):
    print(numero, end=' ')
    print()


    
