class Calculator:
    def __init__(self):
        self.a = None
        self.b = None
        self.operation = None

    # User Input
    def user_input(self):
        self.a = int(input("First Number? "))
        self.b = int(input("Second Number? "))

    # Supported Operators
    def operation_list(self):
        operations = ["+ Addition", 
                      "- Subtraction", 
                      "* Multiplication", 
                      "/ Division"]
        for operation in operations:
            print(operation)

    # Math Logic
    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b
    
    # User Operation Input
    def operation_selector(self):
        self.operation = str(input("Select an operator: "))
        
        match self.operation:
            case "+":
                print("Result: " + str(self.addition()))
            case "-":
                print("Result: " + str(self.subtraction()))
            case "*":
                print("Result: " + str(self.multiplication()))
            case "/":
                print("Result: " + str(self.division()))

    # Runner
    def run(self):
        self.user_input()
        self.operation_list()
        self.operation_selector()