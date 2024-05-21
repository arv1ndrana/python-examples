def sorta(lista):
    for j in range(len(lista)):
        for i in range(len(lista) - 1):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]

    return lista

result = sorta([4,2,1,3,128, 5,10,123])

print(result) # I am so happy right now
