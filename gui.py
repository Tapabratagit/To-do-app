import functions
import PySimpleGUI as sg

label = sg.Text('Type in a todo: ')
input_box = sg.InputText(tooltip='Enter todo')
button = sg.Button('Add')

window = sg.Window('My Todos', layout=[[label], [input_box, button]])
window.read()
window.close()
