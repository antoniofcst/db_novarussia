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
sqlInsert = 'INSERT INTO Departamento(nome_departamento, cod_departamento) VALUES(%s, %s)'

# entrada de dados do usuário para popular a tabela
nome_departamento = input('Nome do departamento: ')
cod_departamento = input('Código cadastral: ')

# coleção de dados
dados = (nome_departamento,cod_departamento)

cursor.execute(sqlInsert, dados)

# salvar registro 
conexao.commit()

# registro inserido
registroInsert = cursor.rowcount
print(f'Registro inserido: {registroInsert}')


# encerrando conexão

cursor.close()
conexao.close()