# this program visualizes activities with pyglet
import os, time

from pyglet import app, window, image
from pyglet.window import key
from pyglet.sprite import Sprite
from pyglet.text import Label

from activity_recognizer import Recogniser
from activity import Activity

class ActivityIndicator():

  NAME = "Verdana"
  XLARGE = 56
  COLOUR = (255,255,255,255)
  X_LABEL = 100
  Y_LABEL = 50
  Z_LABEL = 2

  def __init__(self, image_path: str, activity: Activity) -> None:
    image_file = image.load(image_path)
    self._image_sprite = Sprite(x=0, y=0, img=image_file)
    self._activity_label = Label(text=activity.name, font_name=self.NAME, font_size=self.XLARGE, color=self.COLOUR, z=self.Z_LABEL, x=self.X_LABEL, y=self.Y_LABEL)

  def draw(self) -> None:
    self._image_sprite.draw()
    self._activity_label.draw()

class Application:
  WIDTH = 1280
  HEIGTH = 720
  NAME = "Activity Visualiser"
  SCRIPT_DIR = os.path.dirname(__file__)
  ASSET_STANDING = "/assets/STANDING.jpg"
  ASSET_LYING = "/assets/LYING.jpg"
  ASSET_JUMPING = "/assets/JUMPING.jpg"
  ASSET_UNKNOWN = "/assets/UNKNOWN.jpg"
  FPS = 1 / 60

  def __init__(self) -> None:
    self.window = window.Window(self.WIDTH, self.HEIGTH, caption=self.NAME)
    self.on_draw = self.window.event(self.on_draw)
    self.on_key_press = self.window.event(self.on_key_press)
    self._recogniser = Recogniser()

    self._activity_sprites = {
      Activity.STANDING.name: ActivityIndicator(os.path.join(self.SCRIPT_DIR + self.ASSET_STANDING), Activity.STANDING),
      Activity.LYING.name: ActivityIndicator(os.path.join(self.SCRIPT_DIR + self.ASSET_LYING), Activity.LYING),
      Activity.JUMPING.name: ActivityIndicator(os.path.join(self.SCRIPT_DIR + self.ASSET_JUMPING), Activity.JUMPING),
      Activity.UNKNOWN.name: ActivityIndicator(os.path.join(self.SCRIPT_DIR + self.ASSET_UNKNOWN), Activity.UNKNOWN),
    }

  def run(self) -> None:
    app.run()        

  def on_draw(self) -> None:
    self.window.clear()

    detected_activity = self._recogniser.get_activity_gui()

    self._activity_sprites[detected_activity.name].draw()

    time.sleep(self.FPS)

  def on_key_press(self, symbol, _):
    if symbol == key.ESCAPE:
      os._exit(0)

if __name__ == "__main__":
  application = Application()
  application.run()