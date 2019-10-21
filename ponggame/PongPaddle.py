from kivy.vector import Vector
from kivy.properties import ListProperty, NumericProperty, ReferenceListProperty,\
    ObjectProperty
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
class PongPaddle(Widget):
    """
    This is the player1, player objects
    """

    color = ListProperty([1, 1, 1, 1])
    paddle_1_sound = SoundLoader.load("./sounds/paddle_1.wav")
    paddle_2_sound = SoundLoader.load("./sounds/paddle_2.wav")
    score = NumericProperty(0)

    def bounce_ball(self, ball, speed_factor, is_player_1):
        """
            ball will bounce based on player   
            Make sound depending on player
        """
        if (self.collide_widget(ball)): 
            velocity_x, velocity_y = ball.velocity 

            offset = (ball.center_y - self.center_y) / (self.height / 2)

            bounce_vector = Vector(-1 * velocity_x, velocity_y)

            new_ball_velocity = bounce_vector * speed_factor

            ball.velocity = new_ball_velocity.x, new_ball_velocity.y + offset

        if(is_player_1 is True):
            self.paddle_1_sound.play()
        else:
            self.paddle_2_sound.player()
        