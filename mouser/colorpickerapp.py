import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from colorpickerscreen import ColorPickerScreen

class ColorPickerApp(App):
    screen_manager = ScreenManager()

    def build(self):
        color_picker_screen = ColorPickerScreen(name="color_picker_screen")
    
        self.screen_manager.add_widget(color_picker_screen)

        return self.screen_manager

if(__name__ == "__main__"):
    print("kivy version:", kivy.version)

    ColorPickerApp().run()

class ColorPickerApp(self):
    color_picker_screen = ColorPickerScreen
