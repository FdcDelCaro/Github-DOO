from conexaodb import*

class Hotel():
    def __init__(self, id, nome, category, id_res):
        self.__id = id
        self.__nome = nome
        self.__category = category
        self.__id_res = id_res


    def incluirdadoshotel(self):
        c = Conexaodb()
        sql  = f"insert into hotel (nome, category,id_res)"   
        sql += f"values ('{self.__nome}','{self.__category}',{self.__id_res})"
        c.executa_DML(sql)

