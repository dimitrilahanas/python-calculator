class Calculator:
    def __init__(self):
        self.a = None
        self.b = None

    def user_input(self):
        self.a = int(input("First Number? "))
        self.b = int(input("Second Number? "))

    def operation_list(self):
        operations = ["+ Addition", 
                      "- Subtraction", 
                      "* Multiplication", 
                      "/ Division"]
        for operation in operations:
            print(operation)

    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b

    def run(self):
        self.user_input()
        self.operation_list()