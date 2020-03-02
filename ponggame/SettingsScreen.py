from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.colorpicker import ColorPicker
from kivy.uix.screenmanager import Screen

from PongGamePy import PongGamePy
# from GameScreen import GameScreen
from ColorWheel import ColorWheel




class SettingsScreen(Screen):

    player_1_name_widget = ObjectProperty(None)
    player_1_paddle_color = ObjectProperty(None)
    player_1_label_color = ListProperty([0, 0, 0.8, 1])

    player_2_name_widget = ObjectProperty(None)
    player_2_paddle_color = ObjectProperty(None)
    player_2_label_color = ListProperty([0, 0, 0.8, 1])

    max_score_widget = ObjectProperty(None)

    pong_ball_color = ObjectProperty(None)
    pong_ball_label_color = ListProperty([0, 0, 0, 1])

    def __init__(self, **kwargs):
        super(SettingsScreen, self).__init__(**kwargs)
    
  ##     can_pong_ball_config = input("moo")

   #     if(can_pong_ball_config == "y"):
   #         rgba_color = input("rgba")
#
    #    self.pong_ball_on_color(rgba_color)


    def pong_ball_on_color(self, rgba_color):

        self.pong_ball_label_color = rgba_color

        self.manager.get_screen(
            "game_screen").pong_ball_color = rgba_color

    def player_1_paddle_on_color(self, rgba_color):

        self.player_1_label_color = rgba_color

        self.manager.get_screen(
            "game_screen").player_1_paddle_color = rgba_color

    def player_2_paddle_on_color(self, rgba_color):

        self.player_2_label_color = rgba_color

        self.manager.get_screen(
            "game_screen").player_2_paddle_color = rgba_color

    def save(self):

        self.manager.get_screen(
            "game_screen").player_1_name = self.player_1_name_widget.text

        self.manager.get_screen(
            "game_screen").player_2_name = self.player_2_name_widget.text

        self.manager.get_screen(
            "game_screen").max_score = int(self.max_score_widget.text)

        self.manager.current = "game_screen"
