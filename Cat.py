from Animal import Animal


class Cat(Animal):
    """
    创建子类【猫】，继承【动物类】，
    重写父类的__init__方法，继承父类的属性，
    添加一个新的属性，毛发 = 短毛，
    添加一个新的方法， 会捉老鼠，
    重写父类的【会叫】的方法，改成【喵喵叫】
    """
    def __init__(self, name='猫', color='蓝色', age='2', gender='公', hair='短毛'):
        super().__init__(name, color, age, gender)
        self.hair = hair

    def shout(self):
        print(f'{self.name} 正在喵喵叫')

    def catch_mouse(self):
        print(f'{self.name} 会抓老鼠')


if __name__ == '__main__':
    cat = Cat()
    cat.get_animal_info()
    cat.shout()
    cat.run()
    cat.catch_mouse()
