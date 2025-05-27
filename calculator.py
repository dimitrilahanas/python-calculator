class Calculator:
    def __init__(self):
        self.a = None
        self.b = None

    def user_input(self):
        self.a = int(input("First Number? "))
        self.b = int(input("Second Number? "))

    def run(self):
        self.user_input()