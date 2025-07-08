class Pessoa:
    def __init__(self, nome, idade, come=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.come = come
        self.falando = falando

    def comer(self, comendo="Maçã"):
        if self.falando:
            print(f'{self.nome} não pode comer falando')
        else:
            print(f'{self.nome} está comendo {comendo}')
            self.come = True
    
    def parar_comer(self):
        if self.come:
            print(f'{self.nome} parou de comer')
            self.come = False
        else:
            print(f'{self.nome} já parou de comer!')
            

    def falar(self, assunto="nada"):
        if self.come:
            print(f'{self.nome} não pode falar comendo')
        else:
            print(f'{self.nome} está falando sobre {assunto}')


    def parar_falar(self):
        if self.falando:
            print(f'{self.nome} parou de falar')
            self.falando = False
        else:
            print(f'{self.nome} já parou de falar')


pessoa = Pessoa("Matheus", 29, True)
pessoa.comer("Banana")
pessoa.parar_comer()
pessoa.falar("Muitas coisas")