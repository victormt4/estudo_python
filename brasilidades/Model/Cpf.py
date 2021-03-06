from Model.Document import Document
from validate_docbr import CPF


class Cpf(Document):

    def is_valid(self, document):
        return CPF().validate(document)

    def mask(self):
        return CPF().mask(self.document)

    @staticmethod
    def generate_valid_document(mask=False):
        return CPF().generate(mask)
