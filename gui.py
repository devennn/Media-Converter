import PySimpleGUI as sg


def get_window():
    template_name_list = []
    tab_1 = [[sg.Text("Source", size=(15, 1)), sg.InputText(key='-FOLDER1-'), sg.FolderBrowse(target='-FOLDER1-')],
             [sg.Text("Convert to", size=(15, 1)), sg.Combo(template_name_list, size=(43, 1), key='-VID_DES-')],
             [sg.Button("Start", size=(10, 1), key="-CONV_VID-")]]

    tab_2 = [[sg.Text("Source", size=(15, 1)), sg.InputText(key='-FOLDER2-'), sg.FolderBrowse(target='-FOLDER2-')],
             [sg.Text("Convert to", size=(15, 1)), sg.Combo(template_name_list, size=(43, 1), key='-IMG_DES-')],
             [sg.Button("Start", size=(10, 1), key="-CONV_IMG-")]]

    layout = [[sg.TabGroup([[sg.Tab("Video", tab_1), sg.Tab("Images", tab_2)]])]]

    return sg.Window("Media Converter", layout)


def main():
    window = get_window()
    state = "WAITING"

    while True:
        event, values = window.read()

        # Exit the window
        if event in (sg.WINDOW_CLOSED, '-CANCEL-'):
            break

        # Change state
        if event == "-start_templates-":
            state = "RUN_TEMPLATE"
        elif event == "-START_OCR-":
            state = "RUN_OCR"

        # Run state
        if state == "RUN_TEMPLATE" and values['-FILE2-'] != "":
            state = "WAITING"
        elif state == "RUN_OCR" and values["-FOLDER1-"] != "":
            state = "WAITING"

    window.close()


if __name__ == '__main__':
    main()
