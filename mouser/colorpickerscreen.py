from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
import Constants
from time import sleep
from pynput.mouse import Listener
from PIL import ImageGrab

class ColorPickerScreen(Screen):

    is_minimized = False
    target_pixel = ListProperty([1, 1, 1, 1])
    target_coordinate = (0, 0)
    fonts_path = Constants.FONTS_PATH
    screen_capture_image = (0, 0, 0)

    def do_screen_capture(self):
        self.screen_capture_image = ImageGrab.grab(
        bbox=None, include_layered_windows=False, all_screens=False)

    def find_color_with_mouse(self):
        self.get_root_windows().hide()
        sleep(1)
        self.is_minimized = True
        self.do_mouse_listener()
        self.get_rooot_window().show()

    def do_mouse_listener(self):
        with Listener(on_click=self.mouse_on_click) as self.listener:
            print("in listener")
            self.listener.join()

    def mouse_on_click(self, x, y, button, pressed):
        print(
            "ColorPickerScreen - mouse on_click at ({0}, {1} with {2}".format(x, y, button))
        
        self.target_coordinate = (x, y)

        self.listener.stop()

        self.do_screen_capture()

        self.click_position = (x, y)

        self.set_color_swatch()

        def set_color_swatch(self):
            color_picked = self.screen_capture_image_getpixel(
                self.target_coordinate)

            self.target_pixel[0] = round(color_picked[0]/255, 2)
            self.target_pixel[1] = round(color_picked[1]/255, 2)
            self.target_pixel[2] = round(color_picked[2]/255, 2)

            print("color picked: ", self.target_pixel)

        def do_mouse_listener(self):
            with Listener(on_click=self.mouse_on_click) as self.listener:
                print("in listener")
                self.listener.join()
