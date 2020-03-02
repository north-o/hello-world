from PIL import ImageGrab
from PIL import ImageFile
import uuid
import win32api

class MouseThing:
    has_found_target = False
    target_coordinate = (0, 0)
    imageFilePath= "./data/"
    screen_capture_image = ImageGrab.grab(
        bbox=None, include_layered_windows=False, all_screens=False)

    def main(self):
        self.do_screen_capture()

        self.scan_picture_for_target()

    def scan_picture_for_target(self):
        display_width = self.screen_capture_image.width
        display_height = self.screen_capture_image.height

        for row in range(display_height):
            for column in range(display_width):
                self.target_coordinate = column, row

                pixel = self.screen_capture_image.getpixel(
                    self.target_coordinate)

                red, green, blue = pixel

                if (red == 86 and
                    green == 214 and
                        blue == 185):
                    print("Found red, green, blue: ", red, green, blue)

                    self.move_to_mouse_target()

    def move_to_mouse_target(self):
        current_mouse_position = win32api.GetCursorPos()   

        print("mouse current position", current_mouse_position)

        win32api.SetCursorPos(
            self.target_coordinate)

    def do_screen_capture(self):
        self.imageFilePath += "img_" + \
            str(uuid.uuid4()) + ".png"

        self.screen_capture_image.save(self.imageFilePath)
    

        # self.screen_capture_image.show()

if(__name__ == "__main__"):
    MouseThing = MouseThing()
    MouseThing.main()