class Address:
    def __init__(self, zip_code):
        zip_code = str(zip_code)
        if self.is_zip_valid(zip_code):
            self.__zip_code = zip_code
        else:
            raise ValueError('CEP inválido')

    def __str__(self):
        return self.mask()

    @staticmethod
    def is_zip_valid(zip_code):
        return len(zip_code) == 8

    def mask(self):
        return f"{self.__zip_code[:5]}-{self.__zip_code[5:]}"
