import tkinter as tk
from tkinter.scrolledtext import ScrolledText

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('App')
        self.geometry('300x400')
        self.editor = ScrolledText(self)
        self.editor.pack(
            expand=True,
            fill=tk.BOTH,
            padx=(1.75, 2.5),
            pady=(2.5, 1.75),
        )
        self.colormap = {
            ']': '#a94926',
            '+': '#cc7832',
            '-': '#cc7832',
            '<': '#6a8759',
            '>': '#6a8759',
            ',': '#6396ba',
            '.': '#6396ba',
            '[': '#a94926',
        }
        for c in self.colormap:
            self.editor.tag_config(c, foreground=self.colormap[c])
    
        self.editor.bind('<KeyRelease>', self.on_key)

    def on_key(self, event):
        if event.char in self.colormap:
            event.widget.tag_add(event.char, 'insert-1c')

if __name__ == '__main__':
    app = App()
    app.mainloop()