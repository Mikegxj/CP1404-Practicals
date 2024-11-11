from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.names = ["Mike", "Em", "Tom"]
        for name in self.names:
            label = Label(text=name, size_hint_y=None, height=40)
            self.root.ids.main.add_widget(label)
        return self.root

DynamicLabelsApp().run()