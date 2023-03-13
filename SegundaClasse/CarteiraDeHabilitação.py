import datetime

class CarteiraDeHabilitacao:
    
    def __init__(self, nome, cpf, categoria, pontos, validade):
        self.nome = nome
        self.cpf = cpf
        self.categoria = categoria
        self.pontos = pontos
        self.validade = validade
    
    def pegar_nome(self):
        return self.nome
    
    def pegar_cpf(self):
        return self.cpf
    
    def pegar_categoria(self):
        return self.categoria
    
    def definir_categoria(self, nova_categoria):
        self.categoria = nova_categoria
    
    def pegar_pontos(self):
        return self.pontos
    
    def definir_pontos(self, novos_pontos):
        self.pontos = novos_pontos
    
    def pegar_validade(self):
        return self.validade.strftime("%d/%m/%Y")
    
    def renovar_validade(self, anos):
        self.validade += datetime.timedelta(days=anos*365)


def main():

    nome = 'Marcelo Vinicius'
    cpf = '892.031.543-41'
    pontos = 10
    categoria = 'A'
    validade = datetime.date.today()
    carteira = CarteiraDeHabilitacao(nome, cpf, pontos, categoria, validade)


    print(f'\nO Nome do proprietário da Carteira de Habilitação é {nome}')
    print(f'O CPF do proprietário é {cpf}')
    print(f'Você possui atualmente {pontos} pontos em sua Carteira de Habilitação')
    print(f"Você possui atualmente categoria '{categoria}' em sua Carteira de Habilitação")
    print(f'Esta é a validade atual da sua Carteira de Habilitação {carteira.pegar_validade()}.\n')


    carteira.definir_pontos(7)
    carteira.definir_categoria('B')
    carteira.renovar_validade(5)

    print(f'O Nome do proprietário da Carteira de Habilitação é {nome}')
    print(f'O CPF do proprietário é {cpf}')
    print(f'Agora você possui mais {carteira.pontos} pontos em sua Carteira de Habilitação')
    print(f"Você agora possui a categoria '{carteira.categoria}' em sua Carteira de Habilitação")
    print(f'Esta é a nova validade da Carteira de Habilitação {carteira.pegar_validade()}.\n')


if __name__ == '__main__':
    main()
