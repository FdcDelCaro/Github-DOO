import pessoas
class Fornecedor(pessoas.pessoas):
    def __init__(self, cpf, nome,vcredito,vdivida):
        super().__init__(cpf, nome)
        self.__vcredito = vcredito
        self.__vdivida = vdivida
        
    def mostraDados(self):
        return super().mostraDados()
    def mostrarcpf(self):
        return super().mostrarcpf()
    def mostrarcredito(self):
        return self.__vcredito
    def mostrardivida(self):
        return self.__vdivida
    def subtracao(self):
        print(self.__vcredito-self.__vdivida)