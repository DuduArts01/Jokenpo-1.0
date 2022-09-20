from kivymd.app import MDApp as App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
class ScreenManager(ScreenManager):
    pass

class Main_Menu(Screen):
    def Change_Screen(self):
        self.parent.transition.direction = 'left'
        self.parent.current = 'game_screen'
    pass

class jokenpo(App):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        kv = Builder.load_file("./home_screen.kv")
        return kv

if __name__ == "__main__":
    jokenpo().run()
