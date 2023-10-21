lista = [5, 3, 7, 12, 1]
lista_animal = ['cachorro', 'urso' , 'elefante', 'lobo', 'gato']

nova_lista = lista_animal * 3
#print(lista_animal [1])
#print(sum(lista))
#print(nova_lista)
#lista.sort()
#lista_animal.sort()
#print(lista)
#print(lista_animal)
#lista_animal.reverse()
#print(lista_animal)

#if 'lobo' in lista_animal:
#    print('Existe um lobo na lista.')
#else:
#    print('Não existe lobo na lista. Vou inclui-lo!')
#    lista_animal.append('lobo')
#    print(lista_animal)

#lista_animal.pop(0)
#print(lista_animal)

#lista_animal.remove('elefante')
#print(lista_animal)

#tupla = (1, 12, 14 , 15)
#print(tupla)
#tupla [0] = 12 (Isso não pode ser feito)

tupla_animal = tuple(lista_animal)
print(type(tupla_animal))
print(tupla_animal)
