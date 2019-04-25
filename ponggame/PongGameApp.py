from kivy.app import App
from kivy.clock import Clock
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager
from WelcomeScreen import WelcomeScreen
from SettingsScreen import SettingsScreen
from PongGameScreen import PongGameScreen

class PongGameApp(App):
    def build(self):
        PongGameApp.pong_screen_manager = ScreenManager()

        welcome_screen = WelcomeScreen(name="welcome_screen")
        game_screen = PongGameScreen(name="game_screen") 
        settings_screen = SettingsScreen(name="settings_screen") 
        #win_screen = WinScreen(name="win_screen") 

        self.pong_screen_manager.add_widget(welcome_screen)
        self.pong_screen_manager.add_widget(game_screen)
        self.pong_screen_manager.add_widget(settings_screen)
        #self.pong_screen_manager.add_widget(win_screen)

        return self.pong_screen_manager
