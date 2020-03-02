from kivy.uix.widget import Widget
from kivy.properties import ListProperty, NumericProperty, ReferenceListProperty
from kivy.vector import Vector



class PongBall(Widget):
    """Calculate the position of the ball baxed on X,Y coordinates (Vector)"""
    # passing in RGBA: Red, Green, Blue, Transparency (Alpha)
    color = ListProperty([0, .784, 1, 1])

    speed_factor = 1.35

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos