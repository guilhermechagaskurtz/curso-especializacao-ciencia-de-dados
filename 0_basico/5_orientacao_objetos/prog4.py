#w3school é a referência para Python

from random import randint
from . import Util

class Pessoa:
    #construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def sono(self):
        return self.idade / 3


class Aluno(Pessoa):
    #construtor
    def __init__(self, matricula, nome, idade):
        self.matricula = matricula
        # Pessoa.__init__(nome, idade)
        super().__init__(nome, idade)
 
    #sobreescrevendo o toString do python
    def __str__(self):
        return "Nome: " + self.nome + " - Idade: " + str(self.idade) + " - Matrícula: " + str(self.matricula)
    
    #sobreescrevendo o equivalente ao equals do java
    def __lt__(self, object):
        return self.idade < object.idade
        
        
    
lista = []
quantidade = int(input("Quantos alunos quer cadastrar? "))
Util.__popular__(lista, quantidade)
Util.__exibir__(lista)
print("O aluno mais novo é ", Util.__descobre_mais_novo__(lista))
# lista.sort()
# print("Exibindo ordenada por idade")
# Util.__exibir__(lista)




