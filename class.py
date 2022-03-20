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
        if isinstance(lectur, Lecturer) and course in self.courses_in_progress and course in lectur.courses_attached:
            if course in lectur.courses_attached:
                lectur.mid_grade_.setdefault(course, [grade])
                lectur.mid_grade_[course] += [grade]
            else:
                lectur.mid_grade_.setdefault([course], [grade])
                lectur.mid_grade_[course] = [grade]
        else:
            return 'Ошибка'


    def mid_grade(self): #подсчёт средней оценки для студента
        new = []
        if len(self.grades.values()) < 1:
            return f'{self.name} {self.surname} has no ratings.'
        else:
            for i in self.grades.values():
                new += i
            mid_grades = round(sum(new) / len(new), 1)
            return mid_grades

    def course_aver(add_in_lis, course):
        pass


    def __lt__(self, other):    #сравнение по средней оценке студентов
        if not isinstance(other, Student):
            print(f'{other.name} {other.surname} is not a student')
            return
        else:
            if len(other.grades.values()) < 1:
                return f'Student {other.name} {other.surname} has no ratings.'
            else:
                return self.mid_grade() < other.mid_grade()


    def add_in_lis(self):
        lis_student = []
        if isinstance(self, Student):
            lis_student.append(self)
        else:
            return 'invalid class'


    def __str__(self):  #вывод данных об объекте класса студент
        text = f'Student:\nName: {self.name}\nSurname: {self.surname}\n\
Courses finished: {", ".join(self.courses_finished)}\n\
Courses in progress: {", ".join(self.courses_in_progress)}\nAverage rating: {self.mid_grade()}'  #дописать вывод средней оценки
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
        self.courses_attached = []
        self.mid_grade_ = {}


    def mid_grade(self):
        new = []
        if len(self.mid_grade_.values()) < 1:
            return f'{self.name} {self.lastname} has no ratings.'
        else:
            for i in self.mid_grade_.values():
                new += i
            mid_grades = round(sum(new) / len(new), 1)
            return mid_grades

    def add_in_lis(self):
        lis_lectur = []
        if isinstance(self, Lecturer):
            lis_lectur.append(self)
        else:
            return 'invalid class'

    def __lt__(self, other):   #сравнение по средней оценке лекторов
        if not isinstance(other, Lecturer):
            print(f'{other.name} {other.surname} is not a lectur')
            return
        else:
            if len(other.mid_grade_.values()) < 1:
                return f'{other.name} {other.lastname} has no ratings.'
            else:
                return self.mid_grade() < other.mid_grade()



    def __str__(self):   #вывод информации о классе лекторов
        text = f'Lectur:\nName: {self.name}\nSurname: {self.lastname}\nAverage rating: {self.mid_grade()}'
        return text


class Reviewer(Mentor):
    '''
     Инициализация класса проверяющих с наследованием от класса менторов.
    '''
    def __init__(self, name, lastname, courses_attached):  #инициализация класса проверяющих с наследованием от класса менторов
        super().__init__(name, lastname, courses_attached)
        self.courses_attached = []


    def __str__(self):   #вывод информации об объекте класса проверяющих
        description = f'Reviewer:\nName: {self.name}\nSurname: {self.lastname}'
        return description


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades and 0 <= grade <= 10:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

def perform_comparison(person1, person2):  #функция оценок студентов
    if isinstance(person1, Student) and isinstance(person2, Student):
        if person1.mid_grade() > person2.mid_grade():
            return f'Student performance {person1.name} better. Average score {person1.mid_grade()}'
        else:
            return f'Student performance {person2.name} better. Average score {person2.mid_grade()}'
    else:
        return 'Error. Invalid class.'

#student1
Sharikov = Student('Polikarp', 'Sharikov', 'man')
Sharikov.courses_in_progress += ['Python']
Sharikov.courses_finished += ['GIT']
print(Sharikov)
Sharikov.mid_grade()

# student2
Zharovkin = Student('Vasily', 'Zharovkin', 'man')
Zharovkin.courses_in_progress += ['Python', 'Big Data']
Zharovkin.courses_finished += ['GIT']
print(Zharovkin)

#lector1
Philipp = Lecturer('Philipp', 'Phillipovich', 'Python')
Philipp.courses_attached += ['GIT']
Sharikov.rate_hw(Philipp, 'Python', 9)
Zharovkin.rate_hw(Philipp, 'Python', 9)
print(Philipp)

#lector2
Bormental = Lecturer('Doctor', 'Bormental', 'Python')
Bormental.courses_attached += ['GIT']
Sharikov.rate_hw(Bormental, 'Python', 9)
Zharovkin.rate_hw(Bormental, 'Python', 10)
print(Bormental)

#reviewer1
Shvonder = Reviewer('Tovarich', 'Shvonder', 'Python')
Shvonder.courses_attached += ['GIT']
Shvonder.rate_hw(Sharikov, 'Python', 10)
Shvonder.rate_hw(Zharovkin, 'Python', 9)
print(Shvonder)

#reviewer2
Vjazemskaja = Reviewer('Grazhdanka', 'Vjazemskaja', 'Python')
Vjazemskaja.courses_attached += ['GIT']
Vjazemskaja.rate_hw(Sharikov, 'Python', 10)
Vjazemskaja.rate_hw(Zharovkin, 'Python', 9)
print(Vjazemskaja)

print(Sharikov < Zharovkin)