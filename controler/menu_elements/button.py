from controler.menu_elements.actions import Action
from view.elements.bottonStyle import BottonStyle

class Button:
    def __init__(self, action: Action, place=(0.0, 0.0, 0.0)):
        self.action = action
        self.style = BottonStyle(self.action.texture_name(), place)
        self.over = False

    def draw(self):
        self.style.draw()

    def change_over(self):
        self.style.change_shining()

    def select(self):
        self.action.act()
