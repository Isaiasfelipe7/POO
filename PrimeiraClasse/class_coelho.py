class Coelho:
    raça = None
    nome = None
    peso = None
    idade = None

    def mudar_nome(self, nome):
        self.nome = nome

    def engordar(self, peso):
        self.peso += peso

    def envelhecer(self):
        self.idade += 1

mcoelho = Coelho()
mcoelho.nome = "Laranjinha"
mcoelho.peso = 1.5
mcoelho.idade = 1
mcoelho.raça = "Rex"

print(f'O nome atualmente do coelho é {mcoelho.nome}.')
print(f'Seu peso atual é {mcoelho.peso} kg.')
print(f'E sua idade atual é {mcoelho.idade} ano.\n')

mcoelho.mudar_nome("Acerola")
mcoelho.engordar(1)
mcoelho.envelhecer()

print(f'O nome do Coelho agora é {mcoelho.nome}.')
print(f'Seu peso agora é {mcoelho.peso} kg.')
print(f'E sua idade atual é {mcoelho.idade} anos.')
