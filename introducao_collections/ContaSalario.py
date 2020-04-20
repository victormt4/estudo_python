from operator import attrgetter
from functools import total_ordering


@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @property
    def saldo(self):
        return self._saldo

    def __str__(self):
        return f"[>>Codigo {self._codigo} Saldo {self._saldo}<<]"

    def __eq__(self, other):
        return self._codigo == other._codigo

    # lt = less than
    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        else:
            return self._codigo < other._codigo


# Comparando objetos, necessário implementar o __eq__
ca, cb = ContaSalario(100), ContaSalario(100)
print(ca == cb)
print(ca in [cb])

c1, c2, c3 = ContaSalario(1), ContaSalario(2), ContaSalario(3)

c1.deposita(100)
c2.deposita(200)
c3.deposita(300)

contas = [c3, c1, c2]


def extrai_saldo(obj):
    return obj.saldo


# Ordenando objetos
contas = sorted(contas, key=extrai_saldo)
contas = sorted(contas, key=lambda obj: obj.saldo)
contas = sorted(contas, key=attrgetter('_saldo'), reverse=True)
contas = sorted(contas, reverse=True)  # Necessário implementar o __lt__ ou __gt__

for conta in contas:
    print(conta)

# Necessário decorar a classe com o @total_ordering
print(f"{c1} < {c2}: {c1 < c2}")
print(f"{c2} >= {c3}: {c2 >= c3}")
