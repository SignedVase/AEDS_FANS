class Consulta:
    def __init__(self):
        self.alunos = {}
        self.arquivo = ''
    def dicAl(self):
        for linhas in self.arquivo:
            linhas = linhas.replace('\n','')
            linha = linhas.split(':')
            self.alunos.update({linha[0]:linha[1]})
    def consulta(self):
        al = str(input('Informe o nome do aluno que deseja consultar: '))
        try :
            print(f'A nota do aluno foi {self.alunos[al]}')
        except:
            print('Aluno não encontrado')
    def executar(self):
        with open("arquivo1.txt", 'r') as self.arquivo:
            self.dicAl()
        self.arquivo.close()


app = Consulta()
app.executar()
op = 0
while True:
    print('''### Pesquisando notas de alunos ###
 1 - Pesquisar nota aluno
 2 - Sair''')
    try:
        op = int(input('Informe a opção que desejar: '))
    except:
        op = 0
    if op == 1:
        app.consulta()
    if op == 2:
        break
    elif op != 1 and op != 2:
        print('Opção inválida')