'''
8.Suppose your AI has been provided data in a tabular format ( say all country name's) . then 
you are supposed to write a python program for a class 3rd student to say country name and test
he is 'correctly named it '. 
'''
class CountryQuiz:
    def __init__(self, countries):
        self.countries = countries

    def start_quiz(self):
        print("Welcome to the Country Quiz!")
        for country in self.countries:
            answer = input(f"Name a country: ")
            if answer.strip().lower() == country.lower():
                print("Correct!")
            else:
                print(f"Wrong! The correct answer is {country}.")  

countries_list = ["India", "Canada", "Australia", "Germany", "Brazil"]
quiz = CountryQuiz(countries_list)
quiz.start_quiz()
