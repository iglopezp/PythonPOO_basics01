class Pessoa:

    def __init__(self, nome, idade, dormir=False, trabalhar=False, treinar=False):

        self.nome = nome
        self.idade = idade
        self.dormir = dormir
        self.trabalhar = trabalhar
        self.treinar = treinar

        print(f'Seja bem-vindo {self.nome}')
    
    def sleep(self):
        if self.dormir:
            print(f'{self.nome} já está dormindo')
            return
        if self.trabalhar:
            print(f'{self.nome} está trabalhando, não pode dormir agora')
            return
        if self.treinar:
            print(f'{self.nome} está no treino, não pode dormir agora')
            return
        print(f'{self.nome} foi dormir')
        self.dormir = True

    def wake_up(self):
        if not self.dormir:
            print(f'{self.nome} já está acordado')
            return
        if self.trabalhar:
            print(f'{self.nome} já está acordado, e está trabalhando')
            return
        if self.treinar:
            print(f'{self.nome} já está acordado, esta treinando')
            return
        print(f'{self.nome} acordou!!')
        self.dormir = False     
        