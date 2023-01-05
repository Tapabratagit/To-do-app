import PySimpleGUI as sg

label1 = sg.Text('Select files to compress: ')
input_bar1 = sg.Input()
button1 = sg.FileBrowse("Choose")

label2 = sg.Text('Select folder to store compressed file:')
input_bar2 = sg.Input()
button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("Compress")

window = sg.Window('File Compressor', layout=[[label1, input_bar1, button1],
                                              [label2, input_bar2, button2], [compress_button]])
window.read()
window.close()
