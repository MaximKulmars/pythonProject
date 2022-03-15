class Student:
    '''
    Класс студентов.
    '''
    def __init__(self, name, surname, gender):  #инициализация класса студент.
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_finished = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lectur, course, grade):
        if isinstance(lectur, Lecturer) and course in self.courses_attached and course in lectur.courses_in_progress:
            if course in lectur.grades:
                lectur.grades[course] += [grade]
            else:
                lectur.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_grade(self): #подсчёт средней оценки для студента
        new = []
        count = 0
        for i in self.grades.values():
            new.extend(i)
        for q in new:
            count += q
        return round((count / len(new)), 1)



    def __str__(self):  #вывод данных об объекте класса студент
        text = f'Student:\nName: {self.name}\nSurname: {self.surname}\n\
Courses finished: {self.courses_finished}\n\
Courses in progress: {self.courses_in_progress}\nAverage rating: {self.mid_grade()}'  #дописать вывод средней оценки
        return text


class Mentor:
    '''
    Клас менторов. Общий (родительский) для всех типов преподавателей.
    '''

    def __init__(self, name, lastname, courses_attached):  #инициализация класса менторов
        self.name = name
        self.lastname = lastname
        self.courses_attached = []

    def __str__(self):  #вывод информации о классе менторов
        text = f'Имя: {self.name}\nФамилия: {self.lastname}'
        return text

class Lecturer(Mentor):
    '''
    Инициализация класса лекторов с наследованием класса менторов.
    '''
    def __init__(self, name, lastname, courses_attached):   #инициализация класса лекторов с наследованием класса менторов
        super().__init__(name, lastname, courses_attached)
        self.average_rating = []


    def __str__(self):   #вывод информации о классе лекторов
        text = f'Name: {self.name}\nSurname: {self.lastname}\nAverage rating: {self.average_rating}'
        return text


class Reviewer(Mentor):
    '''
     Инициализация класса проверяющих с наследованием от класса менторов.
    '''
    def __init__(self, name, lastname, courses_attached, work_evaluation=True):  #инициализация класса проверяющих с наследованием от класса менторов
        super().__init__(name, lastname, courses_attached)
        self.courses_attached = []


    def __str__(self):   #вывод информации об объекте класса проверяющих
        description = f'Имя: {self.name}\nФамилия: {self.lastname}'
        return description

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

stud1 = Student('Mark', 'Tven', 'man')
stud1.courses_finished += ['Введение в программирование', 'GIT']
stud1.courses_in_progress += ['Python']
review1 = Reviewer('Albert', 'Einstein', 'Python')
lectur1 = Lecturer('Che', 'Gevarra', 'Python')
review1.courses_attached += ['Python']
# print(review1.courses_attached)
# print(review1)

review1.rate_hw(stud1, 'Python', 10)
review1.rate_hw(stud1, 'Python', 9)
review1.rate_hw(stud1, 'Python', 8)
stud1.rate_hw(review1, 'Python', 9)
stud1.mid_grade()
# print(stud1)
# print(lectur1)
stud1.rate_hw(lectur1, 'Python', 9)