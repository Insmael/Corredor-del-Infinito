from model.menu_elements.actions import Action
from view.elements.buttonStyle import ButtonStyle

class Button:
    def __init__(self, action: Action, place=(0.0, 0.0, 0.0)):
        self.action = action
        self.style = ButtonStyle(self.action.texture_name(), place)
        self.over = False

    def draw(self):
        self.style.draw()

    def change_over(self):
        self.style.change_shining()

    def select(self, vista):
        self.action.act(vista)
