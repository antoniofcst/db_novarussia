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
sqlConsulta = 'SELECT Carga_Horaria, Cod_Departamento FROM Disciplina, Departamento WHERE Disciplina.Cod_Departamento = Departamento.Cod_Departamento' 

# utilizando método execute
cursor.execute(sqlConsulta)

# mostrar resultado
registroConsulta = cursor.fetchall() # obtemos todos os dados
print(registroConsulta)


# encerrando conexão

cursor.close()
conexao.close()