#!/usr/bin/env python3

# File: hello.py

import PySimpleGUI as sg

# Create some elements...
layout = [  # Text, InputText and two Buttons
        # use lists to get an in rows layout...
        [sg.Text("What's your name?"), sg.InputText()],
        [sg.Button('OK'), sg.Button('Cancel')]
        ]
# Create the Window: parent Element containing a title and all
# other Elements...
window = sg.Window('Hello PySimpleGUI', layout)

# Create the event loop
while True:
    # read method to extract the events and values...
    event, values = window.read()
    if event in (None, 'Cancel'):
        # User closed the window or hit the Cancel button
        break
    print(f'Event: {event}')
    print(str(values))

window.close()

