import array as py_arr
import numpy as np

# python array, raramente utilizado
py_arr = py_arr.array('d', [1.5, 2, 3, 4.5])

# numpy array
np_array = np.array([1.5, 2, 3, 4.5])

print(py_arr, np_array)

idades = [15, 87, 32, 65, 56, 32, 49, 37]

# ordem crescente
idades = sorted(idades)  # funcional
idades.sort()  # mutável/oo

# ordem decrescente
idades = list(reversed(idades))
idades = sorted(idades, reverse=True)
idades.sort(reverse=True)

for i in range(len(idades)):
    print(i, idades[i])

for index, value in enumerate(idades):
    print(index, value)

# forçando geração dos valores
list_range = list(range(0, len(idades)))

print(list_range)

usuarios = [
    ('Guilherme', 37, 1981),
    ('Daniela', 31, 1987),
    ('Paulo', 39, 1979)
]

# Desempacotando tupla
for nome, idade, ano in usuarios:
    print(f"Nome: {nome}, Idade: {idade}, Ano nascimento: {ano}")
