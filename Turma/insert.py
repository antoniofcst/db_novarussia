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
sqlInsert = 'INSERT INTO Turma(cod_curso, cod_turma , periodo, data_inicio, data_fim) VALUES(%s, %s, %s, %s, %s, %s)'
# entrada de dados do usuário para popular a tabela
cod_curso = input('Código do curso: ')
cod_turma = input('Código da turma: ')
periodo = input('Período: ')
data_inicio = input('Data de início: ')
data_fim = input('Data fim: ')

# coleção de dados
dados = (cod_curso, cod_turma, periodo, data_inicio, data_fim)

cursor.execute(sqlInsert, dados)
# salvar registro 
conexao.commit()
# registro inserido
registroInsert = cursor.rowcount
print(f'Registro inserido: {registroInsert}')


# encerrando conexão

cursor.close()
conexao.close()