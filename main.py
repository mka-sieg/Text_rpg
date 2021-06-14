from facade import Facade


def menu():
    facade = Facade()
    facade.attach(facade)
    print("Menu:")
    print("s - Start Game")
    print("i - Instruction")
    print("k - Exit Game")
    facade.button = input()


a = 0
while a == 0:
    menu()
