import pyautogui
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from KivyOnTop import register_topmost
from kivy.clock import Clock
from kivy.properties import ObjectProperty
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

        self.bnt_1 = Button(text="Start", size_hint=(.35, .9), pos_hint={'center_x': .17, 'y': .03})
        self.add_widget(self.bnt_1)
        self.bnt_1.bind(on_press=self.activate_autoclicker)

        self.now = datetime.now()
        Clock.schedule_interval(self.alarm, 1)
        self.my_label = Label(text=self.now.strftime('%H:%M:%S'), font_size='20dp', size_hint=(.30, .9), pos_hint={'center_x': .50, 'y': .03})
        self.add_widget(self.my_label)

        self.bnt_2 = Button(text="Stop", size_hint=(.35, .9), pos_hint={'center_x': .83, 'y': .03})
        self.bnt_2.bind(on_press=self.stop_autoclicker)
        self.add_widget(self.bnt_2)

    def alarm(self,  event):
        self.now = self.now + timedelta(seconds=1)
        self.my_label.text = datetime.now().strftime('%H:%M:%S')
        current_time = datetime.now().strftime('%H:%M:%S')
        alarms = "15:00:00"
        if alarms == str(current_time):
            self.loop_thread = Clock.schedule_interval(self.click, 0.001)

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


class MyApp(App):

    def build(self):
        sm = ScreenManagement(transition=FadeTransition())
        sm.add_widget(MainScreen(name='main'))
        return sm

    def on_start(self, *args):
        Window.set_title("Lottery Clicker")
        register_topmost(Window, "Lottery Clicker")


if __name__ == "__main__":
	MyApp().run()


