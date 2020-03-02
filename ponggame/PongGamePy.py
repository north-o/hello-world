from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import ListProperty, NumericProperty, ObjectProperty, StringProperty


import logging

from PongBall import PongBall
from PongPaddle import PongPaddle
from pygame.key import name
#from PongGameScreen import PongGameScreen

class PongGamePy(Widget):
    is_game_on = False
    paddle_speed = 25
    max_score = NumericProperty(11)
    player_1_name = StringProperty("Player 1")
    player_2_name = StringProperty("Player 2")
    esc_popup = Popup()

    cheer_sound = SoundLoader.load("./sounds/cheer.wav")

    # should resolve to a PongBall object
    ball = ObjectProperty(None)
    ball = ObjectProperty(None)
    ball = ObjectProperty(None)

    # constructor
    def __init__(self, **kwargs):
        super(PongGamePy, self).__init__(**kwargs)

        self.initialize()

    def initialize(self):
        self.is_game_on = True

        self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self._keyboard.bind(on_key_up=self._on_keyboard_up)

        # creating a "phone directory" tp route key presses
        self.pressed_keys = set()

        #phone directory - includes router with  instruction on particular
        self.pressed_actions = {
        "w": lambda: self.move_paddle_upward("w"),
        "up": lambda: self.move_paddle_upward("up"),
        "s": lambda: self.move_paddle_downward("s"),
        "down": lambda: self.move_paddle_downward("down")
        }

        # increase ball speed every minute
        Clock.schedule_interval
        (self.increase_ball_speed, 120)

    def start(self):
        print("Game start")

        # bind the keyboard
        self.initialize()
        
        self.set_popup()

        self.serve_ball()

        #start game loop
        self.resume_game()

    def set_popup(self, *args):
        
        welcome_button = Button(text="Back to Welcome!", color=(1, 0, 0, 1))
        welcome_button.bind(on_press=self.switch_to_welcome_screen)
        settings_button = Button(text="Settings", color=(1, 0, 0, 1))
        settings_button.bind(on_press=self.switch_to_settings_screen)

        popup_box_layout = BoxLayout()

        popup_box_layout.spacing = 10
        popup_box_layout.size_hint = (.5, .25)

        popup_box_layout.add_widget(welcome_button)
        popup_box_layout.add_widget(settings_button)

        self.esc_popup = Popup(
            title="Leave Game",
            content=popup_box_layout,
            size_hint=(.35, .25),
            auto_dismiss=False # force user to dismiss popup
        )

    def switch_to_welcome_screen(self, *args):
        self.close_popup()

        if(self.parent is not None):
            self.parent.size_switch_to_welcome_screen_click()

    def switch_to_settings_screen(self):
        self.manager.current = "settings_screen"

    def keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard.unbind(on_key_up=self._on_keyboard_up)
        self._keyboard = None

    def _on_keyboard_up(self, keyboard, keycode):
        if(self.pressed_keys.__contains__(keycode[1])):
            self.pressed_keys.remove(keycode[1])

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):

        if (keycode[1] != "escape"):
            self.pressed_keys.add(keycode[1])
        else:
            if(self.is_game_on is True):
                self.pause_game()
                self.open_popup()
            else:
                self.close_popup
                self.resume_game()

        return True

    def increase_ball_speed(self,delta_time):

        if self.ball_speed_factor < 16:
            self.ball.speed_factor += 0.0005

    def serve_ball(self, velocity=(4, 0)):
    
        self.ball.center = self.center

        self.ball.velocity = velocity

    def resume_game(self):
        self.is_game_on = True
        
        Clock.schedule_interval(self.update , 1.0/ 60.0)

    def pause_game(self):

        self.is_game_on = False

        Clock.unschedule(self.update)

    def update(self, delta_time):
        for key in self.pressed_keys:
            try:
                if(key is not "alt"):
                    self.pressed_actions[key]()
            except KeyError:
                pass

        self.ball.move()

        self.player1.bounce_ball(self.ball, self.ball.speed_factor, True)

        self.player2.bounce_ball(self.ball, self.ball.speed_factor, True)

        if ((self.ball.y < self.y) or (self.ball.top > self.top)):
            self.ball.velocity_y *= -1

        self.check_scoring()

  

    def move_paddle_downward(self, keyCode):

       # logging.info(
           # "In GauchoPongGame - move_paddle_downward(), key code: " + keyCode)

        paddle_offset = 50

        if(keyCode == "down"):
            log_params = [keyCode, str(
                self.player2.center_y - self.paddle_speed)]

           # logging.info(
             #   "In GauchoPongGame - move_paddle_downward(), key code: %s.  player 2 y position: %speed", log_params, None)

            if(self.player2.center_y - self.paddle_speed - paddle_offset > 0):
                self.player2.center_y -= self.paddle_speed
        elif(keyCode == "s"):
            if(self.player1.center_y - self.paddle_speed - paddle_offset > 0):
                self.player1.center_y -= self.paddle_speed

    def move_paddle_upward(self, keyCode):
        """
            Make sure paddle doesn't appear partially off screen.
            The paddle_offset will create a buffer with top of screen
        """

        paddle_offset = 50

        if(keyCode == "w"):
            if(self.player1.center_y + self.paddle_speed + paddle_offset < self.height):
                self.player1.center_y += self.paddle_speed
        elif(keyCode == "up"):
            if(self.player2.center_y + self.paddle_speed + paddle_offset < self.height):
                self.player2.center_y += self.paddle_speed


    def check_scoring(self):

        if (self.ball.x < self.x):

            self.player2.score += 1

            self.reset_paddle_positions()

            if(self.player2.score == self.max_score):
#                    self.parent.switch_to_win_screen(self.player_2-name)
                pass
            else:
                self.serve_ball(velocity=(4, 0))

        if (self.ball.x > self.width):
            
            self.player1.score += 1

           # self.cheer_sound_play()

            self.reset_paddle_positions()

            if(self.player1.score == self.max_score):
                self.parent.switch_to_win_screen(self.player_1_name)
            else:
                self.serve_ball(velocity=(4, 0))

    def reset_paddle_positions(self):
        self.player1_center_y = self.center_y
        self.player2_center_y = self.center_y

    def on_touch_move(self, touch):
        if (touch.x < (self.width / 3)):
            self.player1.center_y = touch.center_y

        if (touch.x > (self.width - (self.width / 3))):
            self.player2.center_y = touch.center_y



