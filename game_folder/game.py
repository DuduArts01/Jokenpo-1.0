from kivy.uix.screenmanager import Screen

class Game(Screen):
    def back_menu(self):
        self.parent.transition.direction = 'left'
        self.parent.current = 'main_menu_screen' 
    pass
