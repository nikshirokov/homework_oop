class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate_hw(self):
        return (sum([i for x in self.grades.values() for i in x]) / len(self.grades))

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.average_rate_hw()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __eq__(self, other):
        return self.average_rate_hw() == other.average_rate_hw()

    def __gt__(self, other):
        return self.average_rate_hw() > other.average_rate_hw()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_rate(self):
        return (sum([i for x in self.grades.values() for i in x]) / len(self.grades))

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.average_rate()}')

    def __eq__(self, other):
        return self.average_rate() == other.average_rate()

    def __gt__(self, other):
        return self.average_rate() > other.average_rate()


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

    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')


def average_rate_hw_all_student(students, course):
    avg_rt = sum([gr for student in students for gr in student.grades[course]]) / len(students)
    return f'Средняя оценка студентов за курс {course}: {avg_rt}'


def average_rate_lectures(lecturers, course):
    avg_rt_lec = sum([gr for lecturer in lecturers for gr in lecturer.grades[course]]) / len(lecturers)
    return f'Средняя оценка преподавателей за курс {course}: {avg_rt_lec}'


cool_student = Student('Николай', 'Широков', 'мужской')
cool_student.courses_in_progress += ['Python', 'Git']
cool_student.finished_courses += ['Введение в программирование']

some_student = Student('Ruoy', 'Eman', 'мужской')
some_student.courses_in_progress += ['Python', 'Git']
some_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('Тимур', 'Анвартдинов')
cool_lecturer.courses_attached += ['Python', 'Git']

some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']

cool_reviewer = Reviewer('Олег', 'Булыгин')
cool_reviewer.courses_attached += ['Python', 'Git']
cool_reviewer.rate_hw(cool_student, 'Python', 10)
cool_reviewer.rate_hw(cool_student, 'Git', 9)

some_reviewer = Reviewer('Buddy', 'Some')
some_reviewer.courses_attached += ['Python', 'Git']
some_reviewer.rate_hw(some_student, 'Python', 8)
some_reviewer.rate_hw(some_student, 'Git', 8)

cool_student.rate_lec(cool_lecturer, 'Python', 10)
cool_student.rate_lec(cool_lecturer, 'Git', 9)
some_student.rate_lec(some_lecturer, 'Python', 8)
some_student.rate_lec(some_lecturer, 'Git', 8)

print(cool_student)
print()
print(some_student)
print()
print(cool_lecturer)
print()
print(some_lecturer)
print()
print(cool_reviewer)
print()
print(some_reviewer)
print()
print(cool_lecturer == some_lecturer)
print()
print(cool_lecturer > some_lecturer)
print()
print(cool_student == some_student)
print()
print(cool_student > some_student)
print()
print(average_rate_hw_all_student([cool_student, some_student], 'Python'))
print()
print(average_rate_hw_all_student([cool_student, some_student], 'Git'))
print()
print(average_rate_lectures([cool_lecturer, some_lecturer], 'Python'))
print()
print(average_rate_lectures([cool_lecturer, some_lecturer], 'Git'))
