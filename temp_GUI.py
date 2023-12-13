from kivy.app import App
#importing BoxLayout class from Kivy's boxlayout module. BoxLayout is used for arranging widgets in a vertical or horizontal box.
from kivy.uix.boxlayout import BoxLayout

# importing Button class from Kivy's button module. This is used to create interactive button widgets in the app.
from kivy.uix.button import Button

#importing Label class from Kivy's label module. Label is used to display text.
from kivy.uix.label import Label

#importing TextInput class from Kivy's textinput module. TextInput is used for user input of text.
from kivy.uix.textinput import TextInput

import json

import httpx

#making a class that inherits from the App class
class MyWordApp(App):
    #creating the constructor
    def __init__(self):
        # calling the contructor of the parent class App, to ensure attributes are initialized correctly (not always necessary, but always recommended)
        App.__init__(self)
        # adding attributes to the class we've created
        self.label = Label(text="Nothing yet.")
        self.textbox = TextInput(text="Enter your text here...")
        #creating the button attribute
        self.button = Button(text="my button")
        
    
    # the "build" method, which is where you create the structure of the app (ussually returns a Layout)
    def build(self):
        #creating the vertical structure layout (outer layout)
        b = BoxLayout(orientation='vertical', padding="10pt")
        #creating the horizontal structure layout (inner layout)
        b_inner = BoxLayout(orientation='horizontal', padding="15pt")
        
        # You need to add code here
        # You need to add code here
        b_inner.add_widget(self.textbox)
        b_inner.add_widget(self.button)
        self.button.bind(on_press=self.press)
        # You need to add code here
        #adding the inner layout to the outer layout
        b.add_widget(b_inner)
        b.add_widget(self.label)
        #returns only outer layout, since the inner was added to the outer
        return b

    #assimung the is 
    def press(self, instance):
        self.look_up(self.textbox.text)
#importing to get the restAPI

    def look_up(self, word: str):
        try:
            response = httpx.get("https://api.dictionaryapi.dev/api/v2/entries/en/" + word)
            text_to_json = json.loads(response.text)
            definitions = text_to_json[0]["meanings"][0]["definitions"][0]["definition"]
            self.label.text = definitions
            return response.json()
        except Exception:
            self.label.text = "No meaningful definition found."
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    MyWordApp().run()
