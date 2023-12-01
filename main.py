import random

class Jogador:
    def __init__(self, nome, fichas, idade):
        self.__nome = nome
        self.__fichas = fichas
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_fichas(self):
        return self.__fichas

    def set_fichas(self, fichas):
        self.__fichas = fichas

    def get_idade(self):
        return self.__idade


jogador_1 = Jogador("Emanuelle", 237, 18)
jogador_2 = Jogador("Spotify", 213, 17)

print(jogador_1.get_fichas())
print(jogador_2.get_fichas())

