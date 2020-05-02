from Model.PessoaFactory import PessoaFactory

cpf = '368.528.530-04'
cnpj = '38.487.180/1863-19'

pessoas = [cpf, cnpj]

for index, document in enumerate(pessoas):
    pessoas[index] = PessoaFactory.create_pessoa(document)

print(pessoas)
