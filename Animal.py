# -=- coding=utf-8 -*- #


class Animal:
    """
        创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
    """
    def __init__(self, name='动物', color='黑色', age='10', gender='公'):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def get_animal_info(self):
        print(f'动物信息：{self.__dict__}')

    def shout(self):
        print(f'{self.name} 正在叫')

    def run(self):
        print(f'{self.name} 正在跑')


if __name__ == '__main__':
    animal = Animal('狗', '白色', '3', '母')
    animal.get_animal_info()
    animal.shout()
    animal.run()
