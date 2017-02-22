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
    def __init__(self, id, first_name, last_name, subjects):
        Person.__init__(self, id, first_name, last_name)
        self.subjects = subjects

    def __str__(self):
        return "{} {}. {}".format(self.first_name, self.last_name, self.subjects)

    def __repr__(self):
        return "{} {}. {}".format(self.first_name, self.last_name,self.subjects)


class Schoolboy(Person):
    def __init__(self, id, first_name, last_name, father, mother, level):
        Person.__init__(self, id, first_name, last_name)
        self.father = father
        self.mother = mother
        self.level = level

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name, self.father,
                              self.mother)

    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)


class Level:
    def __init__(self, id, number, letter, schoolboys, teachers):
        self.id = id
        self.number = number
        self.letter = letter
        self.schoolboys = schoolboys
        self.teachers = teachers

    def level_up(self):
        self.number += 1

    def __str__(self):
        return "{}{}. {}. {}".format(self.number, self.letter, self.schoolboys, self.teachers)

    def __repr__(self):
        return "{}{}. {}. {}".format(self.number, self.letter, self.schoolboys, self.teachers)


class Subject:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}".format(self.name)


class School:
    def __init__(self, name, teachers, levels, schoolboys):
        self.name = name
        self.teachers = teachers
        self.levels = levels
        self.schoolboys = schoolboys

    def __str__(self):
        return "{}".format(self.name)

    def show_all_levels(self):
        for level in levels:
            print("{}{}. List of schoolboys: /n {}".format(level.number, level.letter, level.schoolboys))

    def show_all_schoolboys_in_level(self, level_id):
        print(self.levels[level_id].schoolboys)

    def show_schoolboy_subjects(self, schoolboy_id):
        level = self.schoolboys[schoolboy_id].level
        teachers = self.levels[level].teachers
        for t in teachers:
            print(teachers[t].subjects)

    def get_teachers_by_level(self, level_id):
        level = self.levels[level_id]
        print(level.teachers)




sb01 = Schoolboy(3, "Peter", "Pen", Person(7, "papa_name", "papa_last_name"), Person(8, "mama_name", "mama_last_name"),
                 "lvl_5A")
sb02 = Schoolboy(4, "Mashka", "Paska", Person(9, "papa_name", "papa_last_name"),
                 Person(10, "mama_name", "mama_last_name"), "lvl_5B")
sb03 = Schoolboy(5, "Peter", "Pen", Person(11, "papa_name", "papa_last_name"),
                 Person(12, "mama_name", "mama_last_name"), "lvl_6A")
sb04 = Schoolboy(6, "Mashka", "Paska", Person(13, "papa_name", "papa_last_name"),
                 Person(14, "mama_name", "mama_last_name"), "lvl_6B")

sub01 = Subject("id_math", "mathematics")
sub02 = Subject("id_hist", "history")
sub03 = Subject("id_biol", "biology")

tc01 = Teacher(1, "Mari", "Vanna", {sub01.id: sub01})
tc02 = Teacher(2, "Vanya", "Tolstiy", {sub02.id: sub02})

lvl_5A = Level("lvl_5A", 5, "A", {sb01.id: sb01, sb02.id: sb02}, {tc01.id: tc01, tc02.id: tc02})
lvl_5B = Level("lvl_5B", 5, "B", {sb03.id: sb01, sb02.id: sb02}, {tc02.id: tc02})
lvl_6A = Level("lvl_6A", 6, "A", {sb04.id: sb01, sb01.id: sb02}, {tc02.id: tc02})
lvl_6B = Level("lvl_6B", 6, "B", {sb02.id: sb01, sb03.id: sb02}, {tc01.id: tc01})

levels = {
}

subjects = {
    "id_math": sub01,
    "id_hist": sub02,
    "id_biol": sub03,
}

teachers = {

}

levels = {
    lvl_5A.id: lvl_5A,
    lvl_5B.id: lvl_5B,
    lvl_6A.id: lvl_6A,
    lvl_6B.id: lvl_6B,
}
schoolboys = {
    sb01.id: sb01,
    sb02.id: sb02,
    sb03.id: sb03,
    sb04.id: sb04
}

school = School("school_name", teachers, levels, schoolboys)

# 1. Получить полный список всех классов школы
print("Levels list\n", school.levels)

# 2. Получить список всех учеников в указанном классе(каждый ученик отображается в формате "Фамилия И.О.")
print("List of schoolboys at level 4A")
school.show_all_schoolboys_in_level("lvl_5A")

# 3. Получить список всех предметов указанного ученика (Ученик --> Класс --> Учителя --> Предметы)

school.show_schoolboy_subjects(3)

# 4. Узнать ФИО родителей указанного ученика
print(sb01.father)
print(sb01.mother)

# 5. Получить список всех Учителей, преподающих в указанном классе
print(school.get_teachers_by_level("lvl_5A"))