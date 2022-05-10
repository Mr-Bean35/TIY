class User():

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login = 0

    def describe(self):
        print(f"{self.last_name}, \n"
              f"{self.first_name}, \n"
              f"{self.age} years old \n"
              f"Currently resides in {self.country}")

    def greet(self):
        print(f"Hello {self.last_name}, {self.first_name}. How are you today. How is {self.country}? Is the weather good?")

    def incre_login_attempts(self):
        self.login += 1

    def re_login_attempts(self):
        self.login = 0

    def read_attempt(self):
        print(self.login)
