#imports
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.uix.anchorlayout import AnchorLayout

class SoundBoard(Widget):
    screamsound = SoundLoader.load("./sounds/Scream.wav")

    def __init__(self, **kwargs):
        super(SoundBoard, self).__init__(**kwargs)
        
        self.setLayout()

    def setLayout(self):
        self.size = (1500, 1000)
        
        with self.canvas:
            Color(0.7451, 1.0, 1.0, 1.0)
            Rectangle(size=self.size)
        
        sound_board_layout = AnchorLayout()
        sound_board_layout.anchor_x = "center"
        sound_board_layout.anchor_y = "top"
        sound_board_layout.size = self.size
        sound_board_layout.pos = self.pos

        scream_button = Button()
        scream_button.text = "ahhh"
        scream_button.height = 50
        scream_button.bind(on_press=self.scream_button_callback)
        sound_board_layout.add_widget(scream_button)

        self.add_widget(sound_board_layout)

    def scream_button_callback(self, play):
        return self.play_sound("scream")

    def play_sound(self, sound_name):
        if (sound_name == "scream"):
            self.screamsound.play()

