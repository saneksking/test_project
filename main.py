# TODO: New super code


class Animal:
    def __init__(self, name, ):
        self.name = name

    def __str__(self):
        return self.name


class Dog(Animal):
    def __init__(self, name, color, legs):
        super().__init__(name)
        self.color = color
        self.legs = legs

    @staticmethod
    def say():
        print('Woof')


def main():
    pass
    dog = Dog(name='Шарик', color='чёрный', legs=4)
    print(f'У меня есть собака. Её зовут {dog.name}. Её цвет {dog.color}. У неё {dog.legs} лапы.')


if __name__ == '__main__':
    main()
