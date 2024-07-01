'''Цель: Применить знания полученные в модуле, решив задачу повышенного уровня сложности.

Задание "Свой YouTube":
Университет Urban подумывает о создании своей платформы, где будут размещаться дополнительные полезные ролики на тему IT
(юмористические, интервью и т.д.). Конечно же для старта написания интернет ресурса требуются хотя бы базовые знания программирования.

Именно вам выпала возможность продемонстрировать их, написав небольшой набор классов, которые будут выполнять похожий функционал на сайте.

Всего будет 3 класса: UrTube, Video, User.

Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео, авторизации и регистрации пользователя и т.д.
'''

from time import sleep

class User:
    '''
    Каждый объект класса User должен обладать следующими атрибутами и методами:
    Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    '''
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.hPassword = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname} (возраст {self.age})'

    def __contains__(self, item):
        return self.nickname == item
class Video:
    '''
    Каждый объект класса Video должен обладать следующими атрибутами и методами:
    Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    '''

    videos_history_list = []

    def __new__(cls, *args, **kwargs):
        cls.videos_history_list.append(args[0])
        return super().__new__(cls)
        #return object.__new__(cls)

    def __init__(self, title: str, duration: int, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0 #в секундах
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __contains__(self, item):
        return item in self.title

class UrTube:
    '''Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
    Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    '''
    def __init__(self):
        self.users = [] #users(список объектов User)
        self.videos = [] #videos(список объектов Video)
        self.current_user = None #current_user(текущий пользователь, User)

    def log_in(self, nickname, password) -> bool:
        #Метод log_in, который принимает на вход аргументы: и пытается найти пользователя в users с такими же логином и паролем.
        #Если такой пользователь существует, то current_user меняется на найденного.
        #Помните, что password передаётся в виде строки, а сравнивается по хэшу.
        for U in self.users:
            if nickname in U and hash(password) == U.hPassword:
                self.current_user = U
                return True
        return False

    def register(self, nickname, password, age):
        #Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
        #если пользователя не существует (с таким же nickname).
        #Если существует, выводит на экран: "Пользователь {nickname} уже существует". После регистрации, вход выполняется автоматически.
        if not nickname in self.users:
            u = User(nickname, password, age)
            self.users.append(u)
            print('Новый пользователь зарегистрирован.')
        #автоматический вход:
        self.log_in(nickname, password)

    def log_out(self):
        #Метод log_out для сброса текущего пользователя на None.
        self.current_user = None
        print('Выход выполнен.')

    def add(self, *args):
        #Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        #если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
        for v in args:
            if v.title in self.videos:
                print('Видео с таким именем уже загружено, пропускаем.')
            else:
                self.videos.append(v)
                print('Видео успешно загружено.')

    def get_videos(self, search_word: str):
        #Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        #содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).
        word = search_word.upper()
        search_result = []
        for v in self.videos:
            if word in v.title.upper():
                search_result.append(v.title)
        print(f'Найдено {len(search_result)} видео.')
        return search_result

    def find_video(self, title):
        if title == '':
            return None
        for v in self.videos:
            if title.upper() in v.title.upper():
                return v
        return None

    def watch_video(self, title):
        #Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        #то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        #После текущее время просмотра данного видео сбрасывается.
        #Для метода watch_video так же учитывайте следующие особенности:
        #Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        #Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        #Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        #После воспроизведения нужно выводить: "Конец видео"
        if self.current_user == None:
            print('Войдите в аккаунт, чтобы смотреть видео.')
            return
        v = self.find_video(title)
        if v is None:
            print('Видео не найдено.')
            return
        #play:
        for t in range(v.duration):
            print(t + 1, end=' > ')
            sleep(1)
            v.time_now += 1
        print('Конец видео.')
        v.time_now = 0

def main():
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    v3 = Video('Клип на 3 секунды', 3)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')

    # Выход:
    ur.log_out()

    ur.add(v3)
    vv = ur.get_videos('3')
    print(vv)
    ur.watch_video(vv[0])
    ur.log_in('vasya_pupkin', 'F8098FM8fjm9jmi')
    ur.watch_video(vv[0])

if __name__ == '__main__':
    main()

'''
Видео успешно загружено.
Видео успешно загружено.
Найдено 1 видео.
['Лучший язык программирования 2024 года']
Найдено 2 видео.
['Лучший язык программирования 2024 года', 'Для чего девушкам парень программист?']
Войдите в аккаунт, чтобы смотреть видео.
Новый пользователь зарегистрирован.
1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9 > 10 > Конец видео.
Новый пользователь зарегистрирован.
1 > 2 > 3 > 4 > 5 > 6 > 7 > 8 > 9 > 10 > Конец видео.
Новый пользователь зарегистрирован.
vasya_pupkin (возраст 55)
Видео не найдено.
Выход выполнен.

Process finished with exit code 0
'''