# Для решения этой задачи нам необходимо сделать так, чтобы классы Lecturer и Reviewer
# унаследовали свойства и методы от базового класса Mentor. Важно учесть специфику
# каждого подкласса.

# Класс Student оставляем без изменений.
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}


# Базовый класс Mentor
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


# Класс для лекторов (наследуется от Mentor)
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Метод для выставления оценки студенту (метод из Mentor)
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


# Класс для экспертов (также наследуется от Mentor)
class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    # Методы для проверки домашних заданий
    def check_homework(self, student, course):
        print(f"{student.name} {student.surname}, ваш домашний задание по курсу {course} проверено.")


# Создаем экземпляры классов
best_student = Student('Олег', 'Воробьев', 'мужской')
best_student.courses_in_progress += ['Python']

lecturer = Lecturer('Сергей', 'Петров')
lecturer.courses_attached += ['Python']

reviewer = Reviewer('Игорь', 'Самохвалов')
reviewer.courses_attached += ['Python']

# Лектор ставит оценку студенту
lecturer.rate_hw(best_student, 'Python', 9)
lecturer.rate_hw(best_student, 'Python', 8)
lecturer.rate_hw(best_student, 'Python', 7)

# Эксперт проверяет домашнее задание студента
reviewer.check_homework(best_student, 'Python')

# Проверяем оценки студента
print(best_student.grades)