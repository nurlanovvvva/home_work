# class SuperHero:
#     people = 'people'
#     def __init__(self, name, nickname, superpower, health_points, catchrase):
#         self.name = name
#         self.nickname = nickname
#         self.superpower = superpower
#         self.health_points = health_points
#         self.catchrse = catchrase
#
#     def name_hero(self):
#         print(f'Имя героя : {self.name}')
#
#     def double_up_health_points(self):
#         self.health_points *= 2
#
#     def __str__(self):
#         return (f'Прозвище героя: {self.nickname}'
#                 f'\nСуперспособность: {self.superpower}\nЗдоровье героя: {self.health_points}')
#
#     def __len__(self):
#         return len(self.catchrse)
#
# class AirHero(SuperHero):
#     def __init__(self, *args, wing_span, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.wing_span = wing_span
#
# class EarthHero(SuperHero):
#     def __init__(self, *args, ground_speed, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.ground_speed = ground_speed
#
#
# class Villain(AirHero):
#     people = 'monster'
#     def gen_x(self):
#         pass
#     def crit(self, power):
#         self.damage **= power
#
#
# hero = SuperHero("Диана", "Чудо-женщина", "Летание", "1000", "За справедливость!")
# hero.name_hero()
# hero.double_up_health_points()
# print(hero)
# print(f'Длинна коронной фразы героя: {len(hero)} ')
#
# # Создание объектов
# air_hero = AirHero("AirMan", "The Flyer", "Flying", 100, "Up and away!", 10, wing_span=15)
# earth_hero = EarthHero("EarthMan", "The Groundbreaker", "Earth control", 150, "Down to Earth!", 15, ground_speed=25)
#
# # Демонстрация методов
# air_hero.double_up_health_points()
# earth_hero.double_up_health_points()
#
# air_hero.true_phrase()
# earth_hero.true_phrase()
#
# print(air_hero)
# print(earth_hero)
#
# # Создание объекта злодея и демонстрация метода crit
# villain = Villain("VillainName", "The Evil Flyer", "Dark Flying", 200, "Fear the sky!", 20, wing_span=20)
# villain.crit(2)
# print(f"Злодей после усиления урона: Урон: {villain.damage}")



class SuperHero:
    people = 'people'
    def __init__(self, name, nickname, superpower, health_points, catchrase, damage=0):  # Добавлен параметр damage
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = int(health_points)  # Убедимся, что health_points является числом
        self.catchrse = catchrase
        self.damage = damage  # Новый атрибут

    def name_hero(self):
        print(f'Имя героя: {self.name}')

    def double_up_health_points(self):
        self.health_points *= 2

    def __str__(self):
        return (f'Прозвище героя: {self.nickname}'
                f'\nСуперспособность: {self.superpower}\nЗдоровье героя: {self.health_points}')

    def __len__(self):
        return len(self.catchrse)
#
class AirHero(SuperHero):
    def __init__(self, *args, wing_span, **kwargs):
        super().__init__(*args, **kwargs)
        self.wing_span = wing_span
        self.fly = False  # Новый атрибут fly

    def double_up_health_points(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

class EarthHero(SuperHero):
    def __init__(self, *args, ground_speed, **kwargs):
        super().__init__(*args, **kwargs)
        self.ground_speed = ground_speed
        self.fly = False  # Новый атрибут fly

    def double_up_health_points(self):
        self.health_points **= 2
        self.fly = True

    def true_phrase(self):
        print("True in the True_phrase")

class Villain(AirHero):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self, target, power):
        target.damage **= power

# Пример использования
# Создание объекта злодея и объекта героя
villain = Villain("VillainName", "The Evil Flyer", "Dark Flying", 200, "Fear the sky!", 20, wing_span=20)
hero = AirHero("HeroName", "The Brave Flyer", "Heroic Flying", 100, "For the skies!", damage=10, wing_span=15)

# Применение метода crit к герою
villain.crit(hero, 2)
print(villain)
print(hero)
print(f"Герой после атаки злодея: Урон: {hero.damage}")




