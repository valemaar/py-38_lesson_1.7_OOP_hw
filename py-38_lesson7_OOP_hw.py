class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached\
                and course in self.courses_in_progress and grade in range(1, 11):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return print('Ошибка!!')

    # перегрузим метод __str__ для класса Student
    def __str__(self):
        # list_to_str = (*self.courses_in_progress)
        if isinstance(self, Student):
            return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за' \
                   f' домашние задания: {average_grade(self.grades)}\nКурсы в процессе изучения:' \
                   f' {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return

    # добавим возможность сравнения студентов по средним оценкам за дз операторами > <
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Класс объекта не "Student" !')
            return
        return average_grade(self.grades) < average_grade(other.grades)

    # добавим возможность сравнения студентов по средним оценкам за дз оператором ==
    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Класс объекта не "Student" !')
            return
        return average_grade(self.grades) == average_grade(other.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        if isinstance(self, Lecturer):
            return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за' \
                   f' лекции: {average_grade(self.grades)}'
        return

    # добавим возможность сравнения лекторов по средним оценкам операторами > <
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Класс объекта не "Lecturer" !')
            return
        return average_grade(self.grades) < average_grade(other.grades)

    # добавим возможность сравнения лекторов по средним оценкам оператором ==
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Класс объекта не "Lecturer" !')
            return
        return average_grade(self.grades) == average_grade(other.grades)


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and\
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return print('Ошибка!')

    def __str__(self):
        if isinstance(self, Reviewer):
            return f'Имя: {self.name}\nФамилия: {self.surname}'
        return


def average_grade(person):
    my_sum = 0
    my_len = 0
    for el in person:
        my_sum += sum(person[el])
        my_len += len(person[el])
    return round(my_sum/my_len, 1)

    # for key, value in person.items():
    #     my_sum += sum(value)
    #     my_len += len(value)
    # return round(my_sum/my_len, 1)


def give_all_stud_average_grades(stud_list, course):
    aver_sum = 0
    aver_len = 0
    for stud in stud_list:
        for key, value in stud.grades.items():
            if key == course:
                aver_sum += sum(value)
                aver_len += len(value)
    summary = aver_len
    if summary == 0:
        summary = 'Ни один студент не изучает данный курс!'
    else:
        summary = round(aver_sum/aver_len, 2)
    return summary


def give_all_lect_average_grades(lect_list, course):
    aver_sum = 0
    aver_len = 0
    for lect in lect_list:
        for key, value in lect.grades.items():
            if key == course:
                aver_sum += sum(value)
                aver_len += len(value)
    summary = aver_len
    if summary == 0:
        summary = 'Ни один лектор не преподает данный курс!'
    else:
        summary = round(aver_sum/aver_len, 2)
    return summary


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.courses_in_progress += ['C++']
best_student.finished_courses += ['HTML']

some_student = Student('John', 'Smith', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Java']
some_student.courses_in_progress += ['HTML']
some_student.finished_courses += ['C++']

best_lecturer = Lecturer('Best', 'Teacher')
best_lecturer.courses_attached += ['Python', 'Java', 'C++', 'HTML']

some_lecturer = Lecturer('Donald', 'Thumb')
some_lecturer.courses_attached += ['Python', 'Java']

best_reviewer = Reviewer('Some', 'Buddy')
best_reviewer.courses_attached += ['Python', 'Java', 'C++']

some_reviewer = Reviewer('April', 'March')
some_reviewer.courses_attached += ['Python', 'Java', 'HTML']

best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Python', 10)
best_reviewer.rate_hw(best_student, 'Java', 9)
best_reviewer.rate_hw(best_student, 'Java', 8)
best_reviewer.rate_hw(best_student, 'C++', 8)
best_reviewer.rate_hw(best_student, 'C++', 7)

best_reviewer.rate_hw(some_student, 'Python', 8)
best_reviewer.rate_hw(some_student, 'Python', 7)
best_reviewer.rate_hw(some_student, 'Java', 6)
best_reviewer.rate_hw(some_student, 'Java', 7)
some_reviewer.rate_hw(some_student, 'HTML', 9)
some_reviewer.rate_hw(some_student, 'HTML', 8)


best_student.rate_lecturer(best_lecturer, 'Python', 10)
best_student.rate_lecturer(best_lecturer, 'Python', 5)

best_student.rate_lecturer(some_lecturer, 'Python', 6)
best_student.rate_lecturer(some_lecturer, 'Python', 8)

print('best_student.grades =', best_student.grades)
print(str(best_student))
print()

print('some_student.grades =', some_student.grades)
print(str(some_student))
print()

print('best_lecturer.grades =', best_lecturer.grades)
print(str(best_lecturer))
print()

print('some_lecturer.grades =', some_lecturer.grades)
print(str(some_lecturer))
print()

print('best_reviewer')
print(str(best_reviewer))
print()

print('some_reviewer')
print(str(some_reviewer))
print()

print(best_lecturer == some_lecturer)
print(best_lecturer > some_lecturer)
print(best_lecturer < some_lecturer)
print()

print(best_student == some_student)
print(best_student > some_student)
print(best_student < some_student)
print()

# Task 4.1
students_list = [best_student, some_student]
course_title_st = 'Python'

print(f'Средняя оценка среди всех студентов по курсу "{course_title_st}":')
print(give_all_stud_average_grades(students_list, course_title_st))
print()

# Task 4.2
lecturers_list = [best_lecturer, some_lecturer]
course_title_lec = 'Python'

print(f'Средняя оценка за лекции среди всех лекторов по курсу "{course_title_lec}":')
print(give_all_lect_average_grades(lecturers_list, course_title_lec))
