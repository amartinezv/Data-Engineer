from car import Car
from account import Account
from uberX import UberX
from user import User

if __name__ == "__main__":
    car = Car("AMS453", Account("Andres Herrera", "113234427"))
    print(vars(car))
    print(vars(car.driver))

    uberX = UberX("DMQ123", Account("Maria Gonzales", "38484839"), "chevrolet", "spark")
    print(vars(uberX))

    user = User("Andrea Perez", "24892302")
    print(vars(user))
