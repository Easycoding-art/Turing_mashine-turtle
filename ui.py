import PySimpleGUI as sg
from emulator import Mashine
import random
sg.theme('BluePurple')

layout = [[sg.Input(key='-IN-')],
          [sg.Input(key='ALPHABET')],
          [sg.Checkbox('Random band',  default=False, key='AUTO')],
          [sg.Text('Result:'), sg.Text(size=(15,1), key='-OUTPUT-')],
          [sg.Button('Play'), sg.Button('Exit')]]

window = sg.Window('Turing machine', layout)
commands = []
text = "w"
while True:
    text = input()
    if text == "end" :
        break
    else :
        commands.append(text)
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Play':
        mashine = Mashine(list(values['ALPHABET']), commands, len(list(values['-IN-']))*2 + 50)
        if values["AUTO"] == True:
            after = mashine.test()[1:]
            window['-IN-'].update(after)
            window['-OUTPUT-'].update(''.join(mashine.print_band()[1:]))
        else :
            # Update the "output" text element to be the value of "input" element
            mashine.manual(list(values['-IN-']))
            window['-OUTPUT-'].update(''.join(mashine.print_band()[1:]))

window.close()