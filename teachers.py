import pandas as pd
import os
from print_utils import print_title

def save_teacher(teacher):
    df = pd.read_csv('data/teachers.csv')
    df = pd.concat([df, pd.DataFrame(teacher, index=[df.shape[1]])], ignore_index=True)
    df.to_csv('data/teachers.csv', index=False)

def add_teacher():
    os.system('cls')
    print_title('Add Teacher')

    id_ = input('Enter teacher id: ')
    name = input('Enter teacher name: ')
    age = int(input('Enter teacher age: '))

    teacher = {
        'id': id_,
        'name': name,
        'age': age
    }
    save_teacher(teacher)

    print('\nTeacher added successfully\n')
    os.system('pause')

def delete_teacher():
    pass

def update_teacher():
    pass

def search_teacher():
    pass

