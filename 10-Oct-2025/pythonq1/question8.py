# 8.Suppose your AI has been provided data in a tabular format ( say all country name's) . then 
# you are supposed to write a python program for a class 3rd student to say country name and test
# he is 'correctly name it '.

# Simple quiz: show a country and ask student to type it back (case-insensitive)

countries = ['India', 'Australia', 'Canada', 'Brazil', 'Japan']

def quiz():
    for c in countries:
        ans = input(f"Please type the country name shown ({c}): ").strip()
        if ans.lower() == c.lower():
            print('Correct!')
        else:
            print(f"Incorrect. The correct name is {c}.")

if __name__ == '__main__':
    quiz()
