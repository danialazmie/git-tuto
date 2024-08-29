import pandas as pd
import os
from print_utils import print_title

def save_student(student: dict):
    df = pd.read_csv('data/students.csv')
    df = pd.concat([df, pd.DataFrame(student, index=[df.shape[1]])], ignore_index=True)
    df.to_csv('data/students.csv', index=False)

def add_student():
    os.system('cls')
    print_title('Add Student')

    id_ = input('Enter student id: ')
    name = input('Enter student name: ')
    age = int(input('Enter student age: '))

    student = {
        'id': id_,
        'name': name,
        'age': age
    }
    save_student(student)

    print('\nStudent added successfully\n')
    os.system('pause')

    pass

def delete_student():
    pass

def update_student():
    pass

def search_student():
    pass