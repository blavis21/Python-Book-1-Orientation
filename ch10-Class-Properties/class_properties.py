# PRACTICE: Solid Student
class Student():

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

b = Student()
b.__first_name = "Blake"
b.__last_name = "Davis"
