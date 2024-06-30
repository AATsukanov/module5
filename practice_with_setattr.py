
class User:

    def __new__(cls, *args, **kwargs):
        print('я в __new__')
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        print('я в __init__')
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __del__(self):
        print('я в __del__')

kw = {'name': 'Святополк', 'age': 33, 'gender': 'муж.', 'тестъ': 'ого!'}

usr1 = User(**kw)

print(usr1.name)
print(usr1.age)
print(usr1.gender)
print(usr1.тестъ)
