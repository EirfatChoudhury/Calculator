class Model():
    def __init__(self):
        self.current_value = ""
        self.evaluation = []

    def calculate(self, button):
        if button == "C":
            self.current_value = ""

        elif button == "+/-":
            if self.current_value[0] == "-":
                self.current_value = self.current_value[1:]
            else:
                self.current_value = "-"+self.current_value

        elif button == ".":
            if not "." in self.current_value:
                self.current_value += "."
            else:
                pass

        elif isinstance(button, int):
            self.current_value += str(button)

        elif button in ["+", "-", "*", "/"]:
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
        
        elif button == "=":
            self.evaluation.append(self.current_value)
            self.current_value = self._evaluate()
            
            self.evaluation = []

        return self.current_value
    
    def _evaluate(self):
        print(self.evaluation)
        equation = "".join(self.evaluation)
        result = eval(equation)

        if type(result) == float:
            if result.is_integer():
                result = int(result)
                return str(result)
        else:
            return str(result)