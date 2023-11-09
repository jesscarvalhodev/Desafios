class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print(f'O {self.nome} foi comer...')

    def som(self):
        print(f'O {self.nome} está fazendo um som')

class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f'O {self.nome} foi miando...')

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def som(self):
        print(f'O {self.nome} foi latindo...')


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f'O {self.nome} foi mugindo...')


class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def chiar(self):
        print(f'O {self.nome} foi chiando...')
