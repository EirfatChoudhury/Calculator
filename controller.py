from model import Model
from view import View

class Controller():
    def __init__(self):
        self.model = Model() # Connecting model to controller
        self.view = View(self) # Connecting view to controller and allowing view to connect controller to itself
    
    def main(self):
        self.view.main() # Running main function of view within the controller's main function
    
    def button_clicked(self, button): # Creation of a button_clicked function for the user
        result = self.model.calculate(button)
        self.view.value_var.set(result)

if __name__ == "__main__":
    app = Controller() # Creating a controller object
    app.main() # Running main function of controller


# IMPLEMENT BACK BUTTON FUNCTION AND PERCENTAGE FUNCTION, ALSO IMPLEMENT TYPING FUNCTION