class Pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado='vivo(a)', estado_civil='solteiro(a)', conjuge=None):
        self.__nome = nome
        self.__idade = idade
        self.peso = peso
        self.altura = altura
        self.__sexo = sexo
        self.estado = estado
        self.estado_civil = estado_civil
        self.conjuge = conjuge

    def __str__(self):
        return f'\nNome: {self.__nome}    Idade: {self.__idade}     Peso: {self.peso}   Altura:{self.altura}    Sexo: {self.__sexo}     Estado: {self.estado}   Estado Civil: {self.estado_civil}'
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        print('\nSem Permissão!')

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, valor):
        print('\nSem Permissão!')

    def peso(self):
        return self.peso

    def altura(self):
        return self.altura

    @property
    def sexo(self):
        return self.__sexo

    @sexo.setter
    def sexo(self, valor):
        print('\nSem Permissão!')

    def estado(self):
        return self.estado

    def estado_civil(self):
        return self.estado_civil

    def conjuge(self):
        return self.conjuge

    def envelhecer(self):
        if self.estado == 'vivo(a)':
            self.__idade += 1

            if self.__idade < 21:
                self.altura += 0.5
                print(f'\n{self.__nome} está com {self.__idade} anos e {self.altura} cm de altura.')
        else:
            print(f'\nOperação não realizada. {self.__nome} está morto(a).')
        
    def engordar(self, engordar):
        if self.estado == 'vivo(a)':
            self.peso += engordar
            print(f'\n{self.__nome} engordou {engordar} kg')
        else:
            print(f'\nOperação não realizada. {self.__nome} está morto(a).')

    def emagrecer(self, emagrecer):
        if self.estado == 'vivo(a)':
            self.peso -= emagrecer
            print(f'\n{self.__nome} emagreceu {emagrecer} kg')
        else:
            print(f'\nOperação não realizada. {self.__nome} está morto(a).')

    def crescer(self, valor):
        if self.estado == 'vivo(a)':
            if self.__idade < 21:
                self.altura += valor

                print(f'\n{self.__nome} cresceu {valor}cm\nAgora sua Altura é {self.altura}')
            else:
                print(f'\n{self.__nome} não pode mais crescer pois está com 21 anos ou mais')
        else:
            print(f'\nEsta pessoa esta morta!')

    def casar(self, conjuge):
        if self.estado == 'vivo(a)':
            if self.__idade < 18:
                print(f'Casamento não permitido. {self.__nome} é de menor.')
            elif self.estado_civil != 'solteiro(a)':
                print(f'\nCasamento não realizado. {self.__nome} é casado.')
            elif conjuge.estado  == 'morto(a)':
                print(f'\nCasamento não realizado. {self.__nome} está morto.')
            else:
                self.estado_civil = 'casado(a)'
                self.conjuge = conjuge
                conjuge.estado_civil = 'casado(a)'
                conjuge.conjuge = self
                
                print(f'\n{self.__nome} está casado com {conjuge.__nome}')
        else:
            print(f'\nCasamento não realizado. {self.__nome} está morto.')

    def morrer(self):
        if self.estado == 'vivo(a)':
            self.estado = 'morto(a)'
            print(f'\n{self.__nome} morreu.')

def main():

    pessoas = [Pessoa('maria', 5, 20, 100, 'F'),
    Pessoa('joão', 12, 40, 140, 'M'), Pessoa('pedro', 22, 65, 170, 'M'),
    Pessoa('bia', 18, 55, 160, 'F'), Pessoa('julia', 30, 65, 170, 'F'),
    Pessoa('carlos', 2, 11, 80, 'M'), Pessoa('jonas', 34, 70, 180, 'M')]

    while True:

        print('\n==== MENU =====')
        print('\n1 - Listar Pessoas ')
        print('2 - Incluir nova pessoa')
        print('3 - Envelhecer')
        print('4 - Crescer')
        print('5 - Engordar')
        print('6 - Emagrecer')
        print('7 - Casar')
        print('8 - Morrer')
        print('9 - Alterar Idade')
        print('0 - Sair ')

        opcao = str(input('\nEscolha um opção: '))

        if opcao == '1':
            if not pessoas:
                print('\n Não há pessoas cadastradas. Tente Novamente!')
            else:
                print(f'\nLista de pessoas: ')

                for i in pessoas:
                   print(f'{i}')

        elif opcao == '2':
            nome = str(input('Nome: ').strip().lower())
            idade = int(input('Idade: ').strip())
            peso = float(input('Peso: ').strip())
            altura = float(input('Altura: ').strip())
            sexo = str(input('Sexo: ').strip())

            pes = Pessoa(nome, idade, peso, altura, sexo)
            pessoas.append(pes)

            print(f'\n{pes.nome} foi adicionado(a) à lista de pessoas.\n')
        
        elif opcao == '3':
            nome = str(input('Nome da pessoa: ').lower())
            ani = input(f'{nome} fez aniversario (S - Sim ou N - Não): ').upper()

            for pessoa in pessoas:
                if pessoa.nome == nome:
                    if ani == 'S':
                        pessoa.envelhecer()
                    else:
                        pessoa.idade = int(input('Idade para atribuir: '))


        elif opcao == '4':
            nome = str(input('Nome da pessoa: ').strip().lower())
            valor = float(input('Valor para crecer: ').strip())

            for pessoa in pessoas:
                if pessoa.nome == nome:
                    pessoa.crescer(valor)

        elif opcao == '5':
            nome = str(input('Nome: ').strip().lower())

            for pessoa in pessoas:
                if pessoa.nome == nome:
                    valor = float(input('Valor: ').strip())
                    pessoa.engordar(valor)

        elif opcao == '6':
            nome = str(input('Nome: ').strip().lower())

            for pessoa in pessoas:
                if pessoa.nome == nome:
                    valor = float(input('Valor: ').strip())
                    pessoa.emagrecer(valor)
            
        elif opcao == '7':
            nome1 = str(input('Nome da 1º pessoa para casar: ').strip().lower())
            nome2 = str(input('Nome da 2º pessoa para casar: ').strip().lower())

            p1 = None
            p2 = None

            for p in pessoas:
                if p.nome == nome1:
                    p1 = p
                elif p.nome == nome2:
                    p2 = p
                if p1 and p2:
                    break

            if not p1:
                print(f'{nome1} não encontrado.')
            elif not p2:
                print(f'{nome2} não encontrado.')
            else:
                if p2.idade < 18:
                    print(f'\nCasamento não permitido. {p2.nome} é de menor.')
                else:
                    p1.casar(p2)
        elif opcao == '8':
            nome = str(input('Nome: ').strip().lower())

            for pessoa in pessoas:
                if pessoa.nome == nome:
                    pessoa.morrer()

        elif opcao == '9':
            nome = str(input('Nome: ').strip().lower())

            for pessoa in pessoas:
                if pessoa.nome == nome:
                    if pessoa.estado == 'morto(a)':
                        print(f'\n{nome} está morto.')
                    else:
                        if pessoa.estado == 'vivo(a)':
                            pessoa.idade = int(input('Atribuir Idade: '))

        elif opcao == '0':
            break
        else:
            print('Opcão inválida. Tente Novamente.')


if __name__ == '__main__':
    main()
