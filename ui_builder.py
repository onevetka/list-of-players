from main_window_ui import *


def build_main_window():
    root = Tk()

    # Place a window in the middle of the screen -->

    x_position = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y_position = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.wm_geometry("+%d+%d" % (x_position, y_position))

    root.event_add('<<Paste>>', '<Control-igrave>')
    root.event_add("<<Copy>>", "<Control-ntilde>")
    root.iconbitmap("images/LOfP.ico")

    q = Question(root)

    root.title('List Of Players')
    root.config(background="white")

    root.mainloop()