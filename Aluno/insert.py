# importação do módulo
import psycopg2

# conexão com o banco
conexao = psycopg2.connect(user='postgres', 
                           password='admin',
                           host='127.0.0.1',
                           port='5432',
                           database='NovaRussiaV2')
# utilizando o cursor
cursor = conexao.cursor()

# criando sentença de insert sql
sqlInsert = 'INSERT INTO Aluno(cod_aluno, cod_curso, nome_aluno, sobrenome_aluno, cpf, cod_turma, sexo, contato) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)'

# entrada de dados do usuário para popular a tabela
nome = input('Nome: ')
sobrenome = input('Sobrenome: ')
cpf = input('CPF: ')
sexo = input('Sexo: ')
contato = input('Contato: ')

# coleção de dados
dados = (nome, sobrenome, cpf, sexo, contato)

# utilizando método execute
cursor.execute(sqlInsert, dados)

# salvar registro 
conexao.commit()

# registro inserido
registroInsert = cursor.rowcount
print(f'Registro inserido: {registroInsert}')

# encerrando conexão

cursor.close()
conexao.close()