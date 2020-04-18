def teste():
    print("Teste")


def teste2():
    print("Teste 2")


functions = [
    teste,
    teste2
]

for func in functions:
    if type(func) == 'function':
        func()
