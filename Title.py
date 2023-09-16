# GUI Application Wrapper
# Written by Andrew Y. C
# Imports the packages pysimplegui, openpyxl, pandas, and pathlib

# PySimpleGui for the user interface 
# openpyxl for storing the data of the python app to an excel spreadsheet
# pandas to read data from an excel spreadsheet
# pathlib will allow us to manipulate filepaths


from pathlib import Path
import PySimpleGUI as sg
import openpyxl as op

# --- Store Data as CSV
# --- Should store photo of prescription bottle, name of individual, the date, and success or failure
def store_user_csv(input, filename):
    # Input should be the user's name, date, success or failure, and photo of bottle 

    return 0

# -- Will fetch the information we previously stored in the user csv we created
def fetch_user_csv(filename):
    # Only need the name of the csv file

    return 0

# --- Layout --- 

layout = [
            [],
            [],
            []
         ]

sg.Window(title="Prescription Verifier App", layout=layout, margins=(400, 300)).read()

# -- Start the infinite while loop in the background
while True:
    event, values = sg.Window.read()
    print(event, values)
    if event == sg.WINDOW_CLOSED:
        break

sg.Window.close()
del sg.Window
