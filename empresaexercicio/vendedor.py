import funcionarios
class   Vendor(funcionarios.Funcionario):
    def __init__(self, cpf, nome, setor, salario,valor_vendas, comissao):
        super().__init__(cpf, nome, setor, salario)
        self.__valor_vendas = valor_vendas
        self.__comissao = comissao
        

    def mostraDados(self):
        return super().mostraDados()
    def mostrarcpf(self):
         return super().mostrarcpf()
    def getsalario(self):
        return super().getsalario()
    def mostrar_valor_vendas(self):
        return self.__valor_vendas
    def mostrar_comissao(self):
        return self.__comissao