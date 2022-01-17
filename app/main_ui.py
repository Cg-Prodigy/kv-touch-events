from kivy.animation import Animation
from kivy.metrics import dp
from kivy.core.window import Window
from kivy.properties import ObjectProperty,StringProperty
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList
from kivymd.uix.boxlayout import MDBoxLayout

class EntryPoint(MDScreen):
    pass

class TaskWidget(MDBoxLayout):
    t_content=ObjectProperty()
    t_title=ObjectProperty()
    orientation=StringProperty('vertical')
    def __init__(self, **kwargs):
        super(TaskWidget,self).__init__(**kwargs)
        self.tdown=False
        self.t_down=None
        self.init_cords=()
        self.opac=0.01
    def on_touch_down(self, touch):
        if self.collide_point(touch.x,touch.y):
            self.init_cords=(self.x,self.y)
            touch.grab(self)
        return super().on_touch_down(touch)
    def on_touch_move(self, touch):
        if touch.grab_current is self and self.collide_point(touch.x,touch.y):
            delta_x,delta_y=touch.dpos
            anime=Animation(x=self.x+delta_x,y=self.y+delta_y,duration=0)
            anime.start(self)
        return super().on_touch_move(touch)
    def on_touch_up(self, touch):
        if touch.grab_current is self:
            self.x=self.init_cords[0]
            self.y=self.init_cords[1]
            touch.ungrab(self)
        return super().on_touch_up(touch)
class TaskList(MDList):
   def __init__(self, **kwargs):
       super(TaskList,self).__init__(**kwargs)
       for i in range(10):
           self.__task=TaskWidget()
           self.__task.t_content.text=f'Title {i}'
           self.__task.t_title.text=f'Content {i}'
           self.add_widget(self.__task)