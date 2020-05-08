from datetime import datetime


class Date:
    def __init__(self, date=datetime.today()):
        self.__date = date

    def __str__(self):
        return self.mask()

    def mask(self):
        return self.__date.strftime('%d/%m/%Y %H:%M')

    def month(self):
        months = (
            'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro',
            'novembro', 'dezembro'
        )
        return months[self.__date.month - 1]

    def weekday(self):
        days = ('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo')
        return days[self.__date.weekday()]

    def age(self):
        return datetime.today() - self.__date

