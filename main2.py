#import pyautogui
from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from KivyOnTop import register_topmost
from kivy.clock import Clock
from datetime import datetime
from datetime import timedelta
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
#pyautogui.useImageNotFoundException()
Window.size = (540, 30)
class MainScreen(BoxLayout):
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
        #pyautogui.PAUSE = 0.001
        Clock.schedule_interval(self.click, 0.001)

    def stop_autoclicker(self, event):
        Clock.unschedule(self.click)

    def click(self, *args):
        Clock.unschedule(self.click)


class MyApp(App):

    def build(self):
        return MainScreen()

    def on_start(self, *args):
        Window.set_title("Lottery Clicker")
        register_topmost(Window, "Lottery Clicker")


if __name__ == "__main__":
	MyApp().run()


