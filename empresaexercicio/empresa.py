import operario
import funcionarios
import fornecedor
import admin
import vendedor
class Empresa():
    __func = []
    __forn = []
    __admin = []
    __operario = []
    __Vendor = []
    
    def __init__( self, codigo, nome, endereco, cnpj): 
        self.__codigo = codigo
        self.__nome = nome
        self.__endereco = endereco
        self.__cnpj = cnpj
        
        while True: #meu menu
            print ("====== MENU DO PROGRAMA EMPRESA FUTURE COMPANY =====")
            print ("<<<ESCOLHA UMA DAS OPÇÕES>>>")
            print("1. --- Contratar demais áreas ---")
            print("2. --- Exibir os funcionarios ---")
            print("3. --- Cadastrar fornecedor -----")
            print("4. --- Exibirfornecedores/saldo -")
            print("5. --- Cadastrar Administrador --")
            print("6. --- Mostrar Administradores --")
            print("7. --- Cadastrar operarios ------")
            print("8. --- Mostrar Apenas Operarios -")
            print("9. --- Cadastrar Vendedores  ----")
            print("10. -- Mostra Apenas vendedores -")

            op=int( input() )
            if op==1:
                print ("Contratar")
                self.contratar()
            elif op==2:
                print ("Funcionarios: ")
                self.exibir()
            elif op==3:
                print ("Cadastrando Fornecedor: ")
                self.fornecedor()
            elif op==4:
                print ("Exibir Fornecedores e saldos dividendo: ")
                self.exibirforn()
            elif op==5:
                print ("Cadastrando Administradores: ")
                self.admin()     
            elif op==6:
                print ("Exibir apenas os Administradores: ")
                self.exibiradmin()     
            elif op==7:
                print ("Cadastrando Operarios especificos: ")
                self.operario()
            elif op==8:
                print ("Exibir apenas os funcioas da categorias operacional: ")
                self.exibirop()
            elif op==9:
                print ("Cadastrando vendedores: ")
                self.vendor()
            elif op==10:
                print ("Exibir apenas funcionarios da cateria vendendor: ")
                self.exibirvendor()
            else:
                print("______error/Opçao invalida/error______")
    
    
    def contratar(self): #funcao contratar funcionarios /////OPCAO == 1
        cod = input("Numero do CPF: ")
        nome = input("Nome: ")
        setor = input("Setor: ")
        salario = float(input("salario: "))
        self.__func.append( funcionarios.Funcionario(cod, nome, setor,salario) )
    
    def exibir(self): #func exibir lista de funcionarios contratados /////OPCAO==2
        for fun in self.__func:
            print("CPF:",fun.mostrarcpf())
            print("nome:",fun.mostraDados())
            print("Setor:",fun.getsetor())
            print ("Salário:",fun.getsalario())
            print("---------------------------")

    def fornecedor(self): # armazena fornecedores //OPCAO==3
        cpf = input("cpf Fornecedor: ")
        nome = input("nome Fornecedor: ")
        vcredito = float (input("valor de crédito: "))
        vdivida =  float (input ("valor da divida: "))
        self.__forn.append(fornecedor.Fornecedor(cpf, nome, vcredito,vdivida,))

    def exibirforn(self): #exibir lista de fornecedores cadastrados // OPCAO==4
        for fun in self.__forn:
            print("Nome: ",fun.mostraDados())
            print("CPF: ",fun.mostrarcpf())
            print("Crédito: ",fun.mostrarcredito())
            print("Divida: ",fun.mostrardivida())
            print("Saldo: ")
            print(fun.subtracao())
            

    
    def admin(self): #funcao armazenar adms no vetor de adm(admin) e no vetor de funcionarios(func) ///// OPCAO==5
        cpf = input("Numero do CPF: ")
        nome = input("Nome: ")
        setor = input("setor:")
        salario = float(input("salario: "))
        ajuda_de_custo = float (input("Ajuda de custo: "))
        self.__admin.append( admin.Administrador(cpf, nome, setor,salario,ajuda_de_custo) )
        self.__func.append( admin.Administrador(cpf, nome, setor,salario,ajuda_de_custo) )

    def exibiradmin(self): # exibi a lista de administradores // OPCAO ==6
        for fun in self.__admin:
            print("Nome: ",fun.mostraDados())
            print("CPF: ",fun.mostrarcpf())
            print("Valor de Ajuda de custo",fun.mostrar_ajudacusto())

    def operario(self): # armazena operario no vetor de operarios e de funcionarios/CALCULA A COMISSÃO //// OPCAO==7
        cod = input("CPF: ")
        nome = input("Nome: ")
        setor = input("setor: ")
        salario = float(input("salario: "))
        valor_producao = float (input("valor produzido:"))
        comissao = salario+(valor_producao*0.20)
        self.__operario.append( operario.Operario(cod, nome, setor,salario,valor_producao,comissao) )
        self.__func.append( operario.Operario(cod, nome, setor,salario,valor_producao,comissao) )

    def exibirop(self): # exibi a lista de apenas operarios // OPCAO == 8
        for fun in self.__operario:
            print("Nome: ",fun.mostraDados())
            print("CPF: ",fun.mostrarcpf())
            print("Produziu: ",fun.mostrar_valor_producao())
            print("salario fixo: ",fun.getsalario())
            print("Comisssão (Salario Fixo + 20% do valor produzido): ",fun.mostrar_comissao())
    
    def vendor(self): # armazena o vendedor no vetor de vendor e de func CALCULA A COMISSÃO  //// OPCAO==9
        cod = input("CPF: ")
        nome = input("Nome: ")
        setor = input("setor: ")
        salario = float(input("salario: "))
        valor_vendas = float (input("valor das vendas:"))
        comissao = salario+(valor_vendas*0.20)
        self.__Vendor.append( vendedor.Vendor(cod, nome, setor,salario,valor_vendas,comissao) )
        self.__func.append( vendedor.Vendor(cod, nome, setor,salario,valor_vendas,comissao) )

    def exibirvendor(self): # exibi a lista de apenas vendendedores /// OPCAP == 10
        for fun in self.__Vendor:
            print("Nome: ",fun.mostraDados())
            print("CPF: ",fun.mostrarcpf())
            print("Vendas: ",fun.mostrar_valor_vendas())
            print("salario fixo: ",fun.getsalario())
            print("Comisssão (Salario Fixo + 20% do valor de vendas): ",fun.mostrar_comissao())
    
    def mostraDados(self):
        print(str(self.__codigo)+" "+self.__nome)
            