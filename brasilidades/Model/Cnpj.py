from Model.Pessoa import Pessoa
from validate_docbr import CNPJ


class Cnpj(Pessoa):

    def is_valid(self, document):
        return CNPJ().validate(document)

    def mask(self):
        return CNPJ().mask(self.document)

    @staticmethod
    def generate_valid_document(mask=False):
        return CNPJ().generate(mask)
