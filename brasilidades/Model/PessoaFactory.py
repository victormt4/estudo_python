from Model.Cnpj import Cnpj
from Model.Cpf import Cpf
from Model.Pessoa import Pessoa
import re


class PessoaFactory:

    @staticmethod
    def create_pessoa(document) -> Pessoa:

        document = str(document)
        document = re.sub(r'[^0-9]', '', document)

        if len(document) == 11:
            return Cpf(document)
        elif len(document) == 14:
            return Cnpj(document)
        else:
            raise ValueError('Quantidade de dígitos incorreta')
