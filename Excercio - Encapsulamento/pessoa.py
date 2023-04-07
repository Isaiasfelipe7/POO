class Pesssoa:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        a = self.__nome.split(' ')
        b = nome.split(' ')
        if a[0] ==  b[0]:
            self.__nome = nome
        else:
            print('O primeiro nome não pode ser alterado.')

eu = Pesssoa('Isa')
print(eu.nome)
eu.nome = 'Isa de lima'
print(eu.nome)
eu.nome = 'maria'
print(eu.nome)