import PySimpleGUI as sg

# Design pattern 2 - First window remains active

def win1_layout():
    layout = [[sg.Text("velkommen til SA nord ", size=(20, 5), font=("Helvetica", 25))],
             [sg.Text("banken som gjør ting enklere", size=(20, 5), font=("Helvetica", 25))],
             [sg.Button("login"),sg.Button("exit")]
     
]

    return layout

def win2_layout():
    layout = [
        [sg.Text('BANK', size=(20, 5), font=("Helvetica", 25))],
    [sg.InputText('persjonnummer', size=(50,10))],
        [sg.Button("next"),sg.Button("exit")]
     
]


    return layout

win1 = sg.Window('Window 1', win1_layout())

win2_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED or 'exit':
        break

    
    if ev1 == 'login':
        win1.Hide()
        win2_active = True 
         win2 = sg.Window('Window 2', win2_layout())

        
    if not win2_active and ev1 == 'Launch 2':
        win2_active = True
        #win1.Hide()  # fjern hashtag for å skjule window 1 når window 2 skal vises
        win2 = sg.Window('Window 2', win2_layout())

    if win2_active:
        ev2, vals2 = win2.read(timeout=100)
        if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
            win2_active  = False
            #win1.UnHide()   # fjern hashtag for å vise window 1 igjen
            win2.close()

