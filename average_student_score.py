#Список оценок для каждого ученика в алфавитном порядке.
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

#Неупорядоченная последовательность имён всех учеников в классе
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Cловарь для хранения имени ученика и его среднего балла
average_grades = {}

# Преобразуем множество students в отсортированный список для соответствия оценкам
sorted_students = sorted(students)

# Пробегаемся по отсортированным именам учеников и их оценкам
while len(grades) != 0 :
    #Извлекаем первый элемент списка
    list_value = grades.pop(0)

    #Расчитываем средний балл
    calculation_score = sum(list_value) / len(list_value)

    #Извлекаем первый элемент множества
    student = sorted_students.pop(0)

    #Складываем итоговый словарь со средними баллами
    average_grades[student] = calculation_score

# Выводим итоговый словарь со средними баллами
print(average_grades)