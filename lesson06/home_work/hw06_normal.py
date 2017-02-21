# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики. У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя, один учитель может преподавать в неограниченном кол-ве классов
# свой определенный предмет. Т.е. Учитель Иванов может преподавать математику у 5А и 6Б, но больше математику не
# может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе


class Person:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Teacher(Person):
    def __init__(self, first_name, last_name, level_list, subject):
        Person.__init__(self, first_name, last_name)
        self.level_list = level_list
        self.subject = subject

    def __str__(self):
        return "{} {} has {}. Profile: {}".format(self.first_name, self.last_name, self.level_list, self.subject)


class Schoolboy(Person):
    def __init__(self, first_name, last_name, father, mother, subjects):
        Person.__init__(self, first_name, last_name)
        self.father = father
        self.mother = mother
        self.subjects = subjects

    def __str__(self):
        return "{} {}, {}. Parents: {}, {}".format(self.first_name, self.last_name, self.level, self.father,
                                                   self.mother)


class Level:
    def __init__(self, number, letter, schoolboys):
        self.number = number
        self.letter = letter
        self.schoolboys = schoolboys

    def level_up(self):
        self.number += 1

    def __str__(self):
        return "{}{}".format(self.number, self.letter)


class Subject:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "{}".format(self.name)


class School:
    def __init__(self, name, teachers, levels):
        self.name = name
        self.teachers = teachers
        self.levels = levels

    def __str__(self):
        return "{}".format(self.name)


sb01 = Schoolboy(3, "Peter", "Pen", Person("papa_name", "papa_last_name"), Person("mama_name", "mama_last_name"),
                 ["math", "biology", "history"])
sb02 = Schoolboy(4, "Mashka", "Paska", Person("papa_name", "papa_last_name"),
                 Person("mama_name", "mama_last_name"),
                 ["math", "biology", "history"])
sb03 = Schoolboy(5, "Peter", "Pen", Person("papa_name", "papa_last_name"), Person("mama_name", "mama_last_name"),
                 ["math", "biology", "history"])
sb04 = Schoolboy(6, "Mashka", "Paska", Person("papa_name", "papa_last_name"),
                 Person("mama_name", "mama_last_name"),
                 ["math", "biology", "history"])

lvl_5A = Level(5, "A", {sb01})
lvl_5B = Level(5, "B", [sb02, sb01])
lvl_6A = Level(6, "A", [sb01, sb03])
lvl_6B = Level(6, "B", [sb01, sb04])

tc01 = Teacher(1, "Mari", "Vanna", [lvl_5A, lvl_6A], Subject("math"))
tc02 = Teacher(2, "Vanya", "Tolstiy", [lvl_5A, lvl_6A], Subject("math"))

# 1
school = School("school_name", [tc01, tc02], [lvl_5A, lvl_5B, lvl_6A, lvl_6B])
print("List levels", school.levels)

# 2

print(school.levels)
