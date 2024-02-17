import tkinter as tk

class Pencere(tk.Tk):
    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.cikis)

        self.etiket = tk.Label(text="Merhaba Dünya")
        self.etiket.pack()

        self.dugme = tk.Button(text="Çık", command=self.cikis)
        self.dugme.pack()

    def cikis(self):
        self.etiket['text'] = "Elveda dünya..."
        self.dugme['text'] = "Bekleyin..."
        self.dugme['state'] = 'disabled'
        self.after(2000, self.destroy)

pencere = Pencere()
pencere.mainloop()