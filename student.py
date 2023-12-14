class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)

#     @property
#     def name(self):
#         return self.name

#     @name.setter
#     def name(self, name):
#         if not name:
#             raise ValueError("Missing name.")
#         self._name = name

#     @property
#     def house(self):
#         return self._house

#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house.")
#         self._house = house


def main():
    student = Student.get()
    print(student)


# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

# # #

#     student = {"name": input("Name: "), "house": input("House: ")}
#     return student

# # #

# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# # #

# def get_name():
#     name = input("Name: ")
#     return name


# def get_house():
#     house = input("House: ")
#     return house

if __name__ == "__main__":
    main()
