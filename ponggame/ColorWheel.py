"""
    https://kivy.org/doc/stable/api-kivy.uix.colorpicker.html

    https://stackoverflow.com/questions/29199797/kivy-color-wheel
"""
#!C:\Python\Python_3_7_1\python.exe
from kivy.uix.colorpicker import ColorWheel


class CustomColorWheel(ColorWheel):
    """
        Just want the ColorWheel, not the ColorPicker with Slider
    """

    def __init__(self, **kwargs):
        super(CustomColorWheel, self).__init__(**kwargs)

        self.init_wheel(dt=0)

    def on__hsv(self, instance, value):
        """
            hsv is a color format, like rgba
        """
        super(CustomColorWheel, self).on__hsv(instance, value)

        print("In CustomColorWheel - on__hsv(), color selected: " + str(self.rgba))
