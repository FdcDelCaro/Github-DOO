from conexaodb import*

class Prest():
    def __init__(self,nrboleto,valor,vencimento,id_voo):
        self.__nrboleto = nrboleto
        self.__valor = valor
        self.__vencimento = vencimento
        self.__id_voo = id_voo
        



    def incluirprest(self):
        c = Conexaodb()
        sql  = f"insert into prestacao (valor, vencimento, id_voo)"   
        sql += f"values ({self.__valor},'{self.__vencimento}',{self.__id_voo})"
        c.executa_DML(sql)

