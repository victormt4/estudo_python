from abc import ABC, abstractmethod


class Document(ABC):

    def __init__(self, document):

        document = str(document)

        if self.is_valid(document):
            self.document = document
        else:
            raise ValueError(f"{__class__.__name__} is invalid")

    def __str__(self):
        return self.mask()

    @abstractmethod
    def mask(self):
        pass

    @abstractmethod
    def is_valid(self, document):
        pass

    @staticmethod
    @abstractmethod
    def generate_valid_document(mask=False):
        pass
