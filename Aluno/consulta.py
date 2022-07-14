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

# criando sentenças de consulta sql
sqlConsulta = 'SELECT * FROM Aluno WHERE cod_aluno=%s'
# solicitar dados do usuário 
cod_aluno = input('Digite o código do aluno: ')
# utilizando método execute
cursor.execute(sqlConsulta, cod_aluno)

registroConsulta = cursor.fetchone() 
print(registroConsulta)

# encerrando conexão
cursor.close()
conexao.close()