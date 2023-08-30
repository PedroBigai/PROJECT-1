from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from openpyxl import load_workbook
import re


class AplicativoPersiana(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        self.largura_input = TextInput(hint_text="Largura", font_size=20, foreground_color=(1, 1, 1), background_color=(0, 0, 0), padding=10)
        self.layout.add_widget(self.largura_input)
        
        self.altura_input = TextInput(hint_text="Altura", font_size=20, foreground_color=(1, 1, 1), background_color=(0, 0, 0))
        self.layout.add_widget(self.altura_input)

        self.codigo_input = TextInput(hint_text="Qual o código do tecido:", font_size=20, foreground_color=(1, 1, 1), background_color=(0, 0, 0))
        self.layout.add_widget(self.codigo_input)
        
        self.resultado_label = Label(text="", font_size=20, size_hint_y=5, height=100)
        self.layout.add_widget(self.resultado_label)
        
        return self.layout
        
if __name__ == '__main__':
    AplicativoPersiana().run()
   

