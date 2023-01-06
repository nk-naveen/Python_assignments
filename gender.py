

from abc import ABC ,abstractmethod

class Person(ABC):
    # def __init__(self, value):
    #     self.value =value
    #     super().__init__()

    @abstractmethod
    def gender_info(self):
        print("Gender of person is:")

class Male(Person):

    def gender_info(self):
        super().gender_info()
        print("male")

class Female(Person):

    def gender_info(self):
        super().gender_info()

        print("female")

f = Female()
m = Male()
f.gender_info()
m.gender_info()
