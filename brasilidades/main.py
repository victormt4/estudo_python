from Model.Cpf import Cpf
from Model.Cnpj import Cnpj

pessoa_fisica = Cpf(Cpf.generate_valid_document())
pessoa_juridica = Cnpj(Cnpj.generate_valid_document())

print(pessoa_fisica)
print(pessoa_juridica)