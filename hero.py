class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def real_name(self):
        print(f"Имя героя: {self.name}.")

    def double_health(self):
        self.health_points *= 2

    def __str__(self):
        return f"Nickname: {self.nickname},\nSuperpower: {self.superpower}, \nHealth: {self.health_points}"

    def __len__(self):
        return len(self.catchphrase)


hero = SuperHero("Диана", "Чудо-женщина",
                 "Физическая сила и летание", 1000, "За справедливость!")

hero.real_name()
hero.double_health()
print(hero)
print(f"Длина коронной фразы: {len(hero)}")
print('Коронная фраза Чудо-женщины "За справедливость!"')
