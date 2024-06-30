
class User:

    __instance = None

    def __new__(cls, *args, **kwargs):
        print('я в __new__')
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        print('я в __init__')

    def __del__(self):
        print('я в __del__')

usr1 = User()
usr2 = User()
usr3 = User()

print(id(usr1), id(usr2), id(usr3))