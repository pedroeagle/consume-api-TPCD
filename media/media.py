notas = "6,7,85,1,5,9,7,3,6,7"
notas_array = notas.split(',')
soma = 0
for nota in notas_array:
    soma+=int(nota)
print(soma/len(notas_array))