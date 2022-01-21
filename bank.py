from tkinter import Event
import PySimpleGUI as sg




def win1_layout():
    layout1 = [

        [sg.Text("velkommen til SA nord ", size=(20, 5), font=("Helvetica", 25))],
        [sg.Text("banken som gjør ting enklere", size=(20, 5), font=("Helvetica", 25))],
         [sg.Text('persjonnummer', size=(10,10)), sg.InputText()],
         [sg.InputText('', size=(50,10))],
        [sg.Button("login"),sg.Button("exit")]
        
     
    ]







    
    return layout1

def login_layout():
    login_layout = [
        [sg.Text('SA nord')]
  
    ]
    return login_layout

def vips_layout():
    vips_layout = [
        
    ]
    


win1= sg.Window('Everything bagel', default_element_size=(100, )).Layout(win1_layout())

login_win_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
   
    if Event in (None, 'Exit'):
         win1.close()
         
         break

    if ev1 == "login":
        
        win1.Hide()
        login_win = sg.Window('Everything bagel', default_element_size=(100, )).Layout(login_layout())
        login_win_active = True
    if login_win_active: 

        ev1, vals1 = login_win.read(timeout=100)

    
