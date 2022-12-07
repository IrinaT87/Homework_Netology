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


    def _avg_rate_hw(self, grades):
        avg_grade=0
        count=0
        for grade in self.grades.values():
            for el in grade:
                avg_grade+=el
                count+=1
                res=avg_grade/count
        return res  


    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        res=f'Имя: {self.name}\nФамилия: {self.surname}\nКурсы в процессе обучения: {self.courses_in_progress}\n\
Завершенные курсы: {self.finished_courses}\nСредняя оценка за домашние задания: {self._avg_rate_hw(self.grades)}'
        return res

    def __gt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student') 
            return
        return self._avg_rate_hw(self.grades) > other._avg_rate_hw(other.grades)
 
     
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades={}

    def _avg_rate(self, grades):
        avg_grade=0
        count=0
        for grade in self.grades.values():
            for el in grade:
                avg_grade+=el
                count+=1
                res=avg_grade/count
        return res     


    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer') 
            return
        return self._avg_rate(self.grades) < other._avg_rate(self.grades)



    def __str__(self):
        res=f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._avg_rate(self.grades)}'
        return res


class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


    def __str__(self):
        res=f'Имя: {self.name}\nФамилия: {self.surname}'
        return res
 
student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ['Git']

student_2 = Student('Liza', 'Loy', 'female')
student_2.courses_in_progress += ['Python']
student_2.courses_in_progress += ['Git']
student_2.finished_courses += ['English']

lecturer_1=Lecturer('Ivan', 'Ivanov')
lecturer_1.courses_attached=['Git']

lecturer_2=Lecturer('Petr', 'Petrov')
lecturer_2.courses_attached=['Python','Git']

student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Git', 8)

student_2.rate_lecturer(lecturer_2, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 10)
student_1.rate_lecturer(lecturer_2, 'Python', 10)

reviewer_1=Reviewer('Sergey', 'Sergeev')
reviewer_1.courses_attached=['English', 'Git', 'Python']
reviewer_2=Reviewer('Oleg', 'Sokolov')
reviewer_2.courses_attached=['Python']

reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_1, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Git', 9)
reviewer_2.rate_hw(student_2, 'Python', 9)

print(student_1)
print(student_2)

print(lecturer_1)
print(lecturer_2)

print(reviewer_1)
print(reviewer_2)

print(student_1.__gt__(student_2))
print(lecturer_1.__lt__(lecturer_2))

