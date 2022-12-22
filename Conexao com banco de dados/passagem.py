from conexaodb import*

class Psg():
    def __init__(self,nrvoo,horapartida,horachegada,poltrona,id_pct):
        self.__nrvoo = nrvoo
        self.__horapartida = horapartida
        self.__horachegada = horachegada
        self.__poltrona = poltrona
        self.__id_pct = id_pct



    def incluirpsg(self):
        c = Conexaodb()
        sql  = f"insert into passagem (hora_partida, hora_chegada, poltrona,id_pct)"   
        sql += f"values ('{self.__horapartida}','{self.__horachegada}',{self.__poltrona},{self.__id_pct})"
        c.executa_DML(sql)

