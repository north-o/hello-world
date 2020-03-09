from kivy.uix.screenmanager import Screen

def find_color_with_mouse(self):
    self.get_root_windows().hide()
    self.is_minimized = True
    self.do_mouse_listener()
    self.get_rooot_window().show()

def do_mouse_listener(self):
    with Listener(on_click=self.mouse_on_click) as self.listener:
        print("in listener")
        self.listener.join()

def mouse_on_click(self x, y, button, pressed):
    print(
        "ColorPickerScreen - mouse on_click at ({0}, {1} with {2}".format(x, y, button))

    self.click_position = (x, y)

    

class ColorPickerScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)




