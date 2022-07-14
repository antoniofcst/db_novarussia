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
sqlConsulta = 'SELECT * FROM Departamento WHERE cod_departamento=%s' 
# solicitar dados do usuário 
cod_departamento = input('Digite o código do departamento: ')
# utilizando método execute
cursor.execute(sqlConsulta, cod_departamento)

# mostrar resultado
registroConsulta = cursor.fetchone() 
print(registroConsulta)


# encerrando conexão

cursor.close()
conexao.close()