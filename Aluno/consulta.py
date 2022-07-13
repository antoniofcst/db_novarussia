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
sqlConsulta = 'SELECT  Nome_Curso, Cod_Curso FROM Aluno, Curso WHERE Aluno.Cod_Curso = Curso.Cod_Curso'

# utilizando método execute
cursor.execute(sqlConsulta)

registroConsulta = cursor.fetchall() # obtemos todos os dados
print(registroConsulta)

# encerrando conexão
cursor.close()
conexao.close()