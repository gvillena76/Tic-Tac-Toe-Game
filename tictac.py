# ----------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author: Gabriel Villena
# ----------------------------------------------------------------------
"""
To create a game of Tic-Tac-Toe where you play with a computer
"""
import tkinter
import random


class Game(object):
    """
    GUI Game class for a tic-tac-toe game

    Argument:
        parent (tkinter.Tk): the root window objec

    Attributes:
        canvas (tkinter.Canvas): the widget defining the play area.
        restart button (tkinter.Button): the button widget to restart.
        message (tkinter.Label): the frame widget displaying the win/loss/tie
            message.
        user (set): set of user-clicked square ids
        color (string): color of user squares
        opponent (set): set of AI-chosen square ids
        opponent_color (string): color of opponent squares
        none (set): set of square ids that haven't been clicked
        game_over (boolean): boolean determining if you are able to click
    """

    # Add your class variables if needed here - square size, etc...)

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        # Create the restart button widget
        button_frame = tkinter.Frame(parent)
        button_frame.grid()

        restart_button = tkinter.Button(button_frame, text='Restart',
                                        width=10, command=self.restart)
        restart_button.grid(column=0, row=0)

        # Create a canvas widget
        self.canvas = tkinter.Canvas(parent, width=300, height=300)
        self.canvas.create_rectangle(0, 0, 100, 100, outline='black',
                                     fill='white')
        self.canvas.create_rectangle(100, 0, 200, 100, outline='black',
                                     fill='white')
        self.canvas.create_rectangle(200, 0, 300, 100, outline='black',
                                     fill='white')
        self.canvas.create_rectangle(0, 100, 100, 200, outline='black',
                                     fill='white')
        self.canvas.create_rectangle(100, 100, 200, 200, outline='black',
                                     fill='white')
        self.canvas.create_rectangle(200, 100, 300, 200, outline='black',
                                     fill='white')
        self.canvas.create_rectangle(0, 200, 100, 300, outline='black',
                                     fill='white')
        self.canvas.create_rectangle(100, 200, 200, 300, outline='black',
                                     fill='white')
        self.canvas.create_rectangle(200, 200, 300, 300, outline='black',
                                     fill='white')
        self.canvas.grid()

        # Create a label widget for the win/lose message
        self.message = tkinter.Label(parent)
        self.message.grid()

        # Used for when a square is clicked
        self.canvas.bind("<Button-1>", self.play)

        # Create any additional instance variable you need for the game
        self.user = set([])
        self.color = 'red'
        self.opponent = set([])
        self.opponent_color = 'blue'
        self.none = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.game_over = False

    def restart(self):
        """
        Restarts the tic-tac-toe game board

        For all squares found on the canvas, it fills them with a white color
        and resets all the data structures of what squares have and have not
        been chosen.
        :return: None
        """
        # This method is invoked when the user clicks on RESTART.
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, fill='white')
        self.user = set([])
        self.opponent = set([])
        self.none = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.game_over = False
        self.message.configure(text='')

    def play(self, event):
        """
        Makes the clicked square filled and allows opponent to choose square

        First checks if game is over and if not, decides which square the user
        picked by the closest coordinate to the passed in button click.  If
        the square hasn't been chosen, it gets added to the user set of
        squares and removed from the none set of squares.  The opponent then
        chooses its square by randomly selecting coordinates and
        :param event: (event) Object containing the widget instance and
        coordinates of event
        :return: None
        """
        # This method is invoked when the user clicks on a square.
        if not self.game_over:
            user_choice = self.canvas.find_closest(event.x, event.y)[0]
            if user_choice in self.none:
                self.color_square(self.user, user_choice, self.color)
                if not self.test_for_win(self.user):
                    if len(self.none) != 0:
                        opponent_chosen = False
                        while not opponent_chosen:
                            # GO FOR WIN
                            if {1, 2}.issubset(self.opponent) and 3 in \
                                    self.none:
                                opponent_choice = 3
                            elif {2, 3}.issubset(self.opponent)and 1 in \
                                    self.none:
                                opponent_choice = 1
                            elif {3, 1}.issubset(self.opponent)and 2 in \
                                    self.none:
                                opponent_choice = 2
                            elif {4, 5}.issubset(self.opponent)and 6 in \
                                    self.none:
                                opponent_choice = 6
                            elif {5, 6}.issubset(self.opponent)and 4 in \
                                    self.none:
                                opponent_choice = 4
                            elif {6, 4}.issubset(self.opponent)and 5 in \
                                    self.none:
                                opponent_choice = 5
                            elif {7, 8}.issubset(self.opponent)and 9 in \
                                    self.none:
                                opponent_choice = 9
                            elif {8, 9}.issubset(self.opponent)and 7 in \
                                    self.none:
                                opponent_choice = 7
                            elif {9, 7}.issubset(self.opponent)and 8 in \
                                    self.none:
                                opponent_choice = 8
                            elif {1, 4}.issubset(self.opponent)and 7 in \
                                    self.none:
                                opponent_choice = 7
                            elif {4, 7}.issubset(self.opponent)and 1 in \
                                    self.none:
                                opponent_choice = 1
                            elif {7, 1}.issubset(self.opponent)and 4 in \
                                    self.none:
                                opponent_choice = 4
                            elif {2, 5}.issubset(self.opponent)and 8 in \
                                    self.none:
                                opponent_choice = 8
                            elif {5, 8}.issubset(self.opponent)and 2 in \
                                    self.none:
                                opponent_choice = 2
                            elif {8, 2}.issubset(self.opponent)and 5 in \
                                    self.none:
                                opponent_choice = 5
                            elif {3, 6}.issubset(self.opponent)and 9 in \
                                    self.none:
                                opponent_choice = 9
                            elif {6, 9}.issubset(self.opponent)and 3 in \
                                    self.none:
                                opponent_choice = 3
                            elif {9, 3}.issubset(self.opponent)and 6 in \
                                    self.none:
                                opponent_choice = 6
                            elif {1, 5}.issubset(self.opponent)and 9 in \
                                    self.none:
                                opponent_choice = 9
                            elif {5, 9}.issubset(self.opponent)and 1 in \
                                    self.none:
                                opponent_choice = 1
                            elif {9, 1}.issubset(self.opponent)and 5 in \
                                    self.none:
                                opponent_choice = 5
                            elif {3, 5}.issubset(self.opponent)and 7 in \
                                    self.none:
                                opponent_choice = 7
                            elif {5, 7}.issubset(self.opponent)and 3 in \
                                    self.none:
                                opponent_choice = 3
                            elif {7, 3}.issubset(self.opponent)and 5 in \
                                    self.none:
                                opponent_choice = 5
                            # NOW GO FOR BLOCK
                            elif {1, 2}.issubset(self.user) and 3 in self.none:
                                opponent_choice = 3
                            elif {2, 3}.issubset(self.user)and 1 in self.none:
                                opponent_choice = 1
                            elif {3, 1}.issubset(self.user)and 2 in self.none:
                                opponent_choice = 2
                            elif {4, 5}.issubset(self.user)and 6 in self.none:
                                opponent_choice = 6
                            elif {5, 6}.issubset(self.user)and 4 in self.none:
                                opponent_choice = 4
                            elif {6, 4}.issubset(self.user)and 5 in self.none:
                                opponent_choice = 5
                            elif {7, 8}.issubset(self.user)and 9 in self.none:
                                opponent_choice = 9
                            elif {8, 9}.issubset(self.user)and 7 in self.none:
                                opponent_choice = 7
                            elif {9, 7}.issubset(self.user)and 8 in self.none:
                                opponent_choice = 8
                            elif {1, 4}.issubset(self.user)and 7 in self.none:
                                opponent_choice = 7
                            elif {4, 7}.issubset(self.user)and 1 in self.none:
                                opponent_choice = 1
                            elif {7, 1}.issubset(self.user)and 4 in self.none:
                                opponent_choice = 4
                            elif {2, 5}.issubset(self.user)and 8 in self.none:
                                opponent_choice = 8
                            elif {5, 8}.issubset(self.user)and 2 in self.none:
                                opponent_choice = 2
                            elif {8, 2}.issubset(self.user)and 5 in self.none:
                                opponent_choice = 5
                            elif {3, 6}.issubset(self.user)and 9 in self.none:
                                opponent_choice = 9
                            elif {6, 9}.issubset(self.user)and 3 in self.none:
                                opponent_choice = 3
                            elif {9, 3}.issubset(self.user)and 6 in self.none:
                                opponent_choice = 6
                            elif {1, 5}.issubset(self.user)and 9 in self.none:
                                opponent_choice = 9
                            elif {5, 9}.issubset(self.user)and 1 in self.none:
                                opponent_choice = 1
                            elif {9, 1}.issubset(self.user)and 5 in self.none:
                                opponent_choice = 5
                            elif {3, 5}.issubset(self.user)and 7 in self.none:
                                opponent_choice = 7
                            elif {5, 7}.issubset(self.user)and 3 in self.none:
                                opponent_choice = 3
                            elif {7, 3}.issubset(self.user)and 5 in self.none:
                                opponent_choice = 5
                            # GO FOR CENTER
                            elif 5 in self.none:
                                opponent_choice = 5
                            # GO BLOCK CORNER STRAT
                            elif {1, 9}.issubset(self.user)and 6 in self.none:
                                opponent_choice = 6
                            elif {3, 7}.issubset(self.user) and 4 in self.none:
                                opponent_choice = 4
                            # BLOCK FIRST CORNER Y 2-WAYS
                            elif {2, 6}.issubset(self.user) and 3 in self.none:
                                opponent_choice = 3
                            elif {6, 8}.issubset(self.user) and 9 in self.none:
                                opponent_choice = 9
                            elif {4, 8}.issubset(self.user) and 7 in self.none:
                                opponent_choice = 7
                            elif {4, 2}.issubset(self.user) and 1 in self.none:
                                opponent_choice = 1
                            # GO BLOCK L AND Y STRAT
                            elif {2, 9}.issubset(self.user) and 4 not in self.user and 6 in self.none:
                                opponent_choice = 6
                            elif {2, 7}.issubset(self.user) and 8 not in self.user and 4 in self.none:
                                opponent_choice = 4
                            elif {6, 1}.issubset(self.user) and 8 not in self.user and 2 in self.none:
                                opponent_choice = 2
                            elif {6, 7}.issubset(self.user) and 2 not in self.user and 8 in self.none:
                                opponent_choice = 8
                            elif {8, 1}.issubset(self.user) and 6 not in self.user and 2 in self.none:
                                opponent_choice = 4
                            elif {8, 3}.issubset(self.user) and 4 not in self.user and 6 in self.none:
                                opponent_choice = 6
                            elif {4, 3}.issubset(self.user) and 8 not in self.user and 2 in self.none:
                                opponent_choice = 2
                            elif {4, 9}.issubset(self.user) and 2 not in self.user and 8 in self.none:
                                opponent_choice = 8
                            # GO FOR CORNER
                            elif 1 in self.none:
                                opponent_choice = 1
                            elif 3 in self.none:
                                opponent_choice = 3
                            elif 7 in self.none:
                                opponent_choice = 7
                            elif 9 in self.none:
                                opponent_choice = 9
                            else:
                                # RANDOM
                                opponent_x = random.randint(0, 300)
                                opponent_y = random.randint(0, 300)
                                opponent_choice = self.canvas.find_closest\
                                (opponent_x, opponent_y)[0]
                            if opponent_choice in self.none:
                                self.color_square(self.opponent,
                                                  opponent_choice,
                                                  self.opponent_color)
                                opponent_chosen = True
                                if self.test_for_win(self.opponent):
                                    self.message.configure(text='You Lost.')
                                    self.game_over = True
                    else:
                        self.message.configure(text='You Tie!')

    def color_square(self, player, choice, color):
        """
        Colors a square for the player choosing

        Given the player, their choice, and their color, a square gets
        configured to turn into the player's color.  The square's id is also
        added to the player's set of square ids and removed from the
        set of square ids not chosen
        :param player: (set): The player's set of square ids
        :param choice: (int): The id of the square chosen
        :param color: (string): The color associated to the player
        :return: None
        """
        self.canvas.itemconfigure(choice, fill=color)
        player.add(choice)
        self.none.remove(choice)

    def test_for_win(self, player):
        """
        Tests if a player has three in a row

        For the player's set of squares, it tests if any combinations of 3 are
        a subset within the player's set.  If it's true, the instance variable
        of game_over is set to True and the return value is set to True.  If
        not, the return value is set to False.
        :param player: (set) The player to be tested
        :return win: (boolean) The condition on if the player has won
        """
        if {1, 2, 3}.issubset(player)\
                or {4, 5, 6}.issubset(player)\
                or {7, 8, 9}.issubset(player)\
                or {1, 4, 7}.issubset(player)\
                or {2, 5, 8}.issubset(player)\
                or {3, 6, 9}.issubset(player)\
                or {1, 5, 9}.issubset(player)\
                or {3, 5, 7}.issubset(player):
            if player == self.user:
                self.message.configure(text='You Won!')
                self.game_over = True
            win = True
        else:
            win = False
        return win


def main():
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a Game object
    game = Game(root)
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()