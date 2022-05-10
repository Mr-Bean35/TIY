class Restaurant():


    def __init__(self, name, type,):
        self.name = name
        self.type = type
        self.served = 0

    def describe_rest(self):
        print(f'Here at {self.name} we have {self.type} options')

    def open(self):
        print(f'{self.name} is now open for business')

    def serve(self):
        print(f"{self.name} has served {self.served} person(s)")

    def flavors(self):
        self.flavors = ['Chocolate', 'Vanilla', 'Mint', "Cookies N' Cream", 'Cookie Dough']
        print(f'We have:')
        CNT = 0
        for i in self.flavors:
           if CNT + 1 >= len(self.flavors):
            print(f'And {i}')
           else:
            print(i)
            CNT += 1
