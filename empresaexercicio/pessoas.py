class pessoas():
    def __init__(self, cpf, nome):
        self.__cpf = cpf
        self.__nome = nome
    def mostraDados(self):
        return self.__nome

    def mostrarcpf(self):
        return self.__cpf