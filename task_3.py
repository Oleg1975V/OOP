from statistics import mean

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.lecture_grades = {}

    def add_lecture_grade(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        grades_list = []
        for course_grades in self.grades.values():
            grades_list.extend(course_grades)
        if len(grades_list) > 0:
            return round(mean(grades_list), 1)
        else:
            return None

    def __str__(self):
        average_grade = self.get_average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        result = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {average_grade or 'Нет оценок за домашние задания'}
Курсы в процессе изучения: {courses_in_progress_str}
Завершенные курсы: {finished_courses_str}
'''
        return result.strip()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только объекты типа Student")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg < other_avg

    def __gt__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только объекты типа Student")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg > other_avg

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise TypeError("Можно сравнивать только объекты типа Student")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg == other_avg


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    
    def get_average_grade(self):
        grades_list = []
        for course_grades in self.grades.values():
            grades_list.extend(course_grades)
        if len(grades_list) > 0:
            return round(mean(grades_list), 1)
        else:
            return None

    def __str__(self):
        average_grade = self.get_average_grade()
        result = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {average_grade or 'Нет оценок'}
'''
        return result.strip()

    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только объекты типа Lecturer")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg < other_avg

    def __gt__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только объекты типа Lecturer")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg > other_avg

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise TypeError("Можно сравнивать только объекты типа Lecturer")
        my_avg = self.get_average_grade() or 0
        other_avg = other.get_average_grade() or 0
        return my_avg == other_avg


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    
    def check_homework(self, student, course):
        print(f"{student.name} {student.surname}, ваше домашнее задание по курсу {course} проверено.")

    def __str__(self):
        result = f'''
Имя: {self.name}
Фамилия: {self.surname}
'''
        return result.strip()
    
    # Создаём объекты
some_student = Student('Ruoy', 'Eman', 'мужской')
some_student.grades['Python', 'Git'] = [9, 10, 10, 10, 10, 10, 10]
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.grades['Python'] = [9, 10, 10, 10, 10, 10, 10]

some_reviewer = Reviewer('Some', 'Buddy')

# Проверяем вывод информации
print(some_reviewer)
print(some_lecturer)
print(some_student)