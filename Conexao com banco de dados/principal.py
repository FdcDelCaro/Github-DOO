import conexaodb
import cliente
import reserv
import hotel
import pacotes
import passagem
import prestacao
import mysql
import  mysql.connector
from mysql.connector import connection
from conexaodb import*
from reserv import*

class Agencia():
    __cliente = []
    __reserva = []
    __hotel = []
    __pacote = []
    __psg=[]
    __prest=[]
    
    def __init__(self, codigo, nome, endereco, cnpj): 
        self.__codigo = codigo
        self.__nome = nome
        self.__endereco = endereco
        self.__cnpj = cnpj

        while True:
            print("----Se for seu primeiro acesso, crie todas as tabelas na OPÇÃO Nº: 1----")
            print("1.----Criar todas as tabelas----")
            print("\n2.----Iniciar programa----")
            while True:
                try:
                    op = int(input())
                    break
                except ValueError:
                    print("Opção Invalida,(SOMENTE NÚMEROS)")

            if op==2: # PARA INICIAR O PROGRAMA DEPOIS DE CRIAR AS TABLEAS?

                
                while True:     

                  
                    print ("<<<ESCOLHA UMA DAS OPÇÕES>>>")
                    print("0. ------------- VOLTAR -----------------")
                    print("1. -------- Inclusão de Clientes --------")
                    print("2. -------- Relação de Clientes ---------")
                    print("3. -------- Incluir Reservas ------------")
                    print("4. -------- Relação Reservas ------------")
                    print("5. -------- Incluir Hoteis --------------")
                    print("6. -------- Exibir Hoteis ---------------")
                    print("7. -------- Incluir Pacotes -------------")
                    print("8. -------- Exibir somente Pacotes ------")
                    print("9. -------- Incluir Passagens -----------")
                    print("10. ------- Exibir  Passagens -----------")
                    print("11. ------- Incluir Prestações ----------")
                    print("12. ------- Exibir  Boletos -------------")
                    print("13. --- Pacotes e Relatório de preços ----")
                    print("\n14. ---IMPRIMIR TODO O BANCO DE DADOS ---")
                    while True:
                        try:
                            op2=int( input() )
                            break
                        except ValueError:
                            print("Opção Invalida,(SOMENTE NÚMEROS)")

                    if op2==1:
                        print ("Inclusão")
                        self.inclusao()

                    if op2==0:
                        print ("Voltar")
                        break                   

                    if op2==2:
                        print ("clientes")
                        self.listar_clientes()


                   
                    if op2==3:
                        print ("Inclusão")
                        self.inclusaores()

                    if op2==4:
                        print ("Lista Reserva")
                        self.listar_res()
                    
                    if op2==5:
                        print ("Inclusão")
                        self.inclusaohotel()

                    if op2==6:
                        print ("Hoteis na Reserva")
                        self.listar_hotel()

                    if op2==7:
                        print ("Inclusão")
                        self.inclusaopacote()

                    if op2==8:
                        print ("Lista somente da tabela pacote")
                        self.listar_pacote()

                    if op2==9:
                        print ("Inclusão")
                        self.inclusaopsg()

                    if op2==10:
                        print ("Lista das Passagens")
                        self.listar_psg()

                    if op2==11:
                        print ("Inclusão")
                        self.inclusaoprest()

                    if op2==12:
                        print ("Lista das Prestaçoes e Boletos")
                        self.listar_prest()
                    if op2==13:
                        print ("---PACOTES GERADOS---")
                        self.pacotes()
                    if op2==14:
                        print ("----IMPRIMINDO TODO O BANCO DE DADOS----")
                        self.listar_clientes()
                        self.listar_res()
                        self.listar_hotel()
                        self.listar_pacote()
                        self.listar_psg()
                        self.listar_prest()
                                                                                                                              
           
            if op==1: # para criar as tabelas

                
                while True:

                  
                    print ("<<<ESCOLHA UMA DAS OPÇÕES>>>")
                    print("0. ---------------VOLTAR-----------------")
                    print("1. ---------Criar tabela clientes--------")
                    print("2. ---------Criar tabela reserva---------")
                    print("3. ---------Criar tabela hotel-----------")
                    print("4. ---------Criar tabela pacote----------")
                    print("5. ---------Criar tabela passagem--------")
                    print("6. ---------Criar tabela prestação-------")
                    while True:
                        try:
                            op1=int( input() )
                            break
                        except ValueError:
                            print("Opção Invalida,(SOMENTE NÚMEROS)")

                    if op1==0:
                        print ("Voltou")
                        break   

                    if op1==1:  #    criando tabelas clientes antes #    da inserçao de dados, codigos mysql na classe
                        print ("Criando tabela Clientes ")
                        self.createtable(self)
                        print ("Criada com colunas ID>PK e NOME") 

                    if op1==2:
                        print ("Criando tabela Reserva")
                        self.createtableRES(self) 
                        print ("Criada com colunas ID>PK, DATA_RES, PRECO, ID_CLI>FK") 

                    if op1==3:
                        print ("Criando tabela Hotel")
                        self.createhotel(self)
                        print ('Criada com colunas ID>PK, NOME, CATEGORY, ID_RES>FK')
                    if op1==4:
                        print ("Criando tabela Pacotes")
                        self.createpacote(self)               
                    if op1==5:
                        print ("Criando tabela Passagem")
                        self.createpassagem(self)
                    if op1==6:
                        print ("Criando tabela Prestação")
                        self.createprestacao(self)                                     
            

    def inclusao(self): # funcão de incluir clientes, apenas o nome, devido a variavel id ser autoincremente (nr/numero/id) como queira chamnar.

        id=("")
        nome = input("Nome: ")
        self.__cliente.append(cliente.Cliente(id, nome,) )
        for fun in self.__cliente:
            fun.incluirdados()

    def inclusaores(self): # func de inclusao de reservas

        id=("")
        print ("Fomarto de datas em (aaaa-mm-dd)")
        data_res = input("Data: ")
        print ("Fomarto em Decimal EX: >>> (100.20)")
        preco= input("Preço:")
        id_cli= input("Número do cliente:")
        self.__reserva.append(reserv.Reserva(id, data_res,preco,id_cli) )
        for fun in self.__reserva:
            fun.incluirdadosres()

    def listar_clientes(self): # aqui começa as funcçoes de listagem
        print('-----LISTA DE CLIENTES-----:')
        clienteslist = cliente.selecttable()
        for cli_nome in clienteslist:
            id = cli_nome[0]
            nome = cli_nome[1]
            #mensagem = 'cliente -'+id+':'+nome
            mensagem = f'Nº:{id}, Nome: {nome}'
            print(mensagem)
    
    def listar_res(self):
        print('\n----LISTA DE RESERVAS----')
        conn = connection.MySQLConnection(user='root', password="",
                                 host='localhost',
                                 database='dbagencia')
        
        cursor = conn.cursor()

        DB_NAME = 'dbagencia'
        query = ("select * from reserva;")
        try:
            cursor.execute(query)
            for (id, data_Res,preco, id_cli) in cursor:
                
                print("Numero da reserva:{},\nData reserva: {},\nPreço: {},\nCodigo do Cliente: {}\n\n ------- PROXIMA RESERVA ABAIXO -------".format(id,data_Res,preco,id_cli))
        except mysql.connector.Error as err:
            print("se reconect no BD")

        cursor.close()
        conn.close()
    
    def listar_hotel(self):
        print('\n----LISTA DE HOTEIS----')
        conn = connection.MySQLConnection(user='root', password="",
                                 host='localhost',
                                 database='dbagencia')
        
        cursor = conn.cursor()

        DB_NAME = 'dbagencia'
        query = ("select * from hotel;")
        try:
            cursor.execute(query)
            for (id,nome,categoria,id_res) in cursor:
                
                print("Codigo Hotel:{},\nNome: {},\nCategoria: {},\nCodigo da reserva: {}\n\n ------- PROXIMO HOTEL ABAIXO -------".format(id,nome,categoria,id_res))
        except mysql.connector.Error as err:
            print("se reconect no BD")

        cursor.close()
        conn.close()

    def listar_pacote(self):
        print('\n----LISTA DE PACOTES----')
        conn = connection.MySQLConnection(user='root', password="",
                                 host='localhost',
                                 database='dbagencia')
        
        cursor = conn.cursor()

        DB_NAME = 'dbagencia'
        query = ("select * from pacote;")
        try:
            cursor.execute(query)
            for (id,ndias,data_fim,apart,data_ini,id_hot) in cursor:
                
                print("Codigo Pacote:{},\nNº de Dias: {},\nData final: {},\nApartamento: {},\nData Inicio: {},\nCodigo do Hotel reservado: {}\n\n ------- PROXIMO PACOTE ABAIXO -------".format(id,ndias,data_fim,apart,data_ini,id_hot))
        except mysql.connector.Error as err:
            print("se reconect no BD")

        cursor.close()
        conn.close()

    def listar_psg(self):
        print('\n----LISTA DE PASSAGENS----')
        conn = connection.MySQLConnection(user='root', password="",
                                 host='localhost',
                                 database='dbagencia')
        
        cursor = conn.cursor()

        DB_NAME = 'dbagencia'
        query = ("select * from passagem;")
        try:
            cursor.execute(query)
            for (nrvoo,hora_partida,hora_chegada,poltrona,id_pct) in cursor:
                
                print("Nº do Vôo:{},\nHorario de decolagem: {},\nHorario de pouso: {},\nNº da Poltrona: {},\nCodigo do pacote reservado: {}\n\n ------- PROXIMA PASSAGEM ABAIXO -------".format(nrvoo,hora_partida,hora_chegada,poltrona,id_pct))
        except mysql.connector.Error as err:
            print("se reconect no BD")

        cursor.close()
        conn.close()

    def listar_prest(self):
        print('\n----LISTA DE PRESTAÇÕES E BOLETOS----')
        conn = connection.MySQLConnection(user='root', password="",
                                 host='localhost',
                                 database='dbagencia')
        
        cursor = conn.cursor()

        DB_NAME = 'dbagencia'
        query = ("select * from prestacao;")
        try:
            cursor.execute(query)
            for (nrboleto, valor, vencimento, id_voo) in cursor:
                
                print("Nº do boleto:{},\nValor: {},\nData de Vencimento: {},\nCodigo do voo reservado: {}\n\n ------- PROXIMA LISTA BOLETOS ABAIXO -------".format(nrboleto,valor,vencimento,id_voo))
        except mysql.connector.Error as err:
            print("se reconect no BD")

        cursor.close()
        conn.close()
    
    def pacotes(self): #gerando relatorio precos e pacotes # até aqui as funcoes de listar...
        conn = connection.MySQLConnection(user='root', password="",
                                 host='localhost',
                                 database='dbagencia')
        
        cursor = conn.cursor()

        DB_NAME = 'dbagencia'
        query = ("select pacote.id,ndias, data_ini,data_fim,id_hot,apart,nome, category from pacote join hotel on hotel.id = pacote.id_hot;")
        query2 = ("select hora_partida, hora_chegada, poltrona, id_pct ,valor, vencimento, nrboleto from prestacao join passagem on passagem.nrvoo = prestacao.id_voo;")
        try:
            cursor.execute(query)
            for (pacote_id, ndias,data_ini, data_fim,id_hot,apart,nome,category) in cursor:
                
                print("Numero do pacote:{},\nNº Dias: {},\nDATA INICIAL: {},\nDATA FINAL: {},\nCODIGO DO HOTEL:{},\nAPARTAMENTO: {},\nNOME DO HOTEL: {},\nCATEGORIA: {} \n\n ---------PROXIMO PACOTE A BAIXO--------\n".format(pacote_id,ndias,data_ini,data_fim,id_hot,apart,nome,category))
            
            cursor.execute(query2)
            for (hora_partida, hora_chegada, poltrona, id_pct, valor, vencimento, nrboleto) in cursor:
                print ("Relatório de preços e dados de vôo:")
                print("Horario vôo: {},\nChegada: {},\nPoltrona: {},\nNumero do Pacote: {},\nValor (PODE SER PARCELADO): {},\nVencimento boleto: {},\nNº Boleto: {}\n\n ---------PROXIMO RELATÓRIO A BAIXO--------\n".format(hora_partida, hora_chegada, poltrona, id_pct, valor, vencimento, nrboleto))
            
        except mysql.connector.Error as err:
            print("se reconect no BD")

        cursor.close()
        conn.close()

    def createtable(self,sql): # criando tabelas clientes
            c = Conexaodb()
            sql  = '''CREATE TABLE tbcliente (
	                    id int primary key auto_increment,
                        nome varchar(70)
                                            );'''
            c.executa_DML(sql)

    def createtableRES(self,sql): # criando tabela reserva com chave estrangeira vindo de clientes, no caso o ID
            c = Conexaodb()
            sql  = '''CREATE TABLE reserva (
                        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                        data_res DATE NOT NULL,
                        PRECO  DECIMAL (10,2) NOT NULL,
                        id_cli INT NOT NULL,

                        FOREIGN KEY (id_cli) REFERENCES tbcliente (id)
                        );'''
            c.executa_DQL2(sql)

    def createhotel(self,sql): #criando tabela hotem com chave estrageira em Reserva e com id em auto increment
            c = Conexaodb()
            sql  =  '''CREATE TABLE hotel (
                    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    nome varchar(30),
                    category  varchar (20) NOT NULL,
                    id_res INT NOT NULL,

                    FOREIGN KEY (id_res) REFERENCES reserva (id)
                    );'''
            c.executa_DQL2(sql)
    
    def inclusaohotel(self):  # inclusao dos hoteis, com autoincrement nos numeros (id) e chave estrangeira em reserva

        id=("")
        nome = input("Nome do Hotel: ")
        category= input("Categoria:")
        id_res= input("Numero da reserva do cliente:")
        self.__hotel.append(hotel.Hotel(id,nome,category,id_res) )
        for fun in self.__hotel:
            fun.incluirdadoshotel()
    
    def createpacote(self,sql):# criando tabela pacote com chave primaria auto incremento para solicitar depois com outras tabelas, caso necessario, com chave estrangeira em hoteis.
        
            c = Conexaodb() 
            sql  =  '''CREATE TABLE pacote (
                    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    ndias int,
                    data_fim date, 
                    apart int,
                    data_ini date,
                    id_hot int not null,

                    FOREIGN KEY (id_hot) REFERENCES hotel (id)
                    );'''
            c.executa_DQL2(sql)

    def inclusaopacote(self):  # inclusao dos pacotes

        id=("")
        ndias = input("Número dos estadia no Hotel: ")
        print ("Fomarto de datas em (aaaa-mm-dd)")
        data_fim= input("Data de saida:")
        apart= input("Número apartamento:")
        print ("Fomarto de datas em (aaaa-mm-dd)")
        data_ini=input("Qual data de chegada no hotel(inicio):")
        id_hot=input("Qual Código do hotel")
        self.__pacote.append(pacotes.Pacotes(id,ndias,data_fim,apart,data_ini,id_hot) )
        for fun in self.__pacote:
            fun.pacotes()

    def createpassagem(self,sql):# criando tabela passagem com chave primaria auto incremento para solicitar depois com outras tabelas(*NRVOO), caso necessario, com chave estrangeira em hoteis.
        
            c = Conexaodb() 
            sql  =  '''CREATE TABLE passagem (
                    nrvoo INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    hora_partida TIME,
                    hora_chegada TIME, 
                    poltrona int,
                    id_pct int not null,

                    FOREIGN KEY (id_pct) REFERENCES pacote (id)
                    );'''
            c.executa_DQL2(sql)

    def inclusaopsg(self):  # inclusao das passagens no bd

        nrvoo=("")
        print ("Fomarto de horas em (hh:mm:ss)")
        horapartida = input("Horario do Vôo: ")
        print ("Fomarto de horas em (hh:mm:ss)")
        horachegada = input("Previsão de chegada (HORARIO):")
        poltrona = input("Número da poltrona:")
        id_pct=input("Qual Código do pacote")
        self.__psg.append(passagem.Psg(nrvoo,horapartida,horachegada,poltrona,id_pct) )
        for fun in self.__psg:
            fun.incluirpsg()

    def createprestacao(self,sql):# criando tabela prestaçao no bd
        
            c = Conexaodb() 
            sql  =  '''CREATE TABLE prestacao (
                    nrboleto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
                    valor decimal,
                    vencimento date, 
                    
                    id_voo int not null,

                    FOREIGN KEY (id_voo) REFERENCES passagem (nrvoo)
                    );'''
            c.executa_DQL2(sql)

    def inclusaoprest(self): #incluindo dados na tabela prestaçao no bd 

        nrboleto=("")
        print ("Fomarto em Decimal EX: >>> (100.20)")
        valor = input("Valor do boleto: ")
        print ("Fomarto de datas em (aaaa-mm-dd)")
        vencimento = input("Data de vencimento:")
        id_voo=input("Qual Código do vôo do cliente")
        self.__prest.append(prestacao.Prest(nrboleto,valor,vencimento,id_voo) )
        for fun in self.__prest:
            fun.incluirprest()
