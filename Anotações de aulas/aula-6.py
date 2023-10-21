conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjunto_uniao = conjunto.union(conjunto2)
print(f'União: {conjunto_uniao}')
conjunto_interseccao = conjunto.intersection(conjunto2)
print(f'Intersecção: {conjunto_interseccao}')
conjunto_diferenca = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto)
print(f'Diferença entre 1 e 2: {conjunto_diferenca}')
print(f'Diferença entre 2 e 1: {conjunto_diferenca2}')
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print(f'Diferença simetrica: {conjunto_dif_simetrica}')

#conjunto = {1, 2, 3, 4}
#print(type(conjunto))
#conjunto.add(5)
#conjunto.discard(2)
#print(conjunto)

conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}

conjunto_subset = conjunto_a.issubset(conjunto_b)
print(f'A é um subconjunto de B: {conjunto_subset}')
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(f'B é um superconjunto de A: {conjunto_superset}')

lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']

print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)
