class Aluno:
    def __init__(self):
        self.c = 0
        self.a = 0
        self.arquivo = ''
        self.notas = []
        self.alunos = []

    def media(self):
        for linhas in self.arquivo:
            linhas = linhas.replace('\n','')
            linha = linhas.split(':')
            self.notas.append(int(linha[1]))
            self.alunos.append(linha[0])
            self.a += 1
        self.c = sum(self.notas)
        media = self.c / self.a
        print(f'A media dos alunos foi {media}')

    def maior(self):
        maior = max(self.notas)
        print(f"Maior nota: {maior}")

        ind = self.notas.index(maior)
        print(f'Aluno com maior nota: {self.alunos[ind]}')

    def menor(self):
        menor = min(self.notas)
        print(f"Menor nota: {menor}")
        ind = self.notas.index(menor)
        print(f'Aluno com menor nota: {self.alunos[ind]}')

    def execucao(self):
        with open("arquivo1.txt", 'r') as self.arquivo:
            self.media()
        self.arquivo.close()
        self.maior()
        self.menor()
main = Aluno()
main.execucao()