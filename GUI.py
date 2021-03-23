# import the tkinter module
import tkinter


def main():
    # create the GUI application main window
    root = tkinter.Tk()
    # customize our GUI application main window
    root.title('CS 21 A')

    # instantiate a Label widget with root as the parent widget
    # use the text option to specify which text to display
    hello = tkinter.Label(root, text='Hello World!')

    # invoke the pack method on the widget
    hello.pack()

    # create a STOP button
    stop_button = tkinter.Button(root, text='STOP')
    stop_button.pack()

    # create a GO button
    go_button = tkinter.Button(root, text='GO')
    go_button.pack()

    # create the GUI application main window
    root1 = tkinter.Tk()
    # create a label
    title = tkinter.Label(root1, text="Let's Draw!")
    title.pack()

    # instantiate a Canvas widget with root as the parent widget
    canvas = tkinter.Canvas(root1, background='green')

    # draw a blue rectangle on the canvas
    # create_rectangle returns an object id that we save in the variable body
    body = canvas.create_rectangle(50, 50, 150, 100, fill='blue')

    # draw two red circles on the canvas
    # create_oval also returns an object id
    wheel1 = canvas.create_oval(50, 100, 75, 125, fill='red')
    wheel2 = canvas.create_oval(125, 100, 150, 125, fill='red')

    # draw a line
    my_line = canvas.create_line(50, 50, 150, 200)

    canvas.pack()

    # enter the main event loop and wait for events
    root1.mainloop()


if __name__ == '__main__':
    main()