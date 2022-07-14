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
sqlInsert = 'INSERT INTO Professor(cod_professor, nome_professor, sobrenome_professor) VALUES(%s, %s, %s)'

# entrada de dados do usuário para popular a tabela
cod_professor = input('Codigo de matrícula: ')
nome_professor = input('Nome: ')
sobrenome_professor = input('Sobrenome: ')
# coleção de dados
dados = (cod_professor, nome_professor, sobrenome_professor)

cursor.execute(sqlInsert, dados)

# salvar registro 
conexao.commit()

# registro inserido
registroInsert = cursor.rowcount
print(f'Registro inserido: {registroInsert}')
# mostrar resultado
registroConsulta = cursor.fetchall() # obtemos todos os dados
print(registroConsulta)

# encerrando conexão

cursor.close()
conexao.close()