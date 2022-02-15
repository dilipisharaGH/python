from tkinter import *
lwin= Tk()
lwin.geometry("512x512")
lwin.title("Front Window")
splash_label= Label(lwin, text= "Hello World!\nThis is Front page", fg= "#101010",font= ('Courier', 8))
splash_label.pack(expand = True)


def mainWin():
   lwin.destroy()
   win= Tk()
   win.geometry("512x512")
   win.title("Main Window")
   win_label= Label(win, text= "follow dilipisharaGH in GitHub\nThank you!", font= ('Courier', 7), fg= "#101010")
   win_label.pack(expand = True)

lwin.after(3072, mainWin)
mainloop()
