import PySimpleGUI as sg

lebel_a = sg.Text('Enter feet', key='feet')
input_bar1 = sg.Input(key='feetip')

lebel_b = sg.Text('Enter inches', key='inches')
input_bar2 = sg.Input(key='inchesip')

convert_button = sg.Button('Convert', key='Convert')

ans = sg.Text(key='ans')

window = sg.Window('Convertor', layout=[[lebel_a, input_bar1], [lebel_b, input_bar2], [convert_button, ans]])
while True:
    event, value = window.read()
    print(event, value)
    f_result = float(value['feetip']) * 0.304
    i_result = float(value['inchesip']) * 0.0254
    result = f_result + i_result
    window['ans'].update(value=f"{result}m")

window.close()
