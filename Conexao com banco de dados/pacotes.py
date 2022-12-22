from conexaodb import*

class Pacotes():
    def __init__(self,id,ndias, data_fim,apart, data_ini,id_hot):
        self.__id = id
        self.__ndias = ndias
        self.__data_fim = data_fim
        self.__apart = apart
        self.__data_ini = data_ini
        self.__id_hot = id_hot


    def pacotes(self):
        c = Conexaodb()
        sql  = f"insert into pacote (ndias, data_fim,apart, data_ini,id_hot)"   
        sql += f"values ({self.__ndias},'{self.__data_fim}',{self.__apart},'{self.__data_ini}',{self.__id_hot})"
        c.executa_DML(sql)

def selecttable():
    db = mysql.connector.connect(   host = "localhost", 
                                        user = "root", 
                                        password = "", 
                                        database = "dbagencia"    
                                    )
    conexao=db.cursor()
    sql='''select ndias, data_ini,data_fim,id_hot,apart,nome
            from pacote
            join hotel on hotel.id = pacote.id_hot;;'''
    conexao.execute(sql)
    lista=[]
    for registro in conexao:
        lista.append(registro)
    return lista
  