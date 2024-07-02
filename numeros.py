# SOMA E MEDIA DOS NUMEROS DIGITADOS  
soma = 0
quantidade =0 

while True:
    numero = int(input('Digite um numero (digite 0 para finalizar): '))
    if numero == 0:
        break
    soma += numero
    quantidade += 1
    media = soma/quantidade



print(f'voce digitou {quantidade} numeros, \n a soma dos numeros que voce digitou foi {soma} \n a media dos numeros que voce digitou foi {media} ')