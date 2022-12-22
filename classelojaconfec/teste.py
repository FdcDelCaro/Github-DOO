import pessoas
import pickle

p=[]

p.append(pessoas.pessoas("321654987", "Marlon"))
p.append(pessoas.pessoas("165465", "Pedro"))
p.append(pessoas.pessoas("634989", "Paulo"))


file_bn = open("pessoas.pkl", 'wb')
pickle.dump(p, file_bn)
file_bn.close()

file_bn = open("pessoas.pkl", 'rb')
p = pickle.load(file_bn)

print(p[0].mostraDados())
print(p[1].mostraDados())
print(p[2].mostraDados())

for dados in p:
    print(dados.nome)