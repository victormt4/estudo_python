from collections import defaultdict, Counter

d = {
    'Guilherme': 1,
    'Victor': 2,
    'João': 3
}
print(f'd: {d}')
print(f'João in d: {"João" in d}')

# iterações
print('\niterações:')

for key in d.keys():
    print(f'key: {key}, value: {d[key]}')

for key, value in d.items():
    print(f'key: {key}, value: {value}')

# contando palavras no texto
word_count = {}

text = 'Historicamente causadores de inúmeras vítimas, os acidentes de trânsito vêm ocorrendo com frequência cada vez menor, no Brasil. Essa redução se deve, principalmente, à implantação da Lei Seca ao longo de todo o território nacional, diminuindo a quantidade de motoristas que dirigem após terem ingerido bebida alcoólica . A maior fiscalização, aliada à imposição de rígidos limites e à conscientização da população, permitiu que tal alteração fosse possível'

for word in text.lower().split():
    count = word_count.get(word, 0)
    count += 1
    word_count[word] = count

print(word_count)

# dicionário com valor default
word_count = defaultdict(int)  # int() = 0

for word in text.lower().split():
    word_count[word] += 1

print(word_count)

word_count = Counter(text.lower().split())
print(word_count)
