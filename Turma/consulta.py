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
sqlConsulta = 'SELECT CPF, Cod_Turma FROM Aluno, Turma WHERE Aluno.Cod_Turma = Turma.Cod_Turma' 

# utilizando método execute
cursor.execute(sqlConsulta)

# mostrar resultado
registro = cursor.fetchall() # obtemos todos os dados
print(registro)

# encerrando conexão

cursor.close()
conexao.close()