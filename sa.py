import PySimpleGUI as sg
from PIL import Image    # installer med pip: py -m pip install pillow
import io
 
# alle bilder som skal vises i GUI må loades via denne funksjonen, 
def get_img_data(f, maxsize=(1200, 850)):
    """
    Generate image data using PIL
    """
    img = Image.open(f)
    img.thumbnail(maxsize)
    bio = io.BytesIO()
    img.save(bio, format="PNG")
    del img
    return bio.getvalue()
 
sg.theme('BluePurple')
 
# load image data
image1 = get_img_data('gui/car.png')  # her brukes funksjonen vi laget til å laste inn bildefilen i rett format

 
layout = [
 
        [sg.Image(image1, key='image_key')],
        [sg.Text('Det du skriv kommer opp her:'), sg.Text(size=(15, 1), key='-OUTPUT-')],
        [sg.Input(key='-IN-')],
        [sg.Button('Show'), sg.Button('Show new image'), sg.Button('Exit')]
]
 
window = sg.Window('Visning av bilde', layout)
 
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event in (None, 'Exit'):
        break
    if event == 'Show':
        # Update the "output" text element to be the value of "input" element
        window['-OUTPUT-'].update(values['-IN-'])
 
    if event == 'Show new image':
        # Update the "image" key to image2 
        window['image_key'].update(image2)
 
window.close()