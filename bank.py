
from socket import timeout
from tkinter import Event
import PySimpleGUI as sg
import mysql.connector


 
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="bank_db"
)  
 
mycursor = mydb.cursor() 
def win1_layout():
    layout1 = [ 

    [sg.Text("velkommen til SA nord ", size=(20, 5), font=("Helvetica", 25))],
    [sg.Text("banken som gjør ting enklere", size=(20, 5), font=("Helvetica", 25))],
    [sg.Text('brukernavn')],[sg.Input(do_not_clear=True, key='-username-')],
    [sg.Text('Passord: ')],[sg.Input(password_char='*',do_not_clear=True, key='-password-')],
    [sg.Text(key='-wrong_pw-')],
    [sg.Button('Login'), sg.Button('Exit')]
        ]



     
    







    
    return layout1


def tab1_layout():

    tab_layout = [
     [sg.Text("hei", size=(20, 5), font=("Helvetica", 25))]

    ]
    return tab_layout

def tab2_layout():

    tab1_layout = [

     [sg.Text("vips til en bruker i banken", size=(20, 5), font=("Helvetica", 25))],
    [sg.Text('brukernavn')],[sg.Input()],


    ]

    return tab1_layout


def tab_layout():
    layout_tab = [
            [sg.TabGroup(
                   [ [sg.Tab('Tab 1', tab1_layout()), sg.Tab('Tab 2', tab2_layout()) ]]
                )],

            [sg.Button('Read')]


              ]
    return layout_tab



def admin_win():
    admin = [
    [sg.Text('usrname')],[sg.Input()],
    [sg.Text('password')],[sg.Input()]
]
    return admin

win1= sg.Window('Everything bagel', default_element_size=(100, )).Layout(win1_layout())

my_id = '' 
login_win_active = False
loginstate = False
win1active = True
win2_active = False
admin_active= False

while win1active:
    ev1, vals1 = win1.read(timeout=100)
    if Event in (None, 'Exit'):
         win1.close()
         win1active = False
         break
     
    if ev1 == "Login":
        username = vals1['-username-']
        pw = vals1['-password-']


        sql = "SELECT username, password FROM users WHERE username =%s AND password = %s"
        mycursor.execute(sql, (username, pw))
        myresult = mycursor.fetchall()
        
        sql = "SELECT username, admin FROM username WHERE username.admin='{myid}'"
 
        row_count = mycursor.rowcount
        if row_count == 1:
            sql = "SELECT username, admin FROM users WHERE username =%s AND password = %s"
            mycursor.execute(sql, (username, pw))
            myresult = mycursor.fetchone()

            myid = myresult[0]  
            admin = myresult[1]


            win1.Hide()
            
            if admin == 1:
                admin_active = True
                admin1 = sg.Window('Everything bagel', default_element_size=(100, )).Layout(admin_win())
                win1active = False

                win1.close()

            else:
                win2_active=True
                win2 = sg.Window('Everything bagel', default_element_size=(100, )).Layout(tab_layout())
                win1active = False

                win1.close()

        else:
            win1['-wrong_pw-'].update('Wrong password or username')


while admin_active:
    if admin_active:
        ev3, vals3 = admin1.read(timeout=100)
        if ev3  == sg.WIN_CLOSED or ev3 == 'Exit':
            admin_active = False
            admin1.close()               


while win2_active:
    if win2_active:
        ev2, vals2 = win2.read(timeout=100)         
        if ev2  == sg.WIN_CLOSED or ev2 == 'Exit':
            win2_active = False
            win1.close()


    


     
 


