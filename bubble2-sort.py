import matplotlib.pyplot as plt


lista = [11, 18, 3, 1, 16, 12, 6, 19, 5, 0, 14, 4, 17, 9, 13, 7, 10, 15, 2, 8]

 # contar o numero de elementos da lista
#print(N) mostrar o numero de elementos da lista
print("Lista Original:", lista) # mostrar a lista original
#for i in range(0, N - 1, 1): # iterar o i sobre a lista
    #for j in range(i + 1, N, 1): # iterar o j sobre a lista
        #if lista[i] < lista[j]:
            #temp = lista[i]
            #lista[i] = lista[j]
            #lista[j] = temp
#print("Cinco maiores valores:", lista[0 : 5])
#print("Cinco menores valores:", lista[N - 5 : N])
#print("Lista em ordem decrescente:", lista)
N = len(lista)
plt.figure()
plt.plot(range(0, N, 1), lista, 'ok')
plt.title("Lista original")
plt.xlabel("Indice")
plt.ylabel("Valor")
plt.savefig("fig/grafico-inicial.png")
plt.savefig("fig/grafico-fim.png")
plt.close()
troca = 0
for i in range(0, N - 1, 1):
    for j in range(i + 1, N, 1):
        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
            troca = troca + 1
            plt.figure()
            plt.plot(range(0, N), lista, 'ok')
            plt.plot(i, lista[i], 'or')
            plt.plot(j, lista[j], 'ob')
            plt.title("Principio")
            plt.xlabel("Indice")
            plt.ylabel("valor")
            plt.savefig("fig/grafico-troca-{}.png".format(troca))
            plt.close()
for i in range(0, N - 1, 1):
    for j in range(i + 1, N, 1):
        if lista[i] > lista[j]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
print("Lista em ordem crescente:", lista)
print("cinco maiores valores:", lista[N - 5 : N])
print("Cinco menores valores:", lista[0 : 5])


