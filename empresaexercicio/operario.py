import funcionarios
class   Operario(funcionarios.Funcionario):
    def __init__(self, cpf, nome, setor, salario,valor_producao, comissao):
        super().__init__(cpf, nome, setor, salario)
        self.__valor_producao = valor_producao
        self.__comissao = comissao
        

    def mostraDados(self):
        return super().mostraDados()
    def mostrarcpf(self):
        return super().mostrarcpf()
    def getsalario(self):
        return super().getsalario()
    def getsetor(self):
        return super().getsetor()
    def mostrar_valor_producao(self):
        return self.__valor_producao
    def mostrar_comissao(self):
        return self.__comissao
   

    