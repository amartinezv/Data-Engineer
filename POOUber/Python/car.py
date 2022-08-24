from account import Account

class Car:
    id = int
    lincense = str
    driver = Account("","")
    passegenger = int

    def __init__(self, license, driver):
        self.lincense = license
        self.driver = driver