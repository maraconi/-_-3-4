class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lector(self, lecture, course, grade):
        if isinstance(lecture, Lecturer) and course in lecture.lecture_courses and course in self.courses_in_progress:
            if course in lecture.lecture_grades:
                lecture.lecture_grades[course] += grade
            else:
                lecture.lecture_grades[course] = grade
        else:
            return 'Ошибка'

    def average_grades(self):
        sum_grades = 0
        count = 0
        for grades in self.grades.values():
            sum_grades += sum(grades)
            count += len(grades)
        return round(sum_grades / count, 2)

    def __gt__(self, other):
        if self.average_grades() > other.average_grades():
            return f'Лучший студент {self.name} {self.surname}  со средним баллом за оценки: {self.average_grades()}'
        else:
            return f'Лучший студент {other.name} {other.surname} со средним баллом за оценки: {other.average_grades()}'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Курсы в процессе изучения: {self.courses_in_progress[0]}, {self.courses_in_progress[1]}\n' \
              f'Оценки за домашние задания: {self.grades}\n' \
              f'Средняя оценка за домашние задания: {self.average_grades()}\n' \
              f'Завершенные курсы: {self.finished_courses[0]}\n'
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = ['Python', 'Git']


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecture_courses = []
        self.lecture_grades = {}

    def average_grades(self):
        sum_grades = 0
        count = 0
        for grades in self.lecture_grades.values():
            sum_grades += sum(grades)
            count += len(grades)
        return round(sum_grades / count, 2)

    def __gt__(self, other):
        if self.average_grades() > other.average_grades():
            return f'Лучший лектор {self.name} {self.surname}  со средним баллом за оценки: {self.average_grades()}'
        else:
            return f'Лучший лектор {other.name} {other.surname} со средним баллом за оценки: {other.average_grades()}'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n' \
              f'Оценки за лекции: {self.lecture_grades}\n' \
              f'Средняя оценка за лекции: {self.average_grades()}\n'
        return res


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += grade
            else:
                student.grades[course] = grade
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


def average_grades_student(student_list, course):
    sum_grades = 0
    for student in student_list:
        for c, grades in student.grades.items():
            if c == course:
                sum_grades += sum(grades) / len(grades)
    return sum_grades / len(student_list)


def average_grades_lecture(lecture_list, course):
    sum_grades = 0
    for lecture in lecture_list:
        for c, grades in lecture.lecture_grades.items():
            if c == course:
                sum_grades += sum(grades) / len(grades)
    return sum_grades / len(lecture_list)


student_1 = Student('Ivan', 'Petrov', 'your_gender')
student_1.finished_courses = ['Введение в программирование']
student_1.courses_in_progress += ['Python', 'Git']
student_2 = Student('Lev', 'Sidorov', 'your_gender')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses = ['Введение в программирование']

lecture_1 = Lecturer('Pavel', 'Loginov')
lecture_1.lecture_courses = ['Python', 'Git']
student_1.rate_lector(lecture_1, 'Python', [7])
student_2.rate_lector(lecture_1, 'Git', [8])
lecture_2 = Lecturer('Alex', 'Barinov')
lecture_2.lecture_courses = ['Python', 'Git']
student_2.rate_lector(lecture_2, 'Python', [9])
student_1.rate_lector(lecture_2, 'Git', [10])

reviewer_1 = Reviewer('Matvey', 'Kazak')
reviewer_1.rate_hw(student_1, 'Python', [7, 8, 10, 9])
reviewer_1.rate_hw(student_2, 'Python', [10, 8, 10, 10])
reviewer_2 = Reviewer('Irina', 'Kazak')
reviewer_2.rate_hw(student_1, 'Git', [9, 8, 9, 9])
reviewer_2.rate_hw(student_2, 'Git', [10, 8, 10, 9])

print(student_1)
print(lecture_1)
print(reviewer_1)
print(student_1 < student_2)
print(lecture_1 < lecture_2)
print()
print('Средняя оценка за домашние задания по всем студентам:', average_grades_student([student_1, student_2], 'Python'))
print('Средняя оценка за домашние задания по всем лекторам:', average_grades_lecture([lecture_1, lecture_2], 'Python'))