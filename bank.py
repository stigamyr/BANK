from socket import timeout
from tkinter import Event
import PySimpleGUI as sg




def win1_layout():
    layout1 = [ 

     [sg.Text("velkommen til SA nord ", size=(20, 5), font=("Helvetica", 25))],
    [sg.Text("banken som gjør ting enklere", size=(20, 5), font=("Helvetica", 25))],
    [sg.Text('persjonnummer',size=(10,10)), sg.InputText()],
    [sg.InputText('', size=(50,10))],
    [sg.Button("login"),sg.Button("exit")]
        
        
     
    ]







    
    return layout1


def tab1_layout():

tab_layout = [
    [sg.Text("vips til en bruker i banken", size=(20, 5), font=("Helvetica", 25))],
    [sg.Text('navn', size=(10,10)), sg.InputText()],
    [sg.Text('beløp', size=(10,10)), sg.InputText()]

    ]
    return tab_layout

def tab2_layout():
    
tab2_layout = [

]



def tab_layout():
    layout_tab = [
            [sg.TabGroup(
                    [[sg.Tab('Tab 1', tab1_layout), sg.Tab('Tab 2', tab2_layout) ]]
                )],

            [sg.Button('Read')]



              ]
    return layout_tab

win1= sg.Window('Everything bagel', default_element_size=(100, )).Layout(win1_layout())


login_win_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
   
    if Event in (None, 'Exit'):
         win1.close()
         
         break



    if ev1 == "login":
        win1.Hide() 
        win2_active = True
        win2 = sg.Window('Everything bagel', default_element_size=(100, )).Layout(tab_layout())
        ev2, vals2 = win2.read(timeout=100)
    
    if win2_active:
        ev2, vals2 = win2.read(timeout=100)

     
 

    
