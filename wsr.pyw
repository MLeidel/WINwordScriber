import webview
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
import webbrowser

current_file = ""  # tracks current file in use

def on_closing():
    pass

'''
API class to handle various functions
that typically could not be handled by a browser sponsored HTML GUI
because of restricted access to the user's system.
'''
class Api:

    def onClose(self):
        ''' immediate close no ask '''
        window.events.closing -= on_closing
        window.destroy()

    def getFileName(self):
        global current_file
        return current_file

    def open_file(self):
        ''' called from javascript '''
        global current_file
        file_path = filedialog.askopenfilename(initialdir="./docs",
                                               title = "Open file",
                                               filetypes = (("HTML", "*.html"),
                                                            ("all files", "*.*")))
        if file_path:
            current_file = file_path
            with open(current_file, 'r') as file:
                return file.read()
        return ''

    def save_file(self, content):
        ''' called from javascript '''
        global current_file
        file_path = filedialog.asksaveasfilename(initialdir="./docs",
                                                 defaultextension=".html",
                                                 initialfile="",
                                                 filetypes = (("HTML", "*.html"),
                                                            ("all files", "*.*")))
        if file_path:
            current_file = file_path
            with open(file_path, 'w') as file:
                file.write(content)
            return current_file
        return ''

    def quick_save_file(self, content):
        global current_file
        file_path = current_file
        with open(file_path, 'w') as file:
            file.write(content)
        current_file = file_path
        return current_file

    def open_options(self):
        ''' called from javascript '''
        with open("options.dat", 'r') as file:
            lst = [line for line in file if not line.lstrip().startswith('=')]
            lst = [i.strip() for i in lst]  # strip end of lines
            return ','.join(lst)  # make a csv string
        return ''

    def open_editor(self):
        subprocess.Popen([tx, "./options.dat"])

    def open_filemgr(self):
        subprocess.Popen([fm, "./"])

    def open_browser(self):
        # launch current file in browser
        webbrowser.open(current_file)

# Create a webview window
if __name__ == '__main__':

    api = Api()

    opts = api.open_options().split(',')
    tx = opts[6]  # text editor
    fm = opts[7] # file manager

    window = webview.create_window('Word Scriber',
                     url='wsr.html',
                     width=675,
                     height=675,
                     js_api=api)

    window.events.closing += on_closing

    webview.start()
