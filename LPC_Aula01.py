class Projeto:
    def __init__(self, nome, data_inicio, data_fim): 
        self.nome = nome
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        
    def __str__(self):
        return "| Projeto: "+ self.nome+ ' Data inicio: '+ self.data_inicio+ ' Data Fim '+ self.data_fim + ' | '
        
class Pessoa:
    def __init__(self, data_nascimento, nome):
        self.data_nascimento = data_nascimento
        self.nome = nome

    def __str__(self):
        return "| Pessoa: "+ self.nome + ' Data de Nascimento: ' +self.data_nascimento +' | '

class Atividade:
    status = 'ATV. ATIVA'
    def __init__(self, nome, prioridade, pessoa, projeto ):
        self.nome = nome
        self.prioridade = prioridade
        self.pessoa = pessoa
        self.projeto = projeto
        
    def finalizar_atividade(self):
        self.status = 'ATV. FINALIZADA'

proj = Projeto ('Projeto AAAA', '12/12/2018', '12/12/2019')
p = Pessoa('25/01/1993', 'Bruno')
a = Atividade('teste', 1, p, proj)
a. finalizar_atividade()
print (a.nome, a.prioridade, a.pessoa, a.projeto,  a.status)

