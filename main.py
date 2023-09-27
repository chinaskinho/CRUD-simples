import mysql.connector
from tkinter import *

conexao = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = '1234567890',
    database = 'bdgithub',
)

cursor = conexao.cursor()

#Create
def create():
    nome_produto = str(input('Digite o nome do produto: '))
    valor_produto = int(input('Digite o valor do produto: '))
    comando = f'INSERT INTO vendas (nome_produto, valor_produto) VALUES ("{nome_produto}", "{valor_produto}")'
    cursor.execute(comando)
    conexao.commit()
    resultado = cursor.fetchall()
    cursor.close()
    conexao.close()
    return print('Criado com sucesso!')

#READ
def read():
    comando = 'SELECT * FROM vendas'
    cursor.execute(comando)
    resultado = cursor.fetchall()
    texto_resultado['text'] = resultado
    cursor.close()
    conexao.close()

#UPDATE
def update():
    nome_produto = str(input('Digite o nome do produto: '))
    valor_produto = int(input('Digite o valor do produto: '))
    comando = f'UPDATE vendas SET valor_produto = "{valor_produto}" WHERE nome_produto = "{nome_produto}" '
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    return print('Atualizado com sucesso!')

#DELETE
def delete():
    nome_produto = str(input('Digite o nome do produto: '))
    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}" '
    cursor.execute(comando)
    conexao.commit()
    cursor.close()
    conexao.close()
    return print('Deletado com sucesso!')

janela = Tk()
janela.title('CRUD')
texto_orientacao = Label(janela, text='Qual ação deseja realizar? ')
texto_orientacao.grid(column= 0, row= 0, padx= 10, pady= 10)

botao_create = Button(janela, text='Create', command= create)
botao_create.grid(column=0, row= 1, padx= 10, pady= 10)

botao_update = Button(janela, text='Update', command= update)
botao_update.grid(column=0, row= 2, padx= 10, pady= 10)

botao_read = Button(janela, text='Read', command= read)
botao_read.grid(column=0, row= 3, padx= 10, pady= 10)

botao_delete = Button(janela, text='Delete', command= delete)
botao_delete.grid(column=0, row= 4, padx= 10, pady= 10)

texto_resultado = Label(janela, text='')
texto_resultado.grid(column= 0, row= 5, padx= 10, pady= 10 )


janela.mainloop()
