# GUI Application Wrapper
# Written by Andrew Y. C
# Imports the packages pysimplegui, openpyxl, pandas, and pathlib

# PySimpleGui for the user interface 
# openpyxl for storing the data of the python app to an excel spreadsheet
# pandas to read data from an excel spreadsheet
# pathlib will allow us to manipulate filepaths


from pathlib import Path
import PySimpleGUI as sg
import pandas as pd
import os

# --- Store Data as CSV
# --- Should store photo of prescription bottle, name of individual, the date, and success or failure
#def store_user_csv(input, filename):
    # Input should be the user's name, date, success or failure, and photo of bottle 

    #return 0

# -- Will fetch the information we previously stored in the user csv we created
#def fetch_user_csv(filename):
    # Only need the name of the csv file

    #return 0

# --- Layout --- 

sg.theme("BlueMono")

title_layout = [
        [sg.Stretch(), sg.Frame("", [[sg.Stretch(background_color="#E0E0E0"), sg.Text("Prescription Verifier", font=("Arial", 60), background_color="#E0E0E0", pad=((10, 5), (20, 10))), sg.Stretch(background_color="#E0E0E0")]], background_color="#E0E0E0", font=('Arial', 50), size=(800, 125), pad=((20, 30), (30, 20))), sg.Stretch()],
        [sg.Stretch(), sg.FileBrowse("Upload Photo", font=("Arial", 35), button_color=("white on blue"), pad=(5), size=(13, 0.2), file_types=(('PNG', '.png'), ('JPG', '.jpeg'),)), sg.Stretch()],
        [sg.Stretch(), sg.FileBrowse("Import CSV", font=("Arial", 35), button_color=("white on blue"), pad=(5), size=(13, 0.2), file_types=(('Excel', '.csv'),)), sg.Stretch()],
        [sg.Stretch(), sg.Button("View logs", key= '-LOGS-', font=("Arial", 35), button_color=("white on blue"), border_width=2, pad=(5), size=(13, 0.2)), sg.Stretch()],
        [sg.Stretch(), sg.Button("Contact", key='-CONTACT-', font=("Arial", 35), button_color=("white on blue"), border_width=2, pad=(5), size=(13, 0.2)), sg.Stretch()]
        ]

logs_layout = [
        [sg.Stretch(), sg.Text("History", font=('Arial', 24), visible= False), sg.Stretch()],
        [],
        []
              ]


x = 0
layout = [
        [sg.Frame("",title_layout, visible=True, key='Title')],
        
         ]

#sg.Window(title="Prescription Verifier App", layout=layout, size=(700, 500)).read()
window = sg.Window('Prescription Verifier App', layout, size=(700,500))
# -- Start the infinite while loop in the background
while True:
    event, values = window.read()
    #print(event, values)
    
    if event == sg.WIN_CLOSED:
        break
    if event == '-LOGS-':
        x+=1
        window['Title'].update(visible=False)
        #window[test].update("Hi")
        
        
    if event == '-CONTACT-':
        x+=1
        #window['-CONTACT-'].update(values[1])
        #window.refresh()

sg.Window.close()
del sg.Window
