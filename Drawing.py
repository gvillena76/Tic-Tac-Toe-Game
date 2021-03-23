# -----------------------------------------------------------------------------
# Name:        draw
# Purpose:     Implement a simple drawing application
#
# Author:      Rula Khayrallah
# -----------------------------------------------------------------------------
"""
Module to implement a simple drawing app
"""
import tkinter


class DrawApp(object):
    """
    class to support a simple drawing app

    Argument:
    parent: (tkinter.Tk) the root window object

    Attribute:
    canvas:  (tkinter.Canvas) our drawing canvas
    """

    def __init__(self, parent):
        parent.title('CS 21A Drawing App')
        # create the canvas
        # since we need to access the canvas widget from other methods,
        # we save it in the object as an instance variable: self.canvas
        self.canvas = tkinter.Canvas(parent, width=300, height=300)
        # register it with a geometry manager
        self.canvas.grid()
        # bind the leftmost button click to the draw_circle method
        self.canvas.bind("<Button-1>", self.draw_circle)
        # bind the leftmost button double click to the draw_square method
        self.canvas.bind("<Double-Button-1>", self.draw_square)

    def draw_circle(self, event):
        """ Draw a magenta circle centered at the click position"""
        self.canvas.create_oval(event.x - 10,
                                event.y - 10,
                                event.x + 10,
                                event.y + 10,
                                fill="magenta")

    def draw_square(self, event):
        """ Draw a cyan square at the click position"""
        self.canvas.create_rectangle(event.x - 10,
                                     event.y - 10,
                                     event.x + 10,
                                     event.y + 10,
                                     fill="cyan")


def main():
    # create the GUI application main window
    root = tkinter.Tk()

    # instantiate our drawing app object
    my_app = DrawApp(root)

    # enter the main event loop and wait for events
    root.mainloop()


if __name__ == '__main__':
    main()
