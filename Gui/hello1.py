#!/usr/bin/env python3

# File: hello1.py

import PySimpleGUI as sg

# Create some elements...
layout = [  # Text, InputText and two Buttons
        # use lists to get an in rows layout...
        [sg.Text("What's your first name?"), sg.InputText()],
        [sg.Text("What's your last name?"), sg.InputText()],
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
    sg.Print(f'Event: {event}')
    sg.Print(str(values))
    print(f"values: {repr(values)}")

window.close()

