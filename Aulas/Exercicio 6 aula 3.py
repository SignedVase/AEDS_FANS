us = str(input('Informe o nome: ')).lower()
sen = str(input('Informe a senha: ')).lower()
while us == sen:
    print('Por favor, informe novamente!')
    us = str(input('Informe o nome: ')).lower()
    sen = str(input('Informe a senha: ')).lower()
print('Usuario criado com sucesso!')