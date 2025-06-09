from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import firebase_admin
from firebase_admin import credentials, db
import time
import random
import threading

class SenderApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical')
        self.status_label = Label(text="Ready to send data")
        self.layout.add_widget(self.status_label)

        # Initialize Firebase in a separate thread
        threading.Thread(target=self.init_firebase).start()

        return self.layout

    def init_firebase(self):
        cred = credentials.Certificate("firebase_key.json")  # Your Firebase Admin SDK JSON
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://fahimap-fa45f-default-rtdb.firebaseio.com/'
        })
        self.ref = db.reference('devices/deviceA123/data')

        # Schedule sending data