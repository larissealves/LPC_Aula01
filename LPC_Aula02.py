#LPC_AULA02 - HERANÇA
class Pessoa: '''EVENTO PODE TER VÁRIAS PESSOAS | UMA PESOA SÓ PODE TER UM EVENTO'''
    def __init__(self, nome):
        self.nome = nome
        
class Pessoajuridica(Pessoa):
    def __init__(self, cnpj):
        super().__init__(nome)
        self.cnpj = cnpj
        
class PessoaFisica(Pessoa):
    def __init__(self, cpf, idade):
        super().__init__(nome)
        self.cpf = cpf
        self.idade = idade
        
class Autor(PessoaFisica):
    def __init__(self, publicacao):
        super().__init__(cpf, idade)
        self.publicacao = publicacao
        
class Artigo:   ''' Artigos e autor é de Muitos para Muitos'''
    def __init__(self, dataPublicacao):
        self.data_publicacao = dataPublicacao

class AutorPublicacao:
    def __init__(autor, artigo):
        self.autor = autor
        self.artigo = artigo
        
   
art = Artigo ('01/01/2018')
aut = Autor (' ')
