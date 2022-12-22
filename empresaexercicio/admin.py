import funcionarios
class Administrador(funcionarios.Funcionario):
    def __init__(self, cpf, nome, setor, salario,ajuda_de_custo):
        super().__init__(cpf, nome, setor, salario)
        self.__ajuda_de_custo = ajuda_de_custo
        

    def mostraDados(self):
        return super().mostraDados()
    def mostrarcpf(self):
        return super().mostrarcpf()
    def mostrar_ajudacusto(self):
        return self.__ajuda_de_custo

    