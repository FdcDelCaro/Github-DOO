import lojaconf
import pickle

loja=[]

while True:
    print ("1 - Cadastrar Produtos.")
    print ("2 - mostrar Produtos Cadastrados.")

    op=int( input() )
    if op==1:
        print ("Cadastro")
        nome = input("Nome: ")
        tipo = input("Tipo: ")
        caract = input("Características: ")
        while True:
            try:
                qtd = int(input("Quantidade: "))
                break
            except ValueError:
                print(" Digite um numero seu idiota")
    
        valor = float(input("Valor:"))
        loja.append( lojaconf.Confecçao(nome, tipo, caract,qtd,valor) )
        
    if op==2:
        file_bn = open("produtos.pkl", 'rb')
        loja = pickle.load(file_bn)
        for dado in loja:
            print ("nome:")
            print(dado.nome)
            print(dado.tipo)
            print(dado.caract)
            print(dado.qtd)
            print(dado.valor)

        
input 
loja.append(lojaconf.Confecçao("Tecido_cinza","Gray foda","seda","2","35"))

file_bn = open("lojaconfc.pkl", 'wb')
pickle.dump(loja, file_bn)
file_bn.close()

file_bn = open("lojaconfc.pkl", 'rb')
loja = pickle.load(file_bn)


for dado in loja:
    print ("nome:")
    print(dado.nome)
    print(dado.tipo)
    print(dado.caract)
    print(dado.qtd)
    print(dado.valor)