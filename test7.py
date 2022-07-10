from guizero import App, Text, PushButton
from random import choice
def choose_name():
    spy_name = choice(first_names) + " " + choice(last_names)
    print(spy_name)
    name.value = spy_name
    #print('Button was pressed')

first_names = ["John", "Woody", "Dude", "Smokey", "Joe", "Ruby"]
last_names = ["Pinki", "Blinki", "Stinki", "Inki", "Minki", "Flinki"]
app = App("TOP SECRET")
title = Text(app, "Push the red button to find out your spy name")
button = PushButton(app, choose_name, text="Tell me!")
button.text_color = "white"
button.text_size = 50
button.bg = "red"
name = Text(app, text="")
name.text_color = "purple"
name.text_size = 40
app.display()