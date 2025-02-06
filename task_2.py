class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecture_grades = {}  # Новый словарь для хранения оценок лекторов

    def add_lecture_grade(self, lecturer, course, grade):
        """Метод для выставления оценки лектору"""
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}  # Словарь для хранения оценок за лекции


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """Только эксперты могут ставить оценки студентам"""
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def check_homework(self, student, course):
        print(f"{student.name} {student.surname}, ваше домашнее задание по курсу {course} проверено.")


# Создаем экземпляры классов
best_student = Student('Олег', 'Воробьев', 'мужской')
best_student.courses_in_progress += ['Python']

lecturer = Lecturer('Сергей', 'Петров')
lecturer.courses_attached += ['Python']

reviewer = Reviewer('Игорь', 'Самохвалов')
reviewer.courses_attached += ['Python']

# Лектор получает оценку от студента
best_student.add_lecture_grade(lecturer, 'Python', 9)
best_student.add_lecture_grade(lecturer, 'Python', 8)
best_student.add_lecture_grade(lecturer, 'Python', 7)

# Эксперт проверяет домашнее задание студента
reviewer.rate_hw(best_student, 'Python', 10)
reviewer.rate_hw(best_student, 'Python', 9)
reviewer.rate_hw(best_student, 'Python', 8)

# Проверяем оценки студента
print(best_student.grades)

# Проверяем оценки лектора
print(lecturer.grades)