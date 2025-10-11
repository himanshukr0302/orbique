# 3. WAP a 2D list for students roll_no and marks.

def create_2d_list(num_students):
    student_data = []
    for i in range(num_students):
        roll_no = input(f"Enter roll number for student {i+1}: ")
        marks = input(f"Enter marks for student {i+1}: ")
        student_data.append([roll_no, marks])
    return student_data

if __name__ == '__main__':
    num_students = int(input("Enter the number of students: "))
    student_list = create_2d_list(num_students)
    print(student_list)
