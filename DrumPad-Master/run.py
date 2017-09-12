from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.core.audio import SoundLoader
from os.path import join, dirname

def playsound(instance):

    filename = join(dirname(__file__), 'Sound/{0}.wav'.format(instance.id))
    sound = SoundLoader.load(filename)
    if sound:
        sound.play()


def generate_buttons(layout):
    for counter in range(1, 17):
        # device = str(counter)
        new_button = Button(id="{0}".format(counter))
        new_button.bind(on_press=playsound)
        layout.add_widget(new_button)

class TestApp(App):
    def build(self):

        main_layout = BoxLayout(padding=5)
        header_layout = StackLayout()
        self.title="Drum pad"

        grid_layout = GridLayout(cols=4)

        generate_buttons(grid_layout)
        main_layout.add_widget(grid_layout)

        return main_layout

if __name__=="__main__":
    TestApp().run()