import re


class Phone:
    def __init__(self, phone):

        phone = str(phone)

        if self.is_valid(phone):
            self.__phone = phone
        else:
            raise ValueError('Invalid phone')

    def __str__(self):
        return self.mask()

    @staticmethod
    def is_valid(phone):
        return re.match('([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})', phone) is not None

    def mask(self):

        matches = re.search('([0-9]{2,3})?([0-9]{2})?([0-9]{4,5})([0-9]{4})', self.__phone)

        return "{}{}{}-{}".format(
            f"+{matches.group(1)} " if matches.group(1) is not None else '',
            f"({matches.group(2)}) " if matches.group(2) is not None else '',
            matches.group(3),
            matches.group(4)
        )
