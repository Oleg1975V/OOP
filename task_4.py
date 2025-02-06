"""Классы:
Student – класс для представления студентов.
Mentor – базовый класс для наставников.
Lecturer – подкласс класса Mentor, представляющий преподавателей.
Reviewer – еще один подкласс класса Mentor, представляющий рецензентов.
"""

from statistics import mean

class Student:
    """Класс для представления студентов."""

    def __init__(self, name, surname, gender):
        """
        Конструктор класса Student.

        :param name: Имя студента
        :param surname: Фамилия студента
        :param gender: Пол студента
        """
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []  # Список завершенных курсов
        self.courses_in_progress = []  # Список текущих курсов
        self.grades = {}  # Словарь с оценками по каждому курсу

    def add_lecture_grade(self, lecturer, course, grade):
        """
        Добавляет оценку за лекцию от преподавателя.

        :param lecturer: Объект класса Lecturer
        :param course: Название курса
        :param grade: Оценка за лекцию
        """
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        """
        Возвращает среднюю оценку студента по всем курсам или None, если оценок нет.
        """
        grades_list = []
        for course_grades in self.grades.values():
            grades_list.extend(course_grades)
        if len(grades_list) > 0:
            return round(mean(grades_list), 1)
        else:
            return None

    def __str__(self):
        """
        Магический метод для строкового представления объекта.

        :return: Строка с информацией о студенте
        """
        average_grade = self.get_average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        result = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: '
            f'{average_grade or "Нет оценок за домашние задания"}\n'
            f'Курсы в процессе изучения: {courses_in_progress_str}\n'
            f'Завершенные курсы: {finished_courses_str}'
        )
        return result.strip()

    def __lt__(self, other):
        """
        Сравнивает двух студентов по средней оценке.

        :param other: Другой объект класса Student
        :return: True, если средняя оценка текущего объекта меньше средней оценки другого объекта
        """
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только объекты типа Student")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg < other_avg

    def __gt__(self, other):
        """
        Сравнивает двух студентов по средней оценке.

        :param other: Другой объект класса Student
        :return: True, если средняя оценка текущего объекта больше средней оценки другого объекта
        """
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только объекты типа Student")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg > other_avg

    def __eq__(self, other):
        """
        Сравнивает двух студентов по средней оценке.

        :param other: Другой объект класса Student
        :return: True, если средние оценки обоих объектов равны
        """
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только объекты типа Student")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg == other_avg


class Mentor:
    """Базовый класс для наставников."""

    def __init__(self, name, surname):
        """
        Конструктор класса Mentor.

        :param name: Имя наставника
        :param surname: Фамилия наставника
        """
        self.name = name
        self.surname = surname
        self.courses_attached = []  # Список прикрепленных курсов


class Lecturer(Mentor):
    """Подкласс класса Mentor, представляющий преподавателей."""

    def __init__(self, name, surname):
        """
        Конструктор класса Lecturer.

        :param name: Имя преподавателя
        :param surname: Фамилия преподавателя
        """
        super().__init__(name, surname)
        self.grades = {}  # Словарь с оценками за лекции

    def get_average_grade(self):
        """
        Возвращает среднюю оценку преподавателя по всем курсам или None, если оценок нет.
        """
        grades_list = []
        for course_grades in self.grades.values():
            grades_list.extend(course_grades)
        if len(grades_list) > 0:
            return round(mean(grades_list), 1)
        else:
            return None

    def __str__(self):
        """
        Магический метод для строкового представления объекта.

        :return: Строка с информацией о преподавателе
        """
        average_grade = self.get_average_grade()
        result = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {average_grade or "Нет оценок"}'
        )
        return result.strip()

    def __lt__(self, other):
        """
        Сравнивает двух преподавателей по средней оценке.

        :param other: Другой объект класса Lecturer
        :return: True, если средняя оценка текущего объекта меньше средней оценки другого объекта
        """
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только объекты типа Lecturer")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg < other_avg

    def __gt__(self, other):
        """
        Сравнивает двух преподавателей по средней оценке.

        :param other: Другой объект класса Lecturer
        :return: True, если средняя оценка текущего объекта больше средней оценки другого объекта
        """
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только объекты типа Lecturer")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg > other_avg

    def __eq__(self, other):
        """
        Сравнивает двух преподавателей по средней оценке.

        :param other: Другой объект класса Lecturer
        :return: True, если средние оценки обоих объектов равны
        """
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только объекты типа Lecturer")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg == other_avg


