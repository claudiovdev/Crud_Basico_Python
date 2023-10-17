import mysql.connector

conexao = mysql.connector.Connect(
    host= 'localhost',
    user='root',
    password='root123',
    database='db-crud-python'
)

cursor = conexao.cursor()

#CRUD

##CREATE
'''
nome_produto = "CAMISA"
valor_produto = 10
comando = f'INSERT INTO tb_vendas01 (nome_produto, valor_produto) VALUES ("{nome_produto}", {valor_produto})'
cursor.execute(comando)
conexao.commit()
'''

##READ
'''
comando = 'SELECT * FROM tb_vendas01'
cursor.execute(comando)
resultado = cursor.fetchall()
print(resultado)
'''

##UPDATE
'''
nome_produto_novo = "Tenis"
comando = f'UPDATE  tb_vendas01 SET nome_produto = "{nome_produto_novo}" WHERE id_produto = 1'
cursor.execute(comando)
conexao.commit()
'''


##DELETE
'''
comando = 'DELETE FROM tb_vendas01 WHERE id_produto = 1'
cursor.execute(comando)
conexao.commit()
'''

cursor.close()
conexao.close()
