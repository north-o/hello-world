from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

from SoundBoardScreen import SoundBoardScreen

class SoundBoardApp (App):
    sound_board_screen = SoundBoardScreen()
    
    def build(self):
        self.title = "Gauchos Sound Board"

        screen_manager = ScreenManager() 
        screen_manager.add_widget(self.sound_board_screen)

        return screen_manager
