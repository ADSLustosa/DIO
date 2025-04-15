MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input('Digite sua idade: '))

if idade >= MAIOR_IDADE:
    print('Você pode tirar a CNH')

elif idade >= IDADE_ESPECIAL and idade < MAIOR_IDADE:
    print('Você pode tirar a CNH, mas não pode dirigir veículos de transporte coletivo.')

else:
    print('Você é menor de idade. Não pode tirar a CNH!')

print('Fim do programa!')

