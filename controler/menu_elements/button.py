from controler.menu_elements.actions import Action
from view.elements.bottonStyle import BottonStyle

class Button:
    def __init__(self, action: Action, place=(0.0, 0.0, 0.0)):
        self.action = action
        self.style = BottonStyle(self.action.texture_name(), place)

    def draw(self):
        self.style.draw()
