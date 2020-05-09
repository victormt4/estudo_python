from Model.DocumentFactory import DocumentFactory
from Model.Phone import Phone
from Model.Date import Date
from Model.Address import Address
from datetime import datetime, timedelta

cpf = '368.528.530-04'
cnpj = '38.487.180/1863-19'

docs = [cpf, cnpj]

for index, document in enumerate(docs):
    docs[index] = DocumentFactory.create_pessoa(document)

for document in docs:
    print(document.mask())

p = Phone('05562982120751')

print(p)

br_date = Date(datetime.today() - timedelta(days=365))

print(br_date)
print(br_date.month())
print(br_date.weekday())
print(br_date.age())

address = Address(88554481)
print(address)
