# 7.create a chatbot program who is notingdown name's of each student entrying at the main gate.
# later on  class teacher cross checks it at attentdance by user input. chatbot answers as "student"
# is present" or "absent".

# Simple chatbot attendance registrar

def main():
    present = []
    print('Enter student names as they enter the gate. Enter an empty line to stop.')
    while True:
        name = input('Name: ').strip()
        if not name:
            break
        present.append(name)

    # teacher checks
    print('\nTeacher attendance check. Enter student name to check (empty to quit).')
    while True:
        name = input('Check name: ').strip()
        if not name:
            break
        if name in present:
            print(f"{name} is present")
        else:
            print(f"{name} is absent")

if __name__ == '__main__':
    main()
