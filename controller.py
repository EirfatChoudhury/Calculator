from model import Model
from view import View

class Controller():
    def __init__(self):
        self.model = Model() # Connecting model to controller
        self.view = View(self) # Connecting view to controller and allowing view to connect controller to itself
    
    def main(self):
        self.view.main() # Running main function of view within the controller's main function

if __name__ == "__main__":
    app = Controller() # Creating a controller object
    app.main() # Running main function of controller