#imports
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Rectangle, Color
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch



class SoundBoard(Widget):
    screamsound = SoundLoader.load("./sounds/Scream.wav")
    firesound = SoundLoader.load("./sounds/Crackling_Fire.wav")
    jackhammersound = SoundLoader.load("./sounds/jackhammer4.wav")
    airplanesound = SoundLoader.load("./sounds/Airplane.wav")
    grid_layout = GridLayout(cols=3)
    is_looping_on = False


    def __init__(self, **kwargs):
        super(SoundBoard, self).__init__(**kwargs)
        
        self.setLayout()

    def setLayout(self):
        self.size = (1500, 1000)

        with self.canvas:
            Color(.532345, 1.0, .742, 1.0)
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
        title_label.text = "Soundboard :)"
        title_label.color = [.6, .2, 1, .5]
        title_label.font_size = 50
        title_label.font_name = "C:\\Windows\\Fonts\\Arial"
        title_label.size_hint = (1, 1)
        title_layout.add_widget(title_label)

        self.set_settings_layout()

        self.set_sounds()

        title_layout.add_widget(self.grid_layout)
        sound_board_layout.add_widget(title_layout)

        self.add_widget(sound_board_layout)

    def set_settings_layout(self):
        looping_switch_layout = BoxLayout()
        looping_switch_layout.orientation = "horizontal"

        looping_switch = Switch(active=False)
        looping_switch.bind(active=self.toggle_looping_sound)
        self.grid_layout.add_widget(looping_switch)

    def set_scream_sound(self):
        scream_button = Button()
        scream_button.text = "AHHHH"
        scream_button.height = 50
        scream_button.bind(on_press=self.scream_button_callback)
        self.grid_layout.add_widget(scream_button)

    def set_airplane_sound(self):
        airplane_button = Button()
        airplane_button.text = "Airplane"
        airplane_button.height = 50
        airplane_button.bind(on_press=self.airplane_button_callback)
        self.grid_layout.add_widget(airplane_button)

    def set_fire_sound(self):
        fire_button = Button()
        fire_button.text = "Fire"
        fire_button.height = 50
        fire_button.bind(on_press=self.fire_button_callback)
        self.grid_layout.add_widget(fire_button)

    def set_jackhammer_sound(self):
        jackhammer_button = Button()
        jackhammer_button.text = "Jackhammer"
        jackhammer_button.height = 50
        jackhammer_button.bind(on_press=self.jackhammer_button_callback)
        self.grid_layout.add_widget(jackhammer_button)

    def toggle_looping_sound(self, instance, is_loop_on):

        self.is_looping_on = is_loop_on

    def set_sounds(self):
        self.set_scream_sound()

        self.set_airplane_sound()

        self.set_fire_sound()

        self.set_jackhammer_sound()

    def scream_button_callback(self, play):
        return self.play_sound("scream")

    def airplane_button_callback(self, play):
        return self.play_sound("airplane")

    def fire_button_callback(self, play):
        return self.play_sound("Crackling_Fire")

    def jackhammer_button_callback(self, play):
        return self.play_sound("jackhammer4")        

    def play_sound(self, sound_name):
        if (sound_name == "scream"):
            if(self.is_looping_on is True):
                self.screamsound.loop = True
            else:
                self.screamsound.loop = False

            self.screamsound.play()
        elif(sound_name == "Crackling_Fire"):
            if(self.is_looping_on is True):
                self.firesound.loop = True
            else:
                self.firesound.loop = False
            
            self.firesound.play()
        elif(sound_name == "jackhammer4"):
            if(self.is_looping_on is True):
                self.jackhammersound.loop = True
            else:
                self.jackhammersound.loop = False    

            self.jackhammersound.play()
        elif(sound_name == "airplane"):
            if(self.is_looping_on is True):
                self.airplanesound.loop = True
            else:
                self.airplanesound.loop = False

            self.airplanesound.play()


