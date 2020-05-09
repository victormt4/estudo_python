import requests


class Address:
    def __init__(self, zip_code):
        zip_code = str(zip_code)

        if self.is_zip_valid(zip_code):
            self.__zip_code = zip_code

            r = requests.get(f"https://viacep.com.br/ws/{zip_code}/json")

            if r.status_code == 200:
                response_data = r.json()
                self.__address = response_data.get('logradouro', None)
                self.__complement = response_data.get('complemento', None)
                self.__district = response_data.get('bairro', None)
                self.__city = response_data.get('localidade', None)
                self.__state = response_data.get('uf', None)


        else:
            raise ValueError('CEP inválido')

    def __str__(self):
        return "{}{}{}{}{}{}".format(
            f'Endereço: {self.__address}\n' if self.__address else '',
            f'Complemento: {self.__complement}\n' if self.__complement else '',
            f'Bairro: {self.__district}\n' if self.__district else '',
            f'Cidade: {self.__city}\n' if self.__city else '',
            f'Estado: {self.__state}\n' if self.__state else '',
            f'CEP: {self.mask_zip_code()}'
        )

    @staticmethod
    def is_zip_valid(zip_code):
        return len(zip_code) == 8

    def mask_zip_code(self):
        return f"{self.__zip_code[:5]}-{self.__zip_code[5:]}"
