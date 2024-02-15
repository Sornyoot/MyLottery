import pyautogui
from PIL import Image
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from KivyOnTop import register_topmost
from kivy.clock import Clock
from kivy.properties import ObjectProperty
from kivy.uix.image import Image as kiImage
import glob
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from datetime import datetime
from datetime import timedelta
from kivy.uix.label import Label
from kivy.utils import platform
pyautogui.useImageNotFoundException()

class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)

class MainScreen(Screen):
    slider = ObjectProperty(None)
    loop_thread = None

    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)

        self.bnt_1 = Button(text="Cap", size_hint=(.16, .9), pos_hint={'center_x': .08, 'y': .03})
        self.add_widget(self.bnt_1)
        self.bnt_1.bind(on_press=self.screengrab)

        self.bnt_4 = Button(text="Crop", size_hint=(.16, .9), pos_hint={'center_x': .25, 'y': .03})
        self.bnt_4.bind(on_press=self.screenTransition)
        self.add_widget(self.bnt_4)

        self.now = datetime.now()
        Clock.schedule_interval(self.alarm, 1)
        self.my_label = Label(text=self.now.strftime('%H:%M:%S'), font_size='20dp', size_hint=(.30, .9), pos_hint={'center_x': .50, 'y': .03})
        self.add_widget(self.my_label)

        self.bnt_5 = Button(text="Start", size_hint=(.16, .9), pos_hint={'center_x': .76, 'y': .03})
        self.bnt_5.bind(on_press=self.activate_autoclicker)
        self.add_widget(self.bnt_5)

        self.bnt_6 = Button(text="Stop", size_hint=(.16, .9), pos_hint={'center_x': .93, 'y': .03})
        self.bnt_6.bind(on_press=self.stop_autoclicker)
        self.add_widget(self.bnt_6)

    def alarm(self,  event):
        self.now = self.now + timedelta(seconds=1)
        self.my_label.text = datetime.now().strftime('%H:%M:%S')
        current_time = datetime.now().strftime('%H:%M:%S')
        alarms = "15:00:00"
        if alarms == str(current_time):
            self.loop_thread = Clock.schedule_interval(self.click, 0.001)

    def screengrab(self, *largs):
        Window.screenshot(name='/storage/emmc/DCIM/screen_1.jpg')

    def activate_autoclicker(self, event):
        pyautogui.PAUSE = 0.001
        Clock.schedule_interval(self.click, 0.001)

    def stop_autoclicker(self, event):
        Clock.unschedule(self.click)

    def screenTransition(self, *args):
        self.manager.current = 'Pass_1'

    def click(self, *args):
        try:
            location = pyautogui.locateOnScreen('/storage/emmc/DCIM/4.png')
            pyautogui.click(location)
        except pyautogui.ImageNotFoundException:
            print('not pass')
        try:
            location = pyautogui.locateOnScreen('/storage/emmc/DCIM/5.png')
            pyautogui.click(location)
        except pyautogui.ImageNotFoundException:
            print('not pass')
        try:
            location = pyautogui.locateOnScreen('/storage/emmc/DCIM/1.png')
            pyautogui.click(location)
            pyautogui.click(location)
            location = pyautogui.locateOnScreen('/storage/emmc/DCIM/2.png')
            pyautogui.click(location)
            pyautogui.click(location)
            location = pyautogui.locateOnScreen('/storage/emmc/DCIM/3.png')
            pyautogui.click(location)
            pyautogui.click(location)
        except pyautogui.ImageNotFoundException:
            print('not pass')

    def on_pre_enter(self):
        if platform == 'android':
            Window.maximize()
        else:
            Window.size = (540, 30)


class Pass_1(Screen):

    def __init__(self, **kwargs):
        super(Pass_1, self).__init__(**kwargs)
        images = glob.glob('/storage/emmc/DCIM/screen_1.jpg')

        for img in images:
            thumb = kiImage(source=img)
            thumb.bind(on_touch_down=self.Crop_1)
            thumb.bind(on_touch_down=self.screenTransition)
            self.add_widget(thumb)

    def Crop_1(self, obj, touch):
        image = Image.open('/storage/emmc/DCIM/screen_1.jpg')
        x = touch.x - 20
        y = touch.y - 20
        xw = x + 40
        yh = y + 40
        crop = image.crop((x, y, xw, yh))
        crop.save('/storage/emmc/DCIM/1.png', quality=200)
        print('x =', x, 'y =', y, 'xw =', xw, 'yh =', yh)

    def screenTransition(self, *args):
        self.manager.current = 'Pass_2'

    def on_pre_enter(self):
        if platform == 'android':
            Window.maximize()
        else:
            Window.size = (540,960)


