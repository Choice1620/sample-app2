import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.lable import Lable
from kivy.uix.textinput import TextInput
from kivy.uix.buttom import Button

class childApp(GridLayout):
    def __init__(self,**kwargs):
        super(childApp, self).__init__()
        self.cols = 2
        self.add_widget(Label(text = "Student Name"))
        self.s_name = TextInput()
        self.add_widget (self.s_name)

        self.add_widget(Label(text="Student Marks"))
        self.s_marks = TextInput ( )
        self.add_widget(self.s_marks)

        self.add_widget(Label(text="Student Gender"))
        self.s_gender = TextInput()
        self.add_widget(self.s_gender)

class parentApp(App):
    def build(self):
        return childApp()

if __name__ == "__main__":
    parentApp().run()
