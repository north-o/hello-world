from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, ObjectProperty
from PongGamePy import PongGamePy

class PongGameScreen(Screen):
    player_1_name = "Player 1"
    player_1_paddle_color = ListProperty(None)
    player_2_name = "Player 2"
    player_2_paddle_color = ListProperty(None)
    max_score = 6
    pong_ball_color = ListProperty
    game_engine = ObjectProperty(None)

    def _init_(self, **kwargs):
        super(PongGameScreen, self).__init__(**kwargs)

    def on_pre_enter(self):
        self.game_engine.player_1_name = self.player_1_name

        self.game_engine.player1.color = self.player_1_paddle_color

        self.game_engine.player_2_color = self.player_2_paddle_color

        self.game_engine.player_2_name = self.player_2_name

        self.game_engine.player2.color = self.player_2_paddle_color

        self.game_engine.max_score = self.max_score

        # self.game_engine.ball.color = self.pong_ball_color

        # when the screen comes into view, start the game
        self.game_engine.start()

        def switch_to_settings_screen(self):
            self.manager.current = "settings_screen"

        def switch_to_welcome_screen_click(self):
            self.manager.current = "welcome_screen"

        def switch_to_win_screen(self, winner):
            self.manager.get_screen(
                "win_screen").winner_label = "You're the winner!" + winner

            self.manager.current = "win_screen"
            


        