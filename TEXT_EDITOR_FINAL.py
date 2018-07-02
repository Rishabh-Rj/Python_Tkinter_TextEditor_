from tkinter import *
import tkinter.filedialog
from PIL import Image, ImageTk

class TkInterEx:
    @staticmethod
    def quit_app(event=None):
        root.quit()

    def open_file(self, event=None):

        txt_file = tkinter.filedialog.askopenfilename(parent=root,
                                                      initialdir=r'C:\Users\rishabh joshi\Desktop\Python')

        if txt_file:

            self.text_area.delete(1.0, END)

            # Open file and put text in the text widget
            with open(txt_file) as _file:
                self.text_area.insert(1.0, _file.read())

                # Update the text widget
                root.update_idletasks()

    def save_file(self, event=None):

        # Opens the save as dialog box
        file = tkinter.filedialog.asksaveasfile(mode='w')
        if file != None:
            # Get text in the text widget and delete the last newline
            data = self.text_area.get('1.0', END + '-1c')

            # Write the text and close
            file.write(data)
            file.close()


    def __init__(self, root):
        Frame(root, background="blue")


        self.text_to_write = ""

        # Define title for the app
        root.title("RJ Text Editor")

        # Defines the width and height of the window
        root.geometry("600x550")

        frame = Frame(root, width=600, height=550)

        # Create the scrollbar
        scrollbar = Scrollbar(frame)

        # yscrollcommand connects the scroll bar to the text
        # area
        self.text_area = Text(frame, width=600, height=550,
                        yscrollcommand=scrollbar.set,
                        padx=10, pady=10)

        # Call yview when the scrollbar is moved
        scrollbar.config(command=self.text_area.yview)

        # Put scroll bar on the right and fill in the Y direction
        scrollbar.pack(side="right", fill="y")

        # Pack on the left and fill available space
        self.text_area.pack(side="left", fill="both", expand=True)







        # ---------- Create Toolbar ----------

        # RAISED draws a line under the tool bar and bd defines the border width
        toolbar = Frame(root, bd=1, relief=RAISED)

        # Get images for toolbar
        open_img = Image.open("open.jpg")
        save_img = Image.open("save.jpg")
        exit_img = Image.open("quit.jpg")

        # Create a TkInter image to be used in the button
        open_icon = ImageTk.PhotoImage(open_img)
        save_icon = ImageTk.PhotoImage(save_img)
        exit_icon = ImageTk.PhotoImage(exit_img)

        # Create buttons for the toolbar
        open_button = Button(toolbar, image=open_icon, command=self.open_file)
        save_button = Button(toolbar, image=save_icon, command=self.save_file)
        exit_button = Button(toolbar, image=exit_icon, command=self.quit_app)

        open_button.image = open_icon
        save_button.image = save_icon
        exit_button.image = exit_icon

        # Place buttons in the interface
        open_button.pack(side=LEFT, padx=2, pady=2)
        save_button.pack(side=LEFT, padx=2, pady=2)
        exit_button.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)

        root.config(menu=toolbar)
        frame.pack()
root = Tk()
root.geometry("600x550")
text_editor= TkInterEx(root)
root.mainloop()