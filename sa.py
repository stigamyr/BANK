import PySimpleGUI as sg
import mysql.connector
 
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="bank_db"
)  # egen bruker burde lages med tanke på sikkerhet, for innlogging i databasen
 
mycursor = mydb.cursor() # oppretter tilkobling til databasen
 
def login_layout():
    layout = [
            [sg.Text('LOGIN')],
            [sg.Text('Username: ')],[sg.Input(do_not_clear=True, key='-username-')],
            [sg.Text('Password: ')],[sg.Input(password_char='*',do_not_clear=True, key='-password-')],
            [sg.Text(key='-wrong_pw-')],
            [sg.Button('Login'), sg.Button('Exit')]
            ]
 
    return layout
 
def bank_layout(name):
    layout = [[sg.Text('Welcome', name)],
              [sg.Text('Bank balance: '),sg.Text('-amountofmoney-')],
              [sg.Button('Exit')]]
 
    return layout
 
login_win = sg.Window('Magnemaker BANK', login_layout())
 
my_id = ''
 
login_active = True
loginstate = False
bank_active = False
 
while True:
    ev1, values1 = login_win.read(timeout=100)
    if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
        break
        
    if not bank_active and ev1 == 'Login':
        username = values1['-username-']
        pw = values1['-password-']
 
        sql = "SELECT username, password FROM users WHERE username =%s AND password = %s"
        mycursor.execute(sql, (username, pw))
        myresult = mycursor.fetchall()
        
        row_count = mycursor.rowcount
        if row_count == 1:
            sql = "SELECT username FROM users WHERE username =%s AND password = %s"
            mycursor.execute(sql, (username, pw))
            myresult = mycursor.fetchone()
 
            myid = myresult[0]  # setter brukernavn inn i en variabel
 
            loginstate = True
            bank_active = True
            bank_win = sg.Window(f'BANK - User: {myid}', bank_layout(myid))
            login_win.close()
            break
 
        else:
            login_win['-wrong_pw-'].update('Wrong password or username')
        
 
while bank_active and loginstate:
    ev2, vals2 = bank_win.read(timeout=100)
    if ev2 == sg.WIN_CLOSED or ev2 == 'Exit':
        bank_active  = False
        bank_win.close()
 