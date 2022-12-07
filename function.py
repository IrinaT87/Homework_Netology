student_list=[{'name':'Иван', 'surname':'Иванов', 'gender':'male', 'Python':[10,8,10,6], 'Git':[10,10]}, 
{'name':'Мария', 'surname':'Петрова', 'gender':'female', 'Python':[10,10,10], 'Git':[10,10,10]},
{'name':'Ольга', 'surname':'Сидорова', 'gender':'female', 'Python':[8,7,9,10], 'Git':[8,8]}, 
{'name':'Иван', 'surname':'Петров', 'gender':'male', 'Python':[10,10,10,7,8], 'Git':[10]},
{'name':'Виктория', 'surname':'Иванова', 'gender':'female', 'Python':[6,8,10,8], 'Git':[8,7]} ]

def avg_hw (students):
    course=input('Введите название курса, по которому требуется посчитать средний балл: ')
    sum_hw=0
    

    for student in students:
        for key, value in student.items():
            if course == key:
                sum_hw+=sum(student[course])/len(student[course])       
                         
    return round(sum_hw/len(students), 2)
    
print(avg_hw(student_list))


lecturer_list=[{'name':'Иван', 'surname':'Иванов', 'Python':[8, 9,9,10,9]}, 
{'name':'Василий', 'surname':'Васильев', 'Python':[10,10,9]},
{'name':'Петр', 'surname':'Петров', 'Python':[8,10,10,9,10]}, 
{'name':'Виктор', 'surname':'Викторов', 'Python':[10,10,10,7,8]}]

def avg_lecturer(lecturers, course):
    sum_avg_rate = 0
    
    for lecturer in lecturers:
        for key, value in lecturer.items():
            if course == key:
                sum_avg_rate += sum(lecturer[course]) / len(lecturer[course])
                
    return round(sum_avg_rate/len(lecturers), 2)
    

print(avg_lecturer(lecturer_list, 'Python'))
