from conexaodb import*

class Reserva():
    def __init__(self, id, data_res, preco,id_cli):
        self.__id = id
        self.__data_res = data_res
        self.__preco = preco
        self.__id_cli = id_cli

#nr de numero
    #def createtable(self,sql):
     #   c = Conexaodb()
      #  sql  = f"create table reserva (nr INT NOT NULL PRIMARY KEY AUTO_INCREMENT,"
       # sql += f"data_reserva date NULL,preco INT);)"
        #c.executa_DQL3(sql)

 

    def incluirdadosres(self):
        c = Conexaodb()
        sql  = f"insert into reserva (data_res, PRECO,id_cli)"   
        sql += f"values ('{self.__data_res}',{self.__preco},{self.__id_cli})"
        c.executa_DML(sql)

