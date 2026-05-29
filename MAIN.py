from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class PetroCalcApp(App):
    def build(self):
        layout = GridLayout(cols=2, padding=10, spacing=10)
        
        layout.add_widget(Label(text="Enter Value:"))
        self.val_input = TextInput(multiline=False)
        layout.add_widget(self.val_input)
        
        calc_btn = Button(text="Calculate")
        calc_btn.bind(on_press=self.calculate)
        layout.add_widget(calc_btn)
        
        self.result_label = Label(text="Result: ")
        layout.add_widget(self.result_label)
        
        return layout

    def calculate(self, instance):
        try:
            val = float(self.val_input.text)
            self.result_label.text = f"Result: {val * 2}" # یه محاسبه الکی برای تست
        except ValueError:
            self.result_label.text = "Error: Enter a number!"

if __name__ == '__main__':
    PetroCalcApp().run()
  
