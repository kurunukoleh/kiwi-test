from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen


class MainWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        mainline = BoxLayout()
        line = BoxLayout(orientation='vertical')
        text = Label(text="Вибери екран", color = "red", font_size = '50')
        baton1 = Button(text='1' , background_color = 'red', font_size = '50' , on_press = self.onfirst)
        baton2 = Button(text='2' , background_color = 'green',font_size = '50', on_press = self.onsecond)
        baton3 = Button(text='3' , background_color = 'blue',font_size = '50', on_press = self.onthird)
        baton4 = Button(text='4' , background_color = 'yellow',font_size = '50', on_press = self.onfours)
        line.add_widget(baton1)
        line.add_widget(baton2)
        line.add_widget(baton3)
        line.add_widget(baton4)
        mainline.add_widget(text)
        mainline.add_widget(line)
        self.add_widget(mainline)

    def onfirst(self , *args):
        self.manager.current = "first"

    def onsecond(self , *args):
        self.manager.current = "second"

    def onthird(self , *args):
        self.manager.current = "third"

    def onfours(self , *args):
        self.manager.current = "fours"

class FirstWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        mainline = BoxLayout()
        baton1 = Button(text = "nazad" , on_press= self.onmain)
        mainline.add_widget(baton1)
        mainline.add_widget(Label(text= "vikno1"))
        self.add_widget(mainline)

    def onmain(self , *args):
        self.manager.current = "main"

class SecondWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        mainline = BoxLayout()
        baton1 = Button(text = "nazad" , on_press= self.onmain)
        mainline.add_widget(baton1)
        mainline.add_widget(Label(text="vikno2"))
        self.add_widget(mainline)

    def onmain(self , *args):
        self.manager.current = "main"

class ThirdWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        mainline = BoxLayout()
        baton1 = Button(text = "nazad" , on_press= self.onmain)
        mainline.add_widget(baton1)
        mainline.add_widget(Label(text="vikno3"))
        self.add_widget(mainline)

    def onmain(self , *args):
        self.manager.current = "main"

class FoursWindow(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        mainline = BoxLayout()
        baton1 = Button(text = "nazad" , on_press= self.onmain)
        mainline.add_widget(baton1)
        mainline.add_widget(Label(text="vikno4"))
        self.add_widget(mainline)

    def onmain(self , *args):
        self.manager.current = "main"

class Myapp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name = "main"))
        sm.add_widget(FirstWindow(name = "first"))
        sm.add_widget(SecondWindow(name="second"))
        sm.add_widget(ThirdWindow(name="third"))
        sm.add_widget(FoursWindow(name="fours"))
        return sm

Myapp().run()