class Reviewer(Mentor):
    """Подкласс класса Mentor, представляющий рецензентов."""

    def __init__(self, name, surname):
        """
        Конструктор класса Reviewer.

        :param name: Имя рецензента
        :param surname: Фамилия рецензента
        """
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        """
        Выставляет оценку студенту за домашнюю работу.

        :param student: Объект класса Student
        :param course: Название курса
        :param grade: Оценка за домашнюю работу
        """
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def check_homework(self, student, course):
        """
        Проверяет домашнее задание студента.

        :param student: Объект класса Student
        :param course: Название курса
        """
        print(f"{student.name} {student.surname}, ваше домашнее задание по курсу {course} проверено.")

    def __str__(self):
        """
        Магический метод для строкового представления объекта.

        :return: Строка с информацией о рецензенте
        """
        result = (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}'
        )
        return result.strip()
    

# Теперь создадим экземпляры классов и вызовем их методы:
# Создание экземпляров классов

# Студенты
student1 = Student('Иван', 'Петров', 'мужской')
student2 = Student('Анна', 'Иванова', 'женский')

# Преподаватели
lecturer1 = Lecturer('Петр', 'Анечкин')
lecturer2 = Lecturer('Галина', 'Машкина')

# Рецензенты
reviewer1 = Reviewer('Маша', 'Галочкина')
reviewer2 = Reviewer('Арсений', 'Быков')

# Добавление курсов к объектам
student1.courses_in_progress.append('Python')
student2.courses_in_progress.append('Git')

lecturer1.courses_attached.append('Python')
lecturer2.courses_attached.append('Git')

reviewer1.courses_attached.append('Python')
reviewer2.courses_attached.append('Git')

# Выставление оценок студентам
reviewer1.rate_hw(student1, 'Python', 9)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer2.rate_hw(student2, 'Git', 10)
reviewer2.rate_hw(student2, 'Git', 7)

# Проверка домашних заданий
reviewer1.check_homework(student1, 'Python')
reviewer2.check_homework(student2, 'Git')

# Вывод информации о студентах
print(student1)
print(student2)

# Вывод информации о преподавателях
print(lecturer1)
print(lecturer2)

# Выставление оценок лекторам
student1.add_lecture_grade(lecturer1, 'Python', 9)
student1.add_lecture_grade(lecturer1, 'Python', 8)
student2.add_lecture_grade(lecturer2, 'Git', 9)
student2.add_lecture_grade(lecturer2, 'Git', 8)

# Вывод информации о рецензентах
print(reviewer1)
print(reviewer2)

# Сравнение студентов
print("Сравнение студентов:")
if student1 > student2:
    print(f"{student1.name} имеет более высокую среднюю оценку, чем {student2.name}")
elif student1 < student2:
    print(f"{student2.name} имеет более высокую среднюю оценку, чем {student1.name}")
else:
    print(f"{student1.name} и {student2.name} имеют одинаковые средние оценки")

# Сравнение преподавателей
print("\nСравнение преподавателей:")
if lecturer1 > lecturer2:
    print(f"{lecturer1.name} имеет более высокую среднюю оценку, чем {lecturer2.name}")
elif lecturer1 < lecturer2:
    print(f"{lecturer2.name} имеет более высокую среднюю оценку, чем {lecturer1.name}")
else:
    print(f"{lecturer1.name} и {lecturer2.name} имеют одинаковые средние оценки")


# Теперь добавим две функции для расчета средних оценок по курсам:

def avg_student_grade(students, course):
    """
    Функция для подсчета средней оценки за домашние задания по всем студентам в рамках конкретного курса.
    
    :param students: Список студентов
    :param course: Название курса
    :return: Средняя оценка или None, если нет оценок
    """
    grades_list = []
    for student in students:
        if course in student.grades:
            grades_list.extend(student.grades[course])
    if len(grades_list) > 0:
        return round(mean(grades_list), 1)
    else:
        return None

def avg_lecturers_grade(lectors, course):
    """
    Функция для подсчета средней оценки за лекции всех лекторов в рамках курса.
    
    :param lectors: Список лекторов
    :param course: Название курса
    :return: Средняя оценка или 0, если нет оценок
    """
    grades_list = []
    for lecturer in lectors:
        if course in lecturer.grades:
            grades_list.extend(lecturer.grades[course])
    
    if len(grades_list) > 0:
        return round(sum(grades_list) / len(grades_list), 1)
    else:
        return 0

# Пример использования функций:

students = [student1, student2]
lectors = [lecturer1, lecturer2]

avg_students_python = avg_student_grade(students, 'Python')
avg_students_git = avg_student_grade(students, 'Git')

avg_lectors_python = avg_lecturers_grade(lectors, 'Python')

avg_lectors_git = avg_lecturers_grade(lectors, 'Git')

print(f"Средняя оценка студентов по Python: {avg_students_python}")
print(f"Средняя оценка студентов по Git: {avg_students_git}")
print(f"Средняя оценка лекторов по Python: {avg_lectors_python}")
print(f"Средняя оценка лекторов по Git: {avg_lectors_git}")