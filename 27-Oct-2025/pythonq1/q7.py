'''
7.create a chatbot program who is noting down name's of each student entrying at the main gate.  
later on  class teacher cross checks it at attentdance by user input. chatbot answers as "student" 
is present" or "absent".
'''
class Chatbot:
    def __init__(self):
        self.student_names = set()

    def add_student(self, name):
        # store normalized name for case-insensitive matching
        normalized = name.strip().lower()
        self.student_names.add(normalized)
        print(f"{name.strip()} has been noted down.")

    def check_attendance(self):
        print("(Type 'exit' to stop checking attendance)")
        while True:
            name = input("Enter student name to check attendance: ").strip()
            if not name:
                # ignore empty input
                continue
            if name.lower() in ("exit", "quit"):
                print("Stopping attendance check.")
                break
            normalized = name.lower()
            if normalized in self.student_names:
                print(f"{name} is present.")
            else:
                print(f"{name} is absent.")

chatbot = Chatbot()
# Adding students
chatbot.add_student("Alice")
chatbot.add_student("Bob")
chatbot.add_student("Charlie")
# Checking attendance
chatbot.check_attendance()
