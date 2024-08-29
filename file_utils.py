def save_student(student: dict):

    with open('data/students.csv', 'a+') as file:
        file.write(f'{student["id"]},{student["name"]},{student["age"]}\n')