from Model.DocumentFactory import DocumentFactory

cpf = '368.528.530-04'
cnpj = '38.487.180/1863-19'

docs = [cpf, cnpj]

for index, document in enumerate(docs):
    docs[index] = DocumentFactory.create_pessoa(document)

for document in docs:
    print(document.mask())
