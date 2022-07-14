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
sqlConsulta = 'SELECT * FROM Turma WHERE cod_turma=%s' 
# solicitar dados do usuário 
cod_turma = input('Digite o código da turma: ')
# utilizando método execute
cursor.execute(sqlConsulta, cod_turma)

# mostrar resultado
registro = cursor.fetchone() 
print(registro)

# encerrando conexão

cursor.close()
conexao.close()