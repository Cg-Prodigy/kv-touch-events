from kivy.animation import Animation
from kivy.metrics import dp
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
    def on_touch_down(self, touch):
        if self.collide_point(touch.x,touch.y):
            self.tdown=True
            touch.grab(self)
        return super().on_touch_down(touch)
    def on_touch_up(self, touch):
        if self.collide_point(touch.x,touch.y):
            self.tdown=False
            pos=dp(-200)
            anime=Animation(x=pos,duration=.3)
            anime.start(self)
            touch.ungrab(self)
        return super().on_touch_up(touch)
    def on_touch_move(self,touch):
        if self.collide_point(touch.x,touch.y):
            if self.tdown:
                return True
            pos=dp(200)
            anime=Animation(x=pos,duration=.3)
            anime.start(self)
            
class TaskList(MDList):
   def __init__(self, **kwargs):
       super(TaskList,self).__init__(**kwargs)
       for i in range(10):
           self.__task=TaskWidget()
           self.__task.t_content.text=f'Title {i}'
           self.__task.t_title.text=f'Content {i}'
           self.add_widget(self.__task)