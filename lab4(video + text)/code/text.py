from tkinter import  Tk, font, Label, W



root = Tk()

available_fonts = font.families()



fonts = font.Font(family=available_fonts[0],size=15,weight="bold")


Label(root, text=available_fonts[0], bg="green", fg="yellow", font= fonts).pack()


root.mainloop()
