import PySimpleGUI as sg
from views import *

SERVER_HOST = get_ip_address()
SERVER_PORT = 8000

def main():
    # Define the layout
    layout = [
        [sg.Text("Minimalist HTTP Server With @PySimpleGUI", font=("Helvetica", 20), justification='center')],
        [sg.Text("Select a File:", size=(15, 1)), sg.InputText(key="file_path"), sg.FileBrowse()],
        [sg.Button("Start", size=(10, 1)), sg.Button("Shutdown", size=(10, 1))]
    ]

    # Create the window for the created server
    window = sg.Window("HTTP SERVER", layout, resizable=True)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            break
        elif event == "Start":
            
            file_path = values["file_path"]
            sg.popup(f"Server will Start and Listen in http://{SERVER_HOST}:{SERVER_PORT}", title="START SERVER ALERT")
            start_server(file_path, SERVER_HOST,SERVER_PORT)



    window.close()

if __name__ == "__main__":
    main()