class Pass_2(Screen):

    def __init__(self, **kwargs):
        super(Pass_2, self).__init__(**kwargs)
        images = glob.glob('/storage/emmc/DCIM/screen_1.jpg')
        for img in images:
            thumb = kiImage(source=img)
            thumb.bind(on_touch_down=self.Crop_2)
            thumb.bind(on_touch_down=self.screenTransition)
            self.add_widget(thumb)

    def Crop_2(self, obj, touch):
        image = Image.open('/storage/emmc/DCIM/screen_1.jpg')
        x = touch.x - 20
        y = 534 - touch.y - 20
        xw = x + 40
        yh = y + 40
        crop = image.crop((x, y, xw, yh))
        crop.save('/storage/emmc/DCIM/2.png', quality=200)
        print('x =', x, 'y =', y, 'xw =', xw, 'yh =', yh)

    def screenTransition(self, *args):
        self.manager.current = 'Pass_3'

    def on_pre_enter(self):
        if platform == 'android':
            Window.maximize()
        else:
            Window.size = (540,960)


class Pass_3(Screen):

    def __init__(self, **kwargs):
        super(Pass_3, self).__init__(**kwargs)
        images = glob.glob('/storage/emmc/DCIM/screen_1.jpg')
        for img in images:
            thumb = kiImage(source=img)
            thumb.bind(on_touch_down=self.Crop_3)
            thumb.bind(on_touch_down=self.screenTransition)
            self.add_widget(thumb)

    def Crop_3(self, obj, touch):
        image = Image.open('/storage/emmc/DCIM/screen_1.jpg')
        x = touch.x - 20
        y = 534 - touch.y - 20
        xw = x + 40
        yh = y + 40
        crop = image.crop((x, y, xw, yh))
        crop.save('/storage/emmc/DCIM/3.png', quality=200)
        print('x =', x, 'y =', y, 'xw =', xw, 'yh =', yh)

    def screenTransition(self, *args):
        self.manager.current = 'Pass_4'

    def on_pre_enter(self):
        if platform == 'android':
            Window.maximize()
        else:
            Window.size = (540,960)


class Pass_4(Screen):

    def __init__(self, **kwargs):
        super(Pass_4, self).__init__(**kwargs)
        images = glob.glob('/storage/emmc/DCIM/screen_2.jpg')
        for img in images:
            thumb = kiImage(source=img)
            thumb.bind(on_touch_down=self.Crop_4)
            thumb.bind(on_touch_down=self.screenTransition)
            self.add_widget(thumb)

    def Crop_4(self, obj, touch):
        image = Image.open('/storage/emmc/DCIM/screen_2.jpg')
        x = touch.x - 20
        y = 534 - touch.y - 20
        xw = x + 40
        yh = y + 40
        crop = image.crop((x, y, xw, yh))
        crop.save('/storage/emmc/DCIM/4.png', quality=200)
        print('x =', x, 'y =', y, 'xw =', xw, 'yh =', yh)

    def screenTransition(self, *args):
        self.manager.current = 'Pass_5'

    def on_pre_enter(self):
        if platform == 'android':
            Window.maximize()
        else:
            Window.size = (540,960)


class Pass_5(Screen):

    def __init__(self, **kwargs):
        super(Pass_5, self).__init__(**kwargs)
        images = glob.glob('/storage/emmc/DCIM/screen_3.jpg')
        for img in images:
            thumb = kiImage(source=img)
            thumb.bind(on_touch_down=self.Crop_5)
            thumb.bind(on_touch_down=self.screenTransition)
            self.add_widget(thumb)

    def Crop_5(self, obj, touch):
        image = Image.open('/storage/emmc/DCIM/screen_3.jpg')
        x = touch.x - 20
        y = 534 - touch.y - 20
        xw = x + 40
        yh = y + 40
        crop = image.crop((x, y, xw, yh))
        crop.save('/storage/emmc/DCIM/5.png', quality=200)
        print('x =', x, 'y =', y, 'xw =', xw, 'yh =', yh)

    def screenTransition(self, *args):
        self.manager.current = 'main'

    def on_pre_enter(self):
        if platform == 'android':
            Window.maximize()
        else:
            Window.size = (540,960)

class MyApp(App):

    def build(self):
        sm = ScreenManagement(transition=FadeTransition())
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(Pass_1(name='Pass_1'))
        sm.add_widget(Pass_2(name='Pass_2'))
        sm.add_widget(Pass_3(name='Pass_3'))
        sm.add_widget(Pass_4(name='Pass_4'))
        sm.add_widget(Pass_5(name='Pass_5'))
        return sm

    def on_start(self, *args):
        Window.set_title("LOTTERY CLICKER")
        register_topmost(Window, "LOTTERY CLICKER")


if __name__ == "__main__":
	MyApp().run()


