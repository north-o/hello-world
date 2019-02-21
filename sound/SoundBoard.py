#imports
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class SoundBoard(Widget):
    screamsound = SoundLoader.load("./sounds/Scream.wav")
    firesound = SoundLoader.load("./sounds/Crackling_Fire.wav")
    grid_layout = GridLayout(cols=3)


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
        sound_board_layout.size_hint = (1.0, 1.0)
        sound_board_layout.spacing = 50

        title_layout = BoxLayout()
        title_layout.orientation = "vertical"
        title_layout.size_hint = (1.0, 1.0)
        title_layout.spacing = 10

        title_label = Label()
        title_label.color = [0.89, 0.792, 1.61, 1.0]

        self.set_sounds()

        title_layout.add_widget(self.grid_layout)
        sound_board_layout.add_widget(title_layout)

        self.add_widget(sound_board_layout)

    def set_scream_sound(self):
        scream_button = Button()
        scream_button.text = "ahhh"
        scream_button.height = 50
        scream_button.bind(on_press=self.scream_button_callback)
        self.grid_layout.add_widget(scream_button)

    def set_fire_sound(self):
        fire_button = Button()
        fire_button.text = "fire"
        fire_button.height = 50
        fire_button.bind(on_press=self.fire_button_callback)
        self.grid_layout.add_widget(fire_button)

    def set_sounds(self):
        self.set_scream_sound()

        self.set_fire_sound()

    def scream_button_callback(self, play):
        return self.play_sound("scream")

    def fire_button_callback(self, play):
        return self.play_sound("Crackling_Fire")

    def play_sound(self, sound_name):
        if (sound_name == "scream"):
            self.screamsound.play()
        elif(sound_name == "Crackling_Fire"):
            self.firesound.play()

