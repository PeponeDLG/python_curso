import random as ran


class password:
    password = str
    lolong = int
    longMin = 8

    def __init__(self, lingitud: int = self.longMin, password: str = None):
        self.password = str.strip(password)
        self.long = str.count(password)


class genera_password(password):

    def __init__(self, lingitud: int = super().longMin, password: str = None):
        super().password = password
        super().longl = longitud

    def genera_password():
        longi = int

        if password is not None:
            longi = str.count(password)
        else:
            longi = super().longitud

        for i in range(0, longi):
            self.password += chr(ran.randint(48, 122))
