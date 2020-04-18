from typing import List
from collections.abc import Sized


class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    # Representação textual do objeto
    def __str__(self):
        return f'{self._nome} - {self.ano} - {self._likes} Likes'

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.__duracao = duracao

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.__duracao} min - {self._likes} Likes')


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.__temporada = temporadas

    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.__temporada} temporadas - {self._likes} Likes')


class Playlist(Sized):
    def __init__(self, nome, programas: List[Programa]):
        self.nome = nome
        self._programas = programas

    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)


f = Filme('Vingadores', 2018, 200)
s = Serie('Atlanta', 2017, 2)
p = Playlist('Minha playlist', [f, s])
print(len(p))
