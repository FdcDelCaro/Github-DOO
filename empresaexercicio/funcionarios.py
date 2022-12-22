import pessoas
class Funcionario(pessoas.pessoas):
    def __init__(self, cpf, nome, setor, salario):
        super().__init__(cpf, nome)
        self.__setor = setor
        self.__salario = salario

    def mostraDados(self):
        return super().mostraDados()
    def mostrarcpf(self):
         return super().mostrarcpf()

    def getsetor(self):
        return self.__setor

    def getsalario(self):
        return self.__salario