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



