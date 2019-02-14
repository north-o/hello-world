from kivy.uix.screenmanager import Screen

from SoundBoard import SoundBoard

class SoundBoardScreen(Screen):
    def __init__(self, **kwargs):
        super(SoundBoardScreen, self).__init__(**kwargs)

        self.size = (1000, 1000)

        sound_board = SoundBoard()

        self.add_widget(sound_board)