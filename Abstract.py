import abc
import re


class Animal(abc.ABC):
    def __init__(self, name="No-Name", gender="male"):
        self._name = name
        self._shout_num = 3
        self._gender = gender

    @property
    def shout_num(self) -> str:
        return self._shout_num

    @shout_num.setter
    def shout_num(self, num: int):
        self._shout_num = num

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, gender: str):
        pattern = r"^[a-zA-Z]+"
        if re.match(pattern, gender):
            if gender.upper() == "F" or gender.upper() == "FEMALE":
                self._gender = "female"
            else:
                self._gender = "male"

    def shout(self) -> str:
        result = ""
        for _ in range(self._shout_num):
            result += self._getShoutSound()+" "
        gender = ""
        if self._gender == "female":
            gender = "Her"
        else:
            gender = "His"

        return f"{gender} name is {self._name}. {result}"

    @abc.abstractmethod
    def _getShoutSound(self):
        pass


class Cat(Animal):
    def _getShoutSound(self):
        return "Meow~"


class Dog(Animal):
    def _getShoutSound(self):
        return "Woof~"


if __name__ == "__main__":

    dog = Dog("Ago")
    print(dog.shout())
    cat = Cat("Meow")
    print(cat.shout())
    cat.gender = "female"
    print(cat.shout())
