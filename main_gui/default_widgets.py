from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

default_font = 'default_font.ttf'


class DefaultTextInput(TextInput):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultTextInput, self).__init__(**kwargs)
        
        self.font_size = screen_size[1] / 35
        self.size_hint = (1, None)
        self.height = screen_size[1] / 15
        self.multiline = False


class DefaultButton(Button):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultButton, self).__init__(**kwargs)

        self.size_hint = (1, None)
        self.height = screen_size[1] / 15


class DefaultHeadLabel(Label):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultHeadLabel, self).__init__(**kwargs)

        self.font_size = screen_size[1] / 22
        self.size_hint = (1, None)
        self.height = screen_size[1] / 4.5
        self.color = (0, 0, 0, 1)

        self.text_size = (screen_size[0] - 20, None)
        self.halign = 'left'

        self.font_name = default_font


class DefaultLabel(Label):
    def __init__(self, **kwargs):
        super(DefaultLabel, self).__init__(**kwargs)

        self.color = (0, 0, 0, 1)


class DefaultPopup(Popup):
    def __init__(self, screen_size: tuple, **kwargs):
        super(DefaultPopup, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = (screen_size[0] - 20, screen_size[1] / 2)
        self.auto_dismiss = False


class DefaultButtonForPopup(Button):
    def __init__(self, screen_size, **kwargs):
        super(DefaultButtonForPopup, self).__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = (screen_size[0] - 45, screen_size[1] / 12)

