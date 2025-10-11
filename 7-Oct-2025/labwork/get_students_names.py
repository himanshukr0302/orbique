# 4. WAP to get entered name of students of a class by user input

def get_students_names(num_students):
    student_names = []
    for i in range(num_students):
        name = input(f"Enter the name of student (i+1: )")
        student_names.append(name)
    return student_names

if __name__ == '__main__':
    num_students = int(input("Enter the number of students in the class: "))
    student_list = get_students_names(num_students)
    print("Student names entered:")
    for name in student_list:
        print(name)
