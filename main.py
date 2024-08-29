import os
import time
from students import *
from teachers import *
from print_utils import print_title

def main_menu():

    while True:
        os.system('cls')
        print_title('School Management System')

        print('1. Add Student')
        print('2. Delete Student')
        print('3. Update Student')
        print('4. Search Student')
        print()
        print('5. Add Teacher')
        print('6. Delete Teacher')
        print('7. Update Teacher')
        print('8. Search Teacher')
        print()
        print('9. Exit')

        choice = int(input('\nEnter your choice\n> '))

        if choice < 1 or choice > 9:
            print('Invalid choice')
            time.sleep(1)

        if choice == 1:
            add_student()
        elif choice == 2:
            delete_student()
        elif choice == 3:
            update_student()
        elif choice == 4:
            search_student()

        if choice == 1:
            add_teacher()
        elif choice == 2:
            delete_teacher()
        elif choice == 3:
            update_teacher()
        elif choice == 4:
            search_teacher()
        
        elif choice == 9:
            exit()


def main():
    main_menu()

if __name__ == '__main__':
    main()