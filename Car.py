#2
class Car:
    def __init__(car, color, name, price):
        car.color = color
        car.name = name
        car.price = price

    def print_description(car):
        return car

    def print(car):
        print(f'{car.color} {car.name} cost ${car.price}')

first_car = Car('Black', 'Volvo', 5000)

first_car.print()

class Person:
    def __init__(self, name, account_balance):
        self.name = name
        self.account_balance = account_balance

    def print_balance(self):
        return self

    def print(self):
        print(f"{self.name}'s current balance is ${self.account_balance}")


person_account = Person('Janet', 25000)
person_account.print()