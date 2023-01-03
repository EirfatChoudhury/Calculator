class Model():
    def __init__(self):
        """Assigning class attributes"""
        self.current_value = ""
        self.evaluation = []

    def calculate(self, button):
        """Adding button functionality"""
        if button == "C": # Clears value
            self.current_value = ""
        
        elif button == "BACK": # Backspace
            self.current_value = self.current_value[:-1]

        elif button == "+/-": # Changes value from positive to negative and vice versa
            if self.current_value[0] == "-":
                self.current_value = self.current_value[1:]
            else:
                self.current_value = "-"+self.current_value
        
        elif button == "%": # Converts value to percentage
            if "." in self.current_value:
                value = float(self.current_value)
            else:
                value = int(self.current_value)
            
            self.current_value = str(value/100)

        elif button == ".": # Allows value to become a decimal
            if not "." in self.current_value:
                self.current_value += "."
            else:
                pass

        elif isinstance(button, int): # Converts integer buttons to string
            self.current_value += str(button)

        elif button in ["+", "-", "*", "/"]: # Operator purposed to store value and operator in an evaluation list to be evaluated when user hits "="
            if self.current_value == "":
                if button == "-":
                    self.current_value += button
            else:
                self.evaluation.append(self.current_value)
                self.current_value = ""
                try:
                    if self.evaluation[-1] in ["+", "-", "*", "/"]:
                        self.evaluation.pop()
                        self.evaluation.append(button)
                finally:
                    self.evaluation.append(button)
        
        elif button == "=": # Evaluates equation
            self.evaluation.append(self.current_value)
            self.current_value = self._evaluate()
            self.evaluation = []

        return self.current_value # Returns result and stores it as the current_value 
    
    def _evaluate(self):
        """Evaluation function"""
        equation = "".join(self.evaluation) # Joins list stored values and operators and evaluates them, returning the result as a string
        result = eval(equation)

        if type(result) == float:
            if result.is_integer():
                result = int(result)
                return str(result)
        else:
            return str(result)