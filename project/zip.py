import PySimpleGUI as sg
from zip_creater import make_archive

label1 = sg.Text('Select files to compress: ')
input_bar1 = sg.Input()
button1 = sg.FileBrowse("Choose", key='files')

label2 = sg.Text('Select folder to store compressed file:')
input_bar2 = sg.Input()
button2 = sg.FolderBrowse("Choose", key='folders')

output_lebel = sg.Text(key='output', text_color='green')

compress_button = sg.Button("Compress")

window = sg.Window('File Compressor', layout=[[label1, input_bar1, button1],
                                              [label2, input_bar2, button2], [compress_button, output_lebel]],
                   font=('helvetica', 20))
while True:
    event, value = window.read()
    print(event, value)
    file_paths = value['files'].split(';')
    folder = value['folders']
    make_archive(file_paths, folder)
    window['output'].update(value='compression successful !!')

window.close()
