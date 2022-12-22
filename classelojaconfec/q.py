import lojaconf
import pickle
from pathlib import Path

loja=[]
def existe_dado(loja,nome):
    if len(loja)>0:
        for dado in loja:
            if dado['nome'] == nome:
                return True
    return False

def alterar(loja):
    if len(loja)>0:
        nome = input ("qual nome do produto a ser alterado?")
        if existe_dado(loja,nome):
            print("contato encontrado banco de dados")
            for dado in loja:
                if dado['nome'] == nome:
                   dado['nome'] = input("Digite o novo nome:")
                   dado['tipo'] = input ("Digite o novo tipo:")
                   dado['caract'] = input ("Digite a nova caracteristica:")
                   dado['qtd'] = input ("Digite a nova quantidade:")
                   dado['valor'] = input ("Digite o novo valor:")
                   print("===Alterado com sucesso===")


def leitura2():
  
            file_bn = open("produtos.pkl", 'rb+')
            
            loja = pickle.load(file_bn)
        
            file_bn.close()

def leitura():
    while True:
        try:
            file_bn = open("produtos.pkl", 'rb')
            print("Conteúdo do arquivo binario")
            loja = pickle.load(file_bn)
            for dado in loja:
                print ("NOME:")
                print(dado.nome)
                print ("TIPO:")
                print(dado.tipo)
                print ("CARACTERISTICAS:")
                print(dado.caract)
                print ("QUANTIDADE:")
                print(dado.qtd)
                print ("PREÇO:")
                print(dado.valor)
            break  
        except:
            print(" arquivo nao encontrado")
            print("deseja criar um novo arquivo?")
            print("1 para SIM / 2 para NÃO")
            arq=int( input() )
            if arq == 1:
                file_bn = open("produtos.pkl", 'wb')
                file_bn.close()
                break
            elif arq == 2:
                print("seus dados não serão salvos")

def cadastro(): #funcao cadastrar produtos

    nome = input("Nome: ")
    tipo = input("Tipo: ")
    caract = input("Características: ")
    while True:
        try:
            qtd = int(input("Quantidade: "))
            break
        except ValueError:
            print(" Digite um numero")

    while True:
        try:
            valor = float(input("Valor:"))
            break
        except ValueError:
            print(" Digite um numero")


    loja.append( lojaconf.Confecçao(nome, tipo, caract,qtd,valor) )
    file_bn = open("produtos.pkl", 'wb')
    pickle.dump(loja, file_bn)
    file_bn.close()




while True:
    print ("1 - Cadastrar Produtos.")
    print ("2 - mostrar Produtos Cadastrados.")
    print ("3 - alterar dados")
    print ("4 - sair")

    op=int( input() )
    if op==1:
        print ("Cadastro")
        cadastro()
        

    elif op==4:
        break
    elif op==2:   
        leitura()

    #elif op==4:
    #alterar(loja)    # nao funcionou     
    
    elif op == 3:
        
        
        nome = input("nome:")
        i = 0
        achou = False
        while i < len(loja):
            if loja[i].getNome() == nome:
                print("Nome atual:", loja[i].getNome())
                nome = input("Novo nome do produto:")
                tipo = input("novo tipo do produto:")
                caract = input("novas caracteristicas:")
                while True:
                    try:
                        qtd = int(input("Quantidade: "))
                        break
                    except ValueError:
                        print(" Digite um numero seu idiota")
                valor = input("novo preço/valor:")

                achou = True
                loja[i].seta(nome, tipo, caract, qtd, valor)
                
            i+=1
        if achou == False:
            print("nome nao encontrado!!") 
    
   

        


