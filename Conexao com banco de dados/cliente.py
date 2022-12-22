from conexaodb import*

class Cliente():
    def __init__(self, id, nome):
        self.__id = id
        self.__nome = nome

    def incluirdados(self):
        c = Conexaodb()
        sql  = f"insert into tbcliente(nome)"
        sql += f"values ('{self.__nome}');"
        c.executa_DML(sql)

def selecttable():
    db = mysql.connector.connect(   host = "localhost", 
                                        user = "root", 
                                        password = "", 
                                        database = "dbagencia"    
                                    )
    conexao=db.cursor()
    sql='''select * from tbcliente order by nome;'''
    conexao.execute(sql)
    lista=[]
    for registro in conexao:
        lista.append(registro)
    return lista
  