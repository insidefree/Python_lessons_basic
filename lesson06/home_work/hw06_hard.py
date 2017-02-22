# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчеты заработной платы (файл "data/workers"). Рассчитайте зарплату всех работников,
# зная что они получат полный оклад, если отработаю норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают удвоенную ЗП
# пропорциональную норме.
# Кол-во часов, которые были отработаны указаны в файле "data/hours_of"

# С использованием классов.
# Рализуйте классы сотрудников так, чтобы на вход функции-конструктора каждый работник получал строку из файла


from lesson06.home_work.hw06_classes.Company import Company
from lesson06.home_work.hw06_classes.Employee import Employee

file_workers = "data/workers"
file_hours = "data/hours_of"

bench_com = Company("bench.com", {})

worked_hours = {}

with open(file_hours, 'r', encoding="UTF-8") as f:
    first_line = f.readline()
    for l in f:
        worker = l.split()
        worked_hours.update({worker[1]: worker[2]})

with open(file_workers, 'r', encoding='UTF-8') as f:
    first_line = f.readline()
    id = 1
    for l in f:
        emp = l.split()
        print(emp)
        bench_com.add_employee(
            {id: Employee(id, emp[0], emp[1], emp[3], emp[2], emp[4], worked_hours[emp[1]],
                          round((int(emp[2]) / int(emp[4])), 2))})
        id += 1

dic = {
    "a": 1,
    "b": 2
}
dic.update({"c": 3})
print(dic)
print(bench_com.get_employees())
print(worked_hours)
print(bench_com.get_employee_salary)
