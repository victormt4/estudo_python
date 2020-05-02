from validate_docbr import CPF


class Cpf:
    def __init__(self, document):
        document = str(document)
        if self.is_cpf_valid(document):
            self.cpf = document
        else:
            raise ValueError('CPF inválido')

    def __str__(self):
        return self.mask()

    @staticmethod
    def is_cpf_valid(document):
        return CPF().validate(document)

    def mask(self):
        # return f"{self.cpf[:3]}.{self.cpf[3:6]}.{self.cpf[6:9]}-{self.cpf[9:]}"
        return CPF().mask(self.cpf)
