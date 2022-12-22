import mysql.connector as meubanco
dbconfig={
    'host':'localhost',
    'user':'root',
    'password':'',
    'database': 'pizzaria'
}
mysql=meubanco.connect(**dbconfig)
conexao=mysql.cursor()
conexao=mysql.cursor()

def print1():
    print('--' *20, 'DADOS', '--' * 20)
def listarcliente():
    mysql=meubanco.connect(**dbconfig)
    conexao=mysql.cursor()
    tabela = 'tbcliente'
    sql = f'''select * from {tabela};'''


    conexao.execute(sql)
    print1()
    for (cod,nome,endereco,cpf,tel) in conexao:
        print("----Clientes----")
        print ("id:{},\nNome:{},\nEndereço:{},\nCPF:{},\nTelefone:{}\n".format(cod,nome,endereco,cpf,tel))
 
    conexao.close()

def listarproduto():
    mysql=meubanco.connect(**dbconfig)
    conexao=mysql.cursor()
   
    
    sql=f'''select nome,sabor,preco, tamanho from pizza
        join produto on produto.id=pizza.id_produto;'''
  


    conexao.execute(sql)
    print1()
    for (nome,sabor,preco,tamanho) in conexao:

        print (f"Nome:{nome},\nsabor:{sabor},\npreco:{preco},\ntamanho:{tamanho}")
    print1()
 
      


listarcliente()
listarproduto()
conexao.close()


v1 = "felipe gay"

print(f'{v1}')