import mysql.connector


class Conexaodb():
    def __init__(self, host = "localhost", user = "root", 
                 pwd = "", db = "dbagencia"):
        self.host = host
        self.user = user
        self.pwd = pwd
        self.db = db

    
       
    def conecta(self):

        self.con = mysql.connector.connect( host = self.host, 
                                            user = self.user, 
                                            password = self.pwd, 
                                            database = self.db)

        self.cur = self.con.cursor()

    def desconecta(self):
        self.con.close()

    def executa_DQL2(self,sql):
        self.conecta()
        self.cur.execute(sql)
        resultado= self.cur.fetchall()
        self.desconecta()
        
        




    #def executa_DQL(self):
     #   query = ("SELECT * FROM cliente")
      #  try:
       #     self.cur.execute(query)
        #    for (cliente) in self.cur:
         #       print("{}".format(cliente))
        #except mysql.connector.Error as err:
         #   print(err)
#
 #       self.cur.close()
  #      self.con.close()
                
        
    def executa_DML(self, sql):
        self.conecta()
        self.cur.execute(sql)
        self.con.commit
        self.desconecta()


